from tkinter import *
from tkinter import ttk

root = Tk()

s = ttk.Style()

s.configure('Frame2_style.TFrame', background = '#3A3845')

Frame1 = ttk.Frame(root, width = 250, height = 250)

Frame1.grid()

Frame2 = ttk.Frame(Frame1, width=200, height = 200, style = 'Frame2_style.TFrame')

Frame2.grid(padx= 50, pady= 50)

lbl1 = ttk.Label(Frame1, text= "Testing label")

lbl1.grid(row= 0, column = 0)

root.mainloop()