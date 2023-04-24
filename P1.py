from random import randint
import re
from datetime import datetime

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
"""
bayad ye object az product be in def paas dade beshe 
    def add_item(self, product_obj):
        if len(self.products) < self.capacity:
            if item_code in self.products:
                self.products[product_obj.code]['stock'] += quantity
            else:
                self.products[product_obj.code] = {'item_name': product_obj.name, 'price': product_obj.price, 
                'color': product.color, 'size': product_obj.size, 'material': product_obj.material, 'stock': product_obj.quantity}
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



class Cart:

 pay gharare oon safhe vared kardane shomare card va takmil farayand kharid ro shabih sazi kone

"""
"""

class Transaction:
    def __init__(self):
        self.transaction_type = self._get_transaction_type()
        self.amount = self._get_amount()
        self.description = self._get_description()

    def _get_transaction_type(self):
        while True:
            transaction_type = input("Enter transaction type (debit/credit): ")
            if transaction_type.lower() not in ['debit', 'credit']:
                print("Error: Invalid transaction type. Please enter debit or credit.")
                continue
            return transaction_type.lower()

    def _get_amount(self):
        while True:
            try:
                amount = float(input("Enter transaction amount: "))
            except ValueError:
                print("Error: Invalid amount. Please enter a number.")
                continue
            return amount

    def _get_description(self):
        while True:
            description = input("Enter transaction description: ")
            if len(description) > 50:
                print("Error: Description is too long. Please enter a shorter description.")
                continue
            return description

"""


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





pay = Pay("ali", "aghaei")

"""
    def








            self.code_peygiri = np.random()
            self.tarikh_sabt_sefaresh = time.now()
"""
"""
class Address:
    def __init__(self, sharestan, shahr, baze_tahvil, addrees_koli, code_posti, pelak, vahed, phone_number, tahvil_girande):

class Factor:
    def __init__(self, gheymat, ajnas, address,tarikh_sabt_sefaresh ):
"""
