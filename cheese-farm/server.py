import grpc
from concurrent import futures
from time import sleep
from random import randint

#
# Imports all Protoc generated classes/code
#
import cheese_pb2
import cheese_pb2_grpc


class CheeseService(cheese_pb2_grpc.CheeseServiceServicer):
    """ Extends the auto generated CheeseServiceServicer class from Protoc
    compiler. In this class we implement the service layer code
    """

    def Order(self, request, context):
        """ Simulates a Cheese Order load and returns a Cheese """

        sleep(randint(0, 3))  # Simulates some load
        print("[gRPC] Order={0}".format(cheese_pb2.CheeseType.Name(request.type)))

        cheese = cheese_pb2.Cheese()
        cheese.type = request.type
        cheese.age = 10
        return cheese


def main():

    # gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Binds our service implementation to a gRPC server through the
    # auto generated function add_CheeseServiceServicer_to_server
    cheese_pb2_grpc.add_CheeseServiceServicer_to_server(CheeseService(), server)

    print("Cheese Farm service")
    print(
    """
         _--"-.
      .-"      "-.
     |""--..      '-.
     |      ""--..   '-.
     |.-. .-".    ""--..".
     |'./  -_'  .-.      |
     |      .-. '.-'   .-'
     '--..  '.'    .-  -.
          ""--..   '_'   :
                ""--..   |
                      ""-'
    """
    )

    print('Listening on localhost:4000')
    server.add_insecure_port('localhost:4000')
    server.start()

    # server.start() will not block, so we run a sleep-loop to keep
    # alive server alive until an interruption
    try:
        while True:
            sleep(60 * 60)  # Each hour the loop continues
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":

    main()
