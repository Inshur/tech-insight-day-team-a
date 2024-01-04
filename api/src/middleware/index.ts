import { Router } from 'express';
import cors from 'cors';

const middleware = Router();

// Setup cors
middleware.use(cors());

export default middleware;
