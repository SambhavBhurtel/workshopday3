import requests

# ENTER THE PREDICTION URL
url = ""

# ENTER THE PREDICTION KEY
prediction_key = ""

# ENTER THE TEST IMAGE URL
img_url = ""

headers = {"Content-type":"application/json","Prediction-key":prediction_key}
params = {}
data = {"Url":img_url}

response_json = requests.post(url, params=params, headers=headers, json=data).json()

print(response_json)