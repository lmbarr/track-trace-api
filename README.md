# Track and Trace API

This is a basic Flask API for tracking and tracing packages.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them

* [Python 3.9](https://www.python.org/downloads/)
* Pipenv
* Redis
* Docker (Optional)

### Installing for local development

Clone the project from GitHub

```
git clone https://github.com/username/track-and-trace-api
```

Change into the project directory

```
cd track-and-trace-api
```

Install the project requirements 

```
pipenv install --dev
```

### Running the API locally

Set up the Redis Server
```commandline
redis-server 
```

Set up the API Server
```commandline
python main.py
```

### Running the API with Docker (Optional)

#### Build and run needed containers

```commandline
docker-compose up -d

```
#### Retrieve an article: hit this endpoint on your prefer browser
```commandline
http://127.0.0.1:5001/article?tracking_number=TN12345679&carrier=UPS
```