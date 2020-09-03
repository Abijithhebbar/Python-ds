import tkinter as tk
from tkinter import ttk

from tkcalendar import Calendar

def example1():
    def print_sel():
        print('last_date="{}"'.format(cal.selection_get()))
    def quit1():
        top.destroy()

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()
    ttk.Button(top, text="exit", command=quit1).pack()

def example2():
    def print_sel():
        print('next_date="{}"'.format(cal.selection_get()))
    def quit1():
        top.destroy()

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()
    ttk.Button(top, text="exit", command=quit1).pack()

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Last Date', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='Next Date', command=example2).pack(padx=10, pady=10)

root.mainloop()