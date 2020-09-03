from tkinter import *
import tkinter.filedialog as tkFileDialog

root = Tk()
root.filename = tkFileDialog.askopenfilename(initialdir = "\\",title = "Select file",filetypes = (("Python Files","*.py"),("all files","*.*")))
print (root.filename)