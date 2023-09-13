import pymysql

# from module import connectmysql as con

from crudmysqls.connectdb.connectmysql import connectmysql as con

# Create table function


def createtable():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQC create table
    sql = """
        CREATE TABLE person(
            id INT PRIMARY KEY AUTO_INCREMENT,
            fullname VARCHAR(128) NOT NULL,
            email VARCHAR(60) NOT NULL,
            age INT NOT NULL
        )
    """

    try:
        cursor.execute(sql)
        connection.commit
        print("Table created :)")
    except pymysql.Error:
        print(pymysql.Error)


# Call createtable function
createtable()
