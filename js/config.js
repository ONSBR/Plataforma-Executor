var config = {};

config.PORT = 8085;

const processMemoryHost = process.env.PROCESS_MEMORY_HOST || "localhost";

config.pathExecuteWorker = "../../worker/run.js";
config.processMemoryUrl = "http://" + processMemoryHost + ":9091/";

module.exports = config;