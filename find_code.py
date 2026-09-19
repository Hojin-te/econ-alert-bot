import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ECOS_API_KEY")
print("불러온 키:", repr(api_key))

url = f"https://ecos.bok.or.kr/api/StatisticTableList/{api_key}/json/kr/1/3000/"
resp = requests.get(url)
data = resp.json()
print(data)  # 여기 추가 — 실제 응답을 먼저 확인

rows = data["StatisticTableList"]["row"]
matches = [r for r in rows if "대원화환율" in r["STAT_NAME"]]
for m in matches:
    print(m["STAT_CODE"], "-", m["STAT_NAME"])