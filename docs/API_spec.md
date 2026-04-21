# API Specification — Movie Tracker

This document describes the endpoints for the Movie Tracker service. The service allows users to create accounts, search for films from an external movie database, curate a personal collection of movies, rate films they have watched, and query their collection by attributes such as genre, director, lead actor, personal rating, and release year.

## 1. Register a New User

POST /users/register

Creates a new user account. Takes a username, email, and password and returns the new user_id.

Example response:

{ "user_id": 1042, "username": "cinemafan42" }

## 2. Log In

POST /users/login

Authenticates an existing user using their username and password, and returns a session token.

Example response:

{ "user_id": 1042, "token": "eyJhbGciOiJIUzI1NiIs..." }

## 3. Search the External Movie Database

GET /movies/external/search

Searches an external movie database for films matching a query. Accepts a title and an optional year. Returns a list of matches with their external_id, title, release year, director, lead actor, and genre.

Example request: GET /movies/external/search?title=inception&year=2010

## 4. Import a Movie into the Personal Database

POST /movies

Copies a movie record from the external database into our internal relational database using its external_id. Returns the movie with a new internal movie_id.

Example response:

{ "movie_id": 317, "title": "Inception", "release_year": 2010 }

## 5. List Movies in the Personal Database

GET /movies

Returns movies that have been imported into our internal database. Supports optional filters for genre, director, lead_actor, and release_year.

Example request: GET /movies?genre=Science%20Fiction&release_year=2010

## 6. Get a Single Movie's Details

GET /movies/{movie_id}

Returns the full record of a single movie stored in our database, including runtime and synopsis.

## 7. Add a Movie to a User's Collection

POST /users/{user_id}/collection/{movie_id}

Adds a movie that exists in our internal database to a user's personal collection. Optionally accepts a watched boolean in the body.

Example response:

{ "user_id": 1042, "movie_id": 317, "watched": true, "rating": null }

## 8. Update a Collection Entry

PUT /users/{user_id}/collection/{movie_id}

Updates a movie entry in the user's collection. Used to rate a film on a scale from 0 to 10 or to update watched status. Accepts optional rating and watched fields.

Example request body:

{ "rating": 9.5, "watched": true }

## 9. Remove a Movie from a User's Collection

DELETE /users/{user_id}/collection/{movie_id}

Removes a movie from the user's collection. The underlying movie record in the internal database is not deleted.

## 10. Query a User's Collection

GET /users/{user_id}/collection

Returns the movies in a user's collection with filtering and sorting. Supports optional query parameters genre, director, lead_actor, release_year, min_rating, max_rating, watched, sort_by, and order.

Example request: GET /users/1042/collection?genre=Science%20Fiction&min_rating=8&sort_by=rating&order=desc

Example response:

{
  "collection": [
    { "movie_id": 317, "title": "Inception", "rating": 9.5, "release_year": 2010 }
  ]
}
