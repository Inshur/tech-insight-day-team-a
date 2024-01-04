const { Router } = require('express');
const cors = require('cors');

const middleware = Router();

// Setup cors
middleware.use(cors());

module.exports = middleware;
