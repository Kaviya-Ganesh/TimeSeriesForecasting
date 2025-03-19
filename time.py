import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")


def fetch_data(api_url, params):

    try:

        response = requests.get(
            api_url,
            params=params,
            headers={"Authorization": f"Bearer {API_KEY}"},  
            timeout=10  
        )
        response.raise_for_status()  
        return response.json()  
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Connection Error: Please check your API URL or internet connection.")
    except requests.exceptions.Timeout:
        print("Timeout Error: The API request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return None

# Example usage
if __name__ == "__main__":
    api_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=1min&apikey=demo"  # Replace with actual API URL
    params = {
        "symbol": "AAPL",        
        "interval": "1h",      
        "points": 100          
    }

    data = fetch_data(api_url, params)
    if data:
        print("Data retrieved successfully!")
        print(data)  
    else:
        print("Failed to retrieve data.")