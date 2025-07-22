# fetch_employees.py

import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv
import argparse

load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
driver = 'ODBC Driver 17 for SQL Server'


parser = argparse.ArgumentParser()
parser.add_argument('--limit', type=int, default=5, help="Number of employees to fetch")
parser.add_argument('--export', action='store_true', help="Export results to CSV")
args = parser.parse_args()

def fetch_employees(limit):
    try:
        conn_str = (
            f'DRIVER={{{driver}}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password}'
        )
        conn = pyodbc.connect(conn_str)
        print(" Connected to SQL Server.")

        query = f"SELECT TOP {limit} * FROM Employees"
        df = pd.read_sql(query, conn)

        print("\n Top", limit, "Employee Records:\n")
        print(df)

        # Analytics
        print("\n Average salary by department:")
        print(df.groupby("Department")["Salary"].mean())

        print("\n Count of employees by department:")
        print(df["Department"].value_counts())

        # Export
        if args.export:
            df.to_csv("employees.csv", index=False)
            print("\n Exported to employees.csv")

    except pyodbc.Error as db_err:
        print(" DB Error:", db_err)
    except Exception as e:
        print(" Error:", e)
    finally:
        if 'conn' in locals():
            conn.close()
            print(" Connection closed.")

if __name__ == "__main__":
    fetch_employees(args.limit)
