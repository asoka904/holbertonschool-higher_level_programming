#!/usr/bin/node

const fs = require('fs');
const request = require('request');
request(process.argv[2], (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
