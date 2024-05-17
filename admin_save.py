import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from edit_concert import EditConcert, EditConcertAge, EditConcertData, EditConcertName, EditConcertPlace, EditConcertPrice, EditConcertSeats, EditConcertSinger, EditConcertTime

class Admin:
    instance = None

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __new__(cls, login, password):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def edit_concert(self, idCon, name_conc, singer, date_conc, time_conc, age, place, seats, price):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="123",
                                          host="127.0.0.1",
                                          port="5432")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            req_sel = f"""SELECT * FROM Concerts WHERE concertId = {idCon}"""
            cursor.execute(req_sel)
            result = cursor.fetchall()
            if len(result) > 0:
                
                concert = EditConcert()
                flag = False
                
                if name_conc:
                    concert = EditConcertName(concert, name_conc, flag)
                    flag = True
                if singer:
                    concert = EditConcertSinger(concert, singer, flag)
                    flag = True
                if date_conc:
                    concert = EditConcertData(concert, date_conc, flag)
                    flag = True
                if time_conc:
                    concert = EditConcertTime(concert, time_conc, flag)
                    flag = True
                if age:
                    concert = EditConcertAge(concert, age, flag)
                    flag = True
                if place:
                    concert = EditConcertPlace(concert, place, flag)
                    flag = True
                if seats:
                    concert = EditConcertSeats(concert, seats, flag)
                    flag = True
                if price:
                    concert = EditConcertPrice(concert, price, flag)
                req = concert.get_information()
                req += f""" WHERE concertId = {idCon}"""
                cursor.execute(req)
                self.result = result
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    def plus_concert(self, name, singer, town, date, time, age, place, seats, price):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="123",
                                          host="127.0.0.1",
                                          port="5432")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            concert = PlusConcert(name, singer, town, date, time, age, place, seats, price)
            result = concert.get_information()
            cursor.execute(result)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    def delete_concert(self, idCon):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="123",
                                          host="127.0.0.1",
                                          port="5432")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            concert = DeleteConcert(idCon)
            self.result = concert.get_information()
            cursor.execute(self.result)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    def get_result(self):
        return self.result


class PlusConcert:
    def __init__(self, name, singer, town, date, time, age, place, seats, price):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="123",
                                          host="127.0.0.1",
                                          port="5432")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()

            self.req = f"""INSERT INTO Concerts (concertId, concertName, singer, placeName, concertDate, concertTime, ageLimit, freeSeats, price)
                         VALUES"""
            
            req1 = 'SELECT * FROM Concerts'
            cursor.execute(req1)
            res_name = cursor.fetchall()
            n = len(res_name) + 1

            req1 = f"SELECT singerId FROM Singers WHERE singerName = '{singer}'"
            cursor.execute(req1)
            if req1:
                res_name = cursor.fetchall()
                singerId = res_name[0][0]

            req1 = f"SELECT limitId FROM AgeLimits WHERE limitText = '{age}'"
            cursor.execute(req1)
            res_name = cursor.fetchall()
            ageLimit = res_name[0][0]
        
            self.req += f" ({n}, '{name}', {singerId}, '{place}', '{date}', '{time}', {ageLimit}, {seats}, {price})"
            
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")
    
    def get_information(self):
        return self.req
    

class DeleteConcert:
    def __init__(self, idCon):
        self.req = f"""DELETE FROM Concerts WHERE concertId = {idCon}"""

    def get_information(self):
        return self.req