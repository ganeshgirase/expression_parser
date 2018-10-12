#! /usr/bin/python
#
# This program contains generic methods 
# for all arithmetic operatins

import sys

class MathOperations:

  @staticmethod
  def sum(items):
    """
    Calculate sum of all elements 
    Args
      items: List of integers/floats
    Returns:
      sum: Sum of all elements from items
    """
    if items is None or len(items) == 0:
      return None
    try:
        return sum(items)
    except:
      msg = "Error while addition: %s" %sys.exc_info()[0]
      sys.stderr.write(msg)
      raise

  @staticmethod
  def subtract(minuend, subtrahend):
    """
    Subtract subtrahend from minuend.
    Args
      minuend:   
      subtrahend: 
    Returns:
      difference: Result of subtraction subtrahend from minuend
    """
    if minuend is None or subtrahend is None:
      return None
    try:
      difference = minuend - subtrahend
      return difference
    except:
      msg = "Error while subtraction: %s" %sys.exc_info()[0]
      sys.stderr.write(msg)
      raise

  @staticmethod
  def multiply(items):
    """
    Multiply each elements from received items.
    Args
      items: List of integers/floats
    Returns:
      multiplication: Total of multiplication
    """
    if items is None or len(items) == 0:
      return None
    multiplication = 1
    try:
      for item in items:     
        multiplication = multiplication * item 
    except:
      msg = "Error while multiplication: %s" %sys.exc_info()[0]
      sys.stderr.write(msg)
      raise
    return multiplication

  @staticmethod
  def divide(dividend, divisor):
    """
    Division
    Args
      items: List of integers/floats
    Returns:
      division: Result of divident divided by divisor
    """
    if dividend is None or divisor is None:
      return None
    try:
      division = dividend / divisor
      return division
    except:
      msg = "Error while divisiron: %s" %sys.exc_info()[0]
      sys.stderr.write(msg)
      raise


