import requests
import json

prompt = input("Enter a prompt: ")

try:
    url = "https://httpbin.org/post"

    payload = {
        "model": "gpt-4",
        "prompt": prompt,  # ← The variable from line 3
        "max_tokens": 100
    }

    response = requests.post(url, json=payload)  # ← POST not GET

    if response.status_code == 200:
        data = response.json()
        print(f"\nAPI received your data:")
        print(json.dumps(data['json'], indent=2))

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")