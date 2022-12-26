import tkinter
from tkinter import *
from PIL import ImageTk,Image

def goal():
	go = 1
root = Tk()
root.title("Sengal vs Netherlands tkinter score")
root.geometry("800x500")
root.resizable(False,False)

Label(root, font =('Helvetica bold',22), text = 'GOALS').place(x=130,y=30)
#callback : function for changing label
label1 = Label(root, justify=CENTER)
label1.pack()
Label(root, font =('Helvetica bold',22), text = 'GOALS').place(x=530,y=30)

num  = 0
num2 = 0

def increment():

	global num
	if(num<9):
		num += 1
		lbl.configure(text=num) 
	else:
		num=9
def increment2():

	global num2
	if(num2<9):
		num2 += 1
		lb2.configure(text=num2) 
	else:
		num=9
def zero():
		global num2 
		global num
		num2=0
		num=0
		lb2.configure(text=num2)
		lbl.configure(text=num) 

ImgNetherlandslabel = PhotoImage(file = "Netherlands.png")
ImgSenegallabel     = PhotoImage(file = "Senegal.png")

ImgNetherlandslabel = ImgNetherlandslabel.subsample(2,2)
ImgSenegallabel     = ImgSenegallabel.subsample(2,2)


Netherlandsbtn = Button(root, image = ImgNetherlandslabel, command = increment)
Senegalbtn     = Button(root, image = ImgSenegallabel, command = increment2)

Netherlandsbtn.place(x=100, y=190)
Senegalbtn.place(x=500, y=190)

lbl=Label(root, text=num,font = ('Verdana', 15), fg="black")
lbl.place(x=170,y=130)

lb2=Label(root, text=num2,font = ('Verdana', 15), fg="black")
lb2.place(x=570,y=130)

root.mainloop()