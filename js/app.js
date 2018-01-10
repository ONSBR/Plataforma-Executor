var Client = require('node-rest-client').Client;

var config = require('./config');
var cmd = require('node-command-line');

var Contexto = require("plataforma-core/Contexto");
var DataSet = require("plataforma-core/DataSet");
var Reproducao = require("plataforma-core/Reproducao");
var CoreRepository = require("plataforma-sdk/services/CoreRepository");
var utils = require("plataforma-sdk/utils");


// Dependencies
// ===========================================================
var express = require("express");
var bodyParser = require("body-parser");

// Configure the Express application
// ===========================================================
var app = express();
var PORT = config.PORT;

const eventReproduction = "reproduction";

var coreRepository = new CoreRepository();

// Set up the Express application to handle data parsing
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Add headers
app.use(function (req, res, next) {
  
      // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', '*');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', false);

    // Pass to next layer of middleware
    next();
});


app.get("/executor", function(req, res) {
  res.send("OK");
});

// TODO temporário até a api do core ser toda obtida via serviço, pois a base local está apresentando erro no presentation
app.get("/comparereproduction/:reproductionId", function(req, res) {
  
  var reproductionId = req.params.reproductionId;

  console.log("___ENTER PUT REPRODUCTION___" + reproductionId); 

  var reproducao = coreRepository.getReproduction(reproductionId);

  var processInstance = coreRepository.getProcessInstance(reproducao.instanciaOriginal);

  var args = { headers: { "Content-Type": "application/json" } };

  var urlGetProcessMemoryOriginal = config.processMemoryUrl + processInstance.processo + "/" + reproducao.instanciaOriginal + "/history";
  var client = new Client();

  var memoriasOriginal = null;

  var reqMemoriasOriginal = client.get(urlGetProcessMemoryOriginal, function (data, response) {
    
      var memoriasOriginal = data;

      var urlGetProcessMemoryReproc = config.processMemoryUrl + processInstance.processo + "/" + reproducao.instanciaReproducao + "/history";
      
      var reqMemoriasReproc = client.get(urlGetProcessMemoryReproc, function (data, response) {
          
          var memoriasReproc = data;
          
          var retorno = { memoriaProcessoOriginal: memoriasOriginal, memoriaProcessoReproducao: memoriasReproc};
          retorno.jsonMemoryOrigem
      
          res.send(retorno);

      });
      reqMemoriasReproc.on('error', function (err) {
          console.log('request error', err);
      });

  });
  reqMemoriasOriginal.on('error', function (err) {
      console.log('request error', err);
  });

});


/**
 * Recebe os eventos para serem enviados ao executor,
 * por enquanto está sendo feito um curto circuito e enviando 
 * diretamente para o executor na URL configurada.
 */
app.post("/executor", function(req, res) {

  console.log("___ENTER POST EXECUTOR___" + JSON.stringify(req.body));

  //TODO cria o contexto e manda para processmemory
  var evento = req.body;

  var systemEvent = utils.getSystemEvent(evento.name);
  if (systemEvent == eventReproduction) {
    executeReprodutionEvent(evento);
  } else {
    executeBusinessEvent(evento);
  }
  
  res.send("OK");
});

function executeReprodutionEvent(evento) {

  var repData = evento.payload;
  if (repData.instanciaOriginal) {
    executeReprodutionByInstance(repData.instanciaOriginal);
  } else {
    var entidadeId = repData.entidadeId;
    var entidadeType = repData.entidadeType;

    // TODO obtém a instância apartir dos dados da entidade
  }

}

function executeReprodutionByInstance(instanceId, evento) {

  var instance = coreRepository.getProcessInstance(instanceId);
  console.log("___instance___" + instanceId + "/ " + JSON.stringify(instance));
  var processName = instance.processo;

  var urlGetProcessMemory = config.processMemoryUrl + processName + "/" + instanceId + "/first";
  var client = new Client();

  client.get(urlGetProcessMemory, function (data, response) {
    
    var contexto = data;
    var eventoReproducao = contexto.evento;

    var instanciaOriginal = eventoReproducao.instancia;

    var instanciaReproducao = guid();
    var reproducaoId = guid();
    
    eventoReproducao.reproducao = reproducaoId;
    eventoReproducao.instancia = instanciaReproducao;

    contexto.eventoSaida = null;
    contexto.instancia = instanciaReproducao;

    var reproducao = new Reproducao(reproducaoId, instanciaOriginal, instanciaReproducao, new Date(), eventoReproducao.responsavel);

    var urlMemoryCreate = config.processMemoryUrl + processName + "/" + contexto.instancia + "/create";
    
    console.log("urlMemoryCreateReprocess: " +urlMemoryCreate);
    
    var args = { data: contexto, headers: { "Content-Type": "application/json" } };

    var reqExec = client.post(urlMemoryCreate, args, function (data, response) {

      coreRepository.addProcessInstance(contexto.instancia, eventoReproducao.processName, eventoReproducao.data, eventoReproducao.responsavel, reproducaoId);

      coreRepository.addReproduction(reproducao);

      console.log("Contexto salvo na memória de processo com sucesso." + contexto.instancia);
      execute(contexto.instancia);
    });
    reqExec.on('error', function (err) {
      console.log('request error', err);
    });

  });

}

function executeBusinessEvent(evento) {
  
  var contexto = new Contexto();
  contexto.instancia = evento.instancia;
  contexto.evento = evento;
  contexto.dataDeReferencia = evento.dataRef;
  contexto.dataSet = new DataSet();

  // TODO ainda não está recuperando o dataset
  if (!contexto.instancia) {
    
    var args = { data: contexto, headers: { "Content-Type": "application/json" } };
  
    contexto.instancia = guid();
    evento.instancia = contexto.instancia;

    var urlMemoryCreate = config.processMemoryUrl + evento.processName + "/" + contexto.instancia + "/create";

    console.log("urlMemoryCreate: " +urlMemoryCreate);
  
    var client = new Client();
    var reqExec = client.post(urlMemoryCreate, args, function (data, response) {

      coreRepository.addProcessInstance(contexto.instancia, evento.processName, evento.data, evento.responsavel);
  
      console.log("Contexto salvo na memória de processo com sucesso." + contexto.instancia);
      execute(contexto.instancia);
    });
    reqExec.on('error', function (err) {
      console.log('request error', err);
    });
  } else {
    execute(contexto.instancia);
  }

}

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