# 🌤️ Weather API with Redis Caching and Rate Limiting

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![Redis](https://img.shields.io/badge/Redis-Server-red)](https://redis.io/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)](https://flask.palletsprojects.com/)
[![Requests](https://img.shields.io/badge/Requests-2.25%2B-orange)](https://docs.python-requests.org/)
[![Dotenv](https://img.shields.io/badge/Python--Dotenv-0.19%2B-yellow)](https://pypi.org/project/python-dotenv/)
[![Flask-Limiter](https://img.shields.io/badge/Flask--Limiter-1.4%2B-lightgrey)](https://flask-limiter.readthedocs.io/)

This is a Flask application that fetches historical weather data for a specified location and date from the Visual Crossing Weather API, caches it in Redis for 12 hours, and returns the data in JSON format. The application includes rate limiting to control request frequency.

[Project Link](https://roadmap.sh/projects/weather-api-wrapper-service)

## 🛠️ Requirements
- Python 3.6+
- Redis server
- Flask
- Requests
- Python Dotenv
- Flask-Limiter

## 🛠️ Setup

1. **Clone the repository** (if applicable) or download the script file.

2. **Install the required packages**:
    ```bash
    pip install flask requests python-dotenv redis flask-limiter
    ```

3. **Set up Redis**:
    - Ensure you have a running Redis instance or configure access to a Redis server.
    - Set the Redis connection details (host and password) in a `.env` file.

4. **Set up the Weather API**:
    - Obtain an API key from [Visual Crossing Weather](https://www.visualcrossing.com/) and add it to the `.env` file.

## ⚙️ Configuration

Create a `.env` file in the root directory with the following variables:

```
REDIS_HOST=your_redis_host
REDIS_PASSWORD=your_redis_password
WEATHER_API_KEY=your_weather_api_key
```

Replace `your_redis_host`, `your_redis_password`, and `your_weather_api_key` with the actual values for your Redis instance and Visual Crossing Weather API key. This ensures the application can connect to Redis and access the weather API.

## 🚀 Usage

To start the Flask application, run:

```bash
python main.py
```

The application will start on `http://127.0.0.1:5000` by default.

### 🌍 API Endpoint

**GET** `http://127.0.0.1:5000/<location>/<date>`

- **location**: The name of the city or location (e.g., `{Location}`)
- **date**: The date for which to retrieve weather data, in `YYYY-MM-DD` format.

**Example Request** 💻

```bash
curl http://127.0.0.1:5000/{Location}/{From_Date}
```

### 📥 Response

The endpoint will return the weather data in JSON format. Here’s what you can expect in the response:

- **Successful Response (200)**: Returns the weather data for the specified location and date. This data is cached in Redis for 12 hours (43200 seconds) to improve performance for subsequent requests to the same location.
- **Rate Limit Exceeded (429)**: If the rate limit is exceeded, a `429 Too Many Requests` error is returned with an error message: 
    ```
    {
      "Error": "Too Many Requests"
    }
    ```
- **Server Error (500 or 503)**: If the weather API is unavailable or encounters an error, the response will include an error message:
    ```
    {
      "Error": "Server Error"
    }
    ```

## 📝 Code Explanation

- **Dependencies**: 
  - `requests`: Used to fetch data from the weather API.
  - `redis`: Handles data caching in Redis for faster retrieval.
  - `dotenv`: Loads environment variables from the `.env` file.
  - `flask_limiter`: Enforces rate limiting for API endpoints to prevent abuse.

- **Redis Caching**: 
  - The application caches the fetched weather data in Redis with a 12-hour expiration (`setex` with 43200 seconds). This helps reduce repeated calls to the weather API for frequently requested data.

- **Rate Limiting**:
  - Implemented using Flask-Limiter. The `/location/date` endpoint is limited to 1 request per minute, with a global limit of 10 requests per hour.

## 🔑 Environment Variables

- `REDIS_HOST`: Host address for the Redis server.
- `REDIS_PASSWORD`: Password for the Redis server (if required).
- `WEATHER_API_KEY`: API key for accessing the Visual Crossing Weather API.


