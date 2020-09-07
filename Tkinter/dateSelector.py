import tkinter as tk
from tkinter import ttk
from tkinter import *

from tkcalendar import Calendar
def methodrun():
    inputValue = ''
    date = ''
    def example1():
        def print_sel():
            inputValue=textBox.get("1.0","end-1c")
            print(inputValue)
            date = format(cal.selection_get())
            print(date)
            top.destroy()
            return inputValue, date

        top = tk.Toplevel(root)

        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2020, month=1, day=1)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()
        # date = format(cal.selection_get())
        # print(date)



    root = tk.Tk()
    s = ttk.Style(root)
    s.theme_use('clam')
    textBox=Text(root, height=2, width=10)
    textBox.pack()
    ttk.Button(root, text='Select Date', command=example1).pack(padx=10, pady=10)







    root.mainloop()

