#!/usr/bin/node

// Wait for the DOM load
$(document).ready(function () {
  // using AJAX to fetch the requested data from defined api
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    method: 'GET',
    success: function (data) {
      // update the text for the chosen header
      $('#character').text(data.name);
    }
  });
});
