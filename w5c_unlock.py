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
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(1, weight=1)
    self.grid_columnconfigure(0, weight=1)

    gui_actions = Tkinter.LabelFrame(self, text="Unlocker Actions")
    gui_actions.grid(row=0, column=0, padx=5, pady=5)

    # Create Unlock button
    Tkinter.Button(gui_actions, text=u"Unlock Bootloader", width=20, height=2, command = utils.fastboot).grid(row=0, column=0, padx=10, pady=10)

    # Create Lock button
    Tkinter.Button(gui_actions, text=u"Lock Bootloader", width=20, height=2, command = utils.fastboot).grid(row=0, column=1, padx=10, pady=10)

    # Create Fastboot button
    Tkinter.Button(gui_actions, text=u"Fastboot Mode", width=20, height=2, command = utils.fastboot).grid(row=1, column=0, padx=10, pady=10)

    # Create Download button
    Tkinter.Button(gui_actions, text=u"Download Mode", width=20, height=2, command = utils.fastboot).grid(row=1, column=1, padx=10, pady=10)

    # Create Root button
    Tkinter.Button(gui_actions, text=u"Root Device", width=20, height=2, command = utils.fastboot).grid(row=2, column=0, padx=10, pady=10)

    # Create UnRoot button
    Tkinter.Button(gui_actions, text=u"Un-Root Device", width=20, height=2, command = utils.fastboot).grid(row=2, column=1, padx=10, pady=10)


    output_frame = Tkinter.LabelFrame(self, text="Unlocker Output")
    output_frame.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)


    output_window = Tkinter.Text(output_frame)
    print output_window.winfo_width() 
    output_window.grid(row=0, column=0)


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