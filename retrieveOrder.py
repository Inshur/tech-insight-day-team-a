import json
from multiprocessing.sharedctypes import Value
from re import search
import requests

response = requests.get("https://europe-west1-inshur-dev0-service0.cloudfunctions.net/delivery-api-orders")
global orders

orders = response.json()
orders = orders['data']

possibleSearches = ['order_id', 'date', 'restaurant', 'postcode']

def retrieveOrder(searchParameter, Value):
    for order in orders:
        if searchParameter == 'order_id' or searchParameter == 'date':
            if order.get(searchParameter) == str(Value):
                return order
        elif searchParameter == 'restaurant':
            restaurant = order.get('restaurant')
            if restaurant.get('name') == Value:
                return order
        elif searchParameter == 'postcode':
            address = order.get('delivery')
            if address.get('postcode') == Value:
                return order
        else:
            print('Order not in data')
            return 0


#print(retrieveOrder('restaurant', 'Burger Bistro'))
#print(retrieveOrder('order_id', 8))
#print(retrieveOrder('postcode', "BN2 5EF"))