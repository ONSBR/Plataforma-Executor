var config = require('./config');
var cmd = require('node-command-line');

// Dependencies
// ===========================================================
var express = require("express");
var bodyParser = require("body-parser");

// Configure the Express application
// ===========================================================
var app = express();
var PORT = config.PORT;

// Set up the Express application to handle data parsing
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

/**
 * Recebe os eventos para serem enviados ao executor,
 * por enquanto está sendo feito um curto circuito e enviando 
 * diretamente para o executor na URL configurada.
 */
app.post("/executor", function(req, res) {

  console.log("___ENTER POST EVENT___" + JSON.stringify(req.body));

  var commandLine = "node " + config.pathExecuteWorker + " " + req.body.name;
  console.log("commandLine: " + commandLine);
  cmd.run(commandLine);
  
  res.send("OK");
});


// Listener
// ===========================================================
app.listen(PORT, function() {
  console.log("App listening on PORT " + PORT);
});