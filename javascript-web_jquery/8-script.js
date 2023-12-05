#!/usr/bin/node

// Wait for the DOM load
$(document).ready(function () {
    // define the url location
    const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
  
    // function thta fetches a list movie titles
    function fetchAndListMovies() {
      // use get to request from the API
      $.get(apiUrl, function (data) {
        // Check if data is there
        if (data.results && data.results.length > 0) {
          // Select the list that we need
          const $listMovies = $('#list_movies');
          // Go through each movie and add its title
          data.results.forEach(function (movie) {
            $listMovies.append('<li>' + movie.title + '</li>');
          });
        } else { console.error('No movie data found'); } });
    }
    // Call to fetch and list movies
    fetchAndListMovies(); });
  