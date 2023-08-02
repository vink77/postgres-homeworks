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
    cur = conn.cursor()

    # Считывание данных из CSV файла
    with open("north_data/customers_data.csv", encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter=",")
        cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", file_reader)
        cur.execute("SELECT * FROM customers")
        conn.commit()
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print(len((rows)))

    cur.close()
    conn.close()


if __name__ == '__main__':
    main()



