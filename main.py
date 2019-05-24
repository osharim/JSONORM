# encoding: utf-8
# @osharim
from utils.db import Connection


def main():

    # Craete a new connection to our JSON file as a DB
    movies = Connection('movies-database-v2.json')

    # ----------------
    # Clasification by:
    # ----------------

    # ----------------
    # Popularity (top - down)
    # ----------------
    # We calculate 'popularity' with the sum of ratings assigned to each movie.
    # Get 10 last movies ordered by ratings
    ordered_by_popularity = movies.queryset.order_by('ratings')[:10]

    # Similar movies (same genres and/or IMDB rating, similar cast/actors... genres should have more weight)
    # Get only the last 5 moviees with higher IMDB Rank; Ordered from Higher to lowere
    ordered_by_imdb_rating = movies.queryset.order_by('imdbRating')[:5]

    # ----------------
    # Classify by Same actors
    # ----------------
    classified_by_actors = movies.queryset.group_by('actors')

    # ----------------
    # Also we include a <Filtering method built-in as Django does>
    # ----------------

    # ----------------
    # Filter db by Actors
    # ----------------
    classified_by_actors = movies.queryset.filter(
        actors=['Ryan Reynolds', 'William Ackman'])

    # ----------------
    # Filtere db by genres
    # ----------------
    classified_by_genres = movies.queryset.filter(genres=['Horror', 'Sci-Fi'])

    print(ordered_by_imdb_rating)


if __name__ == "__main__":
  main()
