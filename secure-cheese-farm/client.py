from random import randint
from time import sleep

import grpc

#
# Imports all Protoc generated classes/code
#
import cheese_pb2
import cheese_pb2_grpc


def main():

    # Load Certificate file
    trusted_cert = open("ssl/cert.pem", "rb").read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_cert)

    # gRPC channel
    channel = grpc.secure_channel('localhost:4000', credentials)

    # create a stub (client) of our service
    stub = cheese_pb2_grpc.CheeseServiceStub(channel)

    while True:

        try:
            # Do cheeses orders
            cheese_request = cheese_pb2.CheeseRequest(type=randint(0, 4))
            cheese = stub.Order(cheese_request)

            print("[gRPC] Received={0}".format(cheese_pb2.CheeseType.Name(cheese.type)))
        except grpc._channel._Rendezvous as err:
            print(err)
            sleep(3)


if __name__ == "__main__":

    main()
