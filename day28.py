# Authentication Basics
# import requests
# API_KEY="your API key here"
# url=f"https://api.example.com/data?apikey{API_KEY}"
# response=requests.get(url)
# print(response.status_code)

# import os
# api_key=os.getenv("API_KEY")
# print(api_key)


# Practice 
# import os 
# api_key=os.getenv("API_KEY")
# print("API Key :",api_key)



import os
def get_api_key():
    key=os.getenv("API_KEY")

    if key is None:
        print("api key not found")
        return None
    
    return key

api_key=get_api_key()

if api_key:
    print("api key is loaded successfully")
