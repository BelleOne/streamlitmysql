import pymysql
from connectdb import connectmysql as con
from tabulate import tabulate
# Create table function

# create function add data insert data


def updatepersons():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQC create table
    sql = """
        DELETE FROM person
        Where id = 5
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("Delete Data Insert successfully")
    except pymysql.Error:
        print(pymysql.Error)


# Call createtable function
updatepersons()
