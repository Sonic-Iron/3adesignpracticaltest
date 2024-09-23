import json, requests
import time

token_file = "./digikeytokenfile.json"

def get_access_token(token_file):
    # access token takes 10 mins to expire
    with open(token_file, 'r') as file:
        tokens = json.load(file)
    url = "https://sandbox-api.digikey.com/v1/oauth2/token"
    url_data = {
        'client_id' : tokens['client_id'],
        'client_secret' : tokens['client_secret'],
        'grant_type' : 'client_credentials'
    }
    response = requests.post(url, url_data)
    data = response.json()
    if response.status_code == 200: # successful request, and returned access_token
        print("\nAccess token granted\n")
        tokens["access_token"] = data['access_token']
        tokens["expires_in"] = data["expires_in"]
        tokens["timegranted"] = time.time()
        tokens["timeexpired"] = data["expires_in"] + time.time()
        tokens["token_type"] = data['token_type']
    else: # not successful
        print("access token denied")

    with open(token_file, 'w') as file:
        json.dump(tokens, file)

    return (token_file, tokens["access_token"])

def main(token_file):
    digikeytokenfile, access_token = get_access_token(token_file)
    return access_token



if __name__=="__main__":
    main(token_file)