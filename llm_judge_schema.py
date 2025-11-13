import sqlite3
from datetime import datetime

def create_database():
    """Create the LLM judge database with all necessary tables"""
    conn = sqlite3.connect('llm_judge.db')
    cursor = conn.cursor()

    # Prompts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Responses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt_id INTEGER NOT NULL,
            llm_provider TEXT NOT NULL,
            response_text TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (prompt_id) REFERENCES prompts(id)
        )
    ''')

    # Evaluations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS evaluations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            response_id INTEGER NOT NULL,
            criteria TEXT NOT NULL,
            score INTEGER CHECK(score >= 0 AND score <= 10),
            feedback TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (response_id) REFERENCES responses(id)
        )
    ''')

    conn.commit()
    print("✓ Database schema created successfully")
    print("✓ Tables: prompts, responses, evaluations")

    conn.close()

if __name__ == "__main__":
    create_database()