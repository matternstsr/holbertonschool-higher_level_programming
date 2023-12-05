#!/usr/bin/node

  // Wait for the DOM content to be fully loaded
$(document).ready(function () {
    // Using the jQuery API by selecting toogle header
    var toggleHeaderDiv = $("#toggle_header");
  
    // use the click event handler
    toggleHeaderDiv.click(function () {
      // Select the headar
      var headerElement = $("header");
  
      // add a toggle the class between red and green
      headerElement.toggleClass("red green");
    });
  });