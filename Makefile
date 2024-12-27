flaskexample:
	python -m flask --app flask_examples run --host=0.0.0.0 

run:
	python -m flask --app kafka_example run --host=0.0.0.0 

freeze:
	pip freeze > requirements.txt

kafka kafkastart kafkarun:
	docker compose up -d

stopkafka kafkastop:
	docker compose down

kafkalogs:
	docker logs -f broker

kafkaconnect:
	docker exec -it broker /bin/bash