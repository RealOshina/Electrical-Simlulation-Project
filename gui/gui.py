import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.active = {}
        self.selected_component = None

        self.image = {
            "voltage_source": "assests/voltage_source.png",
            "resistor": "assests/resistor.png"
        }

        self.placed_image = []
        self.labels = {}

        self.create_menubar()
        self.create_buildmenu()
        self.create_component_list()
        self.create_workspace()
    def toggle(self, button, component_type):
        was_activate = self.active.get(button, False)

        for x in list(self.active.keys()):
            self.active[x] = False
            x.config(relief="flat")
        
        if not was_activate:
            self.active[button] = True
            button.config(relief="sunken")
            self.selected_component = component_type
        else:
            self.selected_component = None
    def place_component(self, event):
        if self.selected_component is None:
            return

        path = self.image[self.selected_component]
        
        img = tk.PhotoImage(file=path)
        img = img.subsample(3, 3)

        self.placed_image.append(img)
        self.workspace_canvas.create_image(event.x-35, event.y-35, anchor="nw", image=img)
        
        tk.Label(self.component_list_frame, text=self.selected_component).pack()
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

        canvas = tk.Canvas(buildmenu_frame, bg="lightgray", height=105)
        canvas.config(xscrollcommand=scrollbar.set)
        canvas.pack()

        frame_a = tk.Frame(canvas, width=90, height=90, bg="green")
        canvas.create_window(10, 10, anchor="nw", window=frame_a)

        voltage_source_img = tk.PhotoImage(file="assests/voltage_source.png")
        voltage_source_img = voltage_source_img.subsample(3, 3)

        voltage_source_button = tk.Button(frame_a, image=voltage_source_img, relief="flat", 
                                          command= lambda: self.toggle(voltage_source_button, "voltage_source"))
        voltage_source_button.image = voltage_source_img
        voltage_source_button.pack()

        frame_b = tk.Frame(canvas, width=90, height=90, bg="blue")
        canvas.create_window(110, 10, anchor="nw", window=frame_b)

        resistor_img = tk.PhotoImage(file="assests/resistor.png")
        resistor_img = resistor_img.subsample(3, 3)

        resistor_button = tk.Button(frame_b, image=resistor_img, relief="flat", 
                                    command= lambda: self.toggle(resistor_button, "resistor"))
        resistor_button.image = resistor_img
        resistor_button.pack()
    def create_workspace(self):
        self.workspace_frame = tk.Frame(self, bg="lightgray", padx=5, pady=5)
        self.workspace_frame.pack(fill=tk.BOTH, expand=True)

        self.workspace_canvas = tk.Canvas(self.workspace_frame, bg="white", width=500, height=500)
        self.workspace_canvas.pack(fill=tk.BOTH, expand=True)

        self.workspace_canvas.bind("<Button-1>", self.place_component)
    def create_component_list(self):
        self.component_list_frame = tk.Frame(self, bg="lightgray", padx=5, pady=5)
        self.component_list_frame.pack(fill=tk.BOTH, expand=True, side="left")

        label = tk.Label(self.component_list_frame, text="Component List:", bg="lightgray")
        label.pack()
    def newfile(self):
        print("A")
    def simulate(self):
        pass

root = tk.Tk()
app = App()

app.master.title("Electrical Simulation")
app.master.minsize(1000, 1000)

root.mainloop()