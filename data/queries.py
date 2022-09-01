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
    SELECT s.title as title,
       date_part('year',s.year) as starting_date,
       ROUND(s.rating,1) as rating
        FROM shows s
        INNER JOIN show_genres sg on s.id = sg.show_id
        INNER JOIN genres g on sg.genre_id = g.id
        WHERE g.name = '{genre}'
        ORDER BY rating DESC
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


def get_shows_rating_by_year():
    query = """
    SELECT EXTRACT(YEAR FROM s.year) as year,
    ROUND(AVG(s.rating),1) as rating,
    COUNT(s.rating) as count_shows
    FROM shows s
    WHERE date_part('year',s.year) BETWEEN 1970 AND 2010
    GROUP BY s.year
    """
    return data_manager.execute_select(query)


def get_all_shows_more_than_10ep():
    query = """
    SELECT sh.title AS title,
       STRING_AGG(DISTINCT g.name, '/' ) AS genres,
       COUNT(DISTINCT s.id) AS number_of_season,
       EXTRACT(YEAR FROM sh.year) AS year,
       COALESCE(sh.homepage,'No URL') AS website
    FROM shows sh
        INNER JOIN seasons s ON sh.id = s.show_id
        INNER JOIN episodes e ON s.id = e.season_id
        INNER JOIN show_genres sg ON sh.id = sg.show_id
        INNER JOIN genres g ON sg.genre_id = g.id
    GROUP BY sh.title, sh.homepage, sh.year
    HAVING COUNT(DISTINCT e.id) > 10
    """
    return data_manager.execute_select(query)


def get_shows_by_initial(letter):
    query = sql.SQL("""
       SELECT sh.title AS title,
              sh.year AS year,
              COUNT(DISTINCT e.id) as episode_count,
              COUNT(DISTINCT a.id) as actor_count
       FROM shows sh
             INNER JOIN seasons s ON sh.id = s.show_id
             INNER JOIN episodes e ON s.id = e.season_id
        
             INNER JOIN show_characters sc on sh.id = sc.show_id
             INNER JOIN actors a on sc.actor_id = a.id

       GROUP BY sh.title,sh.year
       HAVING(COUNT(DISTINCT e.id)) > 20 and sh.title LIKE '{letter}%'
       """).format(letter=sql.SQL(letter))
    return data_manager.execute_select(query)
