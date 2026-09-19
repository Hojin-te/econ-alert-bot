import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ECOS_API_KEY")

url = f"https://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/kr/1/10/731Y001/D/20250901/20250918/0000001"
resp = requests.get(url)
data = resp.json()

rows = data["StatisticSearch"]["row"]
for row in rows:
    print(row["TIME"], row["DATA_VALUE"], "원")