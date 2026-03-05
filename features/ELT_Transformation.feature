@ETL_Validation
Feature: SalesDataTransformation

@ETL_Validation @Data_Ingestion
  Scenario Outline: TestCase_1 "<file_name>" Data Ingestion
    Given the raw data extract "<file_name>" is ingested to the database
    Then the raw data from the file should be Ingestioned into table "<table_name>"

     Examples:
    | file_name |  table_name   |
    | orders    |    orders     |
    | products  |    products   |

@ETL_Validation @staging_validation
   Scenario Outline: TestCase_2 "<stg_models>" staging validation
   Given I Excute the data transformation for the "<stg_models>"
   Then a staging "<stg_models>" should be generated
   And the "<stg_models>"  transformation should as per the Expectations

     Examples:
    | stg_models   | 
    | stg_orders   |
    | stg_products |


@ETL_Validation @Datamart_validation
   Scenario Outline: TestCase_3 "<datamart>" Datamart validation
   Given I generate a Datamart for "<datamart>"
   Then a "<datamart>" should be generated
   And the "<datamart>" should as per the Expectations

     Examples:
    | datamart  |
    | sales_mart|
 