freeze:
	@pip freeze > requirements.txt

test:
	@pytest -s runner

install:
	@docker build -t plataforma-runner .
	@docker run -d -p 5000:5000 --name plataforma-registry registry:2
	@docker run -d -p 8000:8000 --name plataforma-runner plataforma-runner 

run:
	@docker start plataforma-registry plataforma-runner

stop:
	@docker stop plataforma-registry plataforma-runner

destroy: stop
	@docker rm plataforma-runner plataforma-registry
	@docker rmi plataforma-runner registry:2
