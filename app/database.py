import sqlite3

DB_NAME = "ecobridge.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prompt TEXT,
        classification TEXT,
        model TEXT,
        estimated_tokens INTEGER,
        energy_kwh REAL,
        carbon_g REAL,
        cost_usd REAL,
        energy_saved_kwh REAL,
        carbon_saved_g REAL,
        cost_saved_usd REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def insert_request(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO requests (
        prompt,
        classification,
        model,
        estimated_tokens,
        energy_kwh,
        carbon_g,
        cost_usd,
        energy_saved_kwh,
        carbon_saved_g,
        cost_saved_usd
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["prompt"],
        data["classification"],
        data["model"],
        data["estimated_tokens"],
        data["energy_kwh"],
        data["carbon_g"],
        data["cost_usd"],
        data["energy_saved_kwh"],
        data["carbon_saved_g"],
        data["cost_saved_usd"]
    ))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully!")
