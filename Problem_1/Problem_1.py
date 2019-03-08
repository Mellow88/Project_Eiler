from tkinter import *

root = Tk()
root.title("Project_Euler")
root.geometry("1024x768")

Base_Panel = Frame(root, bg='azure2', bd=5)
Base_Panel.pack(fill=BOTH, expand=True)

Button_Panel = Frame(Base_Panel, bg='azure2', bd=5)
Button_Panel.pack(side=LEFT, fill=BOTH, expand=False)

number = 1
while number <= 20:
    button_name = "Problem. " + str(number)
    button = Button(Button_Panel, text=button_name, background="#555", foreground="#ccc", padx="15", pady="6", font="12")
    # style.configure(button, padding=6, relief="flat", background="#ccc")
    button.pack(fill=BOTH, expand=False)
    number += 1

# scrollbar = Scrollbar(Button_Panel)
# scrollbar.pack(side='top', fill=BOTH)

# var1 = IntVar()
# var2 = IntVar()
# check1 = Checkbutton(root, text=u'1 пункт', variable=var1, onvalue=1, offvalue=0)
# check2 = Checkbutton(root, text=u'2 пункт', variable=var2, onvalue=1, offvalue=0)
# check1.pack(side=LEFT)
# check2.pack(side=LEFT)

root.mainloop()
