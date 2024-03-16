// server.js

const express = require('express');
const { add, multiply } = require('./app');

const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send('Hello Docker!');
});

app.get('/add/:num1/:num2', (req, res) => {
  const { num1, num2 } = req.params;
  const result = add(parseInt(num1), parseInt(num2));
  res.send(`Addition Result: ${result}`);
});

app.get('/multiply/:num1/:num2', (req, res) => {
  const { num1, num2 } = req.params;
  const result = multiply(parseInt(num1), parseInt(num2));
  res.send(`Multiplication Result: ${result}`);
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
