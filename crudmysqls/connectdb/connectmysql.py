import pymysql


def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='bell',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
