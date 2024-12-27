## Setting Up the Virtual Environment
1. Create a virtual environment:
```
 python3 -m venv venv
 source venv/bin/activate
 python3 -m pip install -r requirements.txt
```
2. To activate the virtual environment everytime you run the project, use the command,
```
 source venv/bin/activate
 ```
3. Use the pip freeze command, if you have updated dependecies and if you to write them to `requirements.txt`
```
python3 -m pip freeze > requirements.txt
```

## Run local instance of kafka
1. Ensure docker is installed.
1. Run the command `docker compose up -d`

## Run the Kafka example application
1. Use the command,  
`python -m flask --app kafka_example run --host=0.0.0.0`
1. Then navigate to,  
`http://localhost:5000/produce?value=something5`
1. In another tab keep refreshing  
`http://localhost:5000/consume`  
to receive the message

## Run the Flask example application
1. Use the command,  
`python -m flask --app flask_examples run --host=0.0.0.0`
1. Then navigate to,  
`http://localhost:5000/`
1. Navigate to the different controllers from browser