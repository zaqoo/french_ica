import * as React from 'react';
import ReactDOM from 'react-dom';
import Button from '@mui/material/Button';
var path = require('path');
const express = require("express");


function App() {
  return <Button variant="contained">Hello World</Button>;
}
const app = document.querySelector('#app')

app.use(express.static(__dirname));

app.get("/*", function(req, res) {
  res.sendFile(path.join(__dirname, "index.html"));
});

ReactDOM.render(<App />, app);