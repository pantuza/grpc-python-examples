from time import sleep
from concurrent import futures

import grpc
import cv2

#
# Imports all Protoc generated classes/code
#
import stream_pb2
import stream_pb2_grpc


class SoccerService(stream_pb2_grpc.SoccerServicer):
    """ Soccer Matches stream service based on gRPC """

    def Watch(self, request, context):
        """ Returns a stream to a Match stream """

        print("[gRPC] Match={0}".format(request.id))

        file_path = "{0}.mp4".format(request.id)
        match = cv2.VideoCapture(file_path)
        while match.isOpened():

            ret_val, frame = match.read()
            if not ret_val:
                break

            video = stream_pb2.Video(
                data=frame.tobytes(),
                data_type=frame.dtype.name,
                data_shape=str(frame.shape),
            )

            yield video

        match.release()


def main():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stream_pb2_grpc.add_SoccerServicer_to_server(SoccerService(), server)

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
