from lxml import objectify as etobjectify
from lxml import etree

ns = {'': 'http://csrc.nist.gov/ns/oscal/metaschema/1.0'}


def clean_name(name):
    """Make name python friendly.  Remove spaces, characters,
    and reserved words

    Args:
        name (str): Initial string

    Returns:
        str: String without spaces, non-python friendly characters,
        or reserved words
    """
    bad_characters = ['-']
    for char in bad_characters:
        name = name.replace(char, '_')

    bad_words = ['class', 'property', 'import']
    if name.lower() in bad_words:
        name = "oscal_{}".format(name)
    return name


def stringify(xmlobject):
    """Create string representation of XML/HTML content without
    namespaces or other markup

    Args:
        xmlobject (Element): etree element to return string of

    Returns:
        str: string including any HTML markup, without namespaces
    """
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
        '\'', '').replace(
        '\\n', '').replace(
        'b<', '<')
    joined = joined.replace(' xmlns="http://csrc.nist.gov/ns/oscal/1.0"', '')
    return joined


def get_fieldText(xmlobject, fieldname):
    """If a field has text, return it, if not return blank string

    Args:
        xmlobject (Element): XML Element of look through
        fieldname (str): field to return text of

    Returns:
        str: string of fields content, or blank string
    """
    field = xmlobject.find(fieldname, ns)
    if field is not None:
        return field.text
    else:
        return ""


def has_child(xmlobject, childname):
    """Decided if a named child exists within the XML object

    Args:
        xmlobject (Element): etree xml object
        childname (str): Name of child to look for

    Returns:
        bool: If the XML root has a child by that name
    """
    if xmlobject.find(childname, ns) is not None:
        return True
    else:
        return False
