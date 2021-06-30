# API from https://ipapi.co/
import requests
import os

ip = input("Enter the IP address: ")
key = os.environ.get('API_KEY')
data = requests.get(f"http://ipapi.co/{ip}/json/?key={key}")

data_dict = data.json()

for info in data_dict.items():
    print(info)