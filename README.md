# SQL Server Data Connectivity Project

> **Intern:** Vainavi Lad
> **Internship Role:** Data Engineer Intern at Celebal Tech
> **Intern ID:** CT\_CSI\_DE\_6312

---

##  Overview

This project demonstrates how to establish a secure connection between Python and a remote SQL Server database, fetch data from a specific table, and perform data analysis and export operations. It serves as a proof of concept for real-world data engineering tasks involving external database connectivity, query optimization, error handling, and scripting automation.

##  Tools & Libraries Used

* Python 3.x
* SQL Server
* `pyodbc`
* `pandas`
* `python-dotenv`
* `faker` (for generating synthetic employee data)
* Git & GitHub (version control)

##  Features Implemented

* Secure SQL Server connection using environment variables.
* Query to fetch top N records from the `Employees` table.
* Error handling for robust connection and query execution.
* Export functionality to save query results as CSV.
* Descriptive analytics (average salary, employee count by department).
* Data generation script using `Faker` to insert 350 synthetic employee records.

##  Folder Structure

```bash
sql-data-project/
├── scripts/
│   ├── generate_employee_data.py     # Script to populate Employees table using Faker
│   ├── fetch_employees.py            # Script to connect and query SQL Server
│   └── main.py                       # Optional driver script
├── .env                              # Contains sensitive credentials (not pushed)
├── .env.example                      # Template for .env setup
├── employees.csv                     # Optional output from fetch
├── outputs/                          # Screenshots, sample outputs
├── requirements.txt                  # Python dependencies
└── README.md                         # Project summary and documentation
```


##  How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Fetch top 5 employees
python scripts/fetch_employees.py --limit 5

# Export data
python scripts/fetch_employees.py --limit 10 --export
```

## Sample Outputs

* Top employee records printed in terminal
* Aggregated stats by department
* CSV output saved to `employees.csv`

## Data Generation

Used the `Faker` library to insert \~350 employee records into the `Employees` table.
Each record contains realistic values for:

* EmployeeID
* Name
* Email
* Department
* Salary
* HireDate

This ensures:

* Query logic scales well
* Error handling works on large datasets
* Realistic testing scenarios

## Challenges Faced
* Handling `pyodbc` connection errors robustly
* Formatting and parsing dates using Faker
* Testing connectivity across remote IP
* Maintaining modularity and code reusability

## Deliverables

* `generate_employee_data.py`: inserts \~350 records into `Employees`
* `fetch_employees.py`: connects to DB and prints/analyzes/export data
* `.env.example`: helps securely set environment variables
* `README.md`: full documentation
* `requirements.txt`: installation dependencies
* `outputs/`: contains screenshots and sample output CSVs

## Recommended GitHub Tags

`Python` `SQL Server` `Data Engineering` `Intern Project` `pyodbc` `Faker` `ETL` `Pandas` `Database Connectivity`

---

*This project showcases core backend data engineering skills—connecting to live SQL systems, querying efficiently, handling errors gracefully, generating realistic test data, and documenting for production.*

