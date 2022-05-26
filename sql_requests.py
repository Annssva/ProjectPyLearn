import pymysql


# Метод для проверки наличия инф-ии о пользователе в базе
def check_db(user_id):
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='pylearn_db',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        query = "SELECT * FROM users WHERE id = " + str(user_id)
        cursor.execute(query)

        rows = cursor.fetchall()

        connection.close()

        if rows:
            return True
        else:
            return False


# Метод для добавления пользователя в базу
def create_user_db(user_id):
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='pylearn_db',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        query = "INSERT INTO users (id) VALUES (" + str(user_id) + ")"
        cursor.execute(query)
        connection.commit()

    connection.close()


# Метод для получения кол-ва баллов у пользователя из базы
def get_point(user_id):
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='pylearn_db',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        query = "SELECT point FROM users WHERE id = " + str(user_id)
        cursor.execute(query)

        rows = cursor.fetchall()
        connection.close()

        return rows[0]


# Метод добавлвения баллов пользователю
def add_points(user_id, point_count=1):
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='pylearn_db',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        query = "UPDATE users SET point = point + " + str(point_count) + " WHERE id = " + str(user_id)
        cursor.execute(query)
        connection.commit()
    connection.close()


# Метод для получения значения прогресса пользователя
def get_progress(user_id):
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='pylearn_db',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        query = "SELECT progress FROM users WHERE id = " + str(user_id)
        cursor.execute(query)

        rows = cursor.fetchall()

        return rows[0]
    connection.close()


# Метод для добавления прогресса у пользователя
def add_progress(user_id, prog_count=1):
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='pylearn_db',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        query = "UPDATE users SET progress = progress + " + str(prog_count) + " WHERE id = " + str(user_id)
        cursor.execute(query)
        connection.commit()
    connection.close()
