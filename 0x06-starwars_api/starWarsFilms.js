#!/usr/bin/node
"use strict";

const request = require("request");
const movieId = process.argv[2];

request(
  `https://swapi-api.alx-tools.com/api/films/${movieId}/`,
  (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const data = JSON.parse(body);
      const characters = data.characters;

      characters.forEach((character) => {
        request(character, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }
        });
      });
    }
  }
);
