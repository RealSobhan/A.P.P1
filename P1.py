from random import randint
import re
from datetime import datetime
import csv
import pandas as pd




"""class Inventory:

class Customer:

class Admin:
"""
class Product:
    def __init__(self, code, name, price, color, size, material, stock, warehouse):
        self.code = code
        self.name = name
        self.price = price
        self.color = color
        self.size = size
        self.material = material
        self.stock = stock
        #self.warehouse = warehouse
"""
    def add_stock(self, amount):
        self.stock += amount
    
    def remove_stock(self, amount):
        if self.stock - amount < 0:
            raise ValueError("Not enough stock")
        self.stock -= amount

    def update_price(self, new_price):
        self.price = new_price
        
    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "price": self.price,
            "color": self.color,
            "size": self.size,
            "material": self.material,
            "stock": self.stock,
            "warehouse": self.warehouse
        }
          
    def __str__(self):
        return f"{self.name} - {self.color}, {self.size}, {self.material} (${self.price}) available at {self.warehouse}"
"""
class Warehouse:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products = {}

#bayad ye object az product be in def paas dade beshe
    def add_item(self, product_obj, quantity):
        if len(self.products) < self.capacity:
            if product_obj.code in self.products:
                self.products[product_obj.code]['stock'] += quantity
            else:
                self.products[product_obj.code] = {'item_name': product_obj.name, 'price': product_obj.price, 
                'color': product_obj.color, 'size': product_obj.size, 'material': product_obj.material, 'stock': product_obj.quantity}
        else:
            print("Warehouse is at full capacity.")
"""
    #ye def update gheymat bayad neveshte beshe
    def add_item(self, item_code, item_name, price, color, size, material, quantity):
        if len(self.products) < self.capacity:
            if item_code in self.inventory:
                self.inventory[item_code]['stock'] += quantity
            else:
                self.inventory[item_code] = {'item_name': item_name, 'price': price, 'color': color, 'size': size, 'material': material, 'stock': quantity}
        else:
            print("Warehouse is at full capacity.")
"""
    def remove_item(self, item_code, quantity):
        if item_code not in self.products:
            return False
        if self.products[item_code]['stock'] < quantity:
            return False
        self.products[item_code]['stock'] -= quantity
        return True
    
    def update_price(self, item_code, new_price):
        self.products[item_code]["price"] = new_price
    
    def search_products(self, material=None, color=None, size=None, max_price=None):
        results = []
        for product in self.products:
            if (not material or product.material == material) and \
               (not color or product.color == color) and \
               (not size or product.size == size) and \
               (not max_price or product.price <= max_price):
                results.append(product)
        return results
    
    def get_products_by_color(self, color):
        color_products = []
        for product in self.products:
            if product.color == color:
                color_products.append(product)
        return color_products
    
    def get_products_by_material(self, material):
        material_products = []
        for product in self.products:
            if product.material == material:
                material_products.append(product)
        return material_products
    
    def get_products_by_size(self, size):
        size_products = []
        for product in self.products:
            if product.size == size:
                size_products.append(product)
        return size_products
    
    def get_products_by_price_range(self, min_price, max_price):
        price_range_products = []
        for product in self.products:
            if min_price <= product.price <= max_price:
                price_range_products.append(product)
        return price_range_products
    
    def __str__(self):
        return f"Warehouse at {self.location} - {len(self.products)} products"
from random import uniform
import pandas as pd
#class Inventory:

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



#class Admin :


#class Product:


# ajnas dakhele cart tu ye dictionary rikhte mishan ke key haye dictionary esme jens va value haye dictionary tuple hastan
# tuple[0] = tedad , tuple[1] = gheymate vahede oon jens, tuple[2] = gheymate oon tedad jens
class Cart:
    
    def __init__(self, warehouse) :
        self.my_cart = {}
        self.warehouse = warehouse
        self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
    
    def add_to_cart(self, item, number) : 
        if self.warehouse_items.loc[self.warehouse_items["name"] == item]["stock"].values[0] >= number :
            self.my_cart[str(item)] = (number, item.price, float(number * item.price))
            self.warehouse_items.loc[self.warehouse_items["name"] == item, "stock"] -= number
            self.warehouse_items.to_csv(f"{self.warehouse.name}warehouse.csv", index=False)
            self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
            return True
        else :
            return False

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

def create_csv(csv_name, lst_header):
    with open(f'{csv_name}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(lst_header)
    return "csv created"


class Pay:
    def __init__(self, c_first_name, c_last_name):
        self.confirm_card_number = True
        self.confirm_cvv2 = True
        self.confirm_expire_date = True
        self.card_number = self.get_card_number()
        self.cvv2 = self.get_cvv2()
        self.expire_date = self.get_expire_date()
        self.tracking_code = random_number_with_n_digits(10)  # code peygiri az taraf banke 10 raghami
        self.order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.Transaction = self.Transaction_info(c_first_name, c_last_name)
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
    def Transaction_info(self, first_name, last_name):
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





#pay = Pay(customer.first_name, customer.last_name)




class Address:
    def __init__(self):
        self.state = self.get_state()
        self.city = self.get_city(self.state)
        self.overall_address = self.get_address()
        self.postal_code = self.get_postal_code()
        self.receiver = self.get_receiver()
        self.phone_number = self.get_phone_number()
        self.delivery_type = self.delivery_type(self.state)
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
    def delivery_type(self, state):
        if state == "Tehran":
            delivery_type = "peyk"
        else:
            delivery_type = "post"
        return delivery_type
    def delivery_time(self):
        print("Available delivery times:")
        try:
            df = pd.read_csv("delivery_time.csv")
        except FileNotFoundError:
            create_csv("delivery_time", ["sobh", "zohr", "asr"])
            df = pd.read_csv("delivery_time.csv")
        zohr_capacity = df.iloc[:, 1:].sum()[0]
        asr_capacity = df.iloc[:, 1:].sum()[1]
        print("#.sobh")
        if zohr_capacity < 3:
            print("$.zhor")
        if asr_capacity < 3:
            print("*.asr")

        choice = input("Enter your choice here: ")
        if choice == "#":
            new_row = pd.DataFrame({'sobh': [1], 'zohr': [0], 'asr': [0]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv('delivery_time.csv', index=False)
        elif choice == "$":
            new_row = pd.DataFrame({'sobh': [0], 'zohr': [1], 'asr': [0]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv('delivery_time.csv', index=False)
        elif choice == "*":
            new_row = pd.DataFrame({'sobh': [0], 'zohr': [0], 'asr': [1]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv('delivery_time.csv', index=False)

address = Address()


"""
class Factor:
    def __init__(self, gheymat, ajnas, address,tarikh_sabt_sefaresh ):
"""
    def remove_from_cart(self, item, number) : 
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
        
        

#class Pay:
#    def __init__(self, card_number, cvv2, expire_date, gmail= None):

#class Address:
#    def __init__(self, sharestan, shahr, baze_tahvil, addrees_koli, code_posti, pelak, vahed, phone_number, tahvil_girande):

#class Factor:
#    def __init__(self, gheymat, ajnas, address,tarikh_sabt_sefaresh ):

warehouse = Warehouse("P1","Iran")

while True :
    print("welcome to our online shop")
    print("1.Admin")
    print("2.Customer")
    print("3.Exit")
    choice = int(input("Enter your choice here : "))
    if choice == 1 :
        print('---------Admin panel---------')
        print("1.Add item to inventory")
        print("2.remove item from inventory")
        print("3.Update price")
        print("4.Update warehouse quantity using csv file")
        print("5.Update warehouse quantity manually")
        choice = int(input("Enter your choice here : "))
        if choice == 1 :
            code = int(input("Enter the product code : "))
            name = input("Enter the product name : ")
            price = float(input("Enter the product price : "))
            color = input("Enter the product color : ")
            size = input("Enter the product size : ")
            material = input("Enter the product material : ")
            quantity = int(input("Enter product quantity : "))
            product_obj = Product(code, name, price, color, size, material)
            warehouse.add_item(product_obj, quantity)
            print("Product added seccessfully.")

        elif choice == 2 :
            code = int(input("Enter the product code : "))
            quantity = int(input("Enter product quantity : "))
            warehouse.remove_item(code, quantity)

        elif choice == 3 :
            code = int(input("Enter the product code : "))
            new_price = float(input("Enter product new price : "))
            warehouse.update_price(code, new_price)

        elif choice == 4 :
            

        elif choice == 5 :
            code = int(input("Enter the product code : "))
            quantity = float(input("Enter product new quantity : "))
            warehouse.update_price(code, quantity)
            

    
    if choice == 2 :
        print("1.Show available products")
        print("2.Add product to my cart")
        print("3.Show my cart") # az in gozine mishavad pardakht kard va product ha ra az cart hazf konim
        
        
        
    if choice == 3 :
        break
