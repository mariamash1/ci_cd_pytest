import pymssql
import pytest

MSSQL_HOST = '127.0.0.1'
MSSQL_PORT = 1433
MSSQL_USER = 'testUser'
MSSQL_PASSWORD = '123456!M654321'
MSSQL_DATABASE = 'TRN'

# Fixture for the database connection
@pytest.fixture(scope="function")
def db_connection():
    connection = pymssql.connect(host=MSSQL_HOST, user=MSSQL_USER, password=MSSQL_PASSWORD, database=MSSQL_DATABASE, port=MSSQL_PORT)
    try:
        yield connection
    finally:
        connection.close()


def test_row_count(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM hr.countries")
    result = cursor.fetchone()
    assert result.scalar() == 25, "Should return row count 25 for hr.countries table"


def test_null_values(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("with cte as (SELECT country_id, country_name, region_id "
                                           "FROM hr.countries WHERE country_id IS NULL or country_name IS NULL "
                                           "or region_id IS NULL) SELECT CASE WHEN count(*)=0 THEN 1 ELSE 0 "
                                           "END AS res FROM cte")
    result = cursor.fetchone()
    assert result.scalar() == 1, "Should return 1 for hr.countries table if there is no NULL values"


def test_duplicates(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("WITH cte AS (SELECT job_id, count(*) as cnt FROM hr.jobs GROUP BY job_id HAVING count(*)>1) SELECT CASE WHEN count(*)=0 THEN 1 ELSE 0 END AS res FROM cte")
    result = cursor.fetchone()
    assert result.scalar() == 1, "Should return 1 for hr.jobs table if there is no duplicates"


def test_min_max_salary_comparison(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("WITH cte AS (SELECT * FROM hr.jobs WHERE min_salary>max_salary) SELECT CASE WHEN count(*)=0 THEN 1 ELSE 0 END AS res FROM cte")
    result = cursor.fetchone()
    assert result.scalar() == 1, "Should return 1 for hr.jobs table if min salary is not more than maximal salary"


def test_email(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("with cte as (SELECT * FROM hr.employees WHERE email NOT LIKE '%__@__%.__%') SELECT CASE WHEN count(*)=0 THEN 1 ELSE 0 END AS res FROM cte")
    result = cursor.fetchone()
    assert result.scalar() == 1, "Should return 1 if email field follows specified format in hr.employees table"


def test_main_manager_salary(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("WITH cte AS (SELECT * FROM hr.employees WHERE manager_id is null and salary = (SELECT MAX(salary) FROM hr.employees)) SELECT CASE WHEN COUNT(*)=0 THEN 0 ELSE 1 END AS res FROM cte")
    result = cursor.fetchone()
    assert result.scalar() == 1, "Should return 1 if main manager has the biggest salary in hr.employees table"

