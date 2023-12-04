#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

// Check if the movie ID is provided
if (!movieId) { console.error('Usage: ./3-starwars_title.js <movie-id>'); process.exit(1); }

// Construct the URL for the Star Wars API
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) { console.error(error); process.exit(1); }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Check if the movie data is valid
  if (response.statusCode === 200 && movieData.title) { console.log(movieData.title); } else { console.error('Movie not found.'); }
});
