freeze:
	@pip freeze > requirements.txt

test:
	@pytest runner
