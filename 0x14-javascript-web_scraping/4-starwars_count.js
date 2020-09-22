#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const films = JSON.parse(body).results;
  let c = 0;
  for (const data in films) {
    for (const str in films[data].characters) {
      if (films[data].characters[str].includes('18')) {
        c += 1;
      }
    }
  }
  console.log(c);
});
