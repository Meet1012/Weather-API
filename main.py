import requests
import json
from dotenv import load_dotenv
import os
import redis
import datetime
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(get_remote_address, app=app, default_limits=["10 per hour"])

host_id = os.getenv('REDIS_HOST')
password_id = os.getenv('REDIS_PASSWORD')
r = redis.Redis(
    host=host_id,
    port=12790,
    password=password_id)


@app.route("/<string:location>/<string:date>")
@limiter.limit("1 per minute")
def Display(location, date):
    today = datetime.datetime.now()
    to_date = today.strftime("%Y-%m-%d")
    load_dotenv()
    key = os.getenv('WEATHER_API_KEY')
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{
        location}/{date}/{to_date}?unitGroup=metric&include=days&key={key}&contentType=json"
    data = requests.request("GET", url)
    if data.status_code == 200:
        json_data = json.dumps(data.json())
        r.setex(location, 43200, json_data)
        return json.loads(r.get(location))
    elif data.status_code == 429:
        return {"Error": "Too Many Requests"}
    elif data.status_code in [503, 500]:
        return {"Error": "Server Error"}


if __name__ == "__main__":
    app.run(port=5000, debug=True)
