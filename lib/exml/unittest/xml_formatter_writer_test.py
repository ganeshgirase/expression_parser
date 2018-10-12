#! /usr/bin/python

import expression_parser.lib.exml.xml_writer
import os
import unittest

import xml.etree.ElementTree as ET
from expression_parser.lib.exml.xml_writer import XMLWriter
from expression_parser.lib.exml.xml_formatter import XMLResultFormatter

class TestXMLWriter(unittest.TestCase):

  def test_xml_formatter_writer(self):
    input = ['<result id="1">9</result>',
             '<result id="2">1</result>',
             '<result id="3">5</result>',
             '<result id="4">9</result>']
    output_file = "test.xml"
    if os.path.exists(output_file):
      os.unlink(output_file) 
    with XMLWriter(output_file, "expression") as obj:
      for xml in input:
        element = ET.fromstring(xml)
        output_data= XMLResultFormatter(element)
        obj.write(output_data)
    self.assertEqual(os.path.exists(output_file), True, "Not able to write output to file !!")
    self.assertEqual(os.path.getsize(output_file), 134, "Wrong data to output file !! ")
    

if __name__ == "__main__":
  unittest.main()
