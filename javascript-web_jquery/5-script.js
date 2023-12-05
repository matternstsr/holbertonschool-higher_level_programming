#!/usr/bin/node

$(document).ready(function () {
  // use the click event handler
  $('#add_item').click(function () {
    // Create a new li with "Item" in it?
    const newListItem = $('<li>').text('Item');
    // put li into ul using the class of "my_list"
    $('ul.my_list').append(newListItem);
  });
});
