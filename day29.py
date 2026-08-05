# Build complete API aplication
import requests


def get_user():
    url="https://randomuser.me/api/"
    response=requests.get(url)
    response.raise_for_status()

    return response.json()["results"][0]

def get_advice():
    url="https://api.adviceslip.com/advice"
    response=requests.get(url)
    response.raise_for_status()
    return response.json()["slip"]["advice"]

def show_profile(user,advice):
    print("="*4,"USER Profile","="*4)
    print("Name :",user["name"]["first"])
    print("Gender :",user["gender"])
    print("age :",user["dob"]["age"])
    print("Country:",user["location"]["country"])

    print("="*4,"TODAYS ADVICE","="*4)
    print("Advice:",advice)


# MAin Program

try:
    user=get_user()
    advice=get_advice()
    show_profile(user,advice)
except requests.exceptions.RequestException as e:
    print("failed Request",e)
