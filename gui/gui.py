import tkinter as tk
from tkinter import ttk
#import simulation

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        #self.create_menubar()
        #self.create_buildmenu()

    def create_menubar(self):
        menubar = tk.Menu(self)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=lambda: self.newfile())
        filemenu.add_command(label="Open", command=lambda: print("Open File"))
        filemenu.add_command(label="Save", command=lambda: print("Save File"))
        filemenu.add_command(label="Save as", command=lambda: print("Save As File"))
        filemenu.add_command(label="Export", command= lambda: print("Export File"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=lambda: print("Undo"))
        editmenu.add_command(label="Redo", command=lambda: print("Redo"))
        editmenu.add_separator()
        editmenu.add_command(label="Copy", command=lambda: print("Copy"))
        editmenu.add_command(label="Paste", command=lambda: print("Paste"))
        editmenu.add_command(label="Cut", command=lambda: print("Cut"))
        editmenu.add_command(label="Delete", command=lambda: print("Delete"))
        editmenu.add_separator()
        editmenu.add_command(label="Select All", command=lambda: print("Select All"))
        editmenu.add_command(label="Delete All", command=lambda: print("Delete All"))

        viewmenu = tk.Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Restore Default Zoom")

        simulatemenu = tk.Menu(menubar, tearoff=0)
        simulatemenu.add_command(label="Start Simulate", command=lambda: print("Start Simulate"))
        simulatemenu.add_command(label="Stop Simulate", command=lambda: print("Stop Simulate"))

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="View Help", command=lambda: print("View Help"))
        helpmenu.add_command(label="About App", command=lambda: print("About App"))
        
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="View", menu=editmenu)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)
    def create_buildmenu(self):
        buildmenu_frame = tk.Frame(self, bg="lightgray", padx=5, pady=5)
        buildmenu_frame.pack()

        scrollbar = tk.Scrollbar(buildmenu_frame, orient="horizontal")
        scrollbar.pack(side="bottom", fill="x")

        canvas = tk.Canvas(buildmenu_frame, bg="blue", height=100)
        canvas.config(xscrollcommand=scrollbar.set)
        canvas.pack()

        frame_a = tk.Frame(canvas, width=50, height=50, bg="green")
        frame_a.pack()

        frame_b = tk.Frame(canvas, width=50, height=50, bg="green")
        frame_b.pack()
    def newfile(self):
        print("A")
    def simulate(self):
        pass

root = tk.Tk()
app = App()

app.master.title("Electrical Simulation")
app.master.minsize(1000, 1000)

root.mainloop()