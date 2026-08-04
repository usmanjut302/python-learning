# code without function
# import requests
# url="https://randomuser.me/api/"
#     response=requests.get(url)
#     response.raise_for_status()

#     data=response.json()
#     user=data["results"][0]


# with function

# import requests
# def get_user():
#     url="https://randomuser.me/api/"
#     response=requests.get(url)
#     response.raise_for_status()

#     return response.json()

# user=get_user()
# person=user["results"][0]
# print("name :",person["name"])



# Mini Projects

import requests
def get_user():
    url="https://randomuser.me/api/"
    response=requests.get(url)
    response.raise_for_status()
    data=response.json()

    return data["results"][0]

def show_user():
    print("Name :",user["name"]["first"],user["name"]["last"])
    print("Gender :",user["gender"])
    print("Age :",user["dob"]["age"])
    print("email :",user["email"])
    print("Phone :",user["phone"])
    print("City:",user["location"]["city"])
    print("Nationality :",user["location"]["country"])


user=get_user()
show_user()