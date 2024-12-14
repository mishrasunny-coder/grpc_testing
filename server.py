import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc
from grpc_reflection.v1alpha import reflection


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add (self, request, context):
        result = request.a + request.b
        return calculator_pb2.Result(value=result)
    
    def Subtract(self, request, context):
        result = request.a - request.b
        return calculator_pb2.Result(value=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    # Enable reflection for the Calculator service
    SERVICE_NAMES = (
        calculator_pb2.DESCRIPTOR.services_by_name['Calculator'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
