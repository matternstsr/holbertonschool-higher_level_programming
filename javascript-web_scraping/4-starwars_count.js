#!/usr/bin/node
const request = require('request');

// Geting the API URL from the command line argument
const apiUrl = process.argv[2];

// Checking if the API URL is provided
if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <api-url>');
  process.exit(1);
}

// Setting the char for ID for Wedge Antilles
const wedgeAntillesId = 18;

// Making a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  // Parsing the JSON response
  const filmsData = JSON.parse(body);

  // Filtering movies where Wedge Antilles
  const moviesWithWedge = filmsData.results.filter((film) => {
    return film.characters.includes(`https://swapi-api.hbtn.io/api/people/${wedgeAntillesId}/`);
  });

  // Display the count of movies with Wedge Antilles
  console.log(moviesWithWedge.length);
});
