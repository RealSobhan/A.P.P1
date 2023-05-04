from random import randint, uniform
import re
from datetime import datetime
import csv
import pandas as pd

class Product:
    def __init__(self, code, name, price, color, size, material):
        self.code = code
        self.name = name
        self.price = price
        self.color = color
        self.size = size
        self.material = material
        
# az vizhegihaye(attributes) product kam konim

class Warehouse:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        try:
            self.products = pd.read_csv(f"{self.name}warehouse.csv")
        except FileNotFoundError:
            create_csv(f"{self.name}warehouse", ["code", "name", "color", "size", "material", "stock", "price"])
            self.products = pd.read_csv(f"{self.name}warehouse.csv")

###     bayad ye object az product be in def paas dade beshe

    def add_item(self, product_obj, quantity):
        if product_obj.code in self.products["code"].tolist():
            self.products.loc[self.products["code"] == product_obj.code, "stock"] += quantity
        else:
            new_row = pd.DataFrame({'code': [product_obj.code], 'name': [product_obj.name], 'color': [product_obj.color],"size": [product_obj.size],
                                    "material": [product_obj.material], "stock": quantity, "price": [product_obj.price]})
            self.products = pd.concat([self.products, new_row], ignore_index=True)

        self.products.to_csv(f'{self.name}warehouse.csv', index=False)
        self.products = pd.read_csv(f"{self.name}warehouse.csv")
        
    def remove_item(self, item_code, quantity):
        if item_code not in self.products["code"].tolist():
            return "Item not found"  # error message
        if self.products.loc[self.products["code"] == item_code]["stock"].values[0] <= quantity:
            return "Insufficient items"  # error message
        self.products.loc[self.products["code"] == item_code, "stock"] -= quantity
        self.products.to_csv(f'{self.name}warehouse.csv', index=False)
        self.products = pd.read_csv(f"{self.name}warehouse.csv")
        return "Item removed succesfully"
    
    def update_price(self, item_code, new_price):
        self.products.loc[self.products["code"] == item_code, "price"] = new_price
        self.products.to_csv(f'{self.name}warehouse.csv', index=False)
        self.products = pd.read_csv(f"{self.name}warehouse.csv")
        return "price updated succesfully"
    
    def update_quantity(self, item_code, quantity):
        self.products.loc[self.products["code"] == item_code, "quantity"] = quantity
        self.products.to_csv(f'{self.name}warehouse.csv', index=False)
        self.products = pd.read_csv(f"{self.name}warehouse.csv")
        return "quantity updated succesfully"
    
    def update_quantiy_csv(self, input_csv_address):
        input_csv = pd.read_csv(f"{input_csv_address}")
        merged_df = pd.merge(self.products, input_csv[['code', 'quantity']], on = 'code', how = "left")
        merged_df['quantity'] = merged_df['quantity'].fillna(self.products['quantity'])
        self.products['quantity'] = merged_df['quantity']
        self.products.to_csv(f"{self.name}warehouse.csv", index=False)
        return "quantity updated succesfully"
    
    def file_output(self):
        output = self.products.copy()
        output["warehouse_code"] = 1
        output.to_csv('output.csv', index=False)
    
    def search_products(self, material=None, color=None, size=None, max_price=None):
        filtered_df = self.products.loc[(self.products['material'] == material) & (self.products['color'] == color)
                                        & (self.products['size'] == size) & (self.products['max_price'] == max_price)]
        return filtered_df
    
    def get_products_by_color(self, color):
        filtered_df_color = self.products.loc[(self.products['color'] == color)]
        return filtered_df_color
    
    def get_products_by_material(self, material):
        filtered_df_material = self.products.loc[(self.products['material'] == material)]
        return filtered_df_material
    
    def get_products_by_size(self, size):
        filtered_df_size = self.products.loc[(self.products['size'] == size)]
        return filtered_df_size
    
    def get_products_by_price_range(self, min_price, max_price):
        filtered_df_price = self.products.loc[(self.products['price'] >= min_price) & (self.products['price'] <= max_price)]
        return filtered_df_price


"""
class customer :
    def __init__(self, fname, lname, email) :
        self.shopping_cart = Cart()
        self.fname = fname
        self.lname = lname
        self.email = email        
        self.got_discount = False
    
    def get_discount(self) :
        discount = uniform(-0.1,0.5)
        first_price = self.shopping_cart.total_cost()
        second_price = first_price * (1 - discount)
        self.got_discount = True
        return second_price        
    
    def purchase(self) :
        if self.got_discount == True :
            res = self.get_discount()
        else :
            res = self.shopping_cart.total_cost()
        print(f"you should pay {res } for items in your cart")
        return res
"""



# ajnas dakhele cart tu ye dictionary rikhte mishan ke key haye dictionary esme jens va value haye dictionary tuple hastan
# tuple[0] = tedad , tuple[1] = gheymate vahede oon jens, tuple[2] = gheymate oon tedad jens
class Cart:
    def __init__(self, warehouse):
        self.my_cart = {}
        self.warehouse = warehouse
        self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
    
    def add_to_cart(self, item, number): 
        if self.warehouse_items.loc[self.warehouse_items["name"] == item]["stock"].values[0] >= number :
            self.my_cart[str(item)] = (number, item.price, float(number * item.price))
            self.warehouse_items.loc[self.warehouse_items["name"] == item, "stock"] -= number
            self.warehouse_items.to_csv(f"{self.warehouse.name}warehouse.csv", index=False)
            self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
            return True
        else :
            return False
    def remove_from_cart(self, item, number): 
        first_number = self.my_cart[str(item)][0]
        if number > first_number :
            print(f"you can't remove {number} number of this item from your cart, there was only {first_number} number in it.")

        elif number == first_number :
            self.warehouse_items.loc[self.warehouse_items["name"] == item, "stock"] += number
            self.warehouse_items.to_csv(f"{self.warehouse.name}warehouse.csv", index=False)
            self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
            del self.my_cart[str(item)]

        else : 
            self.warehouse_items.loc[self.warehouse_items["name"] == item, "stock"] += number
            self.warehouse_items.to_csv(f"{self.warehouse.name}warehouse.csv", index=False)
            self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
            remaining_nmber = first_number - number
            self.my_cart[str(item)] = (remaining_nmber, remaining_nmber * item.price)
            print(f"you removed {number} number(s) of this item and now there is {remaining_nmber} number(s) remeining in your cart")

    def show_my_cart(self) :
        print(self.my_cart)

    def empty_my_cart(self) : 
        for i in self.my_cart :
            self.warehouse_items.loc[self.warehouse_items["name"] == i, "stock"] += i[0]

        self.warehouse_items.to_csv(f"{self.warehouse.name}warehouse.csv", index=False)
        self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
        self.my_cart.clear()

    def total_cost(self) : 
        if len(self.my_cart) == 0 :
            return 0
        else :
            items_value = 0
            for i in self.my_cart.values() :
                items_value += i[2]

            return items_value
        
    def total_quantity(self) :
        if len(self.my_cart) == 0 :
            return 0
        else :
            items_quantity = 0
            for i in self.my_cart.values() :
                items_quantity += i[0]
            return items_quantity
        


#pay gharare oon safhe vared kardane shomare card va takmil farayand kharid ro shabih sazi kone



def create_csv(csv_name, lst_header):
    with open(f'{csv_name}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(lst_header)
    return "csv created"
def random_number_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)

def validate_email(email):
    return bool(re.match(
        r"^[a-zA-Z0-9\.\_]+@((gmail)|(yahoo)|(outlook)|(hotmail)|(live)|([a-z]*\.*[a-z]+\.ac)|(chmail))\.((com)|(ir))$",
        email, re.IGNORECASE))


class Pay:
    def __init__(self, c_first_name, c_last_name):
        self.confirm_card_number = True
        self.confirm_cvv2 = True
        self.confirm_expire_date = True
        self.card_number = self.get_card_number()
        self.cvv2 = self.get_cvv2()
        self.expire_date = self.get_expire_date()
        self.tracking_code = random_number_with_n_digits(11)
        self.order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_info(c_first_name, c_last_name)

    def get_card_number(self): #password chon hichi nadasht felan naneveshtamesh
        count = 0
        while count <= 2 and self.confirm_card_number:
            try:
                card_number = int(input("Enter your card number here: "))  # Validate card number
            except ValueError:
                print("Error: Enter numbers for card number!")
                count += 1
                continue
            if len(str(card_number)) != 16:
                print("Error: Enter Valid Card Number!")
                count += 1
                continue

            return card_number
        self.confirm_card_number = False
        return card_number

    def get_cvv2(self):
        count = 0
        while count <= 1 and self.confirm_cvv2:
            try:
                cvv2 = int(input("Enter your cvv2 here: "))  # Validate cvv2
            except ValueError:
                print("Error: Enter numbers for cvv2!")
                count += 1
                continue
            if (len(str(cvv2)) != 3) and (len(str(cvv2)) != 4):
                print("Error: Enter Valid cvv2!")
                count += 1
                continue

            return cvv2
        self.confirm_cvv2 = False
        return cvv2

    def get_expire_date(self):
        count = 0
        while count <= 1 and self.confirm_expire_date:
            expire_date = input("Enter your cards expire date in (YYYY-MM-DD) format: ")
            try:
                date_obj = datetime.strptime(expire_date, "%Y-%m-%d")
            except ValueError:
                print("Error: Enter in date format!")
                count += 1
                continue
            return expire_date
        self.confirm_expire_date = False
        return expire_date
    def transaction_info(self, first_name, last_name):
        with open('notes.txt', 'w') as f:
            f.write(f'First Name: {first_name}\nLast Name: {last_name}\n')
        if not self.confirm_card_number:
            with open('notes.txt', 'a') as f:
                f.write(f'Card Number: {self.card_number}                Card Number Status: Rejected')
        if self.confirm_card_number:
            with open('notes.txt', 'a') as f:
                f.write(f'Card Number: {self.card_number}                Card Number Status: Accepted')
        if not self.confirm_cvv2:
            with open('notes.txt', 'a') as f:
                f.write(f'\ncvv2:{self.cvv2}                             cvv2 Status: Rejected')
        if self.confirm_cvv2:
            with open('notes.txt', 'a') as f:
                f.write(f'\ncvv2:{self.cvv2}                             cvv2 Status: Accepted')
        if not self.confirm_expire_date:
            with open('notes.txt', 'a') as f:
                f.write(f'\nExpire Date:{self.expire_date}                 Expire Date Status: Rejected')
        if self.confirm_expire_date:
            with open('notes.txt', 'a') as f:
                f.write(f'\nExpire Date:{self.expire_date}                 Expire Date Status: Accepted')
        if self.confirm_card_number is False or self.confirm_cvv2 is False or self.confirm_expire_date is False:
            with open('notes.txt', 'a') as f:
                f.write(f'\nTransaction Status: Failed')
        if self.confirm_card_number is True and self.confirm_cvv2 is True and self.confirm_expire_date is True:
            with open('notes.txt', 'a') as f:
                f.write(f'\nTransaction Status: Successful')
            return True




#pay = Pay(customer.first_name, customer.last_name)



class Address:
    def __init__(self):
        self.state = self.get_state()
        self.city = self.get_city(self.state)
        self.overall_address = self.get_address()
        self.postal_code = self.get_postal_code()
        self.receiver = self.get_receiver()
        self.phone_number = self.get_phone_number()
        self.delivery_type = (self.get_delivery_type(self.state))[0]
        self.delivery_price= (self.get_delivery_type(self.state))[1]
        self.delivery_time = self.delivery_time()

    def get_state(self):
        while True:
            print("\nPlease choice your state from following choices:\n1.Tehran\n2.Esfehan\n3.Tabriz")
            choice = int(input("Enter your choice here: "))
            if choice == 1:
                return "Tehran"
            elif choice == 2:
                return "Esfehan"
            elif choice == 3:
                return "Tabriz"
            else:
                print("Invalid choice number!")
    def get_city(self, state):
        while True:
            if state == "Tehran":
                print("Please choice your city from following choices:\n1.Tehran\n2.EslamShahr")
                city = int(input("Enter your choice here: "))
                return city
            elif state == "Esfehan":
                print("Please choice your city from following choices:\n1.Esfehan\n2.Kashan")
                city = int(input("Enter your choice here: "))
                return city
            elif state == "Tabriz":
                print("Please choice your city from following choices:\n1.Tabriz\n2.Shabestar")
                city = int(input("Enter your choice here: "))
                return city
    def get_address(self):
        while True:
            address = input("Please enter your address here: ")
            return address
    def get_postal_code(self):
        while True:
            try:
                postal_code = int(input("Enter your postal-code here: "))  # Validate postal-code
            except ValueError:
                print("Error: Enter numbers for postal-code!")
                continue
            if len(str(postal_code)) != 10:
                print("Error: Enter Valid postal-code!")
                continue
            return postal_code
    def get_receiver(self):
        while True:
            print("Please enter who will receive your product:")
            receiver = input("Full Name: ")
            return receiver
    def get_phone_number(self):
        while True:
            phone_number = input("Enter your phone number in 09######## here: ") # Validate phone number
            if len(str(phone_number)) != 11:
                print("Error: Enter Valid phone number! phone number must be 10 digits")
                continue
            return phone_number
    def get_delivery_type(self, state):
        if state == "Tehran":
            delivery_type = "peyk"
            delivery_price = 20
        else:
            delivery_type = "post"
            delivery_price = 30
        return [delivery_type, delivery_price]
    def delivery_time(self):
        print("Available delivery times:")
        try:
            df = pd.read_csv("delivery_time.csv")
        except:
            create_csv("delivery_time", ["sobh", "zohr", "asr"])
            df = pd.read_csv("delivery_time.csv")
        zohr_capacity = df.iloc[:, 1:].sum()[0]
        asr_capacity = df.iloc[:, 1:].sum()[1]
        print("#.sobh")
        if zohr_capacity < 3:
            print("$.zohr")
        if asr_capacity < 3:
            print("*.asr")

        choice = input("Enter your choice here: ")
        if choice == "#":
            new_row = pd.DataFrame({'sobh': [1], 'zohr': [0], 'asr': [0]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv('delivery_time.csv', index=False)
            return "sobh"
        elif choice == "$":
            new_row = pd.DataFrame({'sobh': [0], 'zohr': [1], 'asr': [0]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv('delivery_time.csv', index=False)
            return "zohr"
        elif choice == "*":
            new_row = pd.DataFrame({'sobh': [0], 'zohr': [0], 'asr': [1]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv('delivery_time.csv', index=False)
            return "asr"


class Accounting:
    def __init__(self, cart, tracking_code, delivery_price):
        self.count_items = cart.total_quantity()
        self.total_cost_products = cart.total_cost()
        self.tax = self.total_cost_products * 0.09
        self.tracking_code = tracking_code
        self.delivery_price = delivery_price
        
    def add_order(self):
        try:
            df = pd.read_csv("accounting.csv")
        except FileNotFoundError:
            create_csv("accounting", ["tracking_code", "count_products", "products_price", "delivery_price", "tax" ])
            df = pd.read_csv("accounting.csv")
            
        new_row = pd.DataFrame({'tracking_code': [self.tracking_code], 'count_products': [self.count_items],
                                'products_price': [self.total_cost_products], 'delivery_price': [self.delivery_price], 'tax': [self.tax] })
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv('accounting.csv', index=False)
        return True
    
    

class Factor:
    def __init__(self, cart, delivery_time, tracking_code, delivery_type, cfirst_name ,clast_name, customer_address):
        self.item_name_list = list(cart.my_cart.keys())
        self.self_item_quantity = [list(cart.my_cart.values())[x][0] for x in range(len(list(cart.my_cart.values())))]
        self.self_item_price = [list(cart.my_cart.values())[x][1] for x in range(len(list(cart.my_cart.values())))]
        self.delivery_time = delivery_time
        self.tracking_code = tracking_code
        self.delivery_type = delivery_type
        self.cfirst_name = cfirst_name
        self.clast_name = clast_name
        self.customer_address = customer_address
        
    def create_factor(self):
        items = []
        for i in range(len(self.item_name_list)):
            item_name = self.item_name_list[i]
            item_price = self.self_item_price[i]
            item_quantity = self.self_item_quantity[i]
            items.append({"Item Name": item_name, "Price": item_price, "Quantity": item_quantity})
            
        total_cost = sum(item["Price"] * item["Quantity"] for item in items)

        invoice = """
-----------------------------------------
            SALES FACTOR
-----------------------------------------
Tracking Code: {}
Delivery Time: {}
Delivery Type: {}
Customer First Name: {}
Customer Last Name: {}
Customer Address: {}

|{:<20} |{:<10} |{:<10} |
|---------------------|-----------|-----------|
{}
------------------------------------------
Thank you for your purchase!        
        """.format(self.tracking_code, self.delivery_time, self.delivery_type, self.cfirst_name, self.clast_name ,self.customer_address, total_cost, "Item Name", "Price", "Quantity",
                "\n".join([f"|{item['Item Name']:<20} |${item['Price']:>9.2f} |{item['Quantity']:>10} |${item['Price']*item['Quantity']:>9.2f}|" for item in items]))
        print("Purchase was successfull!")
        with open('Factor.txt', 'w') as f:
            f.write(invoice)






warehouse_main = Warehouse("P1","Iran")
def admin_scenario():
    while True:
        print('---------Admin panel---------')
        print("1.Add item to inventory")
        print("2.remove item from inventory")
        print("3.Update price")
        print("4.Update warehouse quantity using csv file")
        print("5.Update warehouse quantity manually")
        print("6.Exit")
        choice = int(input("Enter your choice here : "))
        if choice == 1:     ### in okeye

            code = int(input("Enter the product code : "))
            name = input("Enter the product name : ")
            price = float(input("Enter the product price : "))
            color = input("Enter the product color : ")
            size = input("Enter the product size : ")
            material = input("Enter the product material : ")
            quantity = int(input("Enter product quantity : "))
            product_obj = Product(code, name, price, color, size, material)
            warehouse_main.add_item(product_obj, quantity)
            print("Product added successfully.")

        elif choice == 2:   ### in okeye
            code = int(input("Enter the product code : "))
            quantity = int(input("Enter product quantity : "))
            print(warehouse_main.remove_item(code, quantity))
            
        elif choice == 3:       ### in okeye
            code = int(input("Enter the product code : "))
            new_price = float(input("Enter product new price : "))
            print(warehouse_main.update_price(code, new_price))

        elif choice == 4:
            csv_address  = input("Enter the csv address here:")
            print(warehouse_main.update_quantiy_csv(csv_address))

        elif choice == 5:
            code = int(input("Enter the product code : "))
            quantity = float(input("Enter product new quantity : "))
            print(warehouse_main.update_quantity(code, quantity))
            
        elif choice == 6:
            break

        else:
            print("Enter valid choice")
            
            



def customer_scenario(cus_fname, cus_lname, warehouse):
    cart = Cart(warehouse)
    while True:
        print('\n---------Customer panel---------')
        print("1.Show available products")
        print("2.Add product to my cart")
        print("3.Show my cart") # az in gozine mishavad pardakht kard va product ha ra az cart hazf konim
        choice = int(input("Enter your choice here : "))
        if choice == 1:
            df = warehouse.products.set_index('code')

            # print the data frame in the desired format
            print("Code\tName\t\tMaterial\tcolor     \tSize\tQuantity\tPrice")
            print("----------------------------------------------------------------------------------------")
            for index, row in df.iterrows():
                print(f"{index}\t{row['name']}\t {row['material']}\t\t {row['color']}     \t {row['size']}\t   {row['stock']}\t\t${row['price']}")
        elif choice == 2:
            code = int(input("Enter the product code : "))
            quantity = int(input("Enter product quantity : "))
            print(warehouse_main.remove_item(code, quantity))
        elif choice == 3:
            print("\n1.Remove item from the cart")
            print("2.Confirm purchases")
            choice = int(input("Enter your choice here : "))
            if choice == 1:
                code = int(input("Enter the product code : "))
                quantity = int(input("Enter product quantity : "))
                print(warehouse_main.remove_item(code, quantity))
            elif choice == 2:
                address = Address()
                pay = Pay(cus_fname, cus_lname)
                if pay.confirm_card_number == True and pay.confirm_cvv2 == True and pay.confirm_expire_date == True:
                    factor = Factor(cart, address.delivery_time, pay.tracking_code, address.delivery_type, cus_fname, cus_lname, address.overall_address)
                    factor.create_factor()
                    accounting = Accounting(cart, pay.tracking_code, address.delivery_price)
                    accounting.add_order()
                
                
        

while True :
    print("-------------Welcome to our online shop-------------")
    print("1.Admin")
    print("2.Customer")
    print("3.Exit")
    choice = int(input("Enter your choice here : "))
    if choice == 1:
        admin_scenario()
        
    if choice == 2:
        fname = input("Enter your first name here : ")
        lname = input("Enter your last name here : ")
        customer_scenario(fname, lname, warehouse_main)
        
    if choice == 3:
        break

