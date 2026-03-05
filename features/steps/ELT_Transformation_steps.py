from behave import *
from src.core.db_utilities import db_utilities
from src.core.ge_helper import GE_Helper
from src.core.config import db_filepath
from src.core.soft_assertion import SoftAssert
from src.core.dbt_runner import DBTRunner



@given('the raw data extract "{filename}" is ingested to the database')
def Ingest_the_raw_data(context, filename):
      
      context.filename = filename
      cmd = f"seed --select {filename}"
      DBTRunner.execute(cmd)
      
@given('I generate a Datamart for "{data_mart}"')
def Generate_a_Datamart(context,data_mart):
       
       cmd = f"run --select {data_mart}"
       DBTRunner.execute(cmd)

@given('I Excute the data transformation for the "{stg_model}"')
def Execute_data_transformation(context, stg_model):
     
     cmd = f"run --select {stg_model}"
     DBTRunner.execute(cmd)


@then(u'the raw data from the file should be Ingestioned into table "{table_name}"')
def Validate_seeded_Table_creation(context, table_name):
       
   context.db = db_utilities(str(db_filepath))
   soft_assert = SoftAssert()
   
   seeded_datacount  =  context.db .Get_Rowcount(table_name)
   soft_assert.check(seeded_datacount > 0, "Failed to igest orders raw data in to the database")
   print(f"Seeded Table: {context.filename} | Row count: {seeded_datacount}")

@then('a staging "{stg_model}" should be generated')
def Validate_stagging_table_creation(context, stg_model):
    
    soft_assert = SoftAssert()
    stg_rowcount =  context.db.Get_Rowcount(stg_model)
    soft_assert.check(stg_rowcount > 0, "Failed to insert data in to the stagging table")
    print(f"stg_table : {stg_model} | Row count: {stg_rowcount}")

@then(u'the "{stg_model}"  transformation should as per the Expectations')
def Perform_Expected_Vaidations(context, stg_model):

    GE_Helper.validate_expectations(context, stg_model)

@then('a "{data_mart}" should be generated')
def Validate_the_datamart(context,data_mart):

    soft_assert = SoftAssert()
    datamart_rowcount =  context.db.Get_Rowcount(data_mart)

    soft_assert.check(datamart_rowcount > 0, "Failed to insert data in to the stagging table")
    print(f"stg_table : {data_mart} | Row count: {datamart_rowcount}")

@then(u'the "{data_mart}" should as per the Expectations')
def validate_datamart_aganist_expectations(context, data_mart):
   GE_Helper.validate_expectations(context, data_mart)

