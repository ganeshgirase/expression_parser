#! /usr/bin/python
#
# Factory class for various expression types
# like XML, CSV, TEXT etc.


import expression_parser.lib.exml.xml_reader
import expression_parser.lib.exml.xml_expression_processor
import expression_parser.lib.exml.xml_writer

from expression_parser.lib.exml.xml_reader import XMLReader
from expression_parser.lib.exml.xml_expression_processor \
  import XMLExpressionProcessor
from expression_parser.lib.exml.xml_writer import XMLWriter


class ExpressionTypesFactory(object):
   """
   This class is configuration factory for various
   expression types and allows caller programs to
   receive respective object for  specifc types.
   """
   def __init__(self):
     """
     Initialization method
     """
     self.reader = None
     self.processor = None
     self.writer = None

   def xml(self):
     """
     Factory method for XML expression types
     Args:
       None
     Returns:
       reader: XMLReader class
       processor: XMLExpressionProcessor class
       writer: XMLExpressionProcessor object
     """
     self.reader = XMLReader
     self.processor = XMLExpressionProcessor
     self.writer = XMLWriter
     return (self.reader, self.processor, self.writer)
