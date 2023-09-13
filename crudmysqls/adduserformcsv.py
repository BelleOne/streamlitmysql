import pymysql
from connectdb import connectmysql as con
import csv


# Create table function

# create function add data insert data


def addusers():
    connection = con.connectdb()
    cursor = connection.cursor()
    # read file csv
    with open('filedata/user.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            sql = """
                INSERT INTO user (Name, email, mobile)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, tuple(row))
            print('adding user')
    connection.commit()
    connection.close()
    # val = (row[0], row[1], row[2])
    # cursor.execute(sql, val)
    # connection.commit()

    # SQC create table
    # sql = """
    #     INSERT INTO person (fullname, Email, Mobile)
    #     VALUES (%s, %s, %s)
    # """

    # try:
    #     cursor.execute(sql)
    #     connection.commit()
    #     print("Add Data Insert successfully")
    # except pymysql.Error:
    #     print(pymysql.Error)


# Call createtable function
addusers()
