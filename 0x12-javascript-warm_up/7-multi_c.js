#!/usr/bin/node
// prints x times “C is fun”

const x = parseInt(process.argv[2]);
if (x) {
  for (let i = 1; i <= x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
