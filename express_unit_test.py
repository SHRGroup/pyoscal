import os
import sys
import unittest

sys.path.insert(0, './pyoscal/')
# Necessary to below path insert
from pyoscal.OSCAL import OSCAL  # noqa: E402
from pyoscal.ComponentDef import (  # noqa: E402
    ComponentDefinition, Component, Capability
)
script_dir = os.path.dirname(os.path.abspath(__file__))


class TestCompDef(unittest.TestCase):

    def createOSCAL(self):
        filepath = os.path.join(
            script_dir,
            'oscal-content/examples/catalog/xml/basic-catalog.xml'
        )
        oscal = OSCAL()
        oscal.parse_file(filepath)
        return oscal

    def test_createNew(self):
        cdef = ComponentDefinition(
            title="Test Component Defintion",
            description="Description of Test Component"
        )
        component = Component(
            title="Test Component"
        )
        component.add_control(
            controlid='XX-1',
            narrative='This is how I meet XX-1'
        )
        cdef.add_component(component)
        xml = cdef.export()
        self.assertEqual(
            len(xml),
            912
        )

    def test_multipleComponents(self):
        cdef = ComponentDefinition(
            title="Test Component Defintion",
            description="has a capability composed of multiple components"
        )
        component1 = Component(
            title="Test Component"
        )
        component1.add_control(
            controlid='XX-1',
            narrative='This is how I meet XX-1'
        )

        component2 = Component(
            title="Test Component"
        )
        component2.add_control(
            controlid='XX-2',
            narrative='This is how I meet XX-2'
        )
        component2.add_property(
            name='propname', value='propvalue'
        )
        cdef.add_component(component1)
        cdef.add_component(component2)

        capability = Capability(
            name="Full System"
        )
        capability.add_component(component1.uuid)
        capability.add_component(component1.uuid)
        capability.add_control(
            controlid='XX-3',
            narrative='this is how the system meets a control'
        )
        cdef.add_capability(capability)

        xml = cdef.export()
        self.assertEqual(
            len(xml),
            2207
        )


if __name__ == '__main__':
    unittest.main()
