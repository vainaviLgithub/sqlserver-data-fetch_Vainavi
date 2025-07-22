import pyodbc
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# SQL Server connection details
server = '192.168.56.1,1433'
database = 'CompanyDB'
username = 'remote_user'
password = 'rootV'  # Replace this with your actual password
driver = '{ODBC Driver 17 for SQL Server}'  # Confirm your driver version

# Establish connection
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Departments List
departments = ['HR', 'Finance', 'IT', 'Marketing', 'Operations']

# Number of records to insert
num_records = 100

for _ in range(num_records):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    department = random.choice(departments)
    salary = round(random.uniform(30000, 120000), 2)

    # Insert query
    insert_query = """
    INSERT INTO dbo.Employees (FirstName, LastName, Email, Department, Salary)
    VALUES (?, ?, ?, ?, ?)
    """

    cursor.execute(insert_query, (first_name, last_name, email, department, salary))

# Commit and close
conn.commit()
cursor.close()
conn.close()

print(f"{num_records} fake employee records inserted successfully!")
