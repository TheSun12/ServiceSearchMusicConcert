import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class RequestSinger:
    def __init__(self):
        self.req = '''SELECT * FROM Singers 
                     LEFT JOIN Countries ON Singers.country = Countries.countryId
                     LEFT JOIN Genres ON Singers.genre = Genres.genreId'''

    def get_information(self):
        return self.req
    
class RequestSingerName(RequestSinger):
    def __init__(self, singer, name, flag):
        self.singer = singer
        if flag:
            self.req = self.singer.get_information() + f"AND Singers.singerName = '{name}'"
        else:
            self.req = self.singer.get_information() + f"WHERE Singers.singerName = '{name}'"

    def get_information(self):
        return self.req
        
class RequestSingerCountry(RequestSinger):
    def __init__(self, singer, country, flag):
        self.singer = singer

        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        req1 = f"SELECT countryId FROM Countries WHERE countryName = '{country}'"
        cursor.execute(req1)
        res_name = cursor.fetchall()
        self.req = self.singer.get_information()
        if flag:
            self.req += ' AND'
        else:
            self.req += ' WHERE'
        self.req += f" Singers.country = {res_name[0][0]}"

    def get_information(self):
        return self.req


class RequestSingerGenre(RequestSinger):
    def __init__(self, singer, genre, flag):
        self.singer = singer

        connection = psycopg2.connect(user="postgres",
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        req1 = f"SELECT genreId FROM Genres WHERE genreName = '{genre}'"
        cursor.execute(req1)
        res_name = cursor.fetchall()
        self.req = self.singer.get_information()
        if flag:
            self.req += ' AND'
        else:
            self.req += ' WHERE'
        self.req += f" Singers.genre = {res_name[0][0]}"

    def get_information(self):
        return self.req