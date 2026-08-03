# API's and requests libraries
# application programming interface : lets 2 program communicate with each other 

# reuest library 
# used to send HTTP requests


# Sending a GET request 
# import requests
# response=requests.get("https://api.github.com")
# print(response.status_code)


# -------------------------------
# reading json data
{
    "name":"usman",
    "age":23,
    "country":"pakistan"
}
import requests
response=requests.get("https://api.github.com")
data=response.json()
print(data["current_user_url"])
# print(data["current_user"])
print(data["authorizations_url"])
print(data.keys())


