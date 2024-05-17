import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class EditConcert:
    def __init__(self):
        self.req = 'UPDATE Concerts SET'

    def get_information(self):
        return self.req
    

class EditConcertName(EditConcert):
    def __init__(self, concert, name, flag):
        self.concert = concert

        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        self.req = self.concert.get_information()
        self.req += f""" concertName = '{name}'"""

    def get_information(self):
        return self.req


class EditConcertSinger(EditConcert):
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
        self.req = self.concert.get_information()
        if flag:
            self.req += ','
        self.req += f" singer = '{res_name[0][0]}'"

    def get_information(self):
        return self.req
        
class EditConcertPlace(EditConcert):
    def __init__(self, concert, place, flag):
        self.concert = concert

        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        self.req = self.concert.get_information()
        if flag:
            self.req += ','
        self.req += f" placeName = '{place}'"

    def get_information(self):
        return self.req


class EditConcertData(EditConcert):
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
            self.req += ','
        self.req += f" concertDate = '{date}'"

    def get_information(self):
        return self.req
    

class EditConcertTime(EditConcert):
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
            self.req += ','
        self.req += f" concertTime = '{time}'"

    def get_information(self):
        return self.req
    

class EditConcertAge(EditConcert):
    def __init__(self, concert, age, flag):
        self.concert = concert

        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        self.req = self.concert.get_information()
        req1 = f"""SELECT limitId FROM AgeLimits WHERE limitText = '{age}'"""
        cursor.execute(req1)
        res = cursor.fetchall()
        if res:
            if flag:
                self.req += ','
        self.req += f' ageLimit = {res[0][0]}'

    def get_information(self):
        return self.req
    

class EditConcertSeats(EditConcert):
    def __init__(self, concert, seats, flag):
        self.concert = concert

        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        self.req = self.concert.get_information()
        if flag:
            self.req += ','
        self.req += f" freeSeats = {seats}"

    def get_information(self):
        return self.req
    

class EditConcertPrice(EditConcert):
    def __init__(self, concert, price, flag):
        self.concert = concert

        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        self.req = self.concert.get_information()
        if flag:
            self.req += ','
        self.req += f" price = '{price}'"

    def get_information(self):
        return self.req