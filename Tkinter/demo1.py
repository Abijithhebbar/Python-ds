from tkinter import *

"""
This is the base for all the tkinter operations
"""
root = Tk()
root.title("Demo")
"""
Used to check usage of buttons
"""
# demobutton = Button(root, text = "Bottom!", command = root.destroy)
# demobutton.pack(side = BOTTOM)
# demobutton.config(width = 20)
# demobutton1 = Button(root, text = "Right!")
# demobutton1.pack(side = RIGHT)
# demobutton2 = Button(root, text = "Left!")
# demobutton2.pack(side = LEFT)
# demobutton3 = Button(root, text = "Top!")
# demobutton3.pack(side = TOP)
"""
used to check the usage of checkboxes
"""
# checkbox1 = Checkbutton(root, text='male').grid(row = 0)
# checkbox2 = Checkbutton(root, text='female').grid(row = 1)

"""
Used to check the usage of the text box
"""
# FirstName = Label(root, text = "First Name : ").grid(row = 0)
# LastName = Label(root, text = "Last Name : ").grid(row = 1)
# FirstNameText = Entry(root).grid(row = 0, column = 1)
# LastNameText = Entry(root).grid(row = 1, column = 1)
"""
Used to check the ListBox
"""
# Lb = Listbox(root) 
# Lb.insert(1, 'Python') 
# Lb.insert(2, 'Java') 
# Lb.insert(3, 'C++') 
# Lb.insert(4, 'Any other') 
# Lb.pack() 
"""
Used to check MenuButton
"""
# menubutton = Menubutton(root, text = "Language", relief = FLAT)  
  
# menubutton.grid()  
  
# menubutton.menu = Menu(menubutton)  
  
# menubutton["menu"]=menubutton.menu  
  
# menubutton.menu.add_checkbutton(label = "First", variable=IntVar())  
  
# menubutton.menu.add_checkbutton(label = "Second", variable = IntVar())  
  
# menubutton.pack()  

"""
Used to check menu
"""
# menu = Menu(root) 
# root.config(menu=menu) 
# filemenu = Menu(menu) 
# menu.add_cascade(label='File', menu=filemenu) 
# filemenu.add_command(label='New') 
# filemenu.add_command(label='Open...') 
# filemenu.add_separator() 
# filemenu.add_command(label='Exit', command=root.quit) 
# helpmenu = Menu(menu) 
# menu.add_cascade(label='Help', menu=helpmenu) 
# helpmenu.add_command(label='About')
"""
Used to check RadioButton
"""
# v = IntVar() 
# RadioButton1 = Radiobutton(root, text='Button1', variable=v, value=1).pack(anchor=W) 
# RadioButton2 = Radiobutton(root, text='Button2', variable=v, value=2).pack(anchor=W) 

"""
Used to check scale
"""
# scale = Scale(root, from_=0, to=200) 
# scale.pack(side = RIGHT) 
# scale = Scale(root, from_=0, to=50, orient=HORIZONTAL) 
# scale.pack(side = BOTTOM) 

"""
Used to check the scroll bar
"""

# scrollbar = Scrollbar(root) 
# scrollbar.pack( side = RIGHT, fill = Y ) 
# mylist = Listbox(root, yscrollcommand = scrollbar.set ) 
# for line in range(500): 
#    mylist.insert(END, 'This is line number' + str(line)) 
# mylist.pack( side = LEFT, fill = BOTH ) 
# scrollbar.config( command = mylist.yview ) 

"""
Used to check SpinBox
"""
# spinbox = Spinbox(root, from_ = 0, to = 100) 
# spinbox.pack()

"""
Used to check PannedWindow
"""
m1 = PanedWindow() 
m1.pack(fill = BOTH, expand = 10) 
left = Entry(m1, bd = 50) 
m1.add(left) 
m2 = PanedWindow(m1, orient = VERTICAL) 
m1.add(m2) 
top = Scale( m2, orient = HORIZONTAL) 
m2.add(top) 

root.mainloop()
