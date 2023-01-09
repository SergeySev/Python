import csv
import sqlite3


headers = "Site", "login", "password"
db_file = "Rock.csv"
db_sql = "training.db"


def file_to_list() -> list:
    data = []
    with open('Rock.csv', newline='') as file:
        reader = csv.DictReader(file)
        for dict_row in reader:
            data.append(dict_row)
        return data


def write_to_file(file_name, data_new, mode='a'):
    """This function write to file new website and login and password"""
    with open(file_name, newline='', mode=mode) as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if type(data_new) == dict:
            writer.writerow(data_new)
        elif type(data_new) == list:
            writer.writeheader()
            writer.writerows(data_new)


def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return cursor, connection


def close_database(cursor, connection):
    cursor.close()
    connection.close()


def db_to_list(cursor):
    sql = "SELECT * FROM  \"Password_manager\""
    data = cursor.execute(sql)
    return data.fetchall()


def add_data_to_db(cursor):
    pass


def deleted_data_from_db(cursor):
    pass


def update_data_in_db(cursor):
    pass


if __name__ == "__main__":
    from pprint import PrettyPrinter
    pp = PrettyPrinter()
    cursor, connection = create_connection(db_sql)
    data = db_to_list(cursor)
    pp.pprint(data)
    close_database(cursor, connection)