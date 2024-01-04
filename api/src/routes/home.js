const { Router } = require('express');

const home = Router();

home.get('/', (request, response) => {
  response.send({
    success: true
  })
});

 module.exports = home;
