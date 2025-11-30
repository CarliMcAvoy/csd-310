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


def show_films(title):
    global cursor

    cursor = db.cursor()

    cursor.execute("""
                   SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 
                   'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio 
                    ON film.studio_id=studio.studio_id
                   """)

    films = cursor.fetchall()

    print("\n  -- {} --  ".format(title))

    for film in films:
        print('Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n'.format(film[0], film[1],
                                                                                         film[2], film[3]))

show_films("DISPLAYING FLIMS")

cursor.execute("""
        INSERT INTO film(film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) 
        VALUES(4, 'Jurassic Park', 1993, 127, 'Steven Spielberg', 3, 2)
            """)


show_films("DISPLAYING FILMS AFTER INSERT")

cursor.execute("""
        UPDATE film
        SET genre_id = 1
        WHERE film_name = 'Alien'
               """)

show_films("DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")

show_films("DISPLAYING FILMS AFTER DELETE")
