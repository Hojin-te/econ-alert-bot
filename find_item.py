import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ECOS_API_KEY")

url = f"https://ecos.bok.or.kr/api/StatisticItemList/{api_key}/json/kr/1/100/731Y001"
resp = requests.get(url)
data = resp.json()

items = data["StatisticItemList"]["row"]
print(items[0])  # 여기 추가

for item in items:
    print(item["ITEM_CODE1"], "-", item["ITEM_NAME1"])