# working with real API 
# random joke api
# import requests
# url="https://official-joke-api.appspot.com/random_joke"
# response=requests.get(url)
# data=response.json()
# print(data["setup"])
# print(data["punchline"])


# ------------------
# Error handling

# import requests
# url="https://official-joke-api.appspot.com/random_joke"
# response=requests.get(url)
# if response.status_code==200:

#     data=response.json()
#     print(data["setup"])
#     print(data["punchline"])
# else:
#     print("error",response.status_code)    




# Questions 

import requests
url="https://catfact.ninja/fact"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print(data["fact"])
    print(data["length"])
else:
    print("error",response.status_code)    