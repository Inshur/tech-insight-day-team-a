from tkinter import *
from tkinter.ttk import *

main = Tk()
main.geometry('500x500')

def get_val():
   entry_val=entrySearchVal.get()
   labelReturnSearchVal = Label(main, text=entry_val)
   labelReturnSearchVal.grid(row=3, column=0)

def show():
   labelReturnSearchBy.config(text = currentSearchBy)
   labelReturnSearchBy = Label(main, text="order_id")
   labelReturnSearchBy.grid(row=4, column=0)

#dropdown search by values
possibleSearches = ['order_id', 'date', 'restaurant', 'postcode']

labelSearchBy = Label(main, text='Search by: ')
labelSearchVal = Label(main, text='Search val:')

currentSearchBy = StringVar()
currentSearchBy.set('order_id')

dropSearchBy = OptionMenu(main, StringVar(), *possibleSearches)
# entrySearchBy = Entry(main)
entrySearchVal = Entry(main)

buttonSearch = Button(main, text='Search', command=get_val)

labelSearchBy.grid(row=0, column=0, sticky=W, pady=4)
labelSearchVal.grid(row=1, column=0, sticky=W, pady=4)
dropSearchBy.grid(row=0, column=1, sticky=E, pady=4)
entrySearchVal.grid(row=1, column=1, sticky=E, pady=4)
buttonSearch.grid(row=2, column=0, sticky=W, pady=2)



main.mainloop()