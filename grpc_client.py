from __future__ import print_function
import logging

import grpc
from datetime import datetime
import orderUpdateEvent_pb2
import orderUpdateEvent_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
	with grpc.insecure_channel('localhost:50051') as channel:
		stub = orderUpdateEvent_pb2_grpc.CustomerOrderUpdateStub(channel)
		request = {
			"orderId": "123456",
			"wmsId": "1901123456",
			"orderItemId": "12345678"
		}
		before = datetime.utcnow()
		response = stub.OrderUpdate(orderUpdateEvent_pb2.OrderItemInfo(**request))
		after = datetime.utcnow()
	diff = after - before
	diff_str = str(datetime.utcnow()).split(".")[1]
	print("Response took {} microseconds".format(diff_str))
	print("Ack={}".format(response.acknowledged))


if __name__ == '__main__':
	logging.basicConfig()
	run()
