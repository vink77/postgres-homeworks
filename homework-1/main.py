"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
def main() -> None:
    conn = psycopg2.connect(
    host = 'localhost',
    database = 'north',
    user = 'postgres',
    password = '9877'
    )

    file_str = [('customers',"%s, %s, %s"), ("employees", "%s, %s, %s, %s, %s, %s"),("orders","%s, %s, %s, %s, %s")]
    try:
        with conn:
            with conn.cursor() as cur:
                for key, val in file_str:
                    with open(f"north_data\{key}_data.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        next(file_reader)
                        cur.executemany(f"INSERT INTO {key} VALUES({val})", file_reader)
    finally:
        conn.close()
if __name__ == '__main__':
    main()