#!/usr/bin/node

// Wait for the DOM load
$(document).ready(function () {
  // define the url location
  const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  // using AJAX to fetch the requested data from defined api
  $.ajax({
    url: apiUrl,
    method: 'GET',
    success: function (data) {
      // find the charactre that we needed
      const characterName = data.name;

      // update the text for the chosen header
      $('#character').text(characterName);
    }
  });
});
