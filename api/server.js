'use strict';

const express = require('express');

// Constants
const PORT = 8080;

// App
const app = express();
app.get('/', function (req, res) {
    res.send('I\'m a node API for Gary. What are you doing there?\n');
});

app.listen(PORT);
console.log('Running on http://localhost:' + PORT);
