from random import randint
import re
from datetime import datetime
"""class Inventory:

class Customer:

class Admin:

class Product:


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
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def validate_email(email):
    return bool(re.match(r"^[a-zA-Z0-9\.\_]+@((gmail)|(yahoo)|(outlook)|(hotmail)|(live)|([a-z]*\.*[a-z]+\.ac)|(chmail))\.((com)|(ir))$", email, re.IGNORECASE))
class Pay:
    def __init__(self, gmail = None):
        self.card_number = self.get_card_number()
        self.cvv2 = self.get_cvv2()
        self.expire_date = self.get_expire_date()
        #self.gmail = gmail
        #self.tracking_code = random_number_with_n_digits(10) #code peygiri az taraf banke 10 raghami
        #self.order_date = None
        #self.confirm = False
        #self.total_price = total_price


    def get_card_number(self):
        while True:
            try:
                card_number = int(input("Enter your card number here: ")) #Validate card number
            except ValueError:
                print("Error: Enter numbers for card number!")
                continue
            if len(str(card_number)) != 16:
                print("Error: Enter Valid Card Number!")
                continue
            return card_number

    def get_cvv2(self):
        while True:
            try:
                cvv2 = int(input("Enter your cvv2 here: ")) #Validate cvv2
            except ValueError:
                print("Error: Enter numbers for cvv2!")
                continue
            if (len(str(cvv2)) != 3) and (len(str(cvv2)) != 4):
                print("Error: Enter Valid cvv2!")
                continue
            return cvv2

    def get_expire_date(self):
        while True:
            expire_date = input("Enter your cards expire date in (YYYY-MM-DD) format: ")
            try:
                date_obj = datetime.strptime(expire_date, "%Y-%m-%d")
            except ValueError:
                print("Error: Enter in date format!")
                continue
            return expire_date
pay = Pay()
print(pay.expire_date)
print(pay.card_number)
print(pay.cvv2)

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
