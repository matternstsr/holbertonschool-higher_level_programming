#!/usr/bin/node

// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Using the jQuery API by selecting toogle header
  const toggleHeaderDiv = $('#toggle_header');

  // use the click event handler
  toggleHeaderDiv.click(function () {
    // Select the headar
    const headerElement = $('header');

    // add a toggle the class between red and green
    headerElement.toggleClass('red green');
  });
});
