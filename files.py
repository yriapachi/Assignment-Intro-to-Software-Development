import csv

def get_users():
    with open("users.csv") as file:
        reader = csv.DictReader(file)
        users = {row['username']: row for row in reader}
    return users

def get_orders_by_name(name):
    with open('orders.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['name'] == name:
                print(row)
    return None

def get_orders():
    with open("orders.csv") as file:
        reader = csv.DictReader(file)
        orders = {row['id']: row for row in reader}
    return orders






