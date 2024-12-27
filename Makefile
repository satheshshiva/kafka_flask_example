run:
	python -m flask --app flask_examples run --host=0.0.0.0 

freeze:
	pip freeze > requirements.txt

kafka:
	docker compose up -d

kafkalogs:
	docker logs -f kafka