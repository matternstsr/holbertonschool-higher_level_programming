#!/usr/bin/node

// Wait for the DOM load
$(document).ready(function () {
  // Using the jQuery API by selecting red header
  const redHeaderDiv = $('#red_header');

  // use the click event handler
  redHeaderDiv.click(function () {
    // add the class "red" to i the header that is chosen
    $('header').addClass('red');
  });
});
