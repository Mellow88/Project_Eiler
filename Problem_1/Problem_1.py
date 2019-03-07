from tkinter import *

# from tkinter import ttk as ttk

root = Tk()
root.title("Project_Euler")
root.geometry("400x400")

Task_1_Name = "Задача 1. Числа, кратные 3 или 5"

Title_Task = Label(root, text=Task_1_Name, background="#555", foreground="#ccc", padx="15", pady="6", font="15")
Title_Task.pack(expand=False, fill=X)

but = Button(root)
but["text"] = "Печать"
but.pack()


var1 = IntVar()
var2 = IntVar()
check1 = Checkbutton(root, text=u'1 пункт', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(root, text=u'2 пункт', variable=var2, onvalue=1, offvalue=0)
check1.pack()
check2.pack()

root.mainloop()
