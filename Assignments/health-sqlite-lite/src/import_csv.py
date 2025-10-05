import pandas as pd
from sqlalchemy import create_engine, text


DB_PATH = "./clinic_simple.db"
CSV_PATH = "./data/patients.csv"


def main():

    # Read the CSV file.
    df = pd.read_csv(CSV_PATH, dtype=str)  

    # Create the database engine.
    engine = create_engine(f"sqlite:///{DB_PATH}")

    df.to_sql("patients", con=engine, if_exists="append", index=False)

    ## Verify the number of rows loaded.
    sql_count = text("SELECT COUNT(*) FROM patients")
    with engine.connect() as conn:
        result = conn.execute(sql_count)
        total = result.scalar_one() # scalar_one() is new in SQLAlchemy 2.0 that returns a single value.
        
    print(f"Loaded {len(df)} rows into patients. Table now has {total} rows.")

if __name__ == "__main__":
    main()

