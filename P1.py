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
    
    # dar vagheyiat faghat baazi az afrad (anhayi ke code e takhfif darand) shamele takhfif mishavand, baraye shabihsazie in mozu va baraye inke 
    # betavanim dar in onlineshop ham takhfif dashte bashim function e zir ra taarif mikonim :
    def get_discount(self) :
        discount = uniform(-0.1,0.5)
        first_price = self.shopping_cart.total_cost()
        second_price = first_price * (1 - discount)
        self.got_discount = True
        return second_price        
    # dar vaghe dar in function be moshtari in emkan dade mishavad ke agar mikhahad dar in ghore keshi sherkat konad 
    # va agar shans biavarad ta saghfe 50% takhfif begirad, hamchenin 1/6 ehtemal darad ba sherkat dar in ghore keshi gheymat ta saghfe 10% afzayesh yabad
    
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
        #in shart check mikonad ta moshtari bish az mojudie 1 jens az an be sabade kharide khod ezafe nakonad :
        if self.warehouse_items.loc[self.warehouse_items["name"] == item]["stock"].values[0] >= number : 
            self.my_cart[str(item)] = (number, item.price, float(number * item.price)) # taghirat dar dictionary save shavad
            # dar 3 khate baad taghirate hasel baraye file csv ra emal mikonim
            self.warehouse_items.loc[self.warehouse_items["name"] == item, "stock"] -= number 
            self.warehouse_items.to_csv(f"{self.warehouse.name}warehouse.csv", index=False)
            self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
            return True
        else : 
            return False  # agar moshtari bekhahad bishtar az mojudi e anbar be sabad ezafe konad False return mishavad

    def remove_from_cart(self, item, number) : 
        first_number = self.my_cart[str(item)][0]
        # check mikonim ta moshtari be ehtebah bishtar az tedadi ke dar sabad kharid hast ra remove nakonad
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
        print('4.search in available products')
        
        
        
    if choice == 3 :
        break
