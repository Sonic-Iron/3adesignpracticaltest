import sys, os, json
import requests

token_file = "digikeytokenfile.json"
auth_code = ""

#OAUTH requires that you get a authorisation code which can then be exchanged for an access token
#A refresh token can then be made which can be exchanged for another access token after the previous one expires
def generate_access_token(auth_code, token):
    auth_code = input("Go to localhost and enter the authcode from the url")
    with open(token_file, 'r') as file:
        token = json.load(file)

    url = 'https://sandbox-api.digikey.com/v1/oauth2/token'
    url_data = {
        'auth_code': auth_code,
        'client_id': token['client_id'],
        'client_secret': token['client_secret'],
        'redirect_url': 'https://localhost',
        'grant_type': 'authorization_code'
    }

    response = requests.post(url, data=url_data)
    #gets the access token and the time to expiration,
    #expires in 1800 seconds or 30 mins

    if response.status_code == 200: #successful request for access token
        data = response.json()
        token['access_token'] = data['access_token']
        token['access_token'] = data['access_token']
        token['refresh_token'] = data['refresh_token']
        token['expires_in'] = data['expires_in']
        token['refresh_token_expires_in'] = data['refresh_token_expires_in']
        token['token_type'] = data['token_type']
    with open(file, 'w') as new_file:
        json.dump(token, new_file)
    return response.json()

def get_refresh_token(token, ):
    url = 'https://sandbox-api.digikey.com/v1/oauth2/token'

    pass

def generate_refresh_token():
    pass

def get_new_access_token():
    pass
def main(arguments):
    with open(token_file, 'r') as file:
        token = json.load(file)
    generate_access_token(auth_code, token)
    pass

if __name__ == "__main__":
    main(sys.argv, auth_code, token_file)