from random import randint

class Inventory:

class Customer:

class Admin:

class Product:
    def __init__(self, code, name, price, color, size, material, stock, warehouse):
        self.code = code
        self.name = name
        self.price = price
        self.color = color
        self.size = size
        self.material = material
        self.stock = stock
        self.warehouse = warehouse
        
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
    
class Warehouse:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products = {}
        
    def add_item(self, item_code, item_name, price, color, size, material, quantity):
        if len(self.products) < self.capacity:
            if item_code in self.inventory:
                self.inventory[item_code]['stock'] += quantity
            else:
                self.inventory[item_code] = {'item_name': item_name, 'price': price, 'color': color, 'size': size, 'material': material, 'stock': quantity}
        else:
            print("Warehouse is at full capacity.")



class Cart:

""" pay gharare oon safhe vared kardane shomare card va takmil farayand kharid ro shabih sazi kone"""


def random_number_with_n_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def validate_email(email):
    return bool(re.match(r"^[a-zA-Z0-9\.\_]+@((gmail)|(yahoo)|(outlook)|(hotmail)|(live)|([a-z]*\.*[a-z]+\.ac)|(chmail))\.((com)|(ir))$", email, re.IGNORECASE))
class Pay:
    def __init__(self, card_number, cvv2, expire_date, gmail = None):
        self.card_number = card_number
        self.cvv2 = cvv2
        self.expire_date = expire_date
        self.gmail = gmail
        self.tracking_code = random_number_with_n_digits(10)#code peygiri az taraf banke 10 raghami
        self.order_date = None
        self.confirm = False
        #self.total_price = total_price



        if not isinstance(int, card_number): #validate card number
            return "Enter numbers for card number!"
        elif isinstance(int, card_number):
            if len(str(card_number)) != 16:
                return "Enter Valid Card Number!"
            else:
                pass


        if not isinstance(int, cvv2): #validate cvv2
            return "Enter numbers for cvv2!"
        elif isinstance(int, cvv2):
            if (len(str(cvv2)) != 3) or (len(str(cvv2)) != 4):
                return "Enter valid numbers for cvv2"








            self.code_peygiri = np.random()
            self.tarikh_sabt_sefaresh = time.now()
class Address:
    def __init__(self, sharestan, shahr, baze_tahvil, addrees_koli, code_posti, pelak, vahed, phone_number, tahvil_girande):

class Factor:
    def __init__(self, gheymat, ajnas, address,tarikh_sabt_sefaresh ):