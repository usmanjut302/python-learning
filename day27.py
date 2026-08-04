# import requests
# user=requests.get("https://randomuser.me/api/").json()
# advice=requests.get("https://api.adviceslip.com/advice").json()
# person=user["results"][0]

# print("Name :",person["name"]["first"])
# print("Country:",person["location"]["country"])
# print("Advice:",advice["slip"]["advice"])



# Organized form of code

import requests
def get_user():
    response=requests.get("https://randomuser.me/api/")
    return response.json()["results"][0]
def get_advice():

    response=requests.get("https://api.adviceslip.com/advice")
    return response.json()["slip"]["advice"]

user=get_user()
advice=get_advice()


print("="*4,"USER Profile","="*4)
print("Name :",user["name"]["first"])
print("Gender :",user["gender"])
print("age :",user["dob"]["age"])
print("Country:",user["location"]["country"])

print("="*4,"TODAYS ADVICE","="*4)
print("Advice:",advice)