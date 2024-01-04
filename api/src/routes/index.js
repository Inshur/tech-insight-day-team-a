const { Router } = require('express');
const home = require('./home');

const routes = Router();

routes.use('/', home);

module.exports = routes;
