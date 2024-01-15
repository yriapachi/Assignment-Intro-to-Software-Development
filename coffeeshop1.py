import csv
from files import get_users,get_orders_by_name
from manager import day_orders,total_delivered,customer_names,all_data
from clerk import set_order,check_pending
from delivery import update_order



def find_user_role(username, password):
    file = open("users.csv")
    reader = csv.DictReader(file)
    for row in reader:
        if row['username'] == username \
            and row['password'] == password:
            return row['role']
    return None


username = input("Give username: ")
password = input("Give password: ")

role = find_user_role(username, password)

def manager_menu():
    print('MANAGER')
    print('1. Check number of orders placed by a specific customer')
    print('2. Check number of orders in one specific day')
    print('3. Check total amount of orders delivered')
    print('4. Names of customers')
    print('5. Check all data entered')
    print('0. Exit')
    choice=int(input('Choose: '))
    return choice

def clerk_menu():
    print('CLERK')
    print('1. Set order')
    print('2. Check for pending orders')
    print('0. Exit')
    choice=int(input('Choose: '))
    return choice

def delivery_menu():
    print('DELIVERY')
    print('1. Update order')
    print('0. Exit')
    choice=int(input('Choose: '))
    return choice



choice='0'
while True:
    if role=='manager':
       choice=manager_menu()
       if choice==1:
           name=input('Enter customer name: ')
           get_orders_by_name(name)
       elif choice==2:
           day_orders()
       elif choice==3:
           total_delivered()
       elif choice==4:
           customer_names()
       elif choice==5:
           all_data()
       elif choice==0:
           break
       
    elif role=='clerk':
        choice=clerk_menu()
        if choice==1:
           set_order()
        elif choice==2:
           check_pending()
        elif choice==0:
           break
    elif role=='delivery':
        choice=delivery_menu()
        if choice==1:
            update_order()
        elif choice==0:
            break
  
