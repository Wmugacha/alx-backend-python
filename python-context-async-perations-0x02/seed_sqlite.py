import sqlite3
from faker import Faker
import random

fake = Faker()

def recreate_database_and_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Drop the table if it already exists
    cursor.execute("DROP TABLE IF EXISTS users")

    # Create the new table with an 'age' column
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            city TEXT,
            phone TEXT,
            age INTEGER
        )
    """)

    conn.commit()
    conn.close()
    print("📦 users table recreated successfully.")

def seed_data(db_name, num_records):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for _ in range(num_records):
        name = fake.name()
        email = fake.unique.email()
        city = fake.city()
        phone = fake.phone_number()
        age = random.randint(18, 70)

        cursor.execute("""
            INSERT INTO users (name, email, city, phone, age) VALUES (?, ?, ?, ?, ?)
        """, (name, email, city, phone, age))

    conn.commit()
    conn.close()
    print(f"✅ {num_records} users seeded into the database.")

if __name__ == "__main__":
    db_name = "ALX_prodev.db"  # Make sure to include .db extension
    num_records = 5000

    recreate_database_and_table(db_name)
    seed_data(db_name, num_records)