#!/usr/bin/node

// Wait for the DOM load
$(document).ready(function () {
    // Using the jQuery API by selecting red header
    var redHeaderDiv = $("#red_header");
  
    // use the click event handler
    redHeaderDiv.click(function () {
      // Update the text color to red
      $("header").css("color", "#FF0000");
    });
  });
  