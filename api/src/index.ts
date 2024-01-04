import 'dotenv/config';
import express from 'express';
import middleware from './middleware';
import routes from './routes';

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
