import csv
import psycopg2



def insert_from_csv(file_path):
    conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="123654aA",
    host="localhost"
)
    cursor = conn.cursor()
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        next(csvreader)  # Skip header row if exists
        for row in csvreader:
            first_name, last_name, phone_number = row
            cursor.execute(f"""INSERT INTO phonebook (first_name, last_name, phone_number) VALUES 
                           ('{first_name}', '{last_name}', '{phone_number}');
            """)
            conn.commit()
            cursor.close()
            conn.close()

def insert_from_console():
    conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="123654aA",
    host="localhost"
    )
    cursor = conn.cursor()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    cursor.execute("INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first_name, last_name, phone_number))
    conn.commit()
    cursor.close()
    conn.close()


def update_phonebook_entry(first_name, new_phone_number):
    conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="123654aA",
    host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE PhoneBook SET phone_number = %s WHERE first_name = %s", (new_phone_number, first_name))
    conn.commit()
    cursor.close()
    conn.close()

def query_phonebook(filter=None):
    conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="123654aA",
    host="localhost"
    )
    cursor = conn.cursor()
    if filter:
        cursor.execute("SELECT * FROM PhoneBook WHERE " + filter)
    else:
        cursor.execute("SELECT * FROM PhoneBook")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()


def delete_entry_by_name(first_name):
    conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="123654aA",
    host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PhoneBook WHERE first_name = %s", (first_name,))
    conn.commit()
    cursor.close()
    conn.close()

def delete_entry_by_phone(phone_number):
    conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="123654aA",
    host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PhoneBook WHERE phone_number = %s", (phone_number,))
    conn.commit()
    cursor.close()
    conn.close()

def main():
    # Connect to PostgreSQL
    conn = psycopg2.connect("dbname=phonebook user=postgres password=123654aA")
    
    # Insert data from CSV
    insert_from_csv("phonebook_data.csv")
    
    # Insert data from console
    insert_from_console()
    
    # Update data
    update_phonebook_entry("ara", "+1234567890")
    
    # Query data
    print("All entries:")
    query_phonebook()
    
    print("Filtered entries:")
    query_phonebook("first_name = 'ara'")
    
    # Delete data
    delete_entry_by_name("qwerty")
    delete_entry_by_phone("+1234567890")
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    main()
