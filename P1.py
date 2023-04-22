from random import randint

class Inventory:

class Customer:

class Admin:

class Product: #kimia


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