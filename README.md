# Dockerized Application and API Testing Framework

This repository contains a Dockerized Python HTTP application with two REST APIs, along with a testing framework implemented using pytest. 
The testing framework allows developers to easily add and run tests for the provided APIs.

### Requirements ###

Tested on MAC OS in respect to HTTP port number 5000.
This port is subject to be used in "Airdrop" service so you may want to disable it.

### Docker Container ###

The Docker container includes a Python HTTP application (app.py) with two REST APIs:

#### API 1: /reverse

- **Endpoint:** `/reverse`
- **HTTP Method:** `GET`
- **Query Parameter:**
  - `in`: String to reverse the words

**Example**
bash: curl http://127.0.0.1:5000/reverse?in=The%20quick%20brown%20fox%20jumps%20over%20the%20lazy%20dog
expectancy to get: {"result":"dog lazy the over jumps fox brown quick The"}


#### API 2: /restore

- **Endpoint:** `/restore`
- **HTTP Method:** `GET`
- **Query Parameter:**
  - restores the last result

**Example**
bash: curl http://127.0.0.1:5000/restore
expectancy to get: {"result":"dog lazy the over jumps fox brown quick The"}


### Testing Framework ###
- Requirements:
  - Python
  - Docker


### Setup ###
- clone the repository: 
  - "git clone https://github.com/yourusername/dockerized-app-testing-framework.git"
- cd dockerized-app-testing-framework
- install the required Python packages:
  - pip install -r requirements.py


### Running Tests ###
- Build the docker container:
  - "docker build -t app-container ."
- execution : "pytest test_api.py"
- expectancy: 
  - no asserts are shown
  - docker logs <container id> that depict requests are answered:
     - e.g.:
	     - 192.168.65.1 - - [02/Jan/2024 10:42:19] "GET /reverse?in=The+quick+brown+fox+jumps+over+the+lazy+dog HTTP/1.1" 200 -
       - 192.168.65.1 - - [02/Jan/2024 10:42:19] "GET /restore HTTP/1.1" 200 -
