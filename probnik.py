import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Cities')
    print(cursor.fetchall())


    """sql_insert_table = '''INSERT INTO Cities (cityId, cityName) VALUES (1, 'Санкт-Петербург'),
                          (2, 'Москва'), (3, 'Саратов');'''
    cursor.execute(sql_insert_table)
    print(1)

    sql_insert_table = '''INSERT INTO Places (placeName, city, address, capacity)
VALUES ('Газпром Арена', 1, 'Футбольная аллея, 1', 70000),
       ('Юбилейный', 1, 'просп. Добролюбова, 18', 7000),
       ('А2',	1, 'просп. Медиков, 3', 5000),
       ('Космонавт', 1, 'ул. Бронницкая, 24', 1400),
       ('Aurora Concert Hall', 1, 'Пироговская наб., 5/2', 2000),
       ('Sound', 1, 'порт Севкабель, Кожевенная линия, 40б', 1700),
       ('VK Stadium', 2, 'Ленинградский просп., 80, стр. 17', 7000),
       ('Лужники',	2, 'ул. Лужники, 24, стр. 1', 80000),
       ('Мегаспорт', 2, 'Ходынский бул., 3', 16000),
       ('Центр народного творчества им. Руслановой', 3, 'ул. Ломоносова, 20', 600);'''
    cursor.execute(sql_insert_table)
    print(2)

    sql_insert_table = '''INSERT INTO Genres (genreId, genreName, description)
VALUES (1, 'Поп', 'Область массовой культуры, охватывающая различные формы, жанры и стили развлекательной и прикладной музыки 2-й половины XX - начала XXI веков. Основные черты поп-музыки - простота инструментальной части, ритмичность, акцент на вокал.'),
(2, 'Панк-рок',	'Жанр рок-музыки, сформировавшийся к середине 1970-х годов на территории США, Великобритании и Австралии. Как правило, панк-группы записывали короткие, очень динамичные песни с резкими мелодиями и грубым вокалом, минимальным набором аппаратуры, а также социальными текстами.'),
(3,	'Рок', 'Жанр музыки, характеризующийся ярко выраженным ритмом. Так же является обобщённым названием для ряда музыкальных стилей и направлений. Многообразие жанров и поджанров рок-музыки градируется от “легкого” до “тяжёлого”'),
(4,	'Хип-хоп',	'Музыкальный жанр, сочетающий рэп (ритмичный речитатив) с электронным битом, сэмплами и прочим музыкальным сопровождением в исполнении ди-джея.'),
(5,	'Поп-рок', 'Жанр музыки, объединяющий элементы поп-музыки и рок-музыки. Песни характеризуются простой структурой, запоминающимися мелодиями, повторением музыкальных фраз и качающими ритмичными ощущениями, связанными с особой формой движения, с использованием в качестве основных инструментов ударных и электрогитар.'),
(6,	'Инди',	'Постоянно меняющийся и эклектичный жанр, который включает в себя широкий спектр стилей, характеризующихся “сделай сам”, альтернативным вкусом и бунтарским духом. Основной философией инди-музыки является ее ориентация на творческую и художественную свободу и независимость.');'''
    cursor.execute(sql_insert_table)
    print(3)

    sql_insert_table = '''INSERT INTO Countries (countryId, countryName) VALUES (1, 'Россия'), (2, 'Кыргызстан');'''
    cursor.execute(sql_insert_table)
    print(4)

    sql_insert_table = '''INSERT INTO Singers (singerId, singerName, genre, country, description)
VALUES (1, 'Леонид Агутин', 1, 1, 'Советский и российский певец, композитор, музыкант, автор песен, аранжировщик, режиссёр; заслуженный артист Российской Федерации.'), 
(2,	'КняZz', 2,	1, 'Российская рок-группа из Санкт-Петербурга, созданная в 2011 году Андреем Князевым, являвшимся на момент её создания участником панк-группы “Король и Шут”'),
(3,	'Алиса', 3,	1, 'Советская и российская рок-группа, образованная в 1983 году в Ленинграде. Одна из самых популярных групп русского рока.'),
(4,	'Feduk', 4,	1, 'Российский певец, хип-хоп- и хаус-рэп-исполнитель и автор песен. Сольную карьеру начал в 2010 году, с тех пор выпустил два мини-альбома и семь студийных альбомов.'),
(5,	'The Hatters', 5, 1,	'Российская рок- и поп-группа, основанная в 2016 году в Санкт-Петербурге.'),
(6,	'Dabro', 1,	1, 'Музыкальная группа из Казани, состоящая из двух братьев - Ивана и Михаила Засидкевичей. Большую популярность группе принесла песня 2020 года “Юность”.'),
(7,	'Green Apelsin', 6,	1, 'Певица, в творчестве которой тесно переплетаются академический вокал и фолк. А в тексты молодой исполнительницы часто обыгрывают сюжеты народных сказок, мифов и легенд.'),
(8,	'Polnalyubvi', 6, 1,	'Российская певица, выступающая в жанре инди-поп'),
(9,	'Дайте танк (!)', 6, 1, 'По словам участников подмосковной группы, их музыка — это "гаражный рок для танцоров-интровертов, скучающих по русскому языку".'),
(10, 'Баста', 4, 1, 'Российский музыкант, исполнитель рэпа и других жанров, битмейкер, композитор, телерадиоведущий, актёр, сценарист, режиссёр и продюсер.'),
(11, 'Звери', 3, 1, 'Российская поп-рок-группа, созданная Романом Билыком в 2000 году. Лауреат премии MTV Россия и премии “Дебют”. На премии Муз-ТВ группа побеждала в номинации “Лучшая рок-группа” 9 раз.'),
(12, 'Amirchik', 1, 2, 'молодой артист из Бишкека, 18 лет. Стал популярен в TikTok благодаря акустическим каверам на популярные песни');'''
    cursor.execute(sql_insert_table)
    print(5)

    sql_insert_table = '''INSERT INTO AgeLimits (limitId, limitText) VALUES (1, '0+'), (2, '6+'),
                          (3, '12+'), (4, '16+'), (5, '18+');'''
    cursor.execute(sql_insert_table)
    print(6)

    sql_insert_table = '''INSERT INTO Concerts (concertId, concertName, singer, placeName, concertDate, concertTime, ageLimit, freeSeats, price)
VALUES (1, 'Большой сольный концерт Леонида Агутина', 1,	'Газпром Арена', '2024-06-24', '20:00:00', 2, 859, 3500),
(2,	'Как в старой сказке',	2, 'Газпром Арена', '2024-07-19', '20:00:00', 3, 524, 5000),
(3,	'Юбилейный концерт группы Алиса', 3, 'Юбилейный',	'2024-05-10', '20:00:00', 4, 941, 4700),
(4, 'Любовь в твоем городе', 4, 'А2',	'2024-04-12', '20:00:00', 3, 115, 3200),
(5,	'Клубное шоу The Hatters', 5, 'Космонавт', '2024-03-10', '20:00:00', 4, 125, 7000),
(6,	'Концерт группы Dabro',	6, 'А2', '2024-03-22', '20:00:00', 1, 354, 5000),
(7,	'Концерт Green Apelsin', 7, 'Aurora Concert Hall', '2024-04-13', '20:00:00', 3, 103, 4000),
(8, 'Концерт Polnalyubvi', 8, 'Sound', '2024-03-01', '19:00:00', 4, 52, 4500),
(9, 'Концерт Дайте танк (!)', 9, 'VK Stadium', '2024-03-31', '20:00:00', 4, 310, 3100),
(10, 'Стадионный концерт Леонида Агутина', 1,	'Лужники', '2024-07-27', '19:00:00', 2, 1350, 3500),
(11, 'Концерт Басты', 10, 'Мегаспорт',	'2024-04-20', '19:00:00', 3, 236, 6000),
(12, 'Большой концерт Звери', 11, 'Лужники', '2024-08-24', '19:00:00', 2, 10250, 3800),
(13, 'Концерт Amirchik', 12, 'Центр народного творчества им. Руслановой', '2024-03-12', '19:00:00', 1, 436, 2000);'''
    cursor.execute(sql_insert_table)
    print(7)

    sql_insert_table = '''INSERT INTO Roles (roleName, description, rights)
VALUES ('Guest', 'Гость', 'Только поиск и просмотр'),
('User', 'Пользователь', 'Поиск, просмотр и покупка билетов'),
('Admin', 'Администратор', 'Поиск, просмотр, покупка билетов, добавление, удаления и изменение данных о концертах');'''
    cursor.execute(sql_insert_table)
    print(8)

    sql_insert_table = '''INSERT INTO UserData (userId, login, email, userPassword, userRole)
VALUES (1, 'cat123', 'cutecat@mail.ru',	'Mew34214',	'User'),
(2,	'ivanov98', 'i-ivanov98@yandex.ru',	'12fgrskl3!', 'User'),
(3, 'admin', 'admin@mail.ru', 'adminpass', 'Admin');'''
    cursor.execute(sql_insert_table)
    print(9)"""

    """sql_create_table = 'CREATE TABLE Cities(cityId INTEGER NOT NULL, cityName VARCHAR NOT NULL, PRIMARY KEY(cityId));'
    cursor.execute(sql_create_table)
    print(1)

    sql_create_table = '''CREATE TABLE Places(placeName VARCHAR NOT NULL, city INTEGER NOT NULL,
	                      address VARCHAR NOT NULL, capacity INTEGER NOT NULL, PRIMARY KEY(placeName),
                          FOREIGN KEY(city) REFERENCES Cities(cityId));'''
    cursor.execute(sql_create_table)
    print(2)

    sql_create_table = '''CREATE TABLE Genres(genreId INTEGER NOT NULL, genreName VARCHAR NOT NULL,
	                      description VARCHAR NULL, PRIMARY KEY(genreId));'''
    cursor.execute(sql_create_table)
    print(3)

    sql_create_table = '''CREATE TABLE Countries(countryId INTEGER NOT NULL,
                          countryName VARCHAR NOT NULL, PRIMARY KEY(countryId));'''
    cursor.execute(sql_create_table)
    print(4)

    sql_create_table = '''CREATE TABLE Singers(singerId INTEGER NOT NULL, singerName VARCHAR NOT NULL,
	                      genre INTEGER NULL, country INTEGER NULL, description VARCHAR NULL,
	                      PRIMARY KEY(singerId), FOREIGN KEY(genre) REFERENCES Genres(genreId),
                          FOREIGN KEY(country) REFERENCES Countries(countryId));'''
    cursor.execute(sql_create_table)
    print(5)

    sql_create_table = '''CREATE TABLE AgeLimits(limitId INTEGER NOT NULL,
	                      limitText VARCHAR NOT NULL, PRIMARY KEY(limitId));'''
    cursor.execute(sql_create_table)
    print(6)

    sql_create_table = '''CREATE TABLE Concerts(
	concertId INTEGER NOT NULL,
	concertName VARCHAR NOT NULL,
	singer INTEGER NOT NULL,
	placeName VARCHAR NOT NULL,
	concertDate DATE NOT NULL,
	concertTime TIME NOT NULL,
	ageLimit INTEGER NULL,
	freeSeats INTEGER NOT NULL,
	price MONEY NOT NULL,
	PRIMARY KEY(concertId),
	FOREIGN KEY(singer) REFERENCES Singers(singerId),
	FOREIGN KEY(placeName) REFERENCES Places(placeName),
	FOREIGN KEY(ageLimit) REFERENCES AgeLimits(limitId));'''
    cursor.execute(sql_create_table)
    print(7)

    sql_create_table = '''CREATE TABLE Roles(
	roleName VARCHAR NOT NULL,
	description VARCHAR NOT NULL,
	rights VARCHAR NOT NULL,
	PRIMARY KEY(roleName));'''
    cursor.execute(sql_create_table)
    print(8)

    sql_create_table = '''CREATE TABLE UserData(
	userId INTEGER NOT NULL,
	login VARCHAR NULL,
	email VARCHAR NULL,
	userPassword VARCHAR NULL,
	userRole VARCHAR NOT NULL,
	PRIMARY KEY(userId),
	FOREIGN KEY(userRole) REFERENCES Roles(roleName));'''
    cursor.execute(sql_create_table)
    print(9)"""

    #sql_create_database = 'create database musicConcert'
    #cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")