from random import randint
import re
from datetime import datetime
import csv
import pandas as pd




"""
class Inventory:

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


#class Cart:

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
        self.delivery_type = self.delivery_type(self.state)[0]
        self.delivery_price= self.delivery_type(self.state)[1]
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
            delivery_price = 30
        else:
            delivery_type = "post"
            delivery_price = 20
        return delivery_type, delivery_price
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
#address = Address()


"""
class Factor:
    def __init__(self, gheymat, ajnas, address,tarikh_sabt_sefaresh ):
"""
