import tkinter as tk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        button_panel = tk.Frame(bg='#ccc', bd=2)
        # button_Panel = Frame(Base_Panel, bg='azure2', bd=5)
        button_panel.pack(side=tk.LEFT, fill=tk.Y)

        number = 1
        while number <= 20:
            button_name = "Problem - " + str(number)
            button = tk.Button(button_panel,
                               text=button_name,
                               bg="#555",
                               fg="#ccc",
                               bd=2,
                               padx="20",
                               pady="2",
                               width=15)
            button.grid(row=number, column=1)
            number +=1

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Project_Euler")
    root.geometry("1024x768")
    app = Main(root)
    app.pack()
    root.mainloop()
