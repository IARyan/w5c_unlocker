#!/usr/bin/python -tt

"""
LG Optimus Exceed 2 VS450PP (w5c) bootloader unlock tool
"""

import sys
import os

def in_path(program):
  """
  Checks if a program is in the PATH.
  """
  fpath, fname = os.path.split(program)
  if fpath:
    if os.path.isfile(program) and os.access(program, os.X_OK):
      return True
  else:
    for path in os.environ["PATH"].split(os.pathsep):
      path = path.strip('"')
      exe_file = os.path.join(path, program)
      if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
        return True

    return False

def check_dependencies(dependencies):
  """
  Verifies dependencies are installed.
  """
  for dependency in dependencies:
    print "Checking [-] %s ..." % (dependency)
    if not is_installed(dependency):
      print "[-] %s was not found in the path is it installed?" % (dependency)
      sys.exit(1)

def fastboot(command):
  """
  Runs provided fastboot command.
  """
  for dependency in dependencies:
    print "Checking [-] %s ..." % (dependency)
    if not is_installed(dependency):
      print "[-] %s was not found in the path is it installed?" % (dependency)
      sys.exit(1)

def adb(command):
  """
  Runs provided adb command.
  """
  for dependency in dependencies:
    print "Checking [-] %s ..." % (dependency)
    if not is_installed(dependency):
      print "[-] %s was not found in the path is it installed?" % (dependency)
      sys.exit(1)
