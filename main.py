import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request, jsonify

from data import queries

app = Flask('codecool_series')
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows/most-rated')
def display_most_rated_shows():
    return render_template('most_rated_shows.html')


@app.route('/api/top15-shows')
def handle_most_rated_shows():
    return jsonify(queries.get_top15_rated_shows())


# PA Practices


# 1
@app.route('/stars_for_the_stars')
def display_stars_for_the_stars():
    return render_template('stars_for_the_stars.html')


@app.route('/api/get_genre')
def handle_genre():
    genre = request.args.get('genre')
    return jsonify(queries.stars_for_the_stars(genre))


# 2
@app.route('/what_a_year')
def display_what_a_year():
    shows = queries.get_shows_rating_by_year()
    return render_template('what_a_year.html',show=shows)


@app.route('/api/shows_yearly_rating')
def handle_shows_yearly_rating():
    return jsonify(queries.get_shows_rating_by_year())


@app.route('/young_actors_in_old_shows')
def young_actors_in_old_shows():
    return render_template('young_actors_in_old_shows.html')


@app.route('/api/actors_played_in_year')
def get_actor_year():
    year = request.args.get('year')
    return jsonify(queries.get_actors_by_year(year))


# Robertino
@app.route('/api/shows', methods=['POST'])
def get_shows():
    payload = request.get_json()
    print(payload['title'])
    print(payload['year'])
    print(payload['rating'])
    # insert to db,
    # id of the inserted row,
    # insert
    new_id = 38000
    return {'id': new_id, 'title': payload['title'], 'year': payload['year'], 'rating': payload['rating']}


def main():
    load_dotenv(find_dotenv())
    app.run(port=os.getenv('FLASK_RUN_PORT'),
            host=os.getenv('FLASK_RUN_HOST'), )
    app.run()


if __name__ == '__main__':
    main()
