#  Employee Data Viewer

A Python project that connects to a remote SQL Server database and retrieves employee records securely.

##  Features

-  Secure database connection via `.env` file
-  Fetch top N employee records from the `Employees` table
-  Basic analytics: Average salary, count by department
-  Export results to CSV file
- Error handling and CLI argument support

##  Database Assumptions

- The database is hosted on a remote SQL Server.
- Database name: `CompanyDB`
- Table name: `Employees`
- Table contains fields like `EmployeeID`, `Name`, `Department`, `Salary`, etc.

## Requirements

- Python 3.x
- Packages:  
  `pyodbc`, `pandas`, `python-dotenv`

Install via:
```bash
pip install -r requirements.txt


