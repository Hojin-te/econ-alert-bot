import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return oracledb.connect(
        user="ADMIN",
        password=os.getenv("DB_PASSWORD"),
        dsn="econalertdb_low",
        config_dir=os.getenv("WALLET_DIR"),
        wallet_location=os.getenv("WALLET_DIR"),
        wallet_password=os.getenv("WALLET_PASSWORD")
    )

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE rates (
                id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                rate_date VARCHAR2(8) NOT NULL,
                currency VARCHAR2(20) NOT NULL,
                value NUMBER NOT NULL,
                CONSTRAINT uq_date_currency UNIQUE (rate_date, currency)
            )
        """)
        print("테이블 생성 완료")
    except oracledb.DatabaseError as e:
        error_obj, = e.args
        if error_obj.code == 955:  # ORA-00955: 이미 존재하는 이름
            print("테이블이 이미 존재합니다")
        else:
            raise
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()