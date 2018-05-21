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

// library for logging errors, added with time stamp
const SimpleNodeLogger = require('simple-node-logger'),
opts = {
	logFilePath:'errorLog.log',
	timestampFormat:'YYYY-MM-DD HH:mm:ss.SSS'
},
log = SimpleNodeLogger.createSimpleLogger(opts);
log.setLevel('warn');

// home page
app.get('/', function (req, res) {
	res.sendFile('landing.html',  {"root": __dirname + '/views'});
})

// POST Request for form
app.post('/form', function(req, res) {

	// get data from form
	var data = JSON.stringify(req.body);

	// Set options for python script call
	var options = {
		mode: 'json',
		args: [data]
	}

	var pyshell = new PythonShell('scripts/script.py',options);

	pyshell.on('message', function (message) {
    console.log('messege: '+message);
		res.send(message);
	});

	// end the input stream and allow the process to exit
	pyshell.end(function (err,code,signal) {
		if (err) {
			log.error(err + '\n');
			res.redirect("views/error.html");
		}
		console.log('The exit code was: ' + code);
		console.log('The exit signal was: ' + signal);
		console.log('finished');
		console.log('finished');
	});
})

// set port to localhost:8000
app.listen(8000, function () {
	console.log('\n\n\n\n\n\n                                      =========================================\n')
	console.log('                                                  Code the Change UBC ')
	console.log('\n                   Website: https://codethechangeubc.org  ~  Email: codethechangeubc@gmail.com')
	console.log('\n                                                     Developers:\n')
	console.log('                               Karim Eldegwy, Ahmed Abdelmoniem, Nadim Abdelaziz ,Seif Ghazi\n')
	console.log('                                  ================================================\n')
	console.log('\n                                         Server has sucessfully Started!');
	console.log('\n                             Quitting this window , forcibly shuts down the server');
})
