from tkinter import *
  
# root = Tk() 
# root.title('Abijith')
# frame = Frame(root) 
# frame.pack() 
# bottomframe = Frame(root) 
# bottomframe.pack( side = RIGHT ) 
# redbutton = Button(frame, text = 'Red', fg ='orange') 
# redbutton.pack( side = RIGHT) 
# # greenbutton = Button(frame, text = 'Brown', fg='brown') 
# # greenbutton.pack( side = BOTTOM ) 
# # bluebutton = Button(frame, text ='Blue', fg ='blue') 
# # bluebutton.pack( side = LEFT ) 
# # blackbutton = Button(bottomframe, text ='Black', fg ='black') 
# # blackbutton.pack( side = TOP) 
# root.mainloop() 
"""
Overlap or 2 windows
"""

# root = Tk() 
# root.title('Abijith') 
# top = Toplevel() 
# top.title('Python') 
# top.mainloop() 

"""
Check Spinbox
"""
# master = Tk() 
# w = Spinbox(master, from_ = 0, to = 10) 
# w.pack() 
# mainloop() 


root = Tk()



def callback(event):
    print ("clicked at", event.x, event.y)

frame = Frame(root) 
frame.pack() 
redbutton = Button(frame, text = 'Click me!', fg ='orange') 
redbutton.pack( side = TOP) 

redbutton.config(height = 100, width = 200)
label = Label(redbutton)
label.pack()
label.bind("<Button>", callback)

root.mainloop()

# window = Tk()        
# def mouseClick( event ):
# 	print("Mouse Clicked")
# label = Label(window, text = "click me!")
# label.pack()
# label.bind("<Button>", mouseClick)
# window.mainloop()