from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()
key = os.getenv('WEATHER_API_KEY')
location = "Silvassa"
from_date = "2024-10-07"
to_date = "2024-11-01"
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{from_date}/{to_date}?unitGroup=metric&key={key}&contentType=json"
data = requests.request("GET",url).json()
try:
    json_data = json.dumps(data)
    print(json_data)
except Exception as e:
    print("Error", e)
    