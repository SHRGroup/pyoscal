import os
import sys
import unittest

sys.path.insert(0, './pyoscal/')
from pyoscal.core.OSCAL import OSCAL  # noqa: E402 # Necessary to below path insert

script_dir = os.path.dirname(os.path.abspath(__file__))


class TestCatalog(unittest.TestCase):

    def createOSCAL(self):
        filepath = os.path.join(
            script_dir,
            'oscal-content/examples/catalog/yaml/basic-catalog.yaml'
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
            '74c8ba1e-5cd4-4ad1-bbfd-d888e2f6c724')
        self.assertEqual(
            str(catalog.metadata.title),
            'Sample Security Catalog *for Demonstration* and Testing')


if __name__ == '__main__':
    unittest.main()
