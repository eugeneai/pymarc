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
from pymarc.marcxml import parse_xml
from pymarc.marcxml import record_to_xml, record_to_xml_node

DIGITS=set("0123456789")

class XmlHandler(pymarc.marcxml.XmlHandler):
    """Handler for very strange Russian XML format for RUSMARC.
    """

    def __init__(self, strict=False, normalize_form=None):
        super(XmlHandler,self).\
            __init__(strict=strict, normalize_form=normalize_form)
        self._indicators = None

    def startElementNS(self, name, qname, attrs):
        # NO Stricts
        try:
            element, parameter = name[1].split(".")
        except ValueError:
            element = name[1]

        if element == "rusmarc":
            self._record = Record()
        elif element == "mrk":
            self._record.leader = ""
        elif element.startswith("m_"):
            pass  # See endElementNS for implementation
        elif element == "IND":
            self._indicators = parameter.replace("_"," ")
            self._field.subfields = []
        elif element == "FIELD":
            self._field = Field(parameter, [" ", " "])
        elif element == "SUBFIELD":
            self._subfield_code = parameter
        elif element == "RECORDS":
            pass
        else:
            raise RuntimeError("cannot process tag %s" % element)

        self._text = []

    def endElementNS(self, name, qname):
        element = name[1]

        text = u''.join(self._text)

        if element == "rusmarc":
            record = self.convert_record(self._record)
            self._record = None
            self.process_record(record)
        elif element == "mrk":
            pass
        elif element.startswith("m_"):
            self._record.leader += text
        elif element.startswith("FIELD"):
            if self._field.tag.startswith("00"):
                self._field.data = text
            self._record.add_field(self._field)
            self._field = None
        elif element.startswith("SUBFIELD"):
            if self._subfield_code in [DIGITS] and self._field.tag.startswith("00"):
                self._field.data = text
            else:
                self._field.subfields.append(self._subfield_code)
                self._field.subfields.append(text)
            self._subfield_code = None
        elif element.startswith("IND"):
            if not self._field.tag.startswith("00"):
                self._field.indicator1, self._field.indicator2 = \
                    self._field.indicators = self._indicators
            self._indicators=None
        elif element == "RECORDS":
            pass
        else:
            raise RuntimeError("cannot process tag %s" % element)

    def convert_record(self, record):
        return record


def map_xml(function, *files):
    """
    map a function onto the file, so that for each record that is
    parsed the function will get called with the extracted record

    def do_it(r):
      print(r)

    map_xml(do_it, 'marc.xml')
    """
    handler = XmlHandler()
    handler.process_record = function
    for xml_file in files:
        parse_xml(xml_file, handler)


def parse_xml_to_array(xml_file, strict=False, normalize_form=None):
    """
    parse an xml file and return the records as an array. If you would
    like the parser to explicitly check the namespaces for the MARCSlim
    namespace use the strict=True option.
    Valid values for normalize_form are 'NFC', 'NFKC', 'NFD', and 'NFKD'. See
    unicodedata.normalize info.
    """
    handler = XmlHandler(strict, normalize_form)
    parse_xml(xml_file, handler)
    return handler.records
