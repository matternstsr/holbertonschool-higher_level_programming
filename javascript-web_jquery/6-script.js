#!/usr/bin/node

// Wait for the DOM load
$(document).ready(function () {
    // Using the jQuery API by selecting toogle header
    var updateHeaderDiv = $("#update_header");
  
    // use the click event handler
    updateHeaderDiv.click(function () {
      // update the text for the chosen header
      $("header").text("New Header!!!");
    });
  });
  