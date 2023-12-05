#!/usr/bin/node

// Wait for the DOM load
document.addEventListener("DOMContentLoaded", function () {
    // Select the headerelement using document.querySelector
    var headerElement = document.querySelector("header");
  
    // Update the text color to red (#FF0000)
    headerElement.style.color = "#FFF000";
  });
  