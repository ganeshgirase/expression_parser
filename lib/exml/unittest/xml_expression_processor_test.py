#! /usr/bin/python

import unittest
import expression_parser.lib.exml.xml_reader
import expression_parser.lib.exml.xml_expression_processor
import xml.etree.ElementTree as ET

from expression_parser.lib.exml.xml_reader import XMLReader
from expression_parser.lib.exml.xml_expression_processor import XMLExpressionProcessor

class TestXMLExpressionProcessor(unittest.TestCase):

  def test_evaluate_expression(self):
    root = XMLReader.GetData("data002.xml")
    for element in root:
      element = XMLExpressionProcessor.process_records(element)
      print element.output, element.output_attributes
      #self.assertEqual(element.output, 14, "Unable to process expression")

  def test_addition(self):
    test_data = """
    <data>
	<item>2</item>
	<item>3</item>
	<item>5</item>
    </data>
    """
    data_root = ET.fromstring(test_data)
    addition = XMLExpressionProcessor.addition(data_root.getchildren())
    self.assertEqual(addition, 10, "Error: 'addition' method giving wrong result !!")

  def test_subtraction(self):
    test_data = """
    <data>
	<minuend>7</minuend>
	<subtrahend>3</subtrahend>
    </data>
    """
    data_root = ET.fromstring(test_data)
    difference = XMLExpressionProcessor.subtraction(data_root.getchildren())
    self.assertEqual(difference, 4, "Error: 'subtraction' method giving wrong result !!")

  def test_addition(self):
    test_data = """
    <data>
	<factor>2</factor>
	<factor>3</factor>
	<factor>5</factor>
    </data>
    """
    data_root = ET.fromstring(test_data)
    multiplication = XMLExpressionProcessor.multiplication(data_root.getchildren())
    self.assertEqual(multiplication, 30,
      "Error: 'multiplication' method giving wrong result !!")

  def test_division(self):
    test_data = """
    <data>
	<dividend>21</dividend>
	<divisor>3</divisor>
    </data>
    """
    data_root = ET.fromstring(test_data)
    division = XMLExpressionProcessor.division(data_root.getchildren())
    self.assertEqual(division, 7, "Error: 'division' method giving wrong result !!")

if __name__ == "__main__":
  unittest.main()
