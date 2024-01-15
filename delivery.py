import csv
def update_order():
 with open('orders.csv', 'r') as file:
        reader = csv.DictReader(file)
        orders = list(reader)
    
 for order in orders:
        if order['complete'] == '1':
            answer = input('Update order? ')
            if answer.lower() == 'yes':
                order['complete'] = '0'

   
 with open('orders.csv', 'w', newline='') as file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(orders)


   


