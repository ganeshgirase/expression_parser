#! /usr/bin/python
#
# This module parses expression data files,
# evluates expression and writes to output file
#
import optparse
import os
import sys
import expression_parser.lib.expression_types_factory
import expression_parser.lib.exceptions.expr_error

from expression_parser.lib.expression_types_factory import ExpressionTypesFactory
from expression_parser.lib.exceptions.expr_error import RunTimeError

class ExpressionParser(object):
  """
  This class performs following task
    1. Read expression data from data files.
    2. Evaluate expression.
    3. Write expression result to output files.
  """
  def __init__(self, input_file, input_dir, output_file=None, output_dir=None):
    """
    Intialization method for ExpressionParser project
    Args:
      input_file: Input file for expression processing
      input_dir: Directory from where input file will be picked
                 for expression processing
      output_file: Output file where output data will be written.
      output_dir: Output fdirectory where output file will be written.
    """
    self.input_dir = input_dir
    # if output directory not provided,
    # output ile will be written to current working directory.
    if output_dir is None:
      output_dir = os.getcwd()
    self.output_dir = output_dir

    self.input_file = input_file
    self.output_file = output_file

  @property
  def output_file(self):
    """
    Getter method for output file
    """
    return self._output_file

  @output_file.setter
  def output_file(self, filepath):
    """
    Setter method for output file
    """
    if filepath is None and self.input_file is not None:
      (filename, ext) = os.path.splitext(os.path.basename(self.input_file))
      self._output_file = "%s_result%s" %(filename, ext)
      # If output directory is provided, output file will
      # be written to putput directory
      if self.output_dir:
        self._output_file = "%s/%s" %(self.output_dir, self._output_file)
    else:
      self._output_file = filepath

  def run_expression_parser_workflow(self, ext, input_file, output_file=None):
    """
    This method will run expression parser workflow.
    Below steps will be performed.
    Steps:
      1. Read expression input file.
      2. Process input file.
      3. Write expression result data to output file.
    Args:
      ext: Extension of input file
      input_file: Input file
      output_file: Output file
    Raises:
      RunTimeError: Raises Runtimeerror if any issue occurs/
    """
    obj = ExpressionTypesFactory()
    # If Factory class does not support for other extensions,
    # it will not be processed.
    if not hasattr(obj, ext):
      sys.stdout.write("Files of type '%s' is not supportd. Skipping..\n" %(ext))
      return

    self.input_file = input_file
    self.output_file = output_file
    try:
      # Will get the reader, processor, write object from
      # expression factory class
      (reader, processor, writer) = getattr(obj, ext)()
      # RunTimeContext will be open for Writer class
      with writer(self.output_file) as wd:
        for expression in reader.read_data(self.input_file):
          # Process every expression from input file
          output_data = processor.process_data(expression)
          # Write output data to output file
          wd.write_data(output_data)
      sys.stdout.write("Output written to '%s'\n" %(self.output_file))
    except:
      err_msg = "Unable to process expression for input '%s'" %(self.input_file)
      raise RunTimeError(err_msg)

  def get_input_files_list(self):
    """
    Will return list of input files
    """
    if self.input_file:
      yield self.input_file
    if self.input_dir:
      for (dirpath, _, filenames) in os.walk(self.input_dir):
        for file in filenames:
          filepath = os.path.join(dirpath, file)
          yield filepath

  def run(self):
    """
    This method runs the expression parser workflow.
    It will list all files from input directory and
    will run parser workflow on every file.
    """
    # Factory class for expression types.
    for filepath in self.get_input_files_list():
      if os.path.exists(filepath):
        (_, ext) = os.path.splitext(filepath)
        ext = ext.lstrip(".")
        sys.stdout.write("Processing file %s ..\n" %(filepath))
        self.run_expression_parser_workflow(ext, filepath)

if __name__ == "__main__":
  DESCRIPTION = """This script is used to process the expression provided
    in various formats like XML, CSV etc. Once it's proccessed, it will be
    written to output file"""

  def usage():
    """Print usage of the script."""
    sys.stderr.write("""\tUsage: python {0}
                 --input_file <input expression file>
                 --output_file <output data file>
                 --input_dir <From where input files will be read>
                 --output_dir <Data will writtento this directory>"
    For more info, goto the help section by -h/--help.
    """.format(__file__))


  # Define the command line arguments.
  parser = optparse.OptionParser(description=DESCRIPTION)
  parser.add_option('-i', '--input_file', action="store",
                    dest="input_file",
                    help="Input file you need to process")
  parser.add_option('-a', '--input_dir', action="store",
                    dest="input_dir",
                    help="Input directory where all input file are stored")
  parser.add_option('-o', '--output_file', action="store",
                    dest="output_file",
                    help="Output file where processed data will be written"
                    "if not passed, input file naming will be used to write output file"
                    "For e.g., for input file data001.xml, output file will be data001_result.xml"
                    )
  parser.add_option('-b', '--output_dir', action="store",
                    dest="output_dir",
                    help="Output directory where result data files will be written.")


  # Parse the arguments.
  options, args = parser.parse_args()
  if options.input_file is None and options.input_dir is None:
    sys.stderr.write("Nothing to do !!\n")
    usage()
  ## Creates object of Expression Parser class
  obj = ExpressionParser(options.input_file, options.input_dir,
                         options.output_file, options.output_dir)
  # Call workflow
  obj.run()

