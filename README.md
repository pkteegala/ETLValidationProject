# ETLValidationProject
This project is designed for data validation during the ETL process.

----------------------------------------------------------------------------------------------------------------------------------
## Overview
This project is designed for data validation during the ETL process

1. Data ingestion from raw files into the database
2. Staging transformations created by dbt models
3. Data mart aggregations
4. Data quality rules using Great Expectations

The validations are executed as BDD scenarios, providing clear and readable test cases.

 ---------------------------------------------------------------------------------------------------------------------------------

# Tools Used

dbt                      ->   Data transformation and modeling       ->    **dbt 1.5.1**
SQLLite                  ->   Database                               ->    **sqllite 3.45.1**
Great Expectations       ->   Data quality validation                ->    **ge 1.13.0**
Behave                   ->   BDD test automation framework          ->    **Behave 1.3.3**
Cucumber Formatter       ->   Reporting
Node.js Cucumber Report  ->   HTML test reporting       
Python                   ->   Test orchestration and utilities       ->    **Python 3.11.9**

----------------------------------------------------------------------------------------------------------------------------------
# Project Structure

ETLValidationProject
│
├── dbt_project
│   ├── models
│   │   ├── staging
│   │   └── marts
│   ├── seeds
│   |── dbt_project.yml
|   |── profiles.yml
│
├── features
│   ├── ELT_Transformation.feature
│   ├── steps
│   │   └── ELT_Transformation_steps.py
│   └── environment.py
│
├── src
│   └── core
│       ├── dbt_runner.py
│       ├── ge_runner.py
│       ├── db_utilities.py
│       └── helper
│           └── ge_actions.py
│
├── great_expectations
│
├── sqlite_db
│   └── RetailSalesDatamart.db
│
├── reports
│   ├── cucumber.json
│   └── cucumber_report.html
│
├── generate_cucumber_report.js
└── README.md

----------------------------------------------------------------------------------------------------------------------------------

  # Data Flow

   DataFiles
     ↓
   dbt Seeds
     ↓
   Data Mart
     ↓
   Great Expectations Validation
     ↓
   BDD Test Execution
     ↓
   Cucumber HTML Report

----------------------------------------------------------------------------------------------------------------------------------

   # Data Validation Scenarios

   The Test scenarios are designed and written using simple terms explaing process and also aligned and executed in sequence of the ETL Process
    
    # Data Ingestion
    Scenario Outline: TestCase_1 "<file_name>" Data Ingestion
    Given the raw data extract "<file_name>" is ingested to the database
    Then the raw data from the file should be Ingestioned into table "<table_name>"

     Examples:
    | file_name |  table_name   |
    | orders    |    orders     |
    | products  |    products   |


   # Staging Validation
   Scenario Outline: TestCase_2 "<stg_models>" staging validation
   Given I Excute the data transformation for the "<stg_models>"
   Then a staging "<stg_models>" should be generated
   And the "<stg_models>"  transformation should as per the Expectations

     Examples:
    | stg_models   | 
    | stg_orders   |
    | stg_products |


   # Datamart validation
   Scenario Outline: TestCase_3 "<datamart>" Datamart validation
   Given I generate a Datamart for "<datamart>"
   Then a "<datamart>" should be generated
   And the "<datamart>" should as per the Expectations

     Examples:
    | datamart  |
    | sales_mart|

----------------------------------------------------------------------------------------------------------------------------------

  
   # Data Quality Validations
    Column existence
    Null checks
    Data type validation
    Valid order status
    Order Total calculation

----------------------------------------------------------------------------------------------------------------------------------

   # Dependences

   python 
   behave
   great_expectations
   dbt-core
   dbt-sqlite
   behave-cucumber-formatter

----------------------------------------------------------------------------------------------------------------------------------

   # Execute Test Cmds
   # From the root folder execute below command
   behave -t "@ETL_Validation"  --no-capture

   ===============================================================================================================
   As the data is already and if you want to execute and validate the GE Tests, comment the below function in Steps
   DBTRunner.execute(cmd)
  =================================================================================================================
   If you want to execute and validate from start, please drop all the tables and run the command
   behave -t "@ETL_Validation"  --no-capture
  ==================================================================================================================
   Database check is setup in before feature hooks, to ensure the database exist before test executions
  ===================================================================================================================


----------------------------------------------------------------------------------------------------------------------------------

   # Generate Reporting

   From the root folder execute the below commands in squence
   # Run tests and generate JSON output
   behave -t "@ETL_Validation" -f behave_cucumber_formatter:PrettyCucumberJSONFormatter -o reports/cucumber.json --no-capture

   # Generate the HTML report:
   node .\generate_cucumber_report.js

   # Open the report:
   start .\reports\cucumber_report.html





==========================================================================================================================================
# Set up
==========================================================================================================================================Clone the repository and install dependencies.
Steps

1. clone project from the Url    : git clone https://github.com/username/etl-dbt-ge-pipeline.git
2. Navigate to the folder        : cd etl-dbt-ge-pipeline
3. Create a Virtual Environment  : python -m venv venv 
4. Activate the Environment      : venv\Scripts\activate
5. Install Dependencies          :  python 
                                    behave
                                    great_expectations
                                    dbt-core
                                    dbt-sqlite
                                    behave-cucumber-formatter