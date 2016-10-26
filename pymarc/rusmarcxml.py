"pymarc rusmarcxml file."

import logging
from xml.sax import make_parser
from xml.sax.handler import ContentHandler, feature_namespaces
import unicodedata

import six

try:
    import xml.etree.ElementTree as ET  # builtin in Python 2.5
except ImportError:
    import elementtree.ElementTree as ET

from pymarc import Record, Field, MARC8ToUnicode

#XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
#MARC_XML_NS = "http://www.loc.gov/MARC21/slim"
#MARC_XML_SCHEMA = "http://www.loc.gov/MARC21/slim http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd"

import pymarc.marcxml
from pymarc.marcxml import parse_xml, map_xml, parse_xml_to_array
from pymarc.marcxml import record_to_xml, record_to_xml_node

class XmlHandler(pymarc.marcxml.XmlHandler):
    """Handler for very strange Russian XML format for RUSMARC.
    """

    def startElementNS(self, name, qname, attrs):
        # NO Stricts
        element = name[1]
        print ("Start:", element)

    def endElementNS(self, name, qname):
        element = name[1]
        print ("End:", element)
