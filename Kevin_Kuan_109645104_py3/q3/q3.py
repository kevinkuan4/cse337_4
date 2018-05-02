from tkinter import *

root = Tk()
root.title("CSE 337 Drawing Program")
root.geometry("600x600")
# Only enough room for 600 x 400 for shapes


param1_label = Label(root,text="Param 1")
param2_label = Label(root,text="Param 2")
param3_label = Label(root,text="Param 3")
param4_label = Label(root,text="Param 4")

param1_label.place(x=0,y=400)
param2_label.place(x=0,y=430)
param3_label.place(x=0,y=460)
param4_label.place(x=0,y=490)

param1_entry = Entry(root,width=60)
param2_entry = Entry(root,width=60)
param3_entry = Entry(root,width=60)
param4_entry = Entry(root,width=60)

param1_entry.place(x=70,y=400)
param2_entry.place(x=70,y=430)
param3_entry.place(x=70,y=460)
param4_entry.place(x=70,y=490)

# lab = Label(root, text="Command:")
# k1  = Label(root, text="key/search")
# ke  = Entry(root, width=40)
# vl  = Label(root, text="value")
# ve  = Text(root, width=40, height=5)

root.mainloop()
