import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from request_concert import RequestConcert, RequestConcertData, RequestConcertSinger, RequestConcertTime, RequestConcertTown

class User:
    def __init__(self):
        return
    
    def buy_ticket(self, singer, town, date, time):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="123",
                                          host="127.0.0.1",
                                          port="5432")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            concert = RequestConcert()
            flag = False
            if singer:
                concert = RequestConcertSinger(concert, singer, flag)
                flag = True
            if town:
                concert = RequestConcertTown(concert, town, flag)
                flag = True
            if date:
                concert = RequestConcertData(concert, date, flag)
                flag = True
            if time:
                concert = RequestConcertTime(concert, time, flag)
            req = concert.get_information()
            print(req)
            cursor.execute(req)
            self.result = cursor.fetchall()
            print(self.result)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")
    
    def get_result(self):
        return self.result