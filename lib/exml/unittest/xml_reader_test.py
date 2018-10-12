#! /usr/bin/python

import unittest

import expression_parser.lib.exml.xml_reader
from expression_parser.lib.exml.xml_reader import XMLReader

class TestXMLReader(unittest.TestCase):

  def test_get_data(self):
    reader = XMLReader.GetData
    root = reader("data001.xml")
    for child in root:
      self.assertEqual(child.__class__.__name__, "Element",
        "Not able to parse xml file")

if __name__ == "__main__":
  unittest.main()
