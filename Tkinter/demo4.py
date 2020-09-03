from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.FirstName = Label(root, text = "First Name : ").grid(row = 0)
        self.LastName = Label(root, text = "Last Name : ").grid(row = 1)
        self.FirstNameText = Entry(root).grid(row = 0, column = 1)
        self.LastNameText = Entry(root).grid(row = 1, column = 1)

        self.play = Button(root, command = self.methodfun, text = "Play").grid(row = 2)




    def methodfun(self):
        for i in range(1,10):
            self.i = Button(root, text = i).grid(row = 10, column = i+1)
            print(i)

root = Tk()
app = Application(master=root)
app.mainloop()