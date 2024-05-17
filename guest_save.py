import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from request_concert import RequestConcert, RequestConcertData, RequestConcertSinger, RequestConcertTime, RequestConcertTown
from request_singer import RequestSinger, RequestSingerCountry, RequestSingerGenre, RequestSingerName

class Guest:
    def __init__(self):
        return
    
    def find_concert(self, singer, town, date, time):
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

    def find_singer(self, name, country, genre):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="123",
                                          host="127.0.0.1",
                                          port="5432")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            singer = RequestSinger()
            flag = False
            if name:
                singer = RequestSingerName(singer, name, flag)
                flag = True
            if country:
                singer = RequestSingerCountry(singer, country, flag)
                flag = True
            if genre:
                singer = RequestSingerGenre(singer, genre, flag)
            req = singer.get_information()
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

    def find_genre(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            req = 'SELECT * FROM Genres'
            cursor.execute(req)
            self.result = cursor.fetchall()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    def get_result(self):
        return self.result