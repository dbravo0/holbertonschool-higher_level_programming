#!/usr/bin/node
const dict = require('./101-data').dict;

const listD = {};
for (const i in dict) {
  if (!(dict[i] in listD)) {
    listD[dict[i]] = [];
  }
  listD[dict[i]].push(i);
}

console.log(listD);
