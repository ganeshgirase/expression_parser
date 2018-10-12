#! /usr/bin/python
#
# Base class for all formatter.
#

class Formatter(object):
  # Base class for all formatter
  def __init__(self):
    # Initialization method
    # This method can be overriden to set up the value of
    # output and output_attributes instance variable
    pass
  @property
  def output(self):
    """
    Get output value
    Args: None
    Returns:
      Returns class instance output variable
    """
    return self._output

  @output.setter
  def output(self, value):
    """
    Set output value
    Args:
      value: Value which is going to be associated with output
    """
    self._output = value
