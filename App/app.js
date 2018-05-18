// express framework setup
var express = require('express');
var app = express();

// use body parser to parse form
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

// set view engine to html
app.use(express.static(__dirname + '/views'));

// library for running python script
var PythonShell = require('python-shell');

// home page
app.get('/', function (req, res) {
  res.sendFile('landing.html',  {"root": __dirname + '/views'});
})

// POST Request for form
app.post('/form', function(req, res) {

  // get data from form
  var data = JSON.stringify(req.body);
  console.log(data);

  // Set options for python script call
  var options = {
    mode: 'json',
    args: [data]
  }

  // Run python script
  PythonShell.run('/scripts/test.py', options, function (err, results) {
    if (err) throw err;
    var returnJSON = results[0];
    res.send(returnJSON);
   });
})

// set port to localhost:8000
app.listen(8000, function () {
  console.log('Server Started!');
})
