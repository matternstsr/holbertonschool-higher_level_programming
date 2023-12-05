#!/usr/bin/node

// Wait for the DOM load
$(document).ready(function () {
  // use the click event handler
  $('DIV#red_header').click(function () {
    // Update the text color to red
    $('HEADER').css('color', '#FF0000');
  });
});
