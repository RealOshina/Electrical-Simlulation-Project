import tkinter as tk
import src.simulation as simulation

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.frame = tk.Frame(root, padx=10, pady=10, bg="red")
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Hello World!")
        self.label.pack()

root = tk.Tk()
app = App(root)

app.master.title("Electrical Simulation")
app.master.minsize(500, 500)
app.master.resizable(False, False)

app.mainloop()