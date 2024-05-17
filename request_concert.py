import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class RequestConcert:
    def __init__(self):
        self.req = '''SELECT * FROM Concerts LEFT JOIN Singers ON Concerts.singer = Singers.singerId 
                   LEFT JOIN Places ON Concerts.placeName = Places.placeName'''

    def get_information(self):
        return self.req
    
class RequestConcertSinger(RequestConcert):
    def __init__(self, concert, singer, flag):
        self.concert = concert

        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        req1 = f"SELECT singerId FROM Singers WHERE singerName = '{singer}'"
        cursor.execute(req1)
        res_name = cursor.fetchall()
        if flag:
            self.req = self.concert.get_information() + f'AND Concerts.singer = {res_name[0][0]}'
        else:
            self.req = self.concert.get_information() + f'WHERE Concerts.singer = {res_name[0][0]}'

    def get_information(self):
        return self.req
        
class RequestConcertTown(RequestConcert):
    def __init__(self, concert, town, flag):
        self.concert = concert

        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        req2 = f"SELECT cityId FROM Cities WHERE cityName = '{town}'"
        cursor.execute(req2)
        res_town = cursor.fetchall()

        req1 = f"SELECT placeName FROM Places WHERE city = '{res_town[0][0]}'"
        cursor.execute(req1)
        res_name = cursor.fetchall()
        self.req = self.concert.get_information()
        if flag:
            self.req += ' AND'
        else:
            self.req += ' WHERE'
        self.req += f' Concerts.placeName IN ('
        for i in range(len(res_name) - 1):
            self.req += f"'{res_name[i][0]}', "
        self.req += f"'{res_name[len(res_name) - 1][0]}')"

    def get_information(self):
        return self.req


class RequestConcertData(RequestConcert):
    def __init__(self, concert, date, flag):
        self.concert = concert

        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        self.req = self.concert.get_information()
        if flag:
            self.req += ' AND'
        else:
            self.req += ' WHERE'
        self.req += f" concertDate = '{date}'"

    def get_information(self):
        return self.req
    

class RequestConcertTime(RequestConcert):
    def __init__(self, concert, time, flag):
        self.concert = concert

        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        self.req = self.concert.get_information()
        if flag:
            self.req += ' AND'
        else:
            self.req += ' WHERE'
        self.req += f" concertTime = '{time}'"

    def get_information(self):
        return self.req