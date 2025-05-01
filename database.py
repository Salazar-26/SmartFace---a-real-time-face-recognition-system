import sqlite3
import os

DB_PATH = r"D:\Facial_Recognition_Attendance\attendance.db"

def initialize_database():
    """Create the database and students table if they don't exist."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)  # Ensure database folder exists
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            photo_path TEXT NOT NULL,
            instances INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def add_student(name, photo_path):
    """Insert a student record into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, photo_path) VALUES (?, ?)", (name, photo_path))
    conn.commit()
    conn.close()

def update_instances(name):
    """Increment instances count for a student."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET instances = instances + 1 WHERE name = ?", (name,))
    conn.commit()
    conn.close()

def get_students():
    """Retrieve all student records."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return data
