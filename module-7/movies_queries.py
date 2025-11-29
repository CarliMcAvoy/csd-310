import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values


secrets = dotenv_values('.env')

config = {
    'user': secrets['USER'],
    'password': secrets['PASSWORD'],
    'host': secrets['HOST'],

    'database': secrets['DATABASE'],
    'raise_on_warnings': True
}

try:

    db = mysql.connector.connect(**config)

    print('\n Database user {} connected MySQL on host {} with database {}'.format(config['user'], config['host'],
                                                                                   config['database']))

    input('\n\n press any key to continue...\n')

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('The supplied username or password are invalid')

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('The specified database does not exist')

    else:
        print(err)



studio_header = "-- DISPLAYING Studio RECORDS --"
centered_s_header = studio_header.center(40)
print(centered_s_header)

cursor = db.cursor()

cursor.execute('SELECT studio_id, studio_name FROM studio')

studios = cursor.fetchall()

for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))


genre_header = "-- DISPLAYING Genre RECORDS --"
centered_g_header = genre_header.center(40)
print(centered_g_header)

cursor.execute('SELECT genre_id, genre_name FROM genre')

genres = cursor.fetchall()

for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))


film_header = "-- DISPLAYING Short Film RECORDS --"
centered_f_header = film_header.center(40)
print(centered_f_header)

cursor.execute('SELECT film_name, film_runtime FROM film WHERE film_runtime < 120')

films = cursor.fetchall()

for film in films:
    print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))


director_header = "-- DISPLAYING Director RECORDS in Order --"
centered_d_header = director_header.center(40)
print(centered_d_header)

cursor.execute('SELECT film_name, film_director FROM film ORDER BY film_director ASC')

directors = cursor.fetchall()

for film in directors:
    print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))










