const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send('Hello Everyone, This is Tanvir from DevOps bootcamp');
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
