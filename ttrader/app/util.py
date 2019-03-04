import hashlib, uuid
import requests

salt = "MYSALT"  # generates a random uuid
encoded_salt = salt.encode() 

""" fake prices to lookup for unit testing purposes """
FAKE_PRICES = {
        'stok': 3.50
    }

def hash_password(password):
    """ WEEK 4 TODO: encrypt with sha512 & a salt """
    encoded_pw = password.encode()
    hashed_pw = hashlib.sha512(encoded_pw + encoded_salt).hexdigest()
    return hashed_pw


def get_price(ticker):
    # if ticker in FAKE_PRICES.keys():
    #     return FAKE_PRICES[ticker]
    
    try: 
        response = requests.get('https://api.iextrading.com/1.0/stock/{}/previous'.format(ticker))
        data = response.json()
        return [data['symbol'], data['open']]
    except ValueError:
        return False
        


    """ WEEK 4 TODO: get price from IEXTrading API """
    # return ord(ticker[0]) * 5.731

