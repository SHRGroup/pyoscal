import os
import sys
import re
import unittest

sys.path.insert(0, './pyoscal/')
from pyoscal.OSCAL import OSCAL  # pylint: disable=import-error # noqa: E402

script_dir = os.path.dirname(os.path.abspath(__file__))


class TestCatalog(unittest.TestCase):

    def createOSCAL(self):
        filepath = os.path.join(
            script_dir,
            'oscal-content/examples/catalog/xml/basic-catalog.xml'
        )
        oscal = OSCAL()
        oscal.parse_file(filepath)
        return oscal

    def test_parseCatalog(self):
        oscal = self.createOSCAL()
        self.assertEqual(len(oscal.objects.get('Catalog')), 1)

    def test_catalogContent(self):
        oscal = self.createOSCAL()
        catalog = oscal.objects.get('Catalog')[0]
        self.assertEqual(
            str(catalog.uuid),
            '22054d80-252f-4ab8-ae9c-5bf69c9109a9')
        self.assertEqual(
            str(catalog.metadata.title),
            'Sample Security Catalog <em>for Demonstration</em> and Testing')


class TestProfile(unittest.TestCase):

    def createOSCAL(self):
        filepath = os.path.join(
            script_dir,
            'oscal-content/fedramp.gov/xml/FedRAMP_HIGH-baseline_profile.xml'
        )
        oscal = OSCAL()
        oscal.parse_file(filepath)
        return oscal

    def test_parseProfile(self):
        oscal = self.createOSCAL()

    def test_countCalls(self):
        oscal = self.createOSCAL()
        count = 0
        for profile in oscal.objects.get('Profile'):
            for imp in profile.imports:
                for inc in imp.include_controls:
                    count += len(inc.with_id)
        self.assertEqual(count, 421)


class TestSSP(unittest.TestCase):

    def createOSCAL(self):
        filepath = os.path.join(
            script_dir,
            'oscal-content/examples/ssp/xml/ssp-example.xml'
        )
        oscal = OSCAL()
        oscal.parse_file(filepath)
        return oscal

    def test_parseSSP(self):
        oscal = self.createOSCAL()
        self.assertEqual(len(oscal.objects.get('System_Security_Plan')), 1)

    def test_SSPContent(self):
        oscal = self.createOSCAL()
        ssp = oscal.objects.get('System_Security_Plan')
        self.assertEqual(len(ssp), 1)


class TestComponentDef(unittest.TestCase):

    def createOSCAL(self):
        file = 'oscal-content/examples/component-definition/' + \
               'xml/example-component.xml'
        filepath = os.path.join(
            script_dir,
            file)
        oscal = OSCAL()
        oscal.parse_file(filepath)
        return oscal

    def test_parseCDEF(self):
        oscal = self.createOSCAL()
        self.assertEqual(len(oscal.objects.get('Component_Definition')), 1)

    def test_CDEFContent(self):
        oscal = self.createOSCAL()
        cdef = oscal.objects.get('Component_Definition')[0]
        self.assertEqual(
            cdef.metadata.title.prose,
            'Test Component Definition'
        )
        self.assertEqual(
            str(cdef.metadata.parties[0].uuid),
            'ee47836c-877c-4007-bbf3-c9d9bd805a9a'
        )

        component = cdef.components[0]
        self.assertEqual(
            len(component.control_implementations),
            2
        )

        cont_imp = component.control_implementations[0]
        self.assertEqual(
            str(cont_imp.uuid),
            '22dbff65-9729-449f-9dfc-4e5fee0906de'
        )
        self.assertEqual(
            len(cont_imp.implemented_requirements),
            1
        )
        self.assertIn(
            'FedRAMP',
            str(cont_imp.implemented_requirements[0].description),
        )


class TestExport(unittest.TestCase):

    def createOSCAL(self, filepath):
        oscal = OSCAL()
        oscal.parse_file(filepath)
        return oscal

    def getExample(self, subpath):
        return os.path.join(
            script_dir,
            'oscal-content/examples',
            subpath
        )

    def test_component_output(self):
        filepath = self.getExample(
            'component-definition/xml/example-component.xml')
        with open(filepath, encoding='utf-8') as src:
            src_text = src.read()

        oscal = self.createOSCAL(filepath)
        out_text = oscal.export()
        self.assertEqual(
            len([c for c in src_text if c == '<']),
            len([c for c in out_text if c == '<'])
        )

    def test_catalog_output(self):
        filepath = self.getExample(
            'catalog/xml/basic-catalog.xml')
        with open(filepath, encoding='utf-8') as src:
            src_text = src.read()
            src_text = re.sub("(<!--.*?-->)", "", src_text, flags=re.DOTALL)

        oscal = self.createOSCAL(filepath)
        out_text = oscal.export()
        self.assertEqual(
            len([c for c in src_text if c == '<']),
            len([c for c in out_text if c == '<'])
        )

    def test_ssp_output(self):
        filepath = self.getExample(
            'ssp/xml/ssp-example.xml')
        with open(filepath, encoding='utf-8') as src:
            src_text = src.read()

        oscal = self.createOSCAL(filepath)
        out_text = oscal.export()
        self.assertEqual(
            len([c for c in src_text if c == '<']),
            len([c for c in out_text if c == '<'])
        )

if __name__ == '__main__':
    unittest.main()
