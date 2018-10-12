#
# Author: Ganesh Girase
#         
"""This module defines Expr base exception."""

import sys

class ExprError(Exception):

  """Base class for all Expression Parser exceptions.
  """
  def __init__(self, message='', **kwargs):
    """Constructor for the base framework exception.

      Args:
        message(str): The exception message.
    """
    super(ExprError, self).__init__(message)

class UnsupportedExpressionError(ExprError):
  """
  If any expression which isn't supported,
  this exception will be raised by caller
  """
  pass

class RunTimeError(ExprError):
  """
  If any error occurs while running workflow,
  this exception will be raised by caller.
  """
  pass

class UnsupportedExpressionType(ExprError):
  """
  If any expression file type which isn't supported,
  this exception will be raised by caller.
  """
  pass
class FileOperationsError(ExprError):
  """
  If any expression file type which isn't supported,
  this exception will be raised by caller.
  """
  pass





   
