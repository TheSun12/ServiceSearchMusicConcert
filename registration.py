import win32api
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from registration_checker import CheckerLogin

class Registration:
    def __init__(self):
        return
    
    def do_registration(self, login, email, pass1):
        check_log = CheckerLogin([login, pass1])
        result_log = check_log.check()
        if result_log != 'OK':
            win32api.MessageBox(0, result_log, 'Ошибка')
        else:
            try:
                connection = psycopg2.connect(user="postgres",
                                            password="123",
                                            host="127.0.0.1",
                                            port="5432")
                connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cursor = connection.cursor()
                req1 = 'SELECT * FROM UserData'
                cursor.execute(req1)
                res = cursor.fetchall()
                n = len(res) + 1
                req = f"""INSERT INTO UserData (userId, login, email, userPassword, userRole)
                         VALUES ({n}, '{login}', '{email}', '{pass1}', 'User');"""
                print(req)
                cursor.execute(req)
            except (Exception, Error) as error:
                print("Ошибка при работе с PostgreSQL", error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    print("Соединение с PostgreSQL закрыто")
