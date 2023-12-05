#!/usr/bin/node

// Wait for the DOM load
$(document).ready(function () {
  // use the click event handler
  $('DIV#update_header').click(function () {
    // update the text for the chosen header
    $('header').text('New Header!!!');
  });
});
