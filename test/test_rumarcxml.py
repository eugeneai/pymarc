import unittest
from pymarc.rusmarcxml import parse_xml_to_array
import os
import textwrap
from six import BytesIO, StringIO, u, binary_type

class LoadRUXMLMARC(unittest.TestCase):
    def test_load(self):
        records = parse_xml_to_array('test/rusmarc.xml')
        self.assertEqual(len(records), 4)
