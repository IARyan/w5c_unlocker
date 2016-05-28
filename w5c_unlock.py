#!/usr/bin/python -tt

"""
LG Optimus Exceed 2 VS450PP (w5c) bootloader unlock tool
"""
import argparse
import utils
import gui_utils
import Tkinter as tk

class unlock_gui(tk.Tk):
  """
  GUI code executed when no command line parameters were provided. 
  """
  def __init__(self,parent):
    tk.Tk.__init__(self,parent)
    self.output_window = None
    self.adb_status = None
    self.fastboot_status = None
    self.file_status = None
    self.parent = parent
    self.resizable(0,0)
    self.grid()
    self.actions()
    self.status()
    self.output()

  def actions(self):
    """
    Creates the action buttons of the gui
    """
    # Allow grid auto resize 
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)
  
    # Actions label frame
    gui_actions = tk.LabelFrame(self, text="Unlocker Actions")
    gui_actions.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

    # Allow grid auto resize 
    gui_actions.grid_rowconfigure(0, weight=1)
    gui_actions.grid_columnconfigure(0, weight=1)
    gui_actions.grid_rowconfigure(0, weight=1)
    gui_actions.grid_columnconfigure(1, weight=1)
    gui_actions.grid_rowconfigure(1, weight=1)
    gui_actions.grid_columnconfigure(0, weight=1)
    gui_actions.grid_rowconfigure(1, weight=1)
    gui_actions.grid_columnconfigure(1, weight=1)
    gui_actions.grid_rowconfigure(2, weight=1)
    gui_actions.grid_columnconfigure(0, weight=1)
    gui_actions.grid_rowconfigure(2, weight=1)
    gui_actions.grid_columnconfigure(1, weight=1)

    # Create Unlock button
    tk.Button(gui_actions, text=u"Unlock Bootloader", width=20, height=2, command = utils.fastboot).grid(row=0, column=0, padx=10, pady=10)

    # Create Lock button
    tk.Button(gui_actions, text=u"Lock Bootloader", width=20, height=2, command = utils.fastboot).grid(row=0, column=1, padx=10, pady=10)

    # Create Fastboot button
    tk.Button(gui_actions, text=u"Fastboot Mode", width=20, height=2, command = utils.fastboot).grid(row=1, column=0, padx=10, pady=10)

    # Create Download button
    tk.Button(gui_actions, text=u"Download Mode", width=20, height=2, command = utils.fastboot).grid(row=1, column=1, padx=10, pady=10)

    # Create Root button
    tk.Button(gui_actions, text=u"Root Device", width=20, height=2, command = utils.fastboot).grid(row=2, column=0, padx=10, pady=10)

    # Create UnRoot button
    tk.Button(gui_actions, text=u"Un-Root Device", width=20, height=2, command = utils.fastboot).grid(row=2, column=1, padx=10, pady=10)


  def status(self):
    # Actions label frame
    tool_status = tk.LabelFrame(self, text="Dependencies Status")
    tool_status.grid(row=0, column=1, padx=5, pady=5, sticky="NSEW")

    # Allow grid auto resize 
    tool_status.grid_rowconfigure(0, weight=1)
    tool_status.grid_columnconfigure(1, weight=1)
    tool_status.grid_rowconfigure(1, weight=1)
    tool_status.grid_columnconfigure(1, weight=1)
    tool_status.grid_rowconfigure(2, weight=1)
    tool_status.grid_columnconfigure(1, weight=1)

    # Create Unlock button
    tk.Label(tool_status, text="Adb:").grid(row=0, column=0, sticky="E")
    self.adb_status = tk.Frame(tool_status, bg="#EE0000")

    self.adb_status.grid(row=0, column=1, sticky="NSEW", padx=5, pady=10)
    
    tk.Label(tool_status, text="Fastboot:").grid(row=1, column=0, sticky="E")
    self.fastboot_status = tk.Frame(tool_status, bg="#EE0000")

    self.fastboot_status.grid(row=1, column=1, sticky="NSEW", padx=5, pady=10)

    tk.Label(tool_status, text="Install Files:").grid(row=2, column=0, sticky="E")
    self.file_status = tk.Frame(tool_status, bg="#EE0000")
  
    self.file_status.grid(row=2, column=1, sticky="NSEW", padx=5, pady=10)
    self.file_status.configure(background="#009900")

  def output(self):
    # Allow grid to auto resize 
    self.grid_rowconfigure(1, weight=1)
    self.grid_columnconfigure(0, weight=1)

    # Output label frame
    output_frame = tk.LabelFrame(self, text="Unlocker Output")
    output_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, ipadx=8, ipady=8, sticky="NSEW")


    self.output_window = gui_utils.ScrolledTextReadOnly(output_frame, height=10)
    self.output_window .insert(tk.INSERT, "A" * 1000 + "\n")
    output_frame.grid_rowconfigure(0, weight=1)
    output_frame.grid_columnconfigure(0, weight=1)
    self.output_window .grid(row=0, column=0)

def main():
  try:
    # Create command line argument parser.
    parser = argparse.ArgumentParser(description="LG Optimus Exceed 2 VS450PP (w5c) Bootloader Unlock Tool", version=('%(prog)s 0.1'))
    parser.add_argument('-u', '--unlock', action='store_true', default=False, dest="unlock_bootloader", help="Unlock Optimus Exceed 2 bootloader")
    parser.add_argument('-l', '--lock',action='store_true', default=False, dest="lock_bootloader", help="Lock Optimus Exceed 2 bootloader")
    parser.add_argument('-f', '--fastboot-mode', action='store_true', default=False, dest="fastboot_mode", help="Set Optimus Exceed 2 to fastboot mode")
    parser.add_argument('-d', '--download-mode', action='store_true', default=False, dest="download_mode", help="Set Optimus Exceed 2 to download mode")
    parser.add_argument('-r', '--root', action='store_true', default=False, dest="root_device", help="Root Optimus Exceed 2")
    parser.add_argument('-x', '--unroot', action='store_true', default=False, dest="unroot_device", help="Un-Root Optimus Exceed 2")

    # Parse the command line arguments.
    args = parser.parse_args()

    # Handle command line arguments if provided else start the GUI
    if args.unlock_bootloader:
      unlock_bootloader( )
    elif args.lock_bootloader:
      utils.lock_bootloader()
    elif args.fastboot_mode:
      utils.fastboot_mode()
    elif args.download_mode:
      utils.download_mode()
    elif args.root_device:
      utils.download_mode()
    elif args.unroot_device:
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