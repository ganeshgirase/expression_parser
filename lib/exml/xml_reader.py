#! /usr/bin/python
#
# Reads XML data and returns data in logical chunk.
#

import sys
import xml.etree.ElementTree as ET

class XMLReader:
  """
  Reads the xml file and returns root
  """
  @classmethod
  def read_data(cls, input_file=None, break_attrib=None):
    """
    1. Reads xml file
    2. Sends data in logical chunk, if asked.

    Args:
      input_file: XML file path
      break_attrib: Attribute on which xml data will be break
    Returns:
      xmldata: XML data.
    """
    # Read xml file
    root = cls._get_file_reader(input_file)
    # Send every expression from xml data
    for child in root:
      yield child

  @classmethod
  def _get_file_reader(self, xml_input_file):
    """
    Opens file in XML reader and returns head of data
    Args:
      input_file: XML file path
    Returns:
      root: head of the xml data tree
    """
    try:
      tree = ET.parse(xml_input_file)
      root = tree.getroot()
      return root
    except:
      err_msg = "Unable to parse input xml file !! \n"
      sys.stderr.write(err_msg)
      err = sys.exc_info()[0]
      raise(err)
