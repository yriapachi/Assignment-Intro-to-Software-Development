import csv
from files import get_orders
 
def set_order():
    order=get_orders()
    new_id=len(order)+1
    name=input('Give name: ')
    address=input('Give address: ')
    description=input('Give description: ')
    date=input('Give date:(DDMMYY) ')
    total=input('Give total: ')
    completed=1
    file=open('orders.csv','a')
    with open('orders.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([new_id, name, address, description, date, total, completed])
    file.close()

def check_pending():
    with open('orders.csv', 'r') as file:
        reader = csv.DictReader(file)
        pending_orders = []

        for row in reader:
            if row['complete']=='1':
                print(row)
                pending_orders.append(row)

        return pending_orders
    if not pending_orders:
        print('No pending orders')



