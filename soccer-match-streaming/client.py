from time import sleep
from ast import literal_eval

import grpc
import cv2
import numpy as np

#
# Imports all Protoc generated classes/code
#
import stream_pb2
import stream_pb2_grpc


def main():

    channel = grpc.insecure_channel('localhost:4000')
    stub = stream_pb2_grpc.SoccerStub(channel)

    match = stream_pb2.Match(id="cruzeiro")
    iterator = stub.Watch(match)

    try:
        for video in iterator:

            frame = np.frombuffer(
                video.data,
                dtype=video.data_type
            ).reshape(literal_eval(video.data_shape))

            cv2.imshow(match.id, frame)
            if cv2.waitKey(1) == 27:
                break  # esc to quit

        cv2.destroyAllWindows()

    except grpc._channel._Rendezvous as err:
        print(err)
        sleep(3)


if __name__ == "__main__":

    main()
