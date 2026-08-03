import requests
url="https://dummyjson.com/quotes/random"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print("Random Quote")
    print("Quotes:")
    print(data["quote"])
    print()
    print("Author:",data["author"])
    print()
    print("-"*25)
    print("thank you for choosing random generator")

else:
    print("error",response.status_code)