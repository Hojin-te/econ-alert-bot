import oracledb
import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
from db import get_connection

load_dotenv()
api_key = os.getenv("ECOS_API_KEY")

end_date = datetime.today().strftime("%Y%m%d")
start_date = (datetime.today() - timedelta(days=14)).strftime("%Y%m%d")

url = f"https://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/kr/1/10/731Y001/D/{start_date}/{end_date}/0000001"
resp = requests.get(url)
data = resp.json()

rows = data["StatisticSearch"]["row"]

conn = get_connection()
cursor = conn.cursor()

for row in rows:
    try:
        cursor.execute(
            "INSERT INTO rates (rate_date, currency, value) VALUES (:1, :2, :3)",
            [row["TIME"], "USD", row["DATA_VALUE"]]
        )
        print(row["TIME"], row["DATA_VALUE"], "원 - 저장됨")
    except oracledb.IntegrityError:
        print(row["TIME"], "- 이미 존재함, 건너뜀")

conn.commit()
conn.close()