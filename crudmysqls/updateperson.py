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
        UPDATE person SET fullname = 'bellow' ,age = 25
        Where id = 4
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("Update Data Insert successfully")
    except pymysql.Error:
        print(pymysql.Error)


# Call createtable function
updatepersons()
