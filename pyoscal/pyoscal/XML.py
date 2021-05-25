
from .Parser import OSCAL_IO
from pyoscal import *


from lxml import etree
from lxml import objectify as etobjectify

import sys


class OSCAL_XML(OSCAL_IO):

    ns = {
        '': 'http://csrc.nist.gov/ns/oscal/metaschema/1.0',
        'oscal': 'http://csrc.nist.gov/ns/oscal/1.0'
    }

    html_tags = ['a', 'em', 'p', 'q', 'insert', 'ol', 'li']

    def clean_name(self, name):
        bad_characters = ['-']
        for char in bad_characters:
            name = name.replace(char, '_')

        bad_words = ['class', 'property', 'import']
        if name in bad_words:
            name = "oscal_{}".format(name)

        return name

    def get_tag(self, xmlobject):
        return xmlobject.tag.replace(
            "{{{}}}".format(
                self.ns['oscal']),
            '').lower()

    def stringify(self, xmlobject):
        if xmlobject is None:
            return ""
        if xmlobject.text is None:
            text = str("")
        else:
            text = xmlobject.text
        combined = [text]
        for e in xmlobject:
            etobjectify.deannotate(e, cleanup_namespaces=True)
            e.tag = etree.QName(e).localname
            combined += [str(etree.tostring(e))]
        joined = ''.join(combined).replace(
            '\'',
            '').replace(
                '\\n',
            '').replace('b<', '<')
        joined = joined.replace(
            ' xmlns="http://csrc.nist.gov/ns/oscal/1.0"',
            '').strip()
        return str(joined)

    def from_string(self, content):
        root = etree.fromstring(content)
        return self.objectify(root)

    def parse(self, filepath):
        parser = etree.XMLParser(
            load_dtd=True,
            no_network=False)

        tree = etree.parse(filepath, parser=parser)
        return self.objectify(tree.getroot())

    def objectify(self, xmlobject, contexts=None):
        classname = self.clean_name(self.get_tag(xmlobject)).title()
        if self.is_class(classname, contexts=contexts):
            classobject = self.find_class(classname, contexts)
            classmodule = sys.modules[self.class_module(classobject)]
            classinstance = getattr(classmodule, classname)
            class_contexts = [
                self.clean_name(
                    "pyoscal.{}".format(c)) for c in classinstance.contexts]
            if contexts is None:
                contexts = [self.class_base(self.find_class(classname))]
            contexts = self.dedup(contexts + class_contexts)
        else:
            return self.stringify(xmlobject)
        attributes = {}
        value_id = 'prose'
        for attribute in xmlobject.attrib:
            attr_name = self.clean_name(attribute).title()
            classpath = self.find_class(attr_name, contexts=contexts)
            local_vars = {
                'attributes': {
                    'prose': xmlobject.attrib.get(attribute)}}
            try:
                exec("newclass = {}.fromDict(attributes)".format(
                    classpath), globals(), local_vars)
            except Exception as e:
                print("No Matching Attr: {}/{}, {}".format(
                    classname, attr_name, e))
            attributes[self.clean_name(attribute)] = local_vars.get('newclass')

        if len(list(xmlobject)) == 0:  # No children, leaf node
            if value_id not in xmlobject.attrib:
                attributes[value_id] = xmlobject.text

        # remark / desc/ title
        elif self.get_tag(list(xmlobject)[0]).lower() in self.html_tags:
            if value_id not in xmlobject.attrib:
                attributes[value_id] = self.stringify(xmlobject)
        else:
            prose_value = ""
            for child in xmlobject:
                childname = self.clean_name(self.get_tag(child)).title()
                if childname.lower() in self.html_tags:
                    prose_value += "<{0}>{1}</{0}>".format(self.get_tag(child),self.stringify(child))
                x = self.objectify(child, contexts)
                paramname = childname.lower()
                if paramname in attributes:
                    if isinstance(attributes[paramname], list):
                        attributes[paramname] += [x]
                    else:
                        attributes[paramname] = [x, attributes[paramname]]
                else:
                    attributes[paramname] = x
            if prose_value != "":
                attributes[value_id] = prose_value

        local_vars = {'attributes': attributes}
        classpath = self.find_class(classname, contexts=contexts)
        try:
            exec("newclass = {}.fromDict(attributes)".format(
                classpath), globals(), local_vars)
        except Exception as e:
            print(
                "Failed on {}: {} ".format(
                    classname,
                    etree.tostring(xmlobject)))

        return local_vars.get('newclass')

    def export_obj(self, obj, rootname=None):
        if rootname is None:
            rootname = obj.use_name
        root = etree.Element(rootname)
        if isinstance(obj, list):
            return list([self.export_obj(o) for o in obj])
        elif isinstance(obj, str):
            return obj
        else:
            if len(obj.parameters) + len(obj.subcomponents) == 0:
                root.text = getattr(obj, obj.value_id)
            for parameter in obj.parameters:
                param = getattr(obj, parameter)
                if param is not None:
                    root.attrib[param.use_name] = param.prose
            for subcomponent in obj.subcomponents:
                subcomponent_obj = getattr(obj, subcomponent)
                if subcomponent_obj:
                    try:
                        if isinstance(subcomponent_obj, list):
                            subrootname = subcomponent_obj[0].use_name
                        else:
                            subrootname = subcomponent_obj.use_name
                    except BaseException:
                        subrootname = subcomponent
                    result = self.export_obj(
                        subcomponent_obj, rootname=subrootname)
                    if isinstance(result, etree._Element):
                        root.append(result)
                    elif isinstance(result, list):  # list of elements
                        for e in result:
                            root.append(e)
                    else:
                        root.text = result
            return root

    def export(self, obj):
        result = self.export_obj(obj)
        result.attrib['xmlns'] = self.ns['']
        return etree.tostring(
            result,
            pretty_print=True,
            xml_declaration=True,
            encoding='UTF-8'
        ).decode('utf-8').replace('&lt;', '<').replace('&gt;', '>')
