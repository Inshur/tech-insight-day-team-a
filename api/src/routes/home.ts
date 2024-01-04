import { Router, Request, Response } from 'express';

const home = Router();

home.get('/', (request: Request, response: Response) => {
  response.send({
    success: true
  })
});

export default home;
