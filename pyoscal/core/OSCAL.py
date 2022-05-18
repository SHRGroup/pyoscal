import os

from .XML import OSCAL_XML
from .YAML import OSCAL_YAML
from pyoscal.core import *  # noqa: F401 F403


class OSCAL:

    def __init__(self):
        self.objects = {}

    def get_parser(self, fmt='xml'):
        fmt = fmt.replace('.', '').lower()
        if fmt == 'xml':
            return OSCAL_XML()
        elif fmt in ['yaml', 'yml']:
            return OSCAL_YAML()
        return OSCAL_XML()

    def parse_file(self, filepath):
        extension = os.path.splitext(filepath)[1]
        parser = self.get_parser(extension)
        obj = parser.parse(filepath)
        # print(f"object: {obj}")
        self.add_model(obj)
        return obj

    def parse_string(self, content, fmt='xml'):
        parser = self.get_parser(fmt)
        obj = parser.from_string(content)
        self.add_model(obj)
        return obj

    def add_model(self, obj):
        obj_type = type(obj).__name__
        if obj_type not in self.objects:
            self.objects[obj_type] = [obj]
        else:
            self.objects[obj_type] += [obj]

    def object_list(self):
        out = []
        for k in self.objects.keys():
            out += self.objects[k]
        return out

    def find_object_byuuid(self, uuid):
        for obj in self.object_list():
            if hasattr(obj, 'uuid'):
                if str(obj.uuid) == uuid:
                    return obj
        return None

    def export(self, outtype='xml', uuid="", outputpath="."):
        parser = self.get_parser(outtype)
        if not uuid:
            for obj in self.object_list():
                out = parser.export(obj)
        else:
            obj = self.find_object_byuuid(uuid)
            out = parser.export(obj)
        return out
