import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#from admin_save import Admin

adm_log = 'admlog'
adm_pas = 'p455w0rd'

class Login:
    def __init__(self, login, password):
        self.login = login
        self.password = password
    
    def check_user(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            req = f"""SELECT * FROM UserData WHERE login = '{self.login}' AND userPassword = '{self.password}' AND userRole != 'Admin'"""
            cursor.execute(req)
            self.result = cursor.fetchall()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    def check_adm(self):
        return self.login == adm_log and self.password == adm_pas

    def get_result(self):
        return self.result