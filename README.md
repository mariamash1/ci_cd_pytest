# SQL Data Validation Testing Project (pytests)

This project is designed to perform data validation testing on an SQL Server database using the Pytest. The test cases cover a range of data integrity checks including row counts, null value checks, duplication checks, and specific data validation rules related to salaries and email formats.

## Pre-requisites

- Python 3.x
- Pytest
- SQL Server (Test database access)



## Configuration

This project's pytest test suite is configured to connect  to an SQL Server database using a connection string defined within the test suite file itself. The connection details are specified in  the `test11.py` file.

### Modifying Database Connection Details

To adjust the database connection details to match your environment, you will need to modify the conn_string within the `tests11.py` file. 

Replace the Server, Database, UID, and PWD values with your actual database server name/address, database name, user ID, and password, respectively.

Steps to Modify the Connection String:
Open the tests11.py file in your preferred text editor.
Find the conn_str.
Modify the connection string's Server, Database, UID, and PWD parameters to reflect your SQL Server's details.
Save your changes with your SQL Server connection details.

## Test Cases

The project includes the following test cases:

1. **Row Counts** - Validates the expected row counts in target tables.
2. **Null Value Check** - Ensures there are no null values in critical fields.
3. **Duplicate Check** - Checks for any duplicate records based on key fields.
4. **Salary Range Validation** - Compares the min and max salaries to ensure data integrity.
5. **Email Format Validation** - Validates that emails follow the standard format.
6. **Main Manager Salary Check** - Ensures the main manager has the maximum salary among employees.

## Merging strategy

Project adopts a streamlined branch management approach, utilizing two primary branches: dev and main. This strategy is particularly efficient for smaller development teams and offers several benefits.

Rationale Behind the Two-Branch Strategy:

Distinct Development and Production Environments: The dev branch serves as the space for continuous development activities, whereas the main branch holds the code considered stable and ready for production deployment.

Streamlined Merging Process: The focus on interactions primarily between the dev and main branches minimizes the complexity and potential conflicts seen with strategies involving multiple branches.

User-Friendly Approach: Its simplicity makes the strategy accessible and manageable, facilitating a smoother adoption by all team members.

Enhanced Team Workflow and Collaboration: This setup allows developers to concurrently work on features within the dev branch. Successful modifications are then moved to the main branch, undergoing standardized processes like code reviews and testing to assure code quality.

Scalable for Future Needs: While starting with a two-branch framework, there is room to incorporate additional branches, such as a QA branch for quality checks or branches dedicated to specific features, should the project's scope expand.