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



#class Admin:

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