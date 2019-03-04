import requests
import json
import os
DIR = os.path.dirname(__file__)
FILENAME = ''
FILEPATH = os.path.join(DIR, FILENAME)
def get_stock():
    return input('Stock symbol: ')

def get_data(stock):
    response = requests.get('https://api.iextrading.com/1.0/stock/{}/chart'.format(stock))
    data = response.json()
    return data

def dump_data(data,FILENAME):
    with open(FILEPATH + FILENAME + '.json', 'w') as file_object:
        json.dump(data, file_object, indent=2)
    # #probably a security hazard but it works
    # with open('{}.json'.format(FILENAME), 'w') as file_object:

if __name__ == "__main__":
    stock = get_stock()
    data = get_data(stock)
    dump_data(data, stock)