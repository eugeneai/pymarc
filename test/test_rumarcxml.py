import unittest
from pymarc.rusmarcxml import parse_xml
import os
import textwrap
from six import BytesIO, StringIO, u, binary_type

class LoadRUXMLMARC(unittest.TestCase):

    def test_load(self):
        self.assertEqual(0,0)
