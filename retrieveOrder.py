import json
from multiprocessing.sharedctypes import Value
from re import search
import requests

response = requests.get("https://europe-west1-inshur-dev0-service0.cloudfunctions.net/delivery-api-orders")
global orders

orders = response.json()
orders = orders['data']

possibleSearches = ['order_id', 'date', 'restaurant', 'postcode']

searched_orders = []

def retrieveOrder(searchParameter, Value):
    for order in orders:
        if searchParameter == 'order_id':
            if Value < 0:
                return (False, 'Error: Value can not be below zero')
            if order.get(searchParameter).contains(str(Value)):
                searched_orders.append(order)
        elif searchParameter == 'date':
            if order.get(searchParameter).contains(str(Value)):
                searched_orders.append(order)
        elif searchParameter == 'restaurant':
            restaurant = order.get('restaurant')
            if restaurant.get('name').contains(Value.lower()):
                searched_orders.append(order)
        elif searchParameter == 'postcode':
            address = order.get('delivery')
            if address.get('postcode').contains(Value.lower()):
                searched_orders.append(order)
        else:
            return (False, 'Error: Cannoy be found within data')
        return (True, searched_orders)


#print(retrieveOrder('restaurant', 'Burger Bistro'))
#print(retrieveOrder('order_id', 8))
#print(retrieveOrder('postcode', "BN2 5EF"))