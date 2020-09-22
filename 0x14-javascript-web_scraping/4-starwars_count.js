#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
    const films = JSON.parse(body).results;
    let c = 0;
    for (const data of films) {
      for (const str of films[data].characters) {
        if (films[data].characters[str],includes('18')) {
          c += 1;
        }
      }
    }
    console.log(c);
});
