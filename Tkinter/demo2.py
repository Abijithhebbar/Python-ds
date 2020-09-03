import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start = tk.Button(self)
        self.start["text"] = "Click me :)"
        self.start["command"] = self.methodfun
        self.start.pack(side="top")



    def methodfun(self):
        print("hi there, everyone!")
        self.newButton = tk.Button(self)
        self.newButton["text"] = "New Button"
        self.newButton.pack(side = "left")
        self.newButton["command"] = self.func
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
    def func(self):
        print("New Button Clicked!!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()