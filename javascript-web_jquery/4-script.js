#!/usr/bin/node

// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // use the click event handler
  $('DIV#toggle_header').click(function () {
    // add a toggle the class between red and green
    $('header').toggleClass('red green');
  });
});
