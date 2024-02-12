from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("200x200")#without the geometry method, 
#adding widgets would change the initial size

root.grid_rowconfigure(0, weight=1) #this is how you adjust the widgets' sizes
#whenever the window is resized
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

s= ttk.Style()

s.configure('Style1.TFrame', background = 'blue')

s.configure('Style2.TFrame', background = 'green')

s.configure('Style3.TFrame', background = 'red')

s.configure('Style4.TLabel', background = '#3A3845')

s.configure('Style5.TFrame', background = '#FFA447')

Frame1 = ttk.Frame(root, width = 250, height = 250, style = 'Style1.TFrame')

Frame1.grid(row= 0, column= 0, sticky= 'nsew')

#Frame1.grid_propagate(False)

Frame2 = ttk.Frame(root, width = 250, height = 250, style = 'Style2.TFrame')



Frame2.grid(row= 1, column= 0, sticky = 'nsew')



#Frame2.grid_propagate(False)

label_1 = ttk.Label(Frame1, text= "Testing label")

label_1.grid(row= 0, column= 0)

Frame1.grid_rowconfigure(0, weight= 1)
Frame1.grid_columnconfigure(0, weight= 1)

label_2 = ttk.Label(Frame2, text= "Testing label 2")

label_2.grid(row= 0, column= 0)

Frame2.grid_rowconfigure(0, weight= 1)
Frame2.grid_columnconfigure(0, weight= 1)

Frame3 = ttk.Frame(root, width = 250, height = 250, style = 'Style3.TFrame')
Frame3.grid(row= 2, column=0, sticky = 'nsew')
Frame3.grid_rowconfigure(0, weight= 1)
Frame3.grid_columnconfigure(0, weight= 1)

label_3 = ttk.Label(Frame3, text= "Testing label 3")
label_3.grid(row= 0, column= 0)

Frame4 = ttk.Frame(root, width = 250, height = 250, style = 'Style4.TLabel')
Frame4.grid(row= 0, column=1, sticky = 'nsew')
Frame4.grid_rowconfigure(0, weight= 1)
Frame4.grid_columnconfigure(1, weight= 1)
label_4 = ttk.Label(Frame4, text= "Testing label 4 on column 1")
label_4.grid(row= 0, column= 1)

Frame5 = ttk.Frame(root, width= 250, height = 250, style = 'Style5.TFrame')
Frame5.grid(row= 1, column= 1, sticky = 'nsew')
label_5 = ttk.Label(Frame5, text= "Testing label on frame 5")
Frame5.grid_rowconfigure(0, weight= 1) #This is necessary if you want
#the label to stay in the center when the window is resized
Frame5.grid_columnconfigure(1, weight= 1)
label_5.grid(row= 0, column= 1)
root.mainloop()