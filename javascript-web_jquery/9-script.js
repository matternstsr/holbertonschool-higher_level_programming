#!/usr/bin/node

$(document).ready(function () {
    // Fetch data in the new lang
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
      type: 'GET',
      success: function (data) {
        // Once the data is fetched successfully, update the content of DIV#hello
        $('#hello').text(data.hello);
      },
    });
  });
  