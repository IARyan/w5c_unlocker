import sys
import os
from subprocess import check_output

def in_path(program):
  """
  Checks if a program is in the PATH.
  """
  fpath, fname = os.path.split(program)
  print fpath
  print fname
  if fpath:
    print "FPATh!!!!!"
    print program
    if os.path.isfile(program) and os.access(program, os.X_OK):
      print "print found %s from path!" % (program)
      return True
  else:
    for path in os.environ["PATH"].split(os.pathsep):
      path = path.strip('"')
      exe_file = os.path.join(path, program)
      if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
        print "MMMMMMMMMAAAAAAAAAAAAADDDDDDDDDDDEEEEEEEEEEEEEEEE IIIIIIIIIIIIIITTTTTTTTTTTTTTT!!!!!!!"
        print exe_file
        return True

    return False

def check_dependencies(sdk_path, gui=False):
  """
  Verifies dependencies are installed.
  """
  dependencies = []

  # Check if sdk_path is specified
  if sdk_path:
    dependencies.append(os.path.join(sdk_path,'platform-tools', 'adb'))
    dependencies.append(os.path.join(sdk_path,'platform-tools', 'fastboot'))
  else:
    dependencies.append('adb')
    dependencies.append('fastboot')

  # Make sure dependencies are installed
  for dependency in dependencies:
    if not in_path(dependency):
      message = '%s was not found in the PATH. To fix download the Android SDK and add the platform-tools folder to the PATH\n Alternatively you can pass the path to the SDK in on the command line (-s or --sdk) ' % (dependency)
      if gui:
        return {'status': 'Error', 'message': message}
      else:
          print message 
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