#  1. Multiple API Fields
# 2 json parsing 
# 3 clean code
# 4 error handling

# import requests
# url="https://api.example.com/user"
# try:
#     response=requests.get(url)
#     response.raise_for_status()

#     data=response.json()
#     print("Name :",data["name"])

# except requests.exceptions.RequestException as e:
#     print("request failed",e)


    # Mini Project Random User API
    # ---------------------------------------------
import requests
url="https://randomuser.me/api/"
try:
    response=requests.get(url)
    response.raise_for_status()

    data=response.json()
    user=data["results"][0]
    print("Name :",user["name"]["first"],user["name"]["last"])
    print("Gender :",user["gender"])
    print("Age :",user["dob"]["age"])
    print("email :",user["email"])
    print("Phone :",user["phone"])
    print("City:",user["location"]["city"])
    print("Nationality :",user["location"]["country"])

except requests.exceptions.RequestException as e:
    print("request failed",e)

# print(user)