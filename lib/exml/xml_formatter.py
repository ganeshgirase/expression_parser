#! /usr/bin/python
#
# Result formatter calass for xml elements
#
import expression_parser.lib.base_formatter
from expression_parser.lib.base_formatter import Formatter

class XMLResultFormatter(Formatter, object):
  """
  Class which retrieve output and attributes from result
  XML element and setup output result and attributes.
  """
  def __init__(self, xml_output_element):
    """
    Initializes output formatter variables
    """
    super(XMLResultFormatter, self).__init__()
    self.output = xml_output_element.text
    self.output_attributes = xml_output_element.attrib
