import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")

db_config = {
    'user': db_user,
    'password': db_password,
    'host': db_host,
    'database': db_name
}

# Database connection: replace with your details
# engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Load data from CSV
df = pd.read_csv('/Users/hitesh/Downloads/test_budy/sqlangchain/NY_housing.csv')

# Insert data into the database
# data.to_sql('nyhousing', con=engine, if_exists='append', index=False)
i = 0
for index, row in df.iterrows():
    # Check if broker exists
    broker_title = row['BROKERTITLE']
    cursor.execute("SELECT broker_id FROM Broker WHERE broker_title = %s", (broker_title,))
    broker_row = cursor.fetchone()
    if broker_row:
        broker_id = broker_row[0]
    else:
        # Insert into Broker table
        cursor.execute("INSERT INTO Broker (broker_title) VALUES (%s)", (broker_title,))
        broker_id = cursor.lastrowid

    # Insert into PropertyType table (assuming you also want to check if type exists)
    type_name = row['TYPE']
    cursor.execute("SELECT type_id FROM PropertyType WHERE type_name = %s", (type_name,))
    type_row = cursor.fetchone()
    if type_row:
        type_id = type_row[0]
    else:
        cursor.execute("INSERT INTO PropertyType (type_name) VALUES (%s)", (type_name,))
        type_id = cursor.lastrowid

    # Insert into Address table
    address_data = (row['MAIN_ADDRESS'], row['ADMINISTRATIVE_AREA_LEVEL_2'], row['LOCALITY'], row['SUBLOCALITY'], row['STREET_NAME'], row['LONG_NAME'], row['FORMATTED_ADDRESS'], row['LATITUDE'], row['LONGITUDE'])
    cursor.execute("INSERT INTO Address (main_address, administrative_area_level_2, locality, sublocality, street_name, long_name, formatted_address, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", address_data)
    address_id = cursor.lastrowid

    # Insert into Property table
    property_data = (broker_id, type_id, row['PRICE'], row['BEDS'], row['BATH'], row['PROPERTYSQFT'], address_id)
    cursor.execute("INSERT INTO Property (broker_id, type_id, price, beds, bath, property_sqft, address_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", property_data)
    print("Finished row: ", i)
    i += 1

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()