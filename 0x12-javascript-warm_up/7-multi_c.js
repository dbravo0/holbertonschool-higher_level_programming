#!/usr/bin/node
const argv = process.argv;
const counter = parseInt(argv[2]);
if (isNaN(counter)) {
  console.log('Missing number of occurrences');
} else {
  for (let idx = 0; idx < counter; idx++) {
    console.log('C is fun');
  }
}
