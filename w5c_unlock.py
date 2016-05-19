#!/usr/bin/python -tt

"""
LG Optimus Exceed 2 VS450PP (w5c) bootloader unlock tool
"""

import argparse
import utils
import sys
import os
from subprocess import check_output

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
    if not in_path(dependency):
      print "[-] %s was not found in the path is it installed?" % (dependency)
      sys.exit(1)

def fastboot(command):
  """
  Runs provided fastboot command.
  """
  try:
   return check_output([command])
  except subprocess.CalledProcessError:
    print e.output
    sys.exit(1)

def adb(command):
  """
  Runs provided adb command.
  """
  try:
   return check_output([command])
  except subprocess.CalledProcessError:
    print e.output
    sys.exit(1)

def unlock_bootloader():
  """
  Unlocks the LG Optimus Exceed 2 bootloader.
  """
  try:
   print "[+] Unlocking bootloader" 
  except subprocess.CalledProcessError:
    print e.output
    sys.exit(1)


def lock_bootloader():
  """
  Runs provided adb command.
  """
  try:
   return check_output([command])
  except subprocess.CalledProcessError:
    print e.output
    sys.exit(1)

def fastboot_mode():
  """
  Runs provided adb command.
  """
  try:
   return check_output([command])
  except subprocess.CalledProcessError:
    print e.output
    sys.exit(1)

def download_mode():
  """
  Runs provided adb command.
  """
  try:
   return check_output([command])
  except subprocess.CalledProcessError:
    print e.output
    sys.exit(1)


def main():
  try:
    # Create command line argument parser.
    parser = argparse.ArgumentParser(description="LG Optimus Exceed 2 VS450PP (w5c) Bootloader Unlock Tool", version=('%(prog)s 0.1'))
    parser.add_argument('-u', '--unlock', action='store_true', default=False, dest="unlock_bootloader", help="Unlock Optimus Exceed 2 bootloader")
    parser.add_argument('-l', '--lock',action='store_true', default=False, dest="lock_bootloader", help="Lock Optimus Exceed 2 bootloader")
    parser.add_argument('-f', '--fastboot-mode', action='store_true', default=False, dest="fastboot_mode", help="Set Optimus Exceed 2 to fastboot mode")
    parser.add_argument('-d', '--download-mode', action='store_true', default=False, dest="download_mode", help="Set Optimus Exceed 2 to download mode")

    # Parse the command line arguments.
    args = parser.parse_args()
    if not vars(args):
      parser.print_help()
      parser.exit(1)

    # Verify an IP argument was provided.
    if not args.ip:
      parser.print_help()
      sys.exit(0)

    # Verify a command line argument was provided.
    if not args.unlock and not args.lock and not args.fastboot and not args.download:
      print "[-] Error you must specifiy an action i.e., (unlock, lock, fastboot-mode, download-mode)"
      sys.exit(1)

    # Make sure adb and fastboot are installed
    print "[+] Checking that dependencies are installed"
    check_dependencies(['adb', 'fastboot'])

    # Handle command line argument 
    if args.unlock_bootloader:
      unlock_bootloader()
    elif args.lock_bootloader:
      lock_bootloader()
    elif args.fastboot_mode:
      fastboot_mode()
    elif args.download_mode:
      download_mode()
  except KeyboardInterrupt:
    sys.exit(1)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
