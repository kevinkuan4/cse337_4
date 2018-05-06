from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CSE 337 Drawing Program")
root.geometry("700x700")
# Only enough room for 600 x 400 for shapes

w = Canvas(root,width=600, height=400)
w.pack()
cmd = IntVar()
clr_cmd= IntVar()
clr="black"

shape_list=[]
def warning():
	messagebox.showwarning("Warning", "Invalid Size: Object may be cut off")

def width_error():
	messagebox.showerror("Error", "Must enter a width 0 or greater")

def set_clr():
	global clr
	# print("set clr ffunction")
	c2 = clr_cmd.get()
	if c2 == 1:
		clr="red"
	elif c2 == 2:
		clr= "green"
	else:
		clr = "blue"


def draw_obj():
	global clr
	if int(param1_entry.get()) < 1 or int(param1_entry.get()) > 600:
		warning()
	elif int(param2_entry.get()) < 1 or int(param2_entry.get()) >400:
		warning()
	elif int(param3_entry.get()) < 1 or int(param3_entry.get()) >600:
		warning()
	elif int(param4_entry.get()) < 1 or int(param4_entry.get()) > 400:
		warning()

	# print(width_entry.get())

	if width_entry.get() == "":
		width_error()
		return
	if not int(width_entry.get()) >= 0:
		width_error()
		return

	c1 = cmd.get()
	
	if c1 == 1:
		shape = w.create_rectangle(param1_entry.get(),param2_entry.get(),param3_entry.get(),param4_entry.get() ,fill=clr,width=width_entry.get())
	elif c1 == 2:
		shape = w.create_line(param1_entry.get(),param2_entry.get(),param3_entry.get(),param4_entry.get(),fill=clr,width=width_entry.get())
	else:
		shape = w.create_oval(param1_entry.get(),param2_entry.get(),param3_entry.get(),param4_entry.get(),fill=clr,width=width_entry.get())
	shape_list.append(shape)

def clear_canvas():
	w.delete("all")

def del_recent():
	# print(shape_list)
	# print(shape_list[-1])
	w.delete(shape_list[-1])
	shape_list.pop()


param1_label = Label(root,text="Param 1")
param2_label = Label(root,text="Param 2")
param3_label = Label(root,text="Param 3")
param4_label = Label(root,text="Param 4")
width_label = Label (root, text="Width")

param1_label.place(x=30,y=410)
param2_label.place(x=30,y=440)
param3_label.place(x=30,y=470)
param4_label.place(x=30,y=500)
width_label.place(x=30,y=600)

param1_entry = Entry(root,width=60)
param2_entry = Entry(root,width=60)
param3_entry = Entry(root,width=60)
param4_entry = Entry(root,width=60)
width_entry = Entry(root, width=60)

param1_entry.place(x=100,y=410)
param2_entry.place(x=100,y=440)
param3_entry.place(x=100,y=470)
param4_entry.place(x=100,y=500)
width_entry.place(x=100,y=600)

r1=Radiobutton(root,text="Rectangle",variable=cmd, value=1,command=draw_obj)
r2=Radiobutton(root,text="Line",variable=cmd, value=2,command=draw_obj)
r3=Radiobutton(root,text="Oval",variable=cmd,value=3,command=draw_obj)
r4=Radiobutton(root,text="Red",variable=clr_cmd, value=1,command=set_clr)
r5=Radiobutton(root,text="Green",variable=clr_cmd, value=2,command=set_clr)
r6=Radiobutton(root,text="Blue",variable=clr_cmd, value=3,command=set_clr)
r7=Radiobutton(root,text="Undo Most Recent",variable=cmd,value=7,command=del_recent)
r8=Radiobutton(root,text="Clear Canvas",variable=cmd,value=8,command=clear_canvas)


r1.place(x=100,y=530)
r2.place(x=100,y=550)
r3.place(x=100,y=570)
r4.place(x=300,y=530)
r5.place(x=300,y=550)
r6.place(x=300,y=570)
r7.place(x=500,y=530)
r8.place(x=500,y=550)

root.mainloop()