import os
import sys
import sqlite3
from src.core.config import db_filepath
from src.core.ge_runner import GERunner
from src.core.db_utilities import db_utilities
from src.core.soft_assertion import SoftAssert

def before_all(context):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)


    def before_scenario(context, scenario):
     context.soft_assert = SoftAssert()
     context.ge_runner = GERunner(
        context_root_dir="great_expectations",
        datasource_name="sqlite_db",
    )
     
     def before_feature(context, feature):
      print(f"Running feature: {feature.name}")

      os.makedirs(os.path.dirname(db_filepath), exist_ok=True)
      if os.path.exists(db_filepath):
            print(f"Database exists at location: {db_filepath}")
      else:
            sqlite3.connect(db_filepath)
            print(f"Database created at location: {db_filepath}")

    context.db = db_utilities(db_filepath)
    print("Database connection established")


    context.ge_runner = GERunner(
        context_root_dir="great_expectations",
        datasource_name="sqlite_db",
    )

    def after_feature(context, feature):
          if context.db:
           context.db.close()
           