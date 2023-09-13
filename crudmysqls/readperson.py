import pymysql
from connectdb import connectmysql as con
from tabulate import tabulate
# Create table function

# create function add data insert data


def readpersons():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQC select data in table
    sql = """
        SELECT * FROM person
    """

    try:
        cursor.execute(sql)
        connection.commit()
        result = cursor.fetchall()
        # for row in result:
        #     print(row['fullname'], row['email'], row['age'])
        headersd = {"id": "ID", "fullname": "Full Name",
                    "email": "Email", "age": "Age"}
        # print(tabulate(cursor))
        print(tabulate(result, headers=headersd, tablefmt="pretty"))

        print("Read Data successfully")
    except pymysql.Error:
        print(pymysql.Error)


# Call createtable function
readpersons()
