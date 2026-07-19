import os
import requests
from dotenv import load_dotenv


load_dotenv()


token = os.getenv("HF_TOKEN")


url = "https://huggingface.co/api/daily_papers"


headers = {
    "Authorization": f"Bearer {token}"
}


response = requests.get(
    url,
    headers=headers,
    params={
        "limit": 3,
        "sort": "trending"
    }
)


print("Status:", response.status_code)

print(response.json())