import sqlite3 
import pandas as pd

conn = sqlite3.connect('database.sqlite')
print("Opened database successfully")

# conn.execute("""CREATE TABLE CLASS_10 
# (SNO INT PRIMARY KEY NOT NULL,
# Roll_No INT NOT NULL,
# Name TEXT NOT NULL,
# Age INT DEFAULT 15,
# Gender TEXT NOT NULL,
# Email_ID TEXT NOT NULL,
# Contact_No REAL NOT NULL);""")
# print("Table created successfully")

# conn.execute("""INSERT INTO CLASS_10 (SNO, Roll_No, Name, Age, Gender, Email_ID, Contact_No)
#                  VALUES (1, 101, 'Alice Smith', 16, 'Female', 'alice.smith@example.com', 9876543210);""")
# conn.execute("""INSERT INTO CLASS_10 (SNO, Roll_No, Name, Age, Gender, Email_ID, Contact_No)
#                     VALUES (2, 102, 'Bob Johnson', 15, 'Male', 'bob.johnson@example.com', 9872583211);""")
# conn.execute("""INSERT INTO CLASS_10 (SNO, Roll_No, Name, Age, Gender, Email_ID, Contact_No)
#                     VALUES (3, 103, 'Charlie Brown', 17, 'Male', 'charlie.brown@example.com', 9181433567);""")

# conn.commit()

# print("Records inserted successfully")


table = pd.read_sql_query("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
print(table)

class_10_df = pd.read_sql_query("SELECT * FROM CLASS_10;", conn)
print(class_10_df.head())

