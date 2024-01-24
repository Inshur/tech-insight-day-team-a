from tkinter import *
from tkinter.ttk import *

main = Tk()
main.geometry('500x500')



def get_val():
   entry_val=e2.get()
   l3 = Label(main, text=entry_val)
   l3.grid(row=3, column=0)

l1 = Label(main, text='Search by: ')
l2 = Label(main, text='Search val:')

e1 = Entry(main)
e2 = Entry(main)

b1 = Button(main, text='Search', command=get_val)

l1.grid(row=0, column=0, sticky=W, pady=4)
l2.grid(row=1, column=0, sticky=W, pady=4)
e1.grid(row=0, column=1, sticky=E, pady=4)
e2.grid(row=1, column=1, sticky=E, pady=4)
b1.grid(row=2, column=0, sticky=W, pady=2)


main.mainloop()