# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import orderUpdateEvent_pb2 as orderUpdateEvent__pb2


class CustomerOrderUpdateStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.OrderUpdate = channel.unary_unary(
        '/OrderUpdateEvent.CustomerOrderUpdate/OrderUpdate',
        request_serializer=orderUpdateEvent__pb2.OrderItemInfo.SerializeToString,
        response_deserializer=orderUpdateEvent__pb2.Acknowledgement.FromString,
        )


class CustomerOrderUpdateServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def OrderUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CustomerOrderUpdateServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'OrderUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.OrderUpdate,
          request_deserializer=orderUpdateEvent__pb2.OrderItemInfo.FromString,
          response_serializer=orderUpdateEvent__pb2.Acknowledgement.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'OrderUpdateEvent.CustomerOrderUpdate', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))