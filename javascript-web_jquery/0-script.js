#!/usr/bin/node

// Wait for the DOM load
document.addEventListener('DOMContentLoaded', function () {
  // Select the headerelement using document.querySelector
  const headerElement = document.querySelector('header');

  // Update the text color to red (#FF0000)
  headerElement.style.color = '#FF0000';
});
