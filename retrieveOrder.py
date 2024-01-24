import json
from multiprocessing.sharedctypes import Value
from re import search
import requests

response = requests.get("https://europe-west1-inshur-dev0-service0.cloudfunctions.net/delivery-api-orders")
global orders
global searched_orders
#Both global variables to allow for larger scope

orders = response.json()
orders = orders['data']
#Takes the successful orders from the JSON file and adds them to a dictionary

<<<<<<< HEAD
possibleSearches = ['order_id', 'date', 'restaurant', 'postcode', 'contact_number', 'house_number', 'dish_id']
=======
possibleSearches = ['order_id', 'date', 'restaurant', 'postcode', 'contact_number', 'house_number']
#List of possible searches, not used in the code at all mainly for frontend
>>>>>>> e7253d78edadf48b6aaa635043ac4db73c8c88a5

#Searched_orders the list that contains all orders that match the search criteria
searched_orders = []

def retrieveOrder(searchParameter, Value):
    for order in orders:
        if searchParameter == 'order_id':
            if Value < 0:
                #Does not allow for a value ID of less than zero
                return (False, 'Error: Value can not be below zero')
                #Returns tuple, the false is for identifying when there is an error string
            if str(Value) in order.get(searchParameter):
                searched_orders.append(order)
                #The order is added to the searched_orders list when it is successful
        elif searchParameter == 'date':
            if str(Value) in order.get(searchParameter):
                searched_orders.append(order)
        elif searchParameter == 'restaurant':
            restaurant = order.get('restaurant')
            if Value.lower() in restaurant.get('name'):
                searched_orders.append(order)
        elif searchParameter == 'postcode':
            address = order.get('delivery')
            #Retrieves address first as there is a nested dictionary, repeated later
            if Value.lower() in address.get('postcode'):
                searched_orders.append(order)
        elif searchParameter == 'contact_number':
            address = order.get('delivery')
            if Value.lower() in address.get('contact_number'):
                searched_orders.append(order)
        elif searchParameter == 'house_number':
            address = order.get('delivery')
            if Value.lower() in address.get('house_number'):
                searched_orders.append('delivery')
<<<<<<< HEAD
        elif searchParameter == 'dish_id':
            address = order.get('delivery')
            if Value.lower() in address.get('dish_id'):
                searched_orders.append.get('dish_id')
=======
>>>>>>> e7253d78edadf48b6aaa635043ac4db73c8c88a5
        else:
            return (False, 'Error: Cannoy be found within data')
    return (True, searched_orders)
    #Ff there is not false return then the true return along with a list of all searched orders is returned



#Tests
print(retrieveOrder('restaurant', 'Burger Bistro'))
print(retrieveOrder('order_id', 8))
print(retrieveOrder('postcode', "BN2 5EF"))
print(retrieveOrder('dish_id', '13123'))