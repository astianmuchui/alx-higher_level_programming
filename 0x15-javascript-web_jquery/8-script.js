#!/usr/bin/node

// fetches and lists the title for all movies by
// using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  for (let movie of data.results) {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  }
});
