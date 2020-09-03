from tkinter import *
from tkcalendar import Calendar,DateEntry

root = Tk()
def example():
	url = Label(root, text = "Enter URL : ").pack(side = "top")
	urlEntry = Entry (root).pack(side = "right")
	# textValue = urlEntry.get()
	# print(textValue)
	def print_sel():
		selectedDate = cal.selection_get()
		print(selectedDate)
		# print('Seleceted Date ="{}"'.format(cal.selection_get()))
	
	
	cal = Calendar(root,
	                   font="Arial 14", selectmode='day',
	                   cursor="hand1", year=2018, month=2, day=5)
	cal.pack(fill="both", expand=True)
	Button(root, text="ok", command=print_sel()).pack( side = "left")



if __name__ == '__main__':
	example()
root.mainloop()


