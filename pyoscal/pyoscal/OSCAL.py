from .XML import OSCAL_XML
from pyoscal import *  # noqa: F401 F403


class OSCAL:

    def __init__(self):
        self.objects = {}

    def parse_file(self, filepath):
        if filepath.lower().endswith('xml'):
            parser = OSCAL_XML()

        obj = parser.parse(filepath)
        self.add_model(obj)
        return obj

    def parse_string(self, content, fmt='xml'):
        if fmt == 'xml':
            parser = OSCAL_XML()
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
        if outtype.lower() == 'xml':
            parser = OSCAL_XML()
        if not uuid:
            for obj in self.object_list():
                out = parser.export(obj)
        else:
            obj = self.find_object_byuuid(uuid)
            out = parser.export(obj)
        return out
