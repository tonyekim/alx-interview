#!/usr/bin/node
const request = require("request");
const movieId = process.argv[2];
const apiUrl = "https://swapi-api.hbtn.io/api/films/" + movieId;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const charactersUrls = JSON.parse(body).characters;
    for (const characterUrl of charactersUrls) {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
