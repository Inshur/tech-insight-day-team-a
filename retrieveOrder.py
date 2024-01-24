import json
from multiprocessing.sharedctypes import Value
from re import search
import requests

response = requests.get("https://europe-west1-inshur-dev0-service0.cloudfunctions.net/delivery-api-orders")
global orders
global searched_orders

orders = response.json()
orders = orders['data']

possibleSearches = ['order_id', 'date', 'restaurant', 'postcode', 'contact_number', 'house_number', 'dish_id']

searched_orders = []

def retrieveOrder(searchParameter, Value):
    for order in orders:
        if searchParameter == 'order_id':
            if Value < 0:
                return (False, 'Error: Value can not be below zero')
            if str(Value) in order.get(searchParameter):
                searched_orders.append(order)
        elif searchParameter == 'date':
            if str(Value) in order.get(searchParameter):
                searched_orders.append(order)
        elif searchParameter == 'restaurant':
            restaurant = order.get('restaurant')
            if Value.lower() in restaurant.get('name'):
                searched_orders.append(order)
        elif searchParameter == 'postcode':
            address = order.get('delivery')
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
        elif searchParameter == 'dish_id':
            address = order.get('delivery')
            if Value.lower() in address.get('dish_id'):
                searched_orders.append.get('dish_id')
        else:
            return (False, 'Error: Cannoy be found within data')
    return (True, searched_orders)


print(retrieveOrder('restaurant', 'Burger Bistro'))
print(retrieveOrder('order_id', 8))
print(retrieveOrder('postcode', "BN2 5EF"))
print(retrieveOrder('dish_id', '13123'))