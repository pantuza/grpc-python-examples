# Secure (TLS) gRPC service

This example is the Cheese service but encrypted using TLS protocol. 

To check this service locally, please run as follows:

### Install dependencies

First, use pipenv to install project dependencies. It will create a virtualenv and
install all libraries on it.

```bash
$> pipenv install
```

### Run the server

The server will listen on localhost at port 4000:

```bash
$> pipenv run python server.py
```

### Run clients

Open as many terminal you want and run an instance of the client code:

```bash
$> pipenv run python client.py
```
