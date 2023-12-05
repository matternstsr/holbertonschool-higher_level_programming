#!/usr/bin/node

// Wait for the DOM load
$(document).ready(function () {
  // function thta fetches a list movie titles
  function fetchAndListMovies () {
    // use get to request from the API
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
      // Check if data is there
      if (data.results && data.results.length > 0) {
        // Go through each movie and add its title
        data.results.forEach(function (movie) {
            $('UL#list_movies').append('<LI>' + movie.title + '</LI>');
        });
      } else { console.error('No movie data found'); }
    });
  }
  // Call to fetch and list movies
  fetchAndListMovies();
});
