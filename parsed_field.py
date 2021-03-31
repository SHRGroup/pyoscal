from lxml import objectify as etobjectify
from lxml import etree

from parsed_common import *


class ParsedField:

    def __init__(self):
        self.name = "NONAME"
        self.required = False
        self.isparameter = False
        self.default = None
        self.schema_name = ""
        self.field_type = ""
        self.description = ""
        self.group_name = ""
        self.ref = ""
        self.orig_name = ""
        self.names = []

    @classmethod
    def static_value(cls):
        """Create an instance of the class that has no children.

        Returns:
            ParsedField: Field to hold prose or raw text
        """
        newcls = cls()
        newcls.name = 'prose'
        newcls.field_type = 'str'
        newcls.description = 'Default value holder for raw data in texts'
        return newcls

    @classmethod
    def from_xml(cls, xml):
        """Create Instance of Parsed Field from provided XML

        Args:
            xml (Element): Input XML content

        Returns:
            ParsedField: Instance of Field from the provided XML
        """
        newcls = cls()

        newcls.name = xml.attrib.get('name', "MISSING")
        newcls.field_type = xml.attrib.get('as-type', 'str')

        if 'ref' in xml.attrib:  # alias to existing class
            newcls.name = xml.attrib.get('ref')

        if has_child(xml, 'use-name'):  # alias has new name
            newcls.name = get_fieldText(xml, 'use-name')
            newcls.ref = xml.attrib.get('ref')

        newcls.orig_name = newcls.name
        newcls.name = clean_name(newcls.name)

        if 'min-occurs' in xml.attrib or bool(
                xml.attrib.get('required')):  # required
            newcls.required = True

        if has_child(xml, 'description'):
            newcls.description = get_fieldText(xml, 'description')

        if has_child(xml, 'group-as'):
            grp = xml.find('group-as', ns)
            newcls.group_name = clean_name(grp.attrib.get('name'))
            newcls.field_type = grp.attrib.get('in-json', 'ARRAY')

        if xml.tag.endswith('flag'):
            newcls.isparameter = True

        return newcls
