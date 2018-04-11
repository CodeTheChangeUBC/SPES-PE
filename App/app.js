// express framework setup
var express = require('express');
var app = express();

// use body parser to parse form
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: true}));

// set view engine to ejs
app.set("view engine", "ejs");

// library for writing to excel
var Excel = require('exceljs');
var workbook = new Excel.Workbook();

// library for running python scripts
var PythonShell = require('python-shell');

// Set directory for stylesheet
app.use(express.static(__dirname + '/'))

// Home page
app.get('/', function (req, res) {
  res.render("home.ejs")
})

// POST Request for form
app.post('/', function(req, res) {
  // get data from form
  var testString = req.body.testString;
  console.log(testString);

  // Add data to excel file and call python scripts
  workbook.xlsx.readFile('Test.xlsx')
    .then(function() {
        var worksheet = workbook.getWorksheet(1);
        var row = worksheet.getRow(worksheet.rowCount + 1);
        row.getCell(1).value = testString;
        row.commit();
        return workbook.xlsx.writeFile('Test.xlsx');
      }
    )

    // Run python script
    PythonShell.run('/scripts/test.py', function (err) {
      if (err) throw err;
      console.log('finished');
    });

  // redirect to home page
  res.redirect("/");
})

app.listen(8000, function () {
  console.log('Server Started!');
})
