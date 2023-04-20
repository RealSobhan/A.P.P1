class Inventory:

class Customer:

class Admin:

class Product:

# ajnas dakhele cart tu ye dictionary rikhte mishan ke key haye dictionary esme jens va value haye dictionary tuple hastan
# tuple[0] = tedad , tuple[1] = gheymate oon tedad jens
class Cart:
    def __init__(self) :
        my_cart = {}
    
    def add_to_cart(self, item, number) : 
        my_cart[item] = (number, number * item.price)

    def remove_from_cart(self, item, number) : 
        first_number = my_cart[item][0]
        if number > first_number :
            print(f"you can't remove {number} number of this item from yourcart, there was only {first_number} number in it.")

        elif number == first_number :
            del my_cart[item]

        else : 
            remaining_nmber = first_number - number
            my_cart[item] = (remaining_nmber, remaining_nmber * item.price)
            print(f"you removed {number} number(s) of this item and now there is {remaining_nmber} number(s) remeining in your cart")

    def show_my_cart(self) :
        my_cart.items()

    def empty_my_cart(self) : 
        my_cart.clear()

    def total_cost(self) : 
        if len(my_cart) == 0 :
            return 0
        else :
            items_value = 0
            for i in my_cart.values() :
                items_value += i[1]

            return items_value
        
        

class Pay:
    def __init__(self, card_number, cvv2, expire_date, gmail= None):

class Address:
    def __init__(self, sharestan, shahr, baze_tahvil, addrees_koli, code_posti, pelak, vahed, phone_number, tahvil_girande):

class Factor:
    def __init__(self, gheymat, ajnas, address,tarikh_sabt_sefaresh ):