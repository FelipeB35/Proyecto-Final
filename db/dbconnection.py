import pymysql.cursors


def createDBConnection():
    connection = pymysql.connect(
        host="localhost",  # 127.0.0.1
        user="root",
        password="root",
        database="todolistdb",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,  # [DictCursor]Jala los datos como un diccionario
    )
    return connection

