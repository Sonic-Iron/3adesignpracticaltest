import json, requests
import time

token_file = "./digikeytokenfile.json"

def get_access_token(token_file):
    # access token takes 10 mins to expire
    with open(token_file, 'r') as file:
        tokens = json.load(file)
    url = "https://sandbox-api.digikey.com/v1/oauth2/token"
    url_data = {
        'client_id': tokens['client_id'],
        'client_secret': tokens['client_secret'],
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, data=url_data)
    data = response.json()
    if response.status_code == 200: # successful request, and returned access_token
        print("\nAccess token granted\n")
        access_token = data['access_token']
        access_token_type = data['token_type']
    else: # not successful
        print("access token denied")

    return access_token, access_token_type

def main(token_file):
    digikeytokenfile, access_token = get_access_token(token_file)
    return access_token



if __name__=="__main__":
    main(token_file)