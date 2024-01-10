#!/usr/bin/node

// Change the color of the HTML tag HEADER to red (#FF0000):
// When DIV#red_header is clicked Using the JQuery API

$('DIV#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
