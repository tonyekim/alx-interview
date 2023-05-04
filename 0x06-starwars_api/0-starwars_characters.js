#!/usr/bin/node

/* Enables strict mode which catches common coding mistakes & throw more errors */
"use strict";

/* Importing the request module */
const request = require("request");

/* Store movie ID from command line arguments */
const movieId = process.argv[2];

/* Sends an HTTP GET request SWAPI's /films/ endpoint using `request` module */
request(
  `https://swapi-api.alx-tools.com/api/films/${movieId}/`,
  (error, response, body) => {
    /* Check for and handles errors in the HTTP request */
    if (error) {
      console.error(error);
    } else {
      /* Parses the response body into a JS obj & retrieve the `character` prop */
      const data = JSON.parse(body);
      const characters = data.characters; // Array of URLs to the chars in movie
      respRequestReturn(characters, 0);
    }
  }
);

/* Makes an HTTP GET request for the character data at the given URL */
function respRequestReturn(character, idx) {
  request(character[idx], (error, response, body) => {
    /* Parses the response body into a JS obj & retrieves the `name` prop of the char */
    if (error) {
      console.error(error);
    } else {
      const characterData = JSON.parse(body);

      /* Logs the character name to the console */
      console.log(characterData.name);

      /* Recursively calls itself with the next character index if there are more characters to process */
      if (idx + 1 < character.length) respRequestReturn(character, ++idx);
    }
  });
}
