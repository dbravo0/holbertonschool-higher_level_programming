#!/usr/bin/node
const counter = parseInt(process.argv[2]);
if (isNaN(counter)) {
  console.log('Missing size');
} else {
  for (let idx = 0; idx < counter; idx++) {
    console.log('X'.repeat(counter));
  }
}
