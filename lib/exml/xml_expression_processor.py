#! /usr/bin/python
#
#  Aurhor: Ganesh Girase
#  Parses xml expressions and evaluates same.
#

import sys
import expression_parser.util.math_operations

from expression_parser.lib.exml.xml_formatter import XMLResultFormatter
from expression_parser.lib.exceptions.expr_error import UnsupportedExpressionError
from expression_parser.util.math_operations import MathOperations

class XMLExpressionProcessor:
  """
  1. Parses xml expression
  2. Evaluates xml expressions
  """
  @classmethod
  def process_data(cls, element):
    """
    This is caller method called by workflow manager.
    Args
      element: XML output Element
    Returns:
      output: Formatted result of xml elements.
    """
    output = cls._evaluate_expression(element)
    return XMLResultFormatter(output)

  @classmethod
  def _evaluate_expression(cls, expression_element):
    """
    Evaluates every expression recursively.
    Args
      expression_element: XML Element
    Returns:
      result: Result of expression evaluation
    """
    if expression_element is None:
      return None
    tag = expression_element.tag
    if hasattr(cls, tag) is True:
      # Get specific expression method and apply that expression on element
      apply_expression_method = getattr(cls, tag)
      text_result = apply_expression_method(expression_element.getchildren())

      #Overwrites xml element with new resulted text
      output_element = cls.overwrite_xml_element(expression_element,
                         text=text_result)
      return output_element
    else:
      err_msg = "Expression type '%s' is not supported !!" %tag
      raise UnsupportedExpressionError(err_msg)

  @classmethod
  def get_resolved_descendancy(cls, elements):
    """
    Resolve descendancy of xml successive childs
    and return result in text.
    Args:
      elements: List of xml elements
    Returns:
      element: Every descendancy resolved element
    """
    for element in elements:
      childs = element.getchildren()
      # Element does have children inside which
      # needs to be processed recursively
      if len(childs) > 0:
        children = childs[0]
        resolved_element = cls._evaluate_expression(children)
        element = cls.overwrite_xml_element(element,
                    text=resolved_element.text)
      yield element

  @classmethod
  def addition(cls, elements):
    """
    Adds all elements and return sum of elements
    Args
      elements: List of xml elements.
    Returns:
      result: Sum of all xml elements
    """
    numbers = []
    for element in cls.get_resolved_descendancy(elements):
      # Parse element and get the number text associated with it.
      if element.tag == 'item':
        num = element.text
      else:
        raise UnsupportedExpressionError("Invalid tag: '%s'" %element.tag)
      # Append resultant number
      numbers.append(int(num))
    if len(numbers) > 0:
      addition = MathOperations.sum(numbers)
      return addition

  @classmethod
  def subtraction(cls, elements):
    """
    Subtracts subtrahend from minuend
    Args
      elements: List of xml elements.
    Returns:
      result: Subtraction of xml elements
    """
    numbers = {'minuend': None, 'subtrahend': None}
    for element in cls.get_resolved_descendancy(elements):
      key = element.tag
      if numbers.has_key(key):
        numbers[key] = int(element.text)
      else:
        raise UnsupportedExpressionError("Invalid tag: '%s'" %element.tag)
    result = MathOperations.subtract(**numbers)
    return result

  @classmethod
  def multiplication(cls, elements):
    """
    Multiplication of all factors
    Args
      elements: List of xml elements.
    Returns:
      result: Multiplication of xml elements
    """
    factors = []
    for element in cls.get_resolved_descendancy(elements):
      # Parse element and get the number text associated with it.
      if element.tag == 'factor':
        num = element.text
      else:
        raise UnsupportedExpressionError("Invalid tag: '%s'" %element.tag)
      # Append resultant number
      factors.append(int(num))
    if len(factors) > 0:
      result = MathOperations.multiply(factors)
      return result

  @classmethod
  def division(cls, elements):
    """
    Divide dividend by divisor
    Args
      elements: List of xml elements.
    Returns:
      result: Division of dividend by divisor
    """
    numbers = {'dividend': None, 'divisor': None}
    for element in cls.get_resolved_descendancy(elements):
      key = element.tag
      if numbers.has_key(key):
        numbers[key] = int(element.text)
      else:
        raise UnsupportedExpressionError("Invalid tag: '%s'" %element.tag)
    result = MathOperations.divide(**numbers)
    return result

  @classmethod
  def overwrite_xml_element(cls, element, text=None, attrib=None, tail=None):
    """
    Overwrite xml element with new properties
    Args:
      element: XML element to overwrite
      text: XML element text
      attrib: XML element attributes
      tail: XML element tail text
    Returns:
      element:XML element overwritten with new properties.
    """
    if text is None:
      text = element.text
    if attrib is None:
      attrib = element.attrib.copy()
    if tail is None:
      tail = element.tail

    # Clear XML Element
    element.clear()

    # Restore element with its properties
    element.attrib = attrib
    element.tail = tail
    element.text = text
    element.set('updated', 'yes')
    return element
