import unittest
from pymarc.rusmarcxml import parse_xml_to_array
import os
import textwrap
from six import BytesIO, StringIO, u, binary_type
from pymarc.rusmarcxml import CFIELDS
from pprint import pprint
from pymarc import Record


class TestLoadRUXMLMARC(unittest.TestCase):
    def test_load(self):
        records = parse_xml_to_array('test/rusmarc.xml')
        self.assertEqual(len(records), 4)
        for rec in records:
            print(rec)

    # def test_big_load(self):
    #     records = parse_xml_to_array('test/exp.XML')
    #     self.assertEqual(len(records), 11596)
