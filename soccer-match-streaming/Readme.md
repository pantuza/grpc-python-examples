# Video Streaming using gRPC

This example shows how to implement a gRPC service that streams from the
server to the client a video. To check this service locally, please run as follows:

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

Run a client program to see the video stream:

```bash
$> pipenv run python client.py
```
