import sys
import inspect
from . import *


class OSCAL_IO:

    def __init__(self):
        pass

    def parse(self):
        pass

    def objectify(self):
        pass

    def export(self):
        pass

    def class_module(self, classpath):
        return '.'.join(classpath.split('.')[:-1])

    def class_base(self, classpath):
        return '.'.join(classpath.split('.')[:2])

    def dedup(self, array):
        retlist = []
        for item in array:
            if item not in retlist:
                retlist += [item]
        return retlist

    def find_class(self, classname, contexts=[]):
        classname = classname.title()
        matched_classes = []
        class_list = []
        oscal_classes = [
            inspect.getmembers(sys.modules[m], inspect.isclass)
            for m in list(sys.modules.keys())
            if m.startswith('pyoscal.oscal_')]
        for collection in oscal_classes:
            for oscal_class in collection:
                class_list += [oscal_class]
        for oscal_class in class_list:
            if oscal_class[0].lower() == classname.lower():
                classpath = ".".join(
                    [oscal_class[1].__module__, oscal_class[1].__name__])
                matched_classes += [classpath]
        if len(matched_classes) == 1:
            return matched_classes[0]
        for context in contexts[::1]:  # direct class before imports
            for matched in matched_classes:  # look for context in the matched
                if context in matched:
                    return matched
        return None

    def is_class(self, classname, contexts=[]):
        if self.find_class(classname, contexts=contexts) is not None:
            return True
        else:
            return False

    def is_builtin_class_instance(self, obj):
        return obj.__class__.__module__ == 'builtins'
