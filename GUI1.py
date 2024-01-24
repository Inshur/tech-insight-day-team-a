from tkinter import *
from tkinter.ttk import *

import retrieveOrder as retrieve

main = Tk()
# main.geometry('1000x1000')
width, height = main.winfo_screenwidth(), main.winfo_screenheight()

main.geometry('%dx%d+0+0' % (width,height))

searchBy = 'order_id'
def callback(selection):
    searchBy = selection

def search():
   searchVal=entrySearchVal.get()
   output = retrieve.retrieveOrder(currentSearchBy.get(), searchVal) #searchParameter, Value)
   # print(currentSearchBy.get())
   print(output)
   labelOutput.config(text=output)

   # for order in output:
   # if output[0] == False:
   #    labelOutput.config(text="ERROR in input")
   # else:
   #    labelOutput.config(text=output)
   #    for key, value in output.items():
   #      print(key)
   #      print(value)

   food_delivery.insert(parent='',index='end',iid=0,text='',
   values=('1','05-01-2023','101','Burger Bisto', '61340', 'BN2 9US', '16675', 'Classic Cheeseburger', '7.99', '92493', 'Sweet Potato Fries', '3.99', '11,98', 'BN2 5EF', '072442766728', '05-01-2023T19:45:00', '12'))



#dropdown search by values
possibleSearches = ['order_id', 'order_id', 'date', 'restaurant', 'postcode', 'contact_number', 'house_number']

labelSearchBy = Label(main, text='Search by: ')
labelSearchVal = Label(main, text='Search val:')

currentSearchBy = StringVar()
currentSearchBy.set('order_id')

dropSearchBy = OptionMenu(main, currentSearchBy, *possibleSearches, command=callback)
entrySearchVal = Entry(main)

buttonSearch = Button(main, text='Search', command=search)

labelOutput = Label(main, text='no errors', wraplength=1000)

labelSearchBy.grid(row=0, column=0, sticky=W, pady=4)
labelSearchVal.grid(row=1, column=0, sticky=W, pady=4)
dropSearchBy.grid(row=0, column=1, sticky=W, pady=4)
entrySearchVal.grid(row=1, column=1, sticky=W, pady=4)
buttonSearch.grid(row=2, column=0, sticky=W, pady=2)
labelOutput.grid(row=3, column=0, sticky=W, pady=2)

food_delivery = Treeview(main)
food_delivery['columns'] = ('order_id', 'date', 'restaurant_name', 'restaurant_id', 'restaurant_postcode', 'dish_id', 'dish_name', 'price', 'total_price', 'delivery_postcode', 'contact_number', 'deliver_by', 'house_number')

food_delivery.column("#0", width=0,  stretch=NO)
food_delivery.column("order_id",anchor=CENTER, width=80)
food_delivery.column("date",anchor=CENTER, width=80)
food_delivery.column("restaurant_name",anchor=CENTER,width=80)
food_delivery.column("restaurant_id",anchor=CENTER,width=80)
food_delivery.column("restaurant_postcode",anchor=CENTER,width=80)
food_delivery.column("dish_id",anchor=CENTER,width=80)
food_delivery.column("dish_name",anchor=CENTER,width=80)
food_delivery.column("price",anchor=CENTER,width=80)
food_delivery.column("total_price",anchor=CENTER,width=80)
food_delivery.column("delivery_postcode",anchor=CENTER,width=80)
food_delivery.column("contact_number",anchor=CENTER,width=80)
food_delivery.column("deliver_by",anchor=CENTER,width=80)
food_delivery.column("house_number",anchor=CENTER,width=80)


food_delivery.heading("#0",text="",anchor=CENTER)
food_delivery.heading("order_id",text="ID",anchor=CENTER)
food_delivery.heading("date",text="Date",anchor=CENTER)
food_delivery.heading("restaurant_name",text="Restaurant Name",anchor=CENTER)
food_delivery.heading("restaurant_id",text="Restaurant ID",anchor=CENTER)
food_delivery.heading("restaurant_postcode",text="Restaurant Postcode",anchor=CENTER)
food_delivery.heading("dish_id",text="Dish ID",anchor=CENTER)
food_delivery.heading("dish_name",text="Dish Name",anchor=CENTER)
food_delivery.heading("price",text="Price",anchor=CENTER)
food_delivery.heading("total_price",text="Total Price",anchor=CENTER)
food_delivery.heading("delivery_postcode",text="Delivery Postcode",anchor=CENTER)
food_delivery.heading("contact_number",text="Contact Number",anchor=CENTER)
food_delivery.heading("deliver_by",text="Deliver By",anchor=CENTER)
food_delivery.heading("house_number",text="House Number",anchor=CENTER)

food_delivery.grid(row= 5, column= 0, rowspan=3)
main.mainloop()

