#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    console.log(films.reduce((cnt, el) => {
      el.characters.forEach(e => {
        if (e.includes('18')) {
          cnt++;
        }
      });
      return cnt;
    }, 0));
  }
});
