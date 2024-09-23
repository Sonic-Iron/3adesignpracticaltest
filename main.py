
import sys, json

import requests

import threeleggedaccesstoken
import twoleggedaccesstoken
from twoleggedaccesstoken import get_access_token
from threeleggedaccesstoken import generate_access_token, generate_refresh_token, get_new_access_token

TOKEN_FILE = "digikeytokenfile.json"
MODE = 2
CURRENCY = "GBP"

def check_inputs(params):
    if len(params) != 2:
        print(params)
        print("A BOM and order quantity must be provided")
        return False
    try: #file can be opened
        with open(params[0]) as file:
            pass
    except:
        pass
    #assuming that the user will always enter a file which can be interpreted as a .csv file
    if str(params[1]).isdigit:
        if int(params[1]) <= 0:
            print("There must be one or more orders of the BOM")
            return False
    else:
        print("The quantity of BOM ordered must be a number")
        return False
    return True
def create_quote(tokens, currency):
    url = "sandbox-api.digikey.com/quoting/v4/quotes"
    url_data = {
        "Authorization" : tokens["access_token"],
        "X-DIGIKEY-Client-Id ": tokens["client_id"],
        "X-DIGIKEY-Locale-Currency" : currency,
        "X-DIGIKEY-Customer-Id" : tokens["customer_id"]
    }
    response = requests.post(url, url_data)
    data = response.json()
    print(data)
    if response == 200:
        print("Created new quote")
        return data['quoteID']
    else:
        print(f"Failed with error : {response.reason}")

def add_to_quote(quoteID, productID, tokens):
    url = f"sandbox-api.digikey.com/quoting/v4/quotes/{quoteID}/details"
    pass

def main(params, token_file, mode, currency):
    if not check_inputs(params):
        print("Please enter both a BOM and quantity of products to be quoted")
        return
    path = params[0]
    path = "Bill Of Materials PowerPortMax-v5.csv" #TODO : get rid of this line for final build
    quantities = params[1]
    match mode:
        case 2:
            twoleggedaccesstoken.get_access_token(token_file)
        case 3:
            threeleggedaccesstoken.generate_access_token(token_file)
        case _:
            print("A valid OAUTH legged mode is not given")
    with open(path, 'r') as bom:
        try:
            product_code_column = bom.readline().split(',').index("Stock Code")
        except ValueError as e:
            raise ValueError("The BOM file doesn't contain a stock code column") from e
            return
    with open(token_file, 'r') as file:
        tokens = json.load(file)
    #quoteID = create_quote(tokens, CURRENCY)
    with open(path, 'r') as bom:
        for row in bom.readlines()[1:]:
            print(row.split(',')[product_code_column])


if __name__ == "__main__":
    main(sys.argv[1:], TOKEN_FILE, MODE, CURRENCY)