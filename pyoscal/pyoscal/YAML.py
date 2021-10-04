
from .Parser import OSCAL_IO
from pyoscal import *  # noqa: F401,F403 # necessary for exec statements

import yaml

import sys


class OSCAL_YAML(OSCAL_IO):



    html_tags = ['a', 'em', 'p', 'q', 'insert', 'ol', 'li']

    def clean_name(self, name):
        bad_characters = ['-']
        for char in bad_characters:
            name = name.replace(char, '_')

        bad_words = ['class', 'property', 'import']
        if name in bad_words:
            name = "oscal_{}".format(name)

        return name

    def stringify(self, xmlobject):
        return

    def from_string(self, content):
        root = yaml.safe_load(content)
        top_key = list(root.keys())[0]
        name = self.clean_name(top_key).title()
        return self.to_object(root.get(top_key), name=name)
        # return self.objectify(root)

    def parse(self, filepath):
        with open(filepath, encoding="utf8") as f:
            return self.from_string(f)

    def to_object(self, obj, name=None, contexts=[]):
        if not isinstance(obj, (list, dict)):
            return obj
        if isinstance(obj, list) and all([isinstance(c, str) for c in obj]):
            return obj
        classpath = self.find_class(name, contexts=contexts)

        if self.is_class(name, contexts=contexts):
            classobject = self.find_class(name, contexts)
            classmodule = sys.modules[self.class_module(classobject)]
            classinstance = getattr(classmodule, name)
            class_contexts = [
                self.clean_name("pyoscal.{}".format(c))
                for c in classinstance.contexts
            ]
            if contexts is None:
                contexts = [self.class_base(self.find_class(name))]
            contexts = self.dedup(contexts + class_contexts)
        else:
            print(f"Returning1: {obj}")
            return self.stringify(obj)

        attributes = {}
        for child_name, child_content in obj.items():
            mod_name = self.clean_name(child_name).title()

            if child_name.endswith('s') and \
               isinstance(child_content, list):
                singular = child_name[:-1].title()
                child = [self.to_object(
                            c,
                            name=singular,
                            contexts=contexts)
                         for c in child_content]

            else:
                child = self.to_object(
                    child_content,
                    name=mod_name,
                    contexts=contexts)
            attributes[child_name] = child

        try:
            local_vars = {'attributes': attributes}
            exec(f"newclass = {classpath}.fromDict(attributes)",
                 globals(), local_vars)
            return local_vars.get('newclass')
        except Exception as e:
            print(f"No Matching Attr: {classpath}, {e}")
        return None

    def export_obj(self, obj, rootname=None):
        if rootname is None:
            rootname = obj.use_name
        children = {}
        if isinstance(obj, list):
            return list([self.export_obj(o) for o in obj])
        elif isinstance(obj, str):
            return obj
        else:
            for child in obj.parameters + obj.subcomponents:
                children[child.use_name: self.export_obj(child)]
        return {rootname: children}

    def export(self, obj):
        return self.export_obj(obj)
