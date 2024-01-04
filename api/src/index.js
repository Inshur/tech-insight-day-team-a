require('dotenv').config();

const express = require('express');
const middleware = require('./middleware');
const routes = require('./routes');

// Setup debug logger
const debug = require('debug')('welcome-api');

// Create express App
const app = express();

// Setup routes
app.use(middleware);
app.use('/api', routes);

// Listen
app.listen(4000, () => {
  debug('Listening at http://localhost:4000')
});
