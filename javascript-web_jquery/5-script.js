#!/usr/bin/node

$(document).ready(function () {
  // use the click event handler
  $('#add_item').click(function () {
    // put li into ul using the class of "my_list"
    $('ul.my_list').append($('<li>').text('Item'));
  });
});
