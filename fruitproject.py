#      Fruit Inventory shop

#Innitial list of Fruits  with quantity , CP , SP

data = [
    {"name": "orange", "qty": 200, "cp": 8, "sp": 10},
    {"name": "banana", "qty": 150, "cp": 4, "sp": 5},
    {"name": "apple", "qty": 200, "cp": 15, "sp": 20},
    {"name": "papaya", "qty": 20, "cp": 30, "sp": 50}}
]


# ************     Common logics for all   ****************
#1)
def present_fruits_data():
    fruits_list_data = [i['name'] for i in data]
    return fruits_list_data # ['orange', 'banana', 'apple']


#3)
def index_val(lst,val_name):
    index_num = lst.index(val_name)
    return index_num
    


# **********           customer related operations logics      ***********

def fruits_values_in_cart():
    fruits_list_cart = [i['name'] for i in cart]
    return fruits_list_cart #['orange', 'banana']




# **********           Owner related operations logics      ***********

owner_id = {'username':'j','password':'h'}




def money_details(data):
    ch_total_profit_estimation = input('You want to know total profit estimation(yes or no): ').strip().lower()
    total_sp = [i['sp']*i['qty'] for i in data]
    total_cp = [i['cp']*i['qty'] for i in data]
    if ch_total_profit_estimation == 'yes':
        print(f'In your presnt stock total profit is {sum(total_sp)-sum(total_cp)}$ only/-')

    ch_total_revenue_estimation = input('You want to know revenue(yes or no): ').strip().lower()
    if ch_total_revenue_estimation == 'yes':
        print(f'In your presnt stock total revenue is {sum(total_sp)}$ only/-')
       



def remove_fruits(data):
    ch_fruit_name = input('Enter fruit name you want to remove: ').strip().lower()
    if ch_fruit_name in present_fruits_data():
        index_of_fruit = present_fruits_data().index(ch_fruit_name)
        del data[index_of_fruit]
        print(f"{ch_fruit_name} is succesfully removed.")

    else:
        print(f'{ch_fruit_name} is not present in the existing fruits.')



def add_new_fruits(data):
    ch_add_fruit_name = input('Enter name of the fruit you want to add: ').strip().lower()
    present_fruits = present_fruits_data()
    if ch_add_fruit_name not in present_fruits:
        while True:
            try:
                ch_qnt_cp_sp = input('Enter Qty, CP, SP (seperate with atleast one space): ').strip().split()
                #ch_qnt_cp_sp = [qnt, CP, SP]
            
                temp = {"name": ch_add_fruit_name, "qty": int(ch_qnt_cp_sp[0]), "cp": int(ch_qnt_cp_sp[1]), "sp": int(ch_qnt_cp_sp[2])}
                break
            except:
                print()
                print('***Condition:Enter theree values seperate with atleast one space *** ')
        data.append(temp)
        print('Succesfully added.')
    else:
         print(f'{ch_add_fruit_name} is already present in Existing fruits.')

    
    

def modify_qnt_prices_of_fruits(data):
    print('*'*30)
    print('Existing fruits are:')
    present_fruits = present_fruits_data()
    print(present_fruits)
    print()
    print('*'*30)
    
    ch_qnt_update = input('Do you want to update Quantity (Yes or No): ' ).strip().lower()
    ch_prices_update  =  input('Do you want to update the prices (Yes or No): ' ).strip().lower()
    if  ch_qnt_update in temp_yes or ch_prices_update in temp_yes:
        fruit_name = input('Enter the fruit name: ').strip().lower()
        
        if fruit_name in present_fruits:
            index_num = present_fruits.index(fruit_name)# index val of fruit
            if ch_qnt_update == 'yes' :
                try:
                    temp_qnt = int(input('Enter how many you want to add: '))
                except:
                    print('You enterred the wrong input ! Enter in positive integer value')
                    return
                
                data[index_num]['qty'] = data[index_num]['qty'] + temp_qnt
                print(f'{"*"*5}{temp_qnt} {fruit_name}s are added.{"*"*5}')
                print()

            if ch_prices_update == 'yes' :
                price_option_CP = input('Do you want to update CP (Yes or No): ').strip().lower()
                if price_option_CP == 'yes':
                    print(f'Present CP price is {data[index_num]["cp"]}')
                    price_of_CP = int(input('Enter the CP price: '))
                    data[index_num]['cp'] = price_of_CP
                    print(f'{"*"*5}Succesfully updated CP price of {fruit_name} {"*"*5}')
                    print()
                                      
                price_option_SP = input('Do you want to update SP (Yes or No): ').strip().lower()
                if price_option_SP == 'yes':
                    print(f'Present SP price is {data[index_num]["sp"]}')
                    price_of_SP = int(input('Enter the SP price: '))
                    data[index_num]['sp'] = price_of_SP
                    print(f'{"*"*5} Succesfully updated SP price of {fruit_name} {"*"*5}')
                    
        else:
            print
            print(f'{fruit_name} is not in the existing fruits.')
    

def View_Inventory(data):
    print('*'*35)
    print(f"{'Item':<10} | {'Qty':<8} | {'CP':<5} | {'SP':<5}")
    print("-" * 35)
    for item in data:
        print(f"{item['name'].capitalize():<10} | {item['qty']:<8} | {item['cp']:<5} | {item['sp']:<5}")
 
    print('*'*35)

def shop_owner_view():
    print("""
Choose one option:
1. View Inventory
2. Add Existing fruits
and Change prices                                                        
3. Add New fruits
4. Remove fruits
5. Money details
6. Exit""")       


# *********  Customer related operations logics  *********

def bill_generate():
    print()
    print('****** Your Total Bill ****** ')
    print(f'Customer Name:{customer_name} -- Phone Number:{customer_number}')
    print()
    
    print(f"{'Item':<10} | {'Quantity':<10} | {'SP':<5} | {'Item Price':<10}")
    print('-'*42)
    for item in cart:
        print(f"{item['name'].capitalize():<10} | {item['qty']:<10} |\
 {item['SP']:<5} | {item['qty']*item['SP']}")
    print('-'*42)
    total_amount = sum([item['qty']*item['SP'] for item in cart])
    print(f"{'Total Amount is':>31} : {total_amount}rupees ")
    print('-'*42)

    

#4view cart
def view_cart():
    flag = True
    if cart:
        print("****** CART ******")
        print('*'*30)
        print(f"{'Item':^10} | {'Qty':^8} | {'SP':^5}")
        print("-" * 30)
        for item in cart:
            print(f"{item['name'].capitalize():^10} | {item['qty']:^8} |  {item['SP']:^5}")

        print('*'*30)
        return flag

    else:
        flag = False
        print('There is no items present in your cart.')
        return flag


#3.Remove items from cart
def remove_items_cart():
    if not view_cart():
        return
    
    print()
    ch_fruit_customer = input("Enter the fruit name you want to remove in your cart: ").strip().lower()
    fruits_list_cart = fruits_values_in_cart()
    
    if ch_fruit_customer in fruits_list_cart:
        index_of_fruit = fruits_list_cart.index(ch_fruit_customer)

        fruit_qnt = cart[index_of_fruit]['qty']
        cart.pop(index_of_fruit)

        print()
        # removed item is adding to the data  present_fruits_data
        index_num_in_data =  present_fruits_data().index(ch_fruit_customer)
        data[index_num_in_data]['qty'] +=  fruit_qnt

        print(f"{ch_fruit_customer} removed and stock updated.")

    else:
        print("Item not found in cart.")
    
#2.Add items to cart
def add_items_to_cart():
    print('Available fruits are: ')
    present_fruits = present_fruits_data()
    print('*'*30)
    print(present_fruits)
    print('*'*30)
    print()
    
    while True:
        ch_fruits = input('Enter one fruit name you want to add to cart: ').strip().lower()
        if ch_fruits in present_fruits:
            
            while True:
                try:
                    fruit_quantity = int(input('Enter quantity : ').strip())
                except:
                    print('Enter Quantity in numbers only.')
                    print()
                    break


                fruit_qty_in_data = data[present_fruits.index(ch_fruits)]['qty']
                
                if fruit_quantity <= fruit_qty_in_data:
                    sp_of_fruit = data[present_fruits.index(ch_fruits)]['sp']

                    present_fruits_cart = fruits_values_in_cart()
                    if ch_fruits in present_fruits_cart:
                        index_of_fruit = present_fruits_cart.index(ch_fruits)
                        cart[index_of_fruit]['qty'] = cart[index_of_fruit]['qty'] + fruit_quantity
                        print()
                        print(f'{fruit_quantity} {ch_fruits} are added to cart.')
                        print()
                        
                    else:
                        cart_append_fruit_info = {'name': ch_fruits, 'qty':fruit_quantity, 'SP':sp_of_fruit}
                        # fruit is adding
                        cart.append(cart_append_fruit_info)
                        print()
                        print(f'{fruit_quantity} {ch_fruits} are added to cart.')
                        print()
                        
                    # Now update data (qty of fruit)
                    index_num = present_fruits.index(ch_fruits)# index val of fruit
                    data[index_num]['qty'] = data[index_num]['qty'] - fruit_quantity

                    ch_customer = input('Do you want to go back(Yes or No): ').strip().lower()
                    print()
                    if ch_customer == 'yes':
                        return
                    break
                        
                    
                else:
                    pritn()
                    print(f'{fruit_quantity} {ch_fruits} are not available in our stock.')
                    print(f'Available {ch_fruits} are {fruit_qty_in_data}.')
                    print()
                

                
        else:
            print()
            print(f'{ch_fruits} is not available in existing fruits.')
            print('Choose in existing fruits.')
            print()
            ch_customer = input('Do you want to go back(Yes or No): ').strip().lower()
            print()
            if ch_customer == 'yes':
                return
            print('Available fruits are: ')
            present_fruits = present_fruits_data()
            print(present_fruits)
            print()


# 1. View Inventory
def Customer_View_Inventory(data):
    print('*'*33)
    print('Inventory')
    print('-'*10)
    print(f"{'Item':<10} | {'Qty':<8} | {'SP':<5}")
    print("-" * 30)
    for item in data:
        print(f"{item['name'].capitalize():<10} | {item['qty']:<8} |  {item['sp']:<5}")
    print('*'*33)


def customer_view():
    print('''
choose one option:
1. View Inventory
2. Add items to cart
3.remove items from cart
4.view cart
5.Bill generate
6.Exit''')


def overal_response_option():
    overal_res = input('Choose one option:\n1.Shop owner view\n2.Customer view\n3.Exit\n\nEnter:')
    return overal_res



while True:
    overal_res = overal_response_option()
    
    if overal_res == '1':# Owner view details     *******************
        user_name = input('Enter your username:')
        pwd = input('Enter your password:')
        if user_name == owner_id['username'] and pwd == owner_id['password']:
            while True:
                shop_owner_view()
                print()
                owner_ch = input("Choose one option (Like 1 or 2): ")
                print()
                
                if owner_ch == '1': # View Inventory
                    View_Inventory(data)
                    
                elif owner_ch == '2':# Add Existing fruits and Change prices
                    modify_qnt_prices_of_fruits(data)
                    
                elif owner_ch == '3':# Add new fruits
                    add_new_fruits(data)

                elif owner_ch == '4':# Remove fruits
                    remove_fruits(data)
                    
                elif owner_ch == '5':
                    money_details(data)
                    
                elif owner_ch == '6':
                    print('Thanks for visiting')
                    print('Have a nice day')
                    break
                
    elif overal_res == '2':# Customer view details    *******************
        customer_name = input('Enter Your name: ').strip()
        try:
            customer_number = int(input('Enter your mobile number: ').strip())
        except:
            print('Enter valid number')
            break

        cart = []
        
        while True:
            customer_view()
            print()
            ch_customer = input('Choose one option: ').strip()
            print()

            if ch_customer == '1':
                Customer_View_Inventory(data)

            elif ch_customer == '2':
                add_items_to_cart()

            elif ch_customer == '3':
                remove_items_cart()

            elif ch_customer == '4':
                view_cart()

            elif ch_customer == '5':
                bill_generate()

            elif ch_customer == '6':
                print('!Thanks for comming, Visit again!')
                break
    break

                
                
                
#************** COMPLETED  SUCCESFULLY ****************                   
                                  


                   
        








