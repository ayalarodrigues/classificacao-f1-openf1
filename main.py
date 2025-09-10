import requests

url = "https://api.openf1.org/v1/standings?year="

response = requests.get(url + "2024")
print(response.json())