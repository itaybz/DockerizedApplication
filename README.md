# Dockerized Application and API Testing Framework

This repository contains a Dockerized Python HTTP application with two REST APIs, along with a testing framework implemented using pytest. 
The testing framework allows developers to easily add and run tests for the provided APIs.

### Requirements ###

Tested on MAC OS (14.2) in respect to HTTP port number 5000.
This port is subject to be used as "Airdrop" service so you may want to disable it in order to execute along with port 5000

### Docker Container ###

The Docker container includes a Python HTTP application (app.py) with two REST APIs:

#### API 1: /reverse

- **Functionality: API will return the string reversed**
- **Endpoint:** `/reverse`
- **HTTP Method:** `GET`
- **Query Parameter:**
  - `in`: String to reverse the words

**Example**
- bash enrty: ```curl http://127.0.0.1:5000/reverse?in=The%20quick%20brown%20fox%20jumps%20over%20the%20lazy%20dog```
- bash expectancy: ```{"result":"dog lazy the over jumps fox brown quick The"}```

#### API 2: /restore

- **Functionality: The API will return the last result from API 1**
- **Endpoint:** `/restore`
- **HTTP Method:** `GET`

**Example**
- bash enrty: ```curl http://127.0.0.1:5000/restore```
- bash expectancy: ```{"result":"dog lazy the over jumps fox brown quick The"}```


### Testing Framework ###
- Requirements (minimum):
  - Python (3.8)
  - Docker (4.26.1)


### Setup ###
- Clone the repository: 
  - ```git clone https://github.com/itaybz/DockerizedApplication.git```
- Navigate to folder:
  - ```cd DockerizedApplication```
- Build a docker image:
  - ```docker build --tag python-docker .```
- Run the image in detached mode and bind port 5000:
  - ```docker run -d -p 5000:5000 python-docker```


### Running Tests ###
- Execution:
  - ```pytest test_api.py```
- Expectancy: 
  - No asserts are shown and tests are noted as "passed"
  - Docker logs <container id> that depict requests are answered: e.g.:
    - ```192.168.65.1 - - [02/Jan/2024 10:42:19] "GET /reverse?in=The+quick+brown+fox+jumps+over+the+lazy+dog HTTP/1.1" 200```
    - ```192.168.65.1 - - [02/Jan/2024 10:42:19] "GET /restore HTTP/1.1" 200```

### Adding New Tests ###
 - You can easily add tests by adding methods to test_my_api.py.
   e.g.:
   - ```def test_my_api()...:```

### Termination ###
- Testing framework will automatically start the application container, run the tests, and shut down the container upon completion or in case of an error
