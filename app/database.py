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

        prompt TEXT NOT NULL,
        response TEXT NOT NULL,

        classification TEXT NOT NULL,
        confidence REAL,
        reasoning TEXT,

        selected_model TEXT NOT NULL,

        estimated_tokens INTEGER,

        energy_score INTEGER,
        energy_saved_score INTEGER,

        estimated_cost_usd REAL,
        estimated_cost_saved_usd REAL,

        response_time_ms REAL,

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
        response,

        classification,
        confidence,
        reasoning,

        selected_model,

        estimated_tokens,

        energy_score,
        energy_saved_score,

        estimated_cost_usd,
        estimated_cost_saved_usd,

        response_time_ms

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        data["prompt"],
        data["response"],

        data["classification"],
        data["confidence"],
        data["reasoning"],

        data["selected_model"],

        data["estimated_tokens"],

        data["energy_score"],
        data["energy_saved_score"],

        data["estimated_cost_usd"],
        data["estimated_cost_saved_usd"],

        data["response_time_ms"]

    ))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully!")