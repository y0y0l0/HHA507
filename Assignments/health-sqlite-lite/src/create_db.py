import sqlite3
from util.common_functions import adjust_path_based_on_OS

# --- Import CSV files ---
#file resides in the sibling directory "data"
DB_PATH = "./clinic_simple.db"
CSV_PATH = "./data/patients.csv"
SCHEMA_PATH = "./sql/schema.sql"


def main():

    # Read the schema SQL file.
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")

    # Create (or overwrite) the database and apply the schema.
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(schema_sql)
        conn.commit()

    print(f"Created database: {DB_PATH}")

if __name__ == "__main__":
    main()
