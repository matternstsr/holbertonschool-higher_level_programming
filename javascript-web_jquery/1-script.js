#!/usr/bin/node

// Wait for the DOM load
$(document).ready(function () {
    // Select the headerelement using the jQuery API
    var headerElement = ("header");
  
    // Update the text color to red (#FF0000)
    headerElement.css("color", "#FF0000");
  });
  