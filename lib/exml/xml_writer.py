#! /usr/bin/python
#
# Writer class for XML Element
#

from expression_parser.lib.exceptions.expr_error import RunTimeError
from xml.etree import ElementTree, cElementTree
from xml.dom import minidom

class XMLWriter(object):
  """
  Receives the output data from workflow manager
  and write output data to provided channel.
  """
  def __init__(self, output_file, root="expression"):
    """
    Initialization method for XML Writer class
    """
    self.output_file = output_file
    self.root = root

  @property
  def root(self):
    """
    Return root XML element of tree
    """
    return self._root

  @root.setter
  def root(self, value):
    """
    Setting up the root value of XML Tree
    """
    self._root = ElementTree.Element(value)
    return self._root

  def write_data(self, data, tag="result"):
    """
    Associate data result and attributes to XML Element
    and attach that element to root tree.
    Args:
      data: Contains data awhich need to written XML Element
      tag: Tag name under which data will be associated.
    """
    element = ElementTree.SubElement(self.root, tag)
    # Setup output value to XML element text
    if hasattr(data, "output"):
      element.text = str(data.output)
    # Setup output attributes to XML element attrib
    if hasattr(data, "output_attributes"):
      attributes = data.output_attributes
      if attributes.has_key("id"):
        attrib = {'id': attributes['id']}
        element.attrib = attrib
    return True

  def __enter__(self):
    """
    Entry method for XML Writer run time context.
    """
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    """
    Dumps XML Element tree output to file
    Args:
      exc_type: Exception Type
      exc_val: Exception value
      exc_tb: Exception trace back
    """
    try:
      # Build pretty XML output string from result tree
      tree_string = minidom.parseString(ElementTree.tostring(self.root)).toprettyxml()
      # Build XML output tree from pretty xml tree
      output = ElementTree.ElementTree(ElementTree.fromstring(tree_string))
      # Write output to the file
      output.write(self.output_file, encoding='utf-8')
    except:
      err_msg = "Not able to write XML output !!"
      raise RunTimeError(err_msg)
