import sqlite3
from pathlib import Path 
# --- Import CSV files ---
#file resides in the sibling directory "data"
DB_PATH = "./clinic_simple.db"
CSV_PATH = "./data/patients.csv"
SCHEMA_PATH = Path("./sql/schema.sql")

def main():

    # Read the schema SQL file.
    try:
        schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: Schema file not found. Checked path: {SCHEMA_PATH}")
        print("Please ensure the 'sql/schema.sql' file exists relative to the project root.")
        return # Stop execution if the file isn't found

    # Create (or overwrite) the database and apply the schema.
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(schema_sql)
        conn.commit()

    print(f"Created database: {DB_PATH}")

if __name__ == "__main__":
    main()
