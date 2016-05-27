#!/usr/bin/python -tt

"""
LG Optimus Exceed 2 VS450PP (w5c) bootloader unlock tool
"""
import argparse
import utils
import Tkinter

class unlock_gui(Tkinter.Tk):
  """
  GUI code executed when no command line parameters were provided. 
  """
  def __init__(self,parent):
    Tkinter.Tk.__init__(self,parent)
    self.parent = parent
    self.initialize()

  def initialize(self):
    self.grid()

    gui_actions = Tkinter.LabelFrame(self, text="Unlocker Actions")
    gui_actions.grid(row=0, column=0, columnspan=4, sticky='NSEW', padx=5, pady=5, ipadx=5, ipady=5)

    unlock_button = Tkinter.Button(gui_actions,text=u"Unlock Bootloader", command = utils.fastboot)
    unlock_button.grid(row=1, column=0, columnspan=2, sticky='W')

    lock_button = Tkinter.Button(gui_actions,text=u"Lock Bootloader", command = utils.fastboot)
    lock_button.grid(row=1, column=2, columnspan=2, sticky='W')

    unlock_button = Tkinter.Button(gui_actions,text=u"Fastboot Mode", command = utils.fastboot )
    unlock_button.grid(row=2, column=0, columnspan=2, sticky='W')

    unlock_button = Tkinter.Button(gui_actions,text=u"Download Mode", command = utils.fastboot)
    unlock_button.grid(row=2, column=2, columnspan=2, sticky='W')


    output_frame = Tkinter.LabelFrame(self, text="Unlocker Output")
    output_frame.grid(row=3, column=0, columnspan=4, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)


    output_window = Tkinter.Text(output_frame)
    output_window.grid(row=4, column=0, columnspan=4)


def main():
  try:
    # Create command line argument parser.
    parser = argparse.ArgumentParser(description="LG Optimus Exceed 2 VS450PP (w5c) Bootloader Unlock Tool", version=('%(prog)s 0.1'))
    parser.add_argument('-u', '--unlock', action='store_true', default=False, dest="unlock_bootloader", help="Unlock Optimus Exceed 2 bootloader")
    parser.add_argument('-l', '--lock',action='store_true', default=False, dest="lock_bootloader", help="Lock Optimus Exceed 2 bootloader")
    parser.add_argument('-f', '--fastboot-mode', action='store_true', default=False, dest="fastboot_mode", help="Set Optimus Exceed 2 to fastboot mode")
    parser.add_argument('-d', '--download-mode', action='store_true', default=False, dest="download_mode", help="Set Optimus Exceed 2 to download mode")
    parser.add_argument('-s', '--sdk', action='store', dest="sdk_path", help="Path to Android SDK (optional)")

    # Parse the command line arguments.
    args = parser.parse_args()

    # Handle command line arguments if provided else start the GUI
    if args.unlock_bootloader:
      utils.check_dependencies(args.sdk_path, gui=False)
      #unlock_bootloader(, )
    elif args.lock_bootloader:
      utils.lock_bootloader()
    elif args.fastboot_mode:
      utils.fastboot_mode()
    elif args.download_mode:
      utils.download_mode()
    else:
      app = unlock_gui(None)
      app.title('LG Optimus Exceed 2 Unlocker')
      app.mainloop()
  except KeyboardInterrupt:
    sys.exit(1)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()