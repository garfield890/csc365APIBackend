# Example workflow

Priya just watched Dances with Wolves and wants to start tracking movies in Movie Manager. She creates a new user account, searches for Dances with Wolves in the movie database, adds the movie to her watched collection, rates it, and then checks her collection to confirm the saved entry.

This workflow uses the deployed Movie Manager API and the production Supabase database. It includes database-modifying endpoints because registering a user inserts a row into `users`, adding a movie inserts a row into `watched_movies`, and rating the movie updates that row.

# Testing results

## Step 1: Register a new user

1. The curl statement called:

```bash
curl -X 'POST' \
  'https://YOUR-RENDER-URL/users/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "priya_watches",
    "email": "priya@example.com",
    "password": "testpassword123"
  }'