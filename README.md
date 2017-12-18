# Engine de execução de processos da plataforma.


#### Installation


[Docker](https://www.docker.com) is the fastest way to run the app. If you don have docker installed, please refer to the
[Project Documentation](https://docs.docker.com/engine/installation/)

#### Building and starting the application container:

    $ make install

> The application will be up and running inside a new Docker Container named plataforma-runner.


#### Stopping container:

	$ make stop
    
  
#### Removing container and image:
	
    $ make destroy

	
#### Basic configuration and use:

The rest api will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)
