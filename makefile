freeze:
	@pip freeze > requirements.txt

test:
	@pytest runner

install:
	@docker build -t plataforma-runner .
	@docker run -d -p 8000:8000 --name plataforma-runner plataforma-runner 

run:
	@docker start plataforma-runner

stop:
	@docker stop plataforma-runner

destroy: stop
	@docker rm plataforma-runner
	@docker rmi plataforma-runner
