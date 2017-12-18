# Engine de execução de processos da plataforma.


### Installation using Docker

[Docker](https://www.docker.com) is the fastest way to run the app. If you don have docker installed, please refer to the
[Project Documentation](https://docs.docker.com/engine/installation/) or just:

    $ curl -fsSL get.docker.com -o get-docker.sh
    $ sh get-docker.sh

#### Building and starting the application container:

    $ make install

> The application will be up and running inside a new container named plataforma-runner.


#### Stopping the container:

    $ make stop
    
  
#### Removing the container and image:
	
    $ make destroy
    
    
#### Starting the container:
   
    $ make run
   
> The rest api will be listening at [http://127.0.0.1:8000](http://127.0.0.1:8000)
   
   
### Installation for development:

> It's highly recommended to install the application inside a virtual enviroment. If you don't know what I'm talking about please take sometime to [check](https://virtualenv.pypa.io/en/stable/).

Once set, activate your virtual enviroment and inside the project directory, type:

    $ pip install -r requirements.txt
    
    
#### Executing tests:

    $ make test



