from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CSE 337 Drawing Program")
root.geometry("700x700")
# Only enough room for 600 x 400 for shapes

w = Canvas(root,width=600, height=400)
w.pack()
cmd = IntVar()


param1_label = Label(root,text="Param 1")
param2_label = Label(root,text="Param 2")
param3_label = Label(root,text="Param 3")
param4_label = Label(root,text="Param 4")

param1_label.place(x=0,y=410)
param2_label.place(x=0,y=440)
param3_label.place(x=0,y=470)
param4_label.place(x=0,y=500)

param1_entry = Entry(root,width=60)
param2_entry = Entry(root,width=60)
param3_entry = Entry(root,width=60)
param4_entry = Entry(root,width=60)

param1_entry.place(x=70,y=410)
param2_entry.place(x=70,y=440)
param3_entry.place(x=70,y=470)
param4_entry.place(x=70,y=500)

# ?essagebox.showinfo("hello","hello")
def warning():
	messagebox.showwarning("Warning", "Invalid Size")

def draw_obj():
	if int(param1_entry.get()) < 1 or int(param1_entry.get()) > 600:
		warning()
	elif int(param2_entry.get()) < 1 or int(param2_entry.get()) >400:
		warning()
	elif int(param3_entry.get()) < 1 or int(param3_entry.get()) >600:
		warning()
	elif int(param4_entry.get()) < 1 or int(param4_entry.get()) > 400:
		warning()

	c = cmd.get()
	if c == 1:
		w.create_rectangle(param1_entry.get(),param2_entry.get(),param3_entry.get(),param4_entry.get())
	elif c==2:
		w.create_line(param1_entry.get(),param2_entry.get(),param3_entry.get(),param4_entry.get())
	else:
		w.create_oval(param1_entry.get(),param2_entry.get(),param3_entry.get(),param4_entry.get())

def clear_canvas():
	w.delete("all")

r1=Radiobutton(root,text="Rectangle",variable=cmd, value=1,command=draw_obj)
r2=Radiobutton(root,text="Line",variable=cmd, value=2,command=draw_obj)
r3=Radiobutton(root,text="Oval",variable=cmd,value=3,command=draw_obj)
r4=Radiobutton(root,text="Clear",variable=cmd,value=4,command=clear_canvas)

r1.place(x=70,y=530)
r2.place(x=70,y=550)
r3.place(x=70,y=570)
r4.place(x=400,y=530)




root.mainloop()

