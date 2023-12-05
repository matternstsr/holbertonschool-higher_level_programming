#!/usr/bin/node

$(document).ready(function () {
  // use the click event handler
  $('DIV#add_item').click(function () {
    // put li into ul using the class of "my_list"
    $('UL.my_list').append('<LI>Item</LI>');
  });
});
