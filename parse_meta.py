from lxml import etree
from jinja2 import Template

from parsed_class import ParsedClass
from parsed_common import clean_name, ns

import os

xmlns = "http://csrc.nist.gov/ns/oscal/metaschema/1.0"

processed_files = []
package_imports = {}
class_data = []


def find_definitions(xmlobject):
    """Return etree xml objects that start with define.  This will be all
    fields, flags, and assemblies that are initiated in this file

    Args:
        xmlobject (Element): Root Etree lxml element to search through

    Returns:
        List: List of etree Elements that begin with 'define'
    """
    defintions = xmlobject.xpath(
        "//oscal:*[starts-with(local-name(), 'define')]",
        namespaces={
            'oscal': ns['']})
    return defintions


# def find_plurals(xmlobject, singular):
#     references = xmlobject.xpath(
#         f'//oscal:assembly[@ref="{singular}"]/g',
#         namespaces={'oscal': ns['']}
#     )
#     return [ref.attrib.get('name') for ref in references]


def find_class(classname, contexts=[]):
    """Find a class by name from the list of currently created class objects

    Args:
        classname (str): friendly name of the class to search for
        contexts (list, optional): current module contexts to search through,
        generated by the current file and any imported files. Defaults to [].

    Returns:
        ParsedClass: a single parsed class instance that matches the name, and
        is in the most specific context.  Most specific context being the
        lowest index.
    """

    matched = []
    classname = classname.lower()
    for c in class_data:
        if c.orig_name == classname:
            matched += [c]
        if c.name == classname:
            matched += [c]
        for alias in c.aliases:
            if alias == classname:
                matched += [c]
    if len(matched) == 1:
        return matched[0]
    elif len(matched) == 0:
        return None
    else:
        for m in matched:
            for context in contexts:
                if context in m.context:
                    return m
        return matched[0]


def create_class(definition, context):
    """Create a ParsedClass Object from xml Element

    Args:
        definition (Element): xml Element rooted at the defined component
        context (string): module the defintion was initiated in.
    """
    global class_data
    newcls = ParsedClass().from_xml(definition)
    newcls.context = context[0]
    newcls.contexts = context
    class_data += [newcls]


def process_imports(xmlobject, sourcepath):
    """Iterate through imported files, and add the modules to the
    list of contexts that will be used in searching for dependencies

    Args:
        xmlobject (Element): Root XML Element instance
        sourcepath (str): Filesystem path where parent file found.
        Necessary to resolve relative paths

    Returns:
        list: List of contexts that the import caused
        (imports could be recursive)
    """
    imports = xmlobject.findall('import', ns)
    contexts = []
    for i in imports:
        filepath = os.path.join(
            os.path.dirname(sourcepath),
            i.attrib['href']
        )
        contexts += [read_file(filepath)]
    return contexts


def read_file(filepath):
    """Read XML Metascema file, iterate through known types to define classes

    Args:
        filepath (str): relative path to file

    Returns:
        list: recursive list of defined module contexts
    """
    global processed_files
    global package_imports

    contexts = []
    parser = etree.XMLParser(load_dtd=True,
                             no_network=False)

    tree = etree.parse(filepath, parser=parser)
    name = tree.find('short-name', ns).text

    if filepath in processed_files:
        return name
    else:
        processed_files += [filepath]

    contexts += [name]

    imports = process_imports(tree, filepath)
    package_imports[name] = imports
    contexts += imports

    for definition in find_definitions(tree):
        create_class(definition, contexts)

    for c in class_data:

        for r in c.get_refs():
            discovered_class = find_class(r[1], contexts)
            discovered_class.add_alias(r[0])
        for field in c.all_attributes():
            field_name = field.name.replace('oscal_', '').title()
            discovered_field = find_class(field_name, contexts)
            if discovered_field is not None:
                field.names = discovered_field.aliases
    return name


def output_puml(outdir='.'):
    """Create Plantuml Class Diagram of created classes and packages

    Args:
        outdir (str, optional): destination directory. Defaults to '.'.
    """
    global class_data
    contexts = {}
    for c in class_data:
        grp = clean_name(c.context)
        if grp not in contexts:
            contexts[grp] = []
        if c.name not in [c.name for c in contexts[grp]]:
            contexts[grp] += [c]

    with open('templates/puml.j2') as f:
        template = Template(f.read())
    output = template.render(
        {
            'classes': contexts,
            'imports': package_imports
        }
    )
    outpath = 'diagram.puml'
    with open(outpath, 'w') as f:
        f.write(output)


def create_importline(module, classes):
    importline = []
    importline += ["from pyoscal.{} import (".format(module)]
    processed = []
    line = "    "
    for cls in classes:
        if cls not in processed:
            if len(line) + len(cls)+2 > 70:
                importline += [line]
                line = "    "
            elif len(processed) > 0:
                line += " "
            line += "{},".format(cls)
            processed += [cls]
    importline += [line]
    importline += [')\n']
    return '\n'.join(importline)


def main():
    """Main function.  finds files, parses them, creates modules,
    creates __init__
    """

    metaschema_root = 'OSCAL/src/metaschema'
    metaschema_xmls = [os.path.join(metaschema_root, f)
                       for f in os.listdir(metaschema_root)
                       if f.lower().endswith('_metaschema.xml')]
    out_dir = 'pyoscal/core'
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for metaschema_xmlpath in metaschema_xmls:
        read_file(metaschema_xmlpath)

    output_puml(outdir=out_dir)

    contexts = {}
    for c in class_data:
        grp = clean_name(c.context)
        if grp not in contexts:
            contexts[grp] = []
        contexts[grp] += [c.name]
        outdir = os.path.join(out_dir, grp)
        if not os.path.isdir(outdir):
            os.makedirs(outdir)
        classpath = os.path.join(outdir, "{}.py".format(c.name))
        with open(classpath, 'w') as f:
            f.write(c.toPY())

    # Write INITS
    globalinit_lines = []
    globalinit_lines += ["from pyoscal.core.OSCAL import *\n"]
    modules = list(contexts.keys())
    modules.sort()
    for grp in modules:
        globalinit_lines += ["from pyoscal.core.{} import *\n".format(grp)]
        classinit_lines = []
        classes = contexts[grp]
        classes.sort()
        for classinit in classes:
            classinit_lines += [
                "import pyoscal.core.{}.{}\n".format(grp, classinit)
            ]
        with open(os.path.join(out_dir, grp, '__init__.py'), 'w') as classinit:
            classinit.writelines(set(classinit_lines))
    with open(os.path.join(out_dir, '__init__.py'), 'w') as globalinit:
        globalinit.writelines(set(globalinit_lines))


if __name__ == "__main__":
    main()
