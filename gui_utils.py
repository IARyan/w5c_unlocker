import Tkinter as tk
from ScrolledText import *
from idlelib.WidgetRedirector import WidgetRedirector

class ScrolledTextReadOnly(ScrolledText):
    def __init__(self, *args, **kwargs):
        ScrolledText.__init__(self, *args, **kwargs)
        _rc_menu_install(self)
        # overwrite default class binding so we don't need to return "break"
        self.bind_class("Text", "<Control-a>", self.event_select_all)  
        self.bind("<Button-3><ButtonRelease-3>", self.show_menu)

        # Make the widget ready only
        self.redirector = WidgetRedirector(self)
        self.insert = self.redirector.register("insert", lambda *args, **kw: "break")
        self.delete = self.redirector.register("delete", lambda *args, **kw: "break")

    def event_select_all(self, *args):
        self.focus_force()        
        self.tag_add("sel","1.0","end")

    def show_menu(self, e):
        self.tk.call("tk_popup", self.menu, e.x_root, e.y_root)


def _rc_menu_install(w):
    w.menu = tk.Menu(w, tearoff=0)
    w.menu.add_command(label="Copy")
    w.menu.add_separator()
    w.menu.add_command(label="Select all")        

    w.menu.entryconfigure("Copy", command=lambda: w.focus_force() or w.event_generate("<<Copy>>"))
    w.menu.entryconfigure("Select all", command=w.event_select_all)        


if __name__ == "__main__":

    class SampleApp(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            self.grid()
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

            output_frame = tk.LabelFrame(self, text="Unlocker Output")
            output_frame.grid(row=0, column=0, padx=5, pady=5, ipadx=8, ipady=8)


            scrollbar = tk.Scrollbar(self)


            output_window = ScrolledTextReadOnly(output_frame, height=20)
            output_window.insert(tk.INSERT, "A" * 1000 + "\n")
            output_window.insert(tk.INSERT, "Some Text After\n\n")
            output_frame.grid_rowconfigure(0, weight=1)
            output_frame.grid_columnconfigure(0, weight=1)
            output_window.grid(row=0, column=0)



    app = SampleApp()
    app.mainloop()