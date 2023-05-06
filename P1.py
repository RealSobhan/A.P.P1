from random import randint
import re
from datetime import datetime
import csv
import pandas as pd

# chandinja csv niaz boode ke tabe zade shode baraye sakht csv
def create_csv(csv_name, lst_header):
    with open(f'{csv_name}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(lst_header)
    return "csv created"

# gharar bood chandin code rahgiri dashte bashim ke tabesh zade shod ama estefade chandin bare nashode, ama baz code tamiz tare
def random_number_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)

# gharar bood email ham validate konim ke goftim baraye test project kar sakht mishe, ama tabesh zade shode va kar mikone 
def validate_email(email):
    return bool(re.match(
        r"^[a-zA-Z0-9\.\_]+@((gmail)|(yahoo)|(outlook)|(hotmail)|(live)|([a-z]*\.*[a-z]+\.ac)|(chmail))\.((com)|(ir))$",
        email, re.IGNORECASE))
    

"""
har mahsool forooshgah ba attribute haye class Product shenakhte mishe ke
attribute code ro farz ba unique boodanesh gereftim
"""
class Product:
    def __init__(self, code, name, price, color, size, material):
        self.code = code 
        self.name = name 
        self.price = price
        self.color = color
        self.size = size # masalan xl, xxl 
        self.material = material
        
"""
class warehouse ba estefade az ye csv, kalahaye forooshgah ro mikhoone ke
age csv az ghabl sakhte nashode bashe, oono misaze ba esmi ke object warehouse_main behesh dade mishe va dar enteha sakhte shode
"""
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
        if self.products.loc[self.products["code"] == item_code]["stock"].values[0] < quantity:
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
        self.products.loc[self.products["code"] == item_code, "stock"] = quantity
        self.products.to_csv(f'{self.name}warehouse.csv', index=False)
        self.products = pd.read_csv(f"{self.name}warehouse.csv")
        return "quantity updated succesfully"
    
    def update_quantiy_csv(self, input_csv_address):
        input_csv = pd.read_csv(f"{input_csv_address}")
        merged_df = pd.merge(self.products, input_csv[['code', 'quantity']], on = 'code', how = "left")
        merged_df['quantity'] = merged_df['quantity'].fillna(self.products['stock'])
        self.products['stock'] = merged_df['quantity']
        self.products.to_csv(f"{self.name}warehouse.csv", index=False)
        return "quantity updated succesfully"
    
    def file_output(self): #khorooji csv ke admin migire
        output = self.products.copy()
        output["warehouse_code"] = 1
        output.to_csv('output.csv', index=False)
    
    #def search_products(self, material=None, color=None, size=None, max_price=None):      #search product ba har meyari!!
    #    filtered_df = self.products.loc[(self.products['material'] == material) & (self.products['color'] == color)
    #                                    & (self.products['size'] == size) & (self.products['max_price'] == max_price)]
    #    return filtered_df
    
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


class Cart:
    def __init__(self, warehouse):
        self.my_cart = {}
        self.warehouse = warehouse
        self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
    def add_to_cart(self, item_code, number):
        if item_code in self.warehouse_items["code"].tolist():
            if self.warehouse_items.loc[self.warehouse_items["code"] == item_code]["stock"].values[0] >= number:
                self.my_cart[item_code] = {"name":self.warehouse_items.loc[self.warehouse_items["code"] == item_code]["name"].values[0],
                                        "color":self.warehouse_items.loc[self.warehouse_items["code"] == item_code]["color"].values[0],
                                        "size":self.warehouse_items.loc[self.warehouse_items["code"] == item_code]["size"].values[0],
                                        "material":self.warehouse_items.loc[self.warehouse_items["code"] == item_code]["material"].values[0],
                                        "price":self.warehouse_items.loc[self.warehouse_items["code"] == item_code]["price"].values[0],
                                        "quantity":number}
                self.warehouse_items.loc[self.warehouse_items["code"] == item_code, "stock"] -= number
                self.warehouse_items.to_csv(f"{self.warehouse.name}warehouse.csv", index=False)
                self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
                print("Item added successfully")
            else:
                print("Please Enter a qauntity that we have!")
        else:
            print("Invalid Code!")
    def remove_from_cart(self, item_code, number): 
        first_number = self.my_cart[item_code]["quantity"]
        if number > first_number :
            print(f"you can't remove {number} number of this item from your cart, there was only {first_number} number in it.")

        elif number == first_number :
            self.warehouse_items.loc[self.warehouse_items["code"] == item_code, "stock"] += number
            self.warehouse_items.to_csv(f"{self.warehouse.name}warehouse.csv", index=False)
            self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
            del self.my_cart[item_code]

        else : 
            self.warehouse_items.loc[self.warehouse_items["code"] == item_code, "stock"] += number
            self.warehouse_items.to_csv(f"{self.warehouse.name}warehouse.csv", index=False)
            self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
            remaining_nmber = first_number - number
            self.my_cart[item_code]["quantity"] = remaining_nmber 
            print(f"you removed {number} number(s) of this item and now there is {remaining_nmber} number(s) remeining in your cart")

    def show_my_cart(self) :
        print(self.my_cart)

    def empty_my_cart(self) : 
        for i in self.my_cart :
            self.warehouse_items.loc[self.warehouse_items["code"] == i, "stock"] += i["quantity"]

        self.warehouse_items.to_csv(f"{self.warehouse.name}warehouse.csv", index=False)
        self.warehouse_items = pd.read_csv(f"{self.warehouse.name}warehouse.csv")
        self.my_cart.clear()

    def total_cost(self) : 
        if len(self.my_cart) == 0 :
            return 0
        else :
            items_value = 0
            for i in self.my_cart :
                items_value += self.my_cart[i]["quantity"] * self.my_cart[i]["price"]

            return items_value
        
    def total_quantity(self) :
        if len(self.my_cart) == 0 :
            return 0
        else :
            items_quantity = 0
            for i in self.my_cart :
                items_quantity += self.my_cart[i]["quantity"]
            return items_quantity
        
#pay gharare oon safhe vared kardane shomare card va takmil farayand kharid ro shabih sazi kone
class Pay:
    def __init__(self, c_first_name, c_last_name):
        self.confirm_card_number = True # 3 flag baraye confirm dorosrt sefaresh gozashte shode, age har 3 True boodan, transaction successfulle
        self.confirm_cvv2 = True
        self.confirm_expire_date = True
        self.card_number = self.get_card_number()
        self.cvv2 = self.get_cvv2()
        self.expire_date = self.get_expire_date()
        self.tracking_code = random_number_with_n_digits(11)
        self.order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_info(c_first_name, c_last_name) # baraye sakht ye file note be esm "notes.txt" baraye sabt inke transaction movafagh bood ya na

    def get_card_number(self): #password chon hichi nadasht neveshte nashod
        count = 0 
        while count <= 2 and self.confirm_card_number: #user maximum 3 bar hagh eshtebah zadan card number ro dare
            try:
                card_number = int(input("Enter your card number here: "))  # Validate card number ke hatman int bashe
            except ValueError:
                print("Error: Enter numbers for card number!")
                count += 1
                continue
            if len(str(card_number)) != 16: # hatman 16 ragham bashe
                print("Error: Enter Valid Card Number!")
                count += 1
                continue

            return card_number
        self.confirm_card_number = False
        return card_number

    def get_cvv2(self):
        count = 0
        while count <= 1 and self.confirm_cvv2:   #user maximum 2 bar hagh eshtebah zadan card number ro dare
            try:
                cvv2 = int(input("Enter your cvv2 here: "))  # Validate cvv2 ke int bashe
            except ValueError:
                print("Error: Enter numbers for cvv2!")
                count += 1
                continue
            if (len(str(cvv2)) != 3) and (len(str(cvv2)) != 4): # ghabool kardan 3 ya 4 ragham
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
                date_obj = datetime.strptime(expire_date, "%Y-%m-%d") # age in variable sakhte shode, yani time be format dorost vared shode,
            except ValueError:                                        # dar gheyre in soorat vared except mishe
                print("Error: Enter in date format!")
                count += 1
                continue
            return expire_date
        self.confirm_expire_date = False
        return expire_date
    """
    harkodoom az card number, cvv2 va tarikh eshtebah bashe nevehste mishe dar file note
    va dar nahayat agar 3 tashoon True bood flagashoon, transaction successfule
    """
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


# sharayet gofte shode dar doc soal ra'ayat shode va chand chizam ezafe shode 
class Address:
    def __init__(self):
        self.state = self.get_state()
        self.city = self.get_city(self.state)
        self.overall_address = self.get_address()
        self.postal_code = self.get_postal_code()
        self.receiver = self.get_receiver()
        self.phone_number = self.get_phone_number()
        self.delivery_type = (self.get_delivery_type(self.state))[0] #list return mishe ke index 0 niaz boode
        self.delivery_price= (self.get_delivery_type(self.state))[1] #list return mishe ke index 1 niaz boode
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
                postal_code = int(input("Enter your postal-code here: "))  # Validate postal-code ke inet bashe
            except ValueError:
                print("Error: Enter numbers for postal-code!")
                continue
            if len(str(postal_code)) != 10: # 10 raghami bashe
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
            phone_number = input("Enter your phone number in 09######## here: ") # Validate phone number, faghat tedad argham validate shode, rooye int boodan dge pa feshari nashode chon chandin bar ghablan anjam shode va tekrari mishe 
            if len(str(phone_number)) != 11:                                     # rooye int boodan dge pa feshari nashode chon chandin bar ghablan anjam shode va tekrari mishe
                print("Error: Enter Valid phone number! phone number must be 10 digits")
                continue
            return phone_number
    def get_delivery_type(self, state): # hazine tehran 20 e va gheyr oon 30, chon ba post mire
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
            df = pd.read_csv("delivery_time.csv") # file csv khoonde mishe ke dadehaye tamami sefareshat hatam bad terminate kardan ro ham dashte bashim,
        except:                                   # va betoonim time haye sobh va zohr va asr ro tedadeshoon ro baraye tamami sefareshat dashte bashim
            create_csv("delivery_time", ["sobh", "zohr", "asr"])
            df = pd.read_csv("delivery_time.csv")
        zohr_capacity = df.iloc[:, 1:].sum()[0]
        asr_capacity = df.iloc[:, 1:].sum()[1]
        print("#.sobh")
        if zohr_capacity < 3:
            print("$.zohr")
        if asr_capacity < 3:
            print("*.asr")

        choice = input("Enter your choice here: ") # age timei entekhab beshe, 1 va baghi timeha 0 vared mishan va baraye inke bebinim khalie oon time ya na, sum gerefte mishe
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


class Accounting: # system hesabdari ke faghat sefareshaye movafagh ro tooye ye csv zakhire mikone
    def __init__(self, cart, tracking_code, delivery_price):
        self.count_items = cart.total_quantity() #tedad ajnas
        self.total_cost_products = cart.total_cost() # cast majmoo
        self.tax = self.total_cost_products * 0.09 # maliat
        self.tracking_code = tracking_code # code rahgiri
        self.delivery_price = delivery_price # mablagh post ya peyk
        
    def add_order(self, c_cart):
        c_cart.my_cart.clear() # khali shodan cart, chon tasvie shode
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
    def __init__(self, cart, delivery_time, tracking_code, delivery_type, cfirst_name ,clast_name, customer_address, delivery_price, tax): #saakht factor ba maghadiri ke attribute hastan
        self.item_name_list = list(cart.my_cart[i]["name"] for i in cart.my_cart) # esme item ha
        self.self_item_quantity = list(cart.my_cart[i]["quantity"] for i in cart.my_cart) # tedad har item
        self.self_item_price = list(cart.my_cart[i]["price"] for i in cart.my_cart) # gheymat vahed
        self.delivery_time = delivery_time
        self.tracking_code = tracking_code
        self.delivery_type = delivery_type #post ya peyk
        self.cfirst_name = cfirst_name
        self.clast_name = clast_name
        self.customer_address = customer_address
        self.delivery_price = delivery_price
        self.tax = tax
        
    def create_factor(self): # sakht file "Factor.txt"
        items = []
        for i in range(len(self.item_name_list)):
            item_name = self.item_name_list[i]
            item_price = self.self_item_price[i]
            item_quantity = self.self_item_quantity[i]
            items.append({"Item Name": item_name, "Price": item_price, "Quantity": item_quantity})
        total_cost = sum(item["Price"] * item["Quantity"] for item in items) + self.delivery_price + self.tax
        invoice = """
-----------------------------------------------------
                   SALES FACTOR
-----------------------------------------------------
Tracking Code: {}
Delivery Time: {}
Delivery Type: {}
Customer First Name: {}
Customer Last Name: {}
Customer Address: {}

|{:<20} |{:<10} |{:<10} |{:<10}
|---------------------|-----------|-----------|
{}
----------------------------------------------------
Tax: {}
Delivery Price: {}
Sum of Costs: {}
----------------------------------------------------
Thank you for your purchase!        
        """.format(self.tracking_code, self.delivery_time, self.delivery_type, self.cfirst_name, self.clast_name ,self.customer_address, "Item Name", "Price", "Quantity", "Cost",
                "\n".join([f"|{item['Item Name']:<20} |${item['Price']:>9.2f} |{item['Quantity']:>10} |${item['Price']*item['Quantity']:>9.2f}|" for item in items]), self.tax, self.delivery_price, total_cost)
        print("Purchase was successfull!")
        with open('Factor.txt', 'w') as f:
            f.write(invoice)




warehouse_main = Warehouse("P1","Iran") #sakhtan warehouse default
def admin_scenario():
    while True:
        print('---------Admin panel---------')
        print("1.Add item to inventory")
        print("2.remove item from inventory")
        print("3.Update price")
        print("4.Update warehouse quantity using csv file")
        print("5.Update warehouse quantity manually")
        print("6.Show inventory items")
        print("7.Get output of items in csv fromat")
        print("8.Exit")
        choice = int(input("Enter your choice here : "))
        if choice == 1:    
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

        elif choice == 2:   
            code = int(input("Enter the product code : "))
            quantity = int(input("Enter product quantity : "))
            print(warehouse_main.remove_item(code, quantity))
            
        elif choice == 3:       
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
            df = warehouse_main.products.set_index('code')
            print("Code\tName\t\tMaterial\tcolor     \tSize\tQuantity\tPrice")
            print("----------------------------------------------------------------------------------------")
            for index, row in df.iterrows():
                print(f"{index}\t{row['name']}\t\t {row['material']}\t\t {row['color']}     \t {row['size']}\t   {row['stock']}\t\t${row['price']}")
        elif choice == 7:
            warehouse_main.file_output()
            print("Your file has been created successfully")
        elif choice == 8:
            break

        else:
            print("Enter valid choice")
            
            

def customer_scenario(cus_fname, cus_lname, warehouse):
    cart = Cart(warehouse)
    while True:
        print('\n---------Customer panel---------')
        print("1.Show available products")
        print("2.Add product to my cart")
        print("3.Show my cart")
        print("4.Exit")# az in gozine mishavad pardakht kard va product ha ra az cart hazf konim
        choice = int(input("Enter your choice here : "))
        if choice == 1:
            df = warehouse.products.set_index('code')
            print("Code\tName\t\tMaterial\tcolor     \tSize\tQuantity\tPrice")
            print("----------------------------------------------------------------------------------------")
            for index, row in df.iterrows():
                if row["stock"] == 0: #  unavailable neshoon dadan quantity vaghti 0 e
                    print(f"{index}\t{row['name']}\t\t{row['material']}\t\t {row['color']}     \t {row['size']}\t   Unavailable\t\t${row['price']}")
                else:
                    print(f"{index}\t{row['name']}\t\t{row['material']}\t\t {row['color']}     \t {row['size']}\t   {row['stock']}\t\t${row['price']}")
                    
        elif choice == 2:
            code = int(input("Enter the product code : "))
            quantity = int(input("Enter product quantity : "))
            warehouse_main.remove_item(code, quantity)
            cart.add_to_cart(code, quantity)

        elif choice == 3:
            cart.show_my_cart()
            print("\n1.Remove item from the cart")
            print("2.Add product to my cart")
            print("3.Confirm purchases")
            choice = int(input("Enter your choice here: "))
            
            if choice == 1:
                code = int(input("Enter the product code: "))
                quantity = int(input("Enter product quantity you want that to be removed: "))
                if code in cart.my_cart:
                    product = Product(code, cart.my_cart[code]["name"], cart.my_cart[code]["price"], cart.my_cart[code]["color"],
                                    cart.my_cart[code]["size"], cart.my_cart[code]["material"])
                    cart.remove_from_cart(code, quantity)
                    warehouse_main.add_item(product ,quantity)
                else:
                    print("You dont have added this item code in your cart!")
                    
            elif choice == 2:
                code = int(input("Enter the product code: "))
                quantity = int(input("Enter product quantity: "))
                warehouse_main.remove_item(code, quantity)
                cart.add_to_cart(code, quantity)
                
            elif choice == 3:
                address = Address()
                pay = Pay(cus_fname, cus_lname)
        #dar in ghesmat age hamechi dorost vared shode bood, factor sakhte mishe va yek seri moshakhasat sefaresh dar csv be esme accounting zakhire mishe
                if pay.confirm_card_number == True and pay.confirm_cvv2 == True and pay.confirm_expire_date == True:
                    accounting = Accounting(cart, pay.tracking_code, address.delivery_price)
                    factor = Factor(cart, address.delivery_time, pay.tracking_code, address.delivery_type, cus_fname, cus_lname, address.overall_address, accounting.delivery_price, accounting.tax)
                    factor.create_factor()
                    accounting.add_order(cart)
                    
        elif choice == 4:
            if len(cart.my_cart) != 0:
                print("you have items in your cart!")
            else:
                break
            
                
# loop avalie ke bar asas entekhab user, def admin ya customer seda zade mishe
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