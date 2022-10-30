import requests
import time

url = "http://127.0.0.1:5000/plantwatering"

# response should be "plant does not need watering"
params = {'plant': 'fern', 'days': 1}
response = requests.get(url, params=params)

print(params, response.text)

time.sleep(2)

# response should be "plant needs watering"
params2 = {'plant': 'fern', 'days': 3}
response2 = requests.get(url, params=params2)

print(params2, response2.text)

time.sleep(2)

# response should be "plant is not in the database"
params3 = {'plant': 'cactus', 'days': 3}
response3 = requests.get(url, params=params3)

print(params3, response3.text)