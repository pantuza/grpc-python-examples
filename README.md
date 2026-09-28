![Python Version](https://img.shields.io/badge/Python-%3E%3D%203.12-green.svg)
![License](https://img.shields.io/badge/license-Apache%202-blue.svg)

# gRPC Python Examples
gRPC Python examples as reference code from a talk: Building Python services through gRPC.

Slides are available at Speakerdeck: [Building Python services through gRPC](https://speakerdeck.com/pantuza/building-python-services-through-grpc)


In this project there is three directories with three examples:

1. [A very simple gRPC service](https://github.com/pantuza/grpc-python-examples/blob/master/cheese-farm/Readme.md)
2. [A video Stream server](https://github.com/pantuza/grpc-python-examples/blob/master/soccer-match-streaming/Readme.md)
3. [A secure (TLS) service](https://github.com/pantuza/grpc-python-examples/blob/master/secure-cheese-farm/Readme.md)

The links above refers to each documentation of how to run services on your machine.

## Runtime and dependency updates

Use Python 3.12 for the Pipenv environments. In each example directory, run
`pipenv sync` to install the versions recorded in `Pipfile.lock`.
The `requirements.txt` files also enforce the patched runtime dependency floors.
The video example needs desktop OpenCV libraries (on Debian/Ubuntu, `libgl1`)
and a graphical session to display frames.

The checked-in protobuf modules were regenerated with `grpcio-tools==1.84.0`.
After changing a `.proto` file, regenerate them from its directory with:

```sh
pipenv run python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. *.proto
```
