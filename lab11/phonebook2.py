import csv
import psycopg2


def query_phonebook_by_pattern(pattern):
    conn = psycopg2.connect(dbname="phonebook", user="postgres", password="123654aA", host="localhost")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PhoneBook WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone_number ILIKE %s",
                   (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()


def insert_or_update_user(first_name, phone_number, last_name=None):
    conn = psycopg2.connect(dbname="phonebook", user="postgres", password="123654aA", host="localhost")
    cursor = conn.cursor()
    if last_name is None:
        last_name = ""  # Provide a default value
    cursor.execute("SELECT COUNT(*) FROM PhoneBook WHERE first_name = %s", (first_name,))
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", 
                       (first_name, last_name, phone_number))
    else:
        cursor.execute("UPDATE PhoneBook SET phone_number = %s WHERE first_name = %s", (phone_number, first_name))
    conn.commit()
    cursor.close()
    conn.close()


def insert_many_users(user_data):
    conn = psycopg2.connect(dbname="phonebook", user="postgres", password="123654aA", host="localhost")
    cursor = conn.cursor()
    incorrect_data = []
    for data in user_data:
        name, phone = data
        if not phone.isdigit():
            incorrect_data.append(data)
        else:
            cursor.execute("INSERT INTO PhoneBook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cursor.close()
    conn.close()
    return incorrect_data


def query_phonebook(limit=None, offset=None):
    conn = psycopg2.connect(dbname="phonebook", user="postgres", password="123654aA", host="localhost")
    cursor = conn.cursor()
    query = "SELECT * FROM PhoneBook"
    if limit is not None:
        query += f" LIMIT {limit}"
    if offset is not None:
        query += f" OFFSET {offset}"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()


def delete_entry_by_username_or_phone(identifier):
    conn = psycopg2.connect(dbname="phonebook", user="postgres", password="123654aA", host="localhost")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PhoneBook WHERE first_name = %s OR phone_number = %s", (identifier, identifier))
    conn.commit()
    cursor.close()
    conn.close()


# Update main function to use the new functions and procedures
def main():
    conn = psycopg2.connect("dbname=phonebook user=postgres password=123654aA")

    # Insert or update data
    insert_or_update_user("ara", "+1234567890")

    # Insert many users
    incorrect_data = insert_many_users([("John", "1234567890"), ("Doe", "invalid"), ("Alice", "9876543210")])
    print("Incorrect data:", incorrect_data)

    # Query data
    print("All entries:")
    query_phonebook()

    # Query data with pagination
    print("Entries with pagination:")
    query_phonebook(limit=5, offset=0)

    # Query data with pattern
    print("Entries matching pattern:")
    query_phonebook_by_pattern("ara")

    # Delete data
    delete_entry_by_username_or_phone("qwerty")

    # Close connection
    conn.close()


if __name__ == "__main__":
    main()
