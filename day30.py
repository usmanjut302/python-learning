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
    print("="*40 )
    print("RANDOM USER DASHBOARD")
    print("="*40)

    print("Name :",user["name"]["first"])
    print("Age :",user["dob"]["age"])
    print("Gender :",user["gender"])
    print("Email :",user["email"])
    print("Phone :",user["phone"])
    print("City :",user["location"]["city"])
    print("Country :",user["location"]["state"])
    print("Nationality :",user["location"]["country"])
    print("Date and Time :",user["location"]["timezone"])
          

    print("Todays Advice")
    print(advice)

try:
    while True:
        user=get_user()
        advice=get_advice()

        show_profile(user,advice)
        while True:
            choice=input("another prifile ? (y/n):")
            if choice=="y":
                break
            elif choice=="n":
                running=False
                break
            else:
                print("enter only y or n ")
        

except requests.exceptions.RequestException as e :
    print("request failed",e)
    

