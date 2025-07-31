import csv
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    password="your_mysql_password",
    database="your_database_name"
)
cursor = conn.cursor()

# Open CSV file
with open('products.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("""
            INSERT INTO products (id, cost, category, name, brand, retail_price, department, sq, distribution, center_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['ID'], row['Cost'], row['Category'], row['Name'],
            row['Brand'], row['Retail Price'], row['Department'],
            row['SQ'], row['Distribution'], row['Center ID']
        ))

conn.commit()
cursor.close()
conn.close()
