# SECURE API REQUEST WITH ENV VARIABLES

import requests
from dotenv import load_dotenv
import os

load_dotenv()

print("="*60)
print("                   SECURE API REQUEST")
print("="*60)

# API KEY
api_key = os.getenv("API_KEY")

if api_key == None:
        print("\n-"*60)
        print("API KEY NOT FOUND")
        print("-"*60)
        exit()

else:
     print("\n-"*60)
     print("API KEY LOADED SUCCESSFULLY")
     print("-"*60)

#HEADERS

url = "https://api.github.com/user"

headers = {
    "Authorization" : "Bearer Token : {api_key}",
    "Accept" : "Application/Json"
}

try:
    response = requests.get(url,headers=headers,timeout=5)
    data = response.json()

    if response.status_code == 200:
        print(f"STATUS CODE : {response.status_code}")
        print(f"LOGIN : {data['login']}")
        print(f"NAME : {data['Name']}")
        print(f"FOLLOWERS : {data['Followers']}")
        print(f"PUBLIC REPOSITORY : {data['public_repos']}")


    elif response.status_code == 401:
        print(f"STATUS CODE : {response.status_code}")
        print("INVALID API KEY")


    else:
        print(f"STATUS CODE : {response.status_code}")
        print("REQUEST FAILED")


except Exception as e:
    print(f"ERROR OCCURS : {e}")


print("-"*60)
print("THANK YOU USING OUR PROGRAM")