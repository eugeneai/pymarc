import unittest
from pymarc.rusmarcxml import parse_xml_to_array


class TestLoadRUXMLMARC(unittest.TestCase):
    def setUp(self):
        self.recs = parse_xml_to_array('test/rusmarc.xml')

    def test_load(self):
        records = self.recs
        self.assertEqual(len(records), 4)
        for rec in records:
            print(rec)

    # def test_big_load(self):
    #     records = parse_xml_to_array('test/exp.XML')
    #     self.assertEqual(len(records), 11596)

    def test_marc(self):
        recs = self.recs
        for rec in recs:
            rec.force_utf8 = True
            ser = rec.as_marc()
            print(ser)

    def test_json(self):
        recs = self.recs
        for rec in recs:
            assert rec.as_json()

    def test_dict(self):
        recs = self.recs
        for rec in recs:
            assert rec.as_dict()
