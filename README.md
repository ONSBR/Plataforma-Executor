# Plataforma-Executor

#### Introdução
O módulo executor é responsável pela execução dos processos de negócio acionados apartir de um evento dos sistema.
O eventmanager identifica que existe uma operação de um processo que espera que ocorra um determinado evento para ser executado. 
Desta forma, quando o eventmanager recebe o evento esperado pelo o executor, este encaminha para que o executor possa chamar o processo.

##### Responsabilidades do executor
O executor é reponsável por receber os eventos de negócio, identificar qual o processo que espera por esse evento, e executar.
Para iniciar a execução o executor precisa recuperar os dados dos mapas esperados pelos processos, instânciar o processo, armazenar na memória desse processo, 
e então disparar a execução.
O executor também é responsável por receber os eventos de sistema (reprodução, reprocessamento...), realizar os tratamentos necessários, e então chamar os processos
relacionados.

#### Estrutura do Projeto

OBS: Foi criada uma versão de teste em javascript para ser utilizada em testes integrados, enquanto o executor ainda não estava pronto. 
Esta versão foi criada na pasta "js" no branch específico.

No projeto podemos encontrar os seguintes arquivos:
* [js/app.js]: disponibiliza os serviços de execução de processos.
* [js/config.js]: contém as configurações do executor

#### Requisitos

Para executar o gerenciador com sucesso você precisa instalar as seguintes ferramentas:
* [NodeJS](https://nodejs.org)
* NPM (vem junto com o NodeJS)
* [Docker](https://www.docker.com/)
* Docker compose

### Para instalar ou atualizar as dependências é necessário executar o comando:
npm install


Caso queira executar o servidor sem utilizar o docker, tem um script no projeto Plataforma-SDK, em:
Plataforma-SDK/_scripts/shell/start-executor.sh

Se você estiver utilizando o windows, é necessário executar o powersheel no modo terminal.

Caso você opte por usar o docker você pode subir com o seguinte comando:
```sh
$ docker-compose up -d
```
Ao executar esse comando o docker irá subir um container com o executor inicializado.

Após a subida dos containers você pode enviar deve acessar o eventmamanger pelo endereço:
http://localhost:8085/executor

Example:
Url: http://localhost:8085/executor
Http Method: POST

    Body: 
        Business Event: {"name":"account.put","processName":"cadastra-conta","payload":{"id":0,"titular":"fernando","saldo":100},"origem":"38913f27-b09c-4240-b13b-b46db0e52591"}
        System Event: {"name":"system.event.reproduction","payload":{"instanciaOriginal":"f6648fdb-6d5a-79d8-5852-0a2d892e9a3c"}}





