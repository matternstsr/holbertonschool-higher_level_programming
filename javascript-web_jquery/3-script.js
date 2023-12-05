#!/usr/bin/node

// Wait for the DOM load
$(document).ready(function () {
  // use the click event handler
  $('DIV#red_header').click(function () {
    // add the class "red" to i the header that is chosen
    $('HEADER').addClass('red');
  });
});
