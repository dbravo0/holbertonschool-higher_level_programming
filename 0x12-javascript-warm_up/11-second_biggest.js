#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const counter = process.argv.slice(2);
  const num = counter.sort((a, b) => a - b);
  console.log(num[num.length - 2]);
}
