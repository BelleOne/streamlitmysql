import pymysql
from connectdb import connectmysql as con
# Create table function

# create function add data insert data


def addpersons():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQC create table
    sql = """
        INSERT INTO person (fullname, email, age)
        VALUES ('bells', 'bell@gmail.com', 39)
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("Add Data Insert successfully")
    except pymysql.Error:
        print(pymysql.Error)


# Call createtable function
addpersons()
