from psycopg2 import sql

from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_top15_rated_shows():
    query = """
            SELECT s.title,
               COALESCE(date_part('year',s.year),0) as year,
               s.runtime,
               ROUND(s.rating,1) as rating,
               string_agg(g.name,', ' ORDER BY g.name) genres,
               COALESCE(s.trailer,'There is no URL') as trailer,
               COALESCE(s.homepage,'There is no URL') as homepage
    FROM shows s
    INNER JOIN show_genres sg on s.id = sg.show_id
    INNER JOIN genres g on g.id = sg.genre_id
    GROUP BY s.title, 
             COALESCE(date_part('year',s.year),0), 
             s.runtime, 
             ROUND(s.rating,1), 
             s.trailer, 
             s.homepage,
             s.rating,
             s.year
    ORDER BY s.rating DESC
    LIMIT 15
    """
    return data_manager.execute_select(query)


# PA practice
def stars_for_the_stars(genre):
    query = """
    SELECT shows.title, shows.year, ROUND(shows.rating, 2) AS rating
    FROM shows
    INNER JOIN show_genres sg ON shows.id = sg.show_id
    INNER JOIN genres g ON sg.genre_id = g.id
    WHERE  g.name = '{genre}'
    ORDER BY rating DESC
    LIMIT 10
    """.format(genre=genre)
    return data_manager.execute_select(query)


def get_actors_by_year(year):
    query = sql.SQL("""
    SELECT name,COALESCE(date_part('year',age(now(),birthday)),0) as age
    FROM actors
    INNER JOIN  show_characters sc ON actors.id = sc.actor_id
    INNER JOIN shows as s ON s.id = sc.show_id
    GROUP BY actors.id,s.year
    HAVING date_part('year',s.year) = {year}
    ORDER BY age DESC
    """).format(year=sql.Literal(year))
    return data_manager.execute_select(query)
