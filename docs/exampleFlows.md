# Example Flows — Movie Tracker

Three example user flows showing how the endpoints in APISpec.md come together.

## Flow 1 — Signing Up and Saving a New Favorite

Priya just watched Inception for the first time and loved it. She decides to start keeping a list of films she has seen, so she signs up for Movie Tracker and saves Inception as her first entry.

She calls POST /users/register with her username, email, and password. The server hands back her new user_id of 1042.

{ "user_id": 1042, "username": "priya_watches" }

She logs in via POST /users/login to get a session token, then searches the external catalog with GET /movies/external/search?title=inception&year=2010. One match comes back with external_id tt1375666.

Inception isn't in our database yet, so her client calls POST /movies with body { "external_id": "tt1375666" }. The server imports it and assigns movie_id 317.

Finally, she adds it to her collection by calling POST /users/1042/collection/317 with body { "watched": true }.

{ "user_id": 1042, "movie_id": 317, "watched": true, "rating": null }

Priya is set up and can rate it whenever she's ready.

## Flow 2 — Picking a Top Sci-Fi Film to Recommend

Marcus wants to recommend a sci-fi film to his partner tonight, but first he needs to finish rating Arrival, which he watched last week.

He logs in with POST /users/login (user_id 2058) and then rates Arrival by calling PUT /users/2058/collection/402 with body { "rating": 8.5, "watched": true }.

{ "user_id": 2058, "movie_id": 402, "rating": 8.5, "watched": true }

With that out of the way, he pulls up his top sci-fi picks by calling GET /users/2058/collection?genre=Science%20Fiction&min_rating=8&sort_by=rating&order=desc.

{
  "collection": [
    { "movie_id": 317, "title": "Inception", "rating": 9.5, "release_year": 2010 },
    { "movie_id": 402, "title": "Arrival",   "rating": 8.5, "release_year": 2016 }
  ]
}

Inception is at the top, so Marcus calls GET /movies/317 to double-check the runtime before hitting play.

## Flow 3 — Tidying Up a Director Shelf

Lina has been on a Denis Villeneuve kick and wants to clean up her library: add Blade Runner 2049, drop Dune: Part One, and see the end result.

She logs in via POST /users/login (user_id 3311) and searches for Blade Runner 2049 with GET /movies/external/search?title=blade%20runner%202049. She finds it with external_id tt1856101.

Since it isn't in our database yet, she calls POST /movies with body { "external_id": "tt1856101" } and gets back movie_id 511. She adds it to her collection via POST /users/3311/collection/511 with body { "watched": true }, then rates it with PUT /users/3311/collection/511 and body { "rating": 9.0 }.

{ "user_id": 3311, "movie_id": 511, "rating": 9.0, "watched": true }

Dune: Part One no longer feels like a favorite, so she drops it with DELETE /users/3311/collection/489.

Finally she checks the updated shelf with GET /users/3311/collection?director=Denis%20Villeneuve&sort_by=release_year&order=asc.

{
  "collection": [
    { "movie_id": 402, "title": "Arrival",           "release_year": 2016, "rating": 8.5 },
    { "movie_id": 511, "title": "Blade Runner 2049", "release_year": 2017, "rating": 9.0 }
  ]
}

Her Villeneuve shelf now matches her current taste.
