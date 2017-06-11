import unittest
from pymarc.rusmarcxml import parse_xml_to_array


class TestLoadRUXMLMARC(unittest.TestCase):
    def test_load(self):
        records = parse_xml_to_array('test/rusmarc.xml')
        self.assertEqual(len(records), 4)
        for rec in records:
            print(rec)

    # def test_big_load(self):
    #     records = parse_xml_to_array('test/exp.XML')
    #     self.assertEqual(len(records), 11596)
