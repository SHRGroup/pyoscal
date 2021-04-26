from lxml import objectify as etobjectify
from lxml import etree
from jinja2 import Template

from parsed_common import *
from parsed_field import ParsedField

ns = {'': 'http://csrc.nist.gov/ns/oscal/metaschema/1.0'}


class ParsedClass:
    """Creates a outline or a Python class based on OSCAL Metaschema XML input.

    Returns:
        ParsedClass: Instance of the Parsed Class Object
    """

    list_types = ['array', 'list', 'by_key']

    def __init__(self):

        self.xmlobject = None

        self.name = ""
        self.context = ""
        self.clean_name = ""

        self.aliases = []
        self.contexts = []

        self.attributes = []
        self.subcomponents = []

        self.value_id = None
        self.tag_name = ""

        self.formal_name = ""
        self.description = ""
        self.remarks = ""

    @classmethod
    def from_xml(cls, xmlobject):
        """Create a Class based on an XMLObject

        Args:
            xmlobject (Element): Etree XML Element

        Returns:
            ParsedClass: Instance of new parsed class
        """
        newcls = cls()

        newcls.orig_name = xmlobject.attrib.get('name')
        newcls.name = clean_name(newcls.orig_name).title()
        newcls.xmlobject = xmlobject
        newcls.formal_name = get_fieldText(xmlobject, 'formal-name')
        newcls.description = get_fieldText(xmlobject, 'description')
        newcls.remarks = get_fieldText(xmlobject, 'remarks')

        if has_child(xmlobject, 'use-name'):
            newcls.add_alias(get_fieldText(xmlobject, 'use-name'))

        newcls.add_attributes()
        newcls.add_subcomponents()
        # if len(newcls.all_attributes()) == 0 or
        # xmlobject.tag.endswith('field'):
        if not newcls.has_attribute('prose'):
            newcls.attributes += [ParsedField().static_value()]
        return newcls

    def toPY(self):
        """Creates the python file to store the class and all
        aliases from a Jinja Template

        Returns:
            str: String of the python file content
        """
        with open('templates/class.j2') as f:
            template = Template(f.read())
        template_data = {}
        for method in dir(self):
            if not method.startswith('_'):
                func = getattr(self, method)
                if callable(func):
                    template_data[method] = func
        template_data.update(self.__dict__)

        return template.render(template_data)

    def has_attribute(self, name):
        """Does the Instance of this class have a attribute with
        name `name`

        Args:
            name (str): name of attribute in question

        Returns:
            bool: Return True/False if name is an attribute
        """
        return name in [p.name
                        for p in self.all_attributes()]

    def all_attributes(self):
        """REturn list of all attributes and subcomponents

        Returns:
            list: all fields, flags, attributes as ParsedField Objects
        """
        return self.attributes + self.subcomponents

    def arr_parameters(self):
        """Creates list of fields that are arrays, lists, or groups

        Returns:
            list: subset of attributes
        """
        return [p
                for p in self.all_attributes()
                if p.field_type.lower() in self.list_types]

    def prim_parameters(self):
        """Creates list of attributes that are not groups or arrays.
        Attributes that have values

        Returns:
            list: subset of attributes with direct values
        """
        return [p
                for p in self.all_attributes()
                if p.field_type.lower() not in self.list_types]

    def required_parameters(self):
        """Generate list of parameters that are Required for the class

        Returns:
            list: parameters that have the `required` flag
        """
        return [p
                for p in self.all_attributes()
                if p.required]

    def optional_parameters(self):
        """Generate list of parameters that are optional

        Returns:
            list: parameters without `required` flag
        """
        return [p
                for p in self.all_attributes()
                if not p.required]

    def list_parameters(self):
        """List Parameters, parameters are attributes or
        flags (not subcomponents)

        Returns:
            list: list of attributes that came from a parameter
        """
        return [p.name
                for p in self.all_attributes()
                if p.isparameter]

    def list_subcomponents(self):
        """List of attributes that are not parameters, they are children
        of the class

        Returns:
            list: list of children of this class
        """
        return [p.name
                for p in self.all_attributes()
                if not p.isparameter]

    def get_refs(self):
        """List of all fields that reference another class

        Returns:
            list: list of fields with the ref defined
        """
        out = []
        for p in self.all_attributes():
            if p.ref:
                out += [(p.orig_name, p.ref)]
        return out

    def add_attributes(self):
        """Find all attributes (flags) and add them as ParsedFields to
        the class
        """
        flags = self.xmlobject.xpath(
            "oscal:*[contains(local-name(),'flag')]",
            namespaces={'oscal': ns['']}
        )
        for flag in flags:
            self.attributes += [ParsedField().from_xml(flag)]

    def add_subcomponents(self):
        """Find all subcomponets (children) and add them to the Class as
        ParsedFields
        """
        model = self.xmlobject.find('model', ns)
        if model is not None:
            components = model.xpath(
                "oscal:*[ \
                    contains(local-name(), 'flag') or \
                    contains(local-name(), 'assembly') or \
                    contains(local-name(), 'field')]",
                namespaces={
                    'oscal': ns['']})
            components += model.xpath(
                "oscal:choice/oscal:*[ \
                    contains(local-name(), 'flag') or \
                    contains(local-name(), 'assembly') or \
                    contains(local-name(), 'field')]",
                namespaces={
                    'oscal': ns['']})
            for component in components:
                self.subcomponents += [ParsedField().from_xml(component)]
        return

    def add_alias(self, alias):
        """add remote reference to list of aliases

        Args:
            alias (str): alias name
        """
        if not self.has_attribute(alias):
            self.aliases += [clean_name(alias).title()]
            self.aliases = list(set(self.aliases))
