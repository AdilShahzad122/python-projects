import requests
import json

city=input("Enter the city name: ")

url=f"http://api.weatherapi.com/v1/current.json?key=be337f4f22dc44bc8c563829251804&q={city}"

r=requests.get(url)

#print(r.text)
#print(type(r.text))
wdic=json.loads(r.text)
print(wdic["current"]["temp_c"])
