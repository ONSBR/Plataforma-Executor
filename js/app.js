var Client = require('node-rest-client').Client;

var config = require('./config');
var cmd = require('node-command-line');

var Contexto = require("plataforma-core/Contexto");
var DataSet = require("plataforma-core/DataSet");
var CoreRepository = require("plataforma-sdk/services/CoreRepository");


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

  console.log("___ENTER POST EXECUTOR___" + JSON.stringify(req.body));

  //TODO cria o contexto e manda para processmemory
  var evento = req.body;
  var contexto = new Contexto();
  contexto.instancia = evento.instancia;
  contexto.evento = evento;
  contexto.dataSet = new DataSet();

  // TODO ainda não está recuperando o dataset
    
  if (!contexto.instancia) {

    var args = { data: contexto, headers: { "Content-Type": "application/json" } };
  
    contexto.instancia = guid();

    var urlMemoryCreate = config.processMemoryUrl + evento.processName + "/" + contexto.instancia + "/create";

    console.log("urlMemoryCreate: " +urlMemoryCreate);
 
    var client = new Client();
    var reqExec = client.post(urlMemoryCreate, args, function (data, response) {

      var coreRepository = new CoreRepository();
      coreRepository.addProcessInstance(data.instanceId, evento.processName, evento.data);
  
      console.log("Contexto salvo na memória de processo com sucesso." + data.instanceId);
      execute(contexto.instancia);
    });
    reqExec.on('error', function (err) {
      console.log('request error', err);
    });
  } else {
    execute(contexto.instancia);
  }
  
  res.send("OK");
});

function execute(instanceId) {
  var commandLine = "node " + config.pathExecuteWorker + " " + instanceId;
  console.log("commandLine: " + commandLine);
  cmd.run(commandLine);
}

function guid() {
  function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  }
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
    s4() + '-' + s4() + s4() + s4();
}

// Listener
// ===========================================================
app.listen(PORT, function() {
  console.log("App listening on PORT " + PORT);
});