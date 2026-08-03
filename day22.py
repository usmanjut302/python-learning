# {
#     "slip":{
#         "id":102,
#         "advice":"dont compare your self to others."
#     }
# }
import requests
url="https://api.adviceslip.com/advice"
response=requests.get(url)
if response.status_code==200:
    data=response.json()

    print(data["slip"]["advice"])
else:
    print("error",response.status_code)    