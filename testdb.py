import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

connection = oracledb.connect(
    user="ADMIN",
    password=os.getenv("DB_PASSWORD"),
    dsn="econalertdb_low",
    config_dir=os.getenv("WALLET_DIR"),
    wallet_location=os.getenv("WALLET_DIR")
)

print("연결 성공!")
connection.close()