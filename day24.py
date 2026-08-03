# age prediction api

# import requests
# name=input("enter the name :")
# url=f"https://api.agify.io/?name={name}"
# response=requests.get(url)
# if response.status_code==200:
#     data=response.json()
#     print()
#     print("Name:",data["name"])
#     print("Predicted age :",data["age"])
# else:
#     print("error",response.status_code)    





# handling missing data

import requests
name=input("enter the name :")
url=f"https://api.agify.io/?name={name}"
response=requests.get(url)
if response.status_code==200:
    data=response.json()

    if data["age"] is None:
        print("sorry no age is predicted")
    else:

        print()
        print("Name:",data["name"])
        print("Predicted age :",data["age"])
else:
    print("error",response.status_code)    