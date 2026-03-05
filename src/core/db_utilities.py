import sqlite3

class db_utilities:
 
   def __init__(self, db_filepath):
        self.db_filepath = str(db_filepath)
        self.conn = None

   def sql_connect(self):
     if self.conn is None:
        self.conn = sqlite3.connect(self.db_filepath)
        print("Database connection established")
     return self.conn
  
  
   def close_connection(self):
        if self.conn:
            self.conn.close()
  
  
   def Load_Data(self, table_name, conn, df):
        df.to_sql(table_name, conn, if_exists="append", index=False)
        print(f"{len(df)} rows inserted into stg_orders", flush=True)


   def Get_Rowcount(self, table_name):
       self.sql_connect()
       cursor = self.conn.cursor()
       cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
       count = cursor.fetchone()[0]
       cursor.close()
       print(f"Row count in stg_orders: {count}")
       return count


   def table_exists(self, table_name):
        self.sql_connect()
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (table_name,)
        )
        result = cursor.fetchone()
        cursor.close()

        return result is not None