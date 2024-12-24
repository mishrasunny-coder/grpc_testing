import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc
from server import CalculatorServicer


def start_grpc_server():
    """Starts a local gRPC server for testing."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    
    # Bind to port 0 to get an available port dynamically
    port = server.add_insecure_port('[::]:0')
    server.start()
    return server, port



def test_add_method():
    """Tests the Add method of the Calculator service."""
    server, port = start_grpc_server()  # Unpack the tuple
    try:
        channel = grpc.insecure_channel(f"localhost:{port}")  # Use the dynamically bound port
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.operands(a=5, b=3))
        assert response.value == 8, f"Expected 8, got {response.value}"
    finally:
        server.stop(None)  # Call stop on the server object


def test_subtract_method():
    """Tests the Subtract method of the Calculator service."""
    server, port = start_grpc_server()  # Unpack the tuple
    try:
        channel = grpc.insecure_channel(f"localhost:{port}")  # Use the dynamically bound port
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Subtract(calculator_pb2.operands(a=10, b=4))
        assert response.value == 6, f"Expected 6, got {response.value}"
    finally:
        server.stop(None)  # Call stop on the server object
