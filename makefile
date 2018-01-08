freeze:
	@pip freeze > requirements.txt

test:
	@pytest -s

install:
	@docker-compose up -d

run: install

up: install

stop:
	@docker-compose stop 
	
destroy: 
	@docker-compose down
