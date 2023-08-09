#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get the Movie ID from the command line argument

if (!movieId) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

// Construct the URL for the Star Wars API films endpoint
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch movie details from the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('API Error:', response.statusCode, response.statusMessage);
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Fetch and print character names
  fetchCharacters(characterUrls);
});

// Fetch and print character names
function fetchCharacters(urls) {
  const promises = urls.map(url =>
    new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    })
  );

  Promise.all(promises)
    .then(characterNames => {
      console.log('Character Names:');
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error fetching character data:', error);
    });
}
