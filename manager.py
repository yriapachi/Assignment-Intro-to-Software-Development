import csv
from files import get_orders_by_name,get_orders

def day_orders():
    d = input("Give date (DDMMYY): ")
    orders = get_orders()
    for key in orders:
        if orders[key]['date'] == d:
            print(orders[key])

def total_delivered():
    with open('orders.csv') as file:
        reader = csv.DictReader(file)
        for key in reader:
            if key['complete'] == '0':
                print(key)

def customer_names():
    file = open('orders.csv')
    reader = csv.DictReader(file)
    for names in reader:
        print(names['name'])

def all_data():
    file = open('orders.csv')
    reader = csv.DictReader(file)
    for row in reader:
        print(row)