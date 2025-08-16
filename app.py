import requests
import json
import os
from datetime import datetime

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Ensure the crypto_data directory exists
    os.makedirs("crypto_data", exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"crypto_data/crypto_data_{timestamp}.json"

    # Save to file
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Data saved to {filename}")

if __name__ == "__main__":
    fetch_crypto_data()