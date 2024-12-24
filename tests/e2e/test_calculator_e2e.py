import grpc
import calculator_pb2
import calculator_pb2_grpc
import pytest


@pytest.fixture(scope="module")
def grpc_stub():
    """Creates a gRPC stub for connecting to the running Calculator service."""
    channel = grpc.insecure_channel("localhost:50051")
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    return stub


def test_add_e2e(grpc_stub):
    """End-to-end test for the Add method."""
    response = grpc_stub.Add(calculator_pb2.operands(a=5, b=3))
    assert response.value == 8, f"Expected 8, got {response.value}"


def test_subtract_e2e(grpc_stub):
    """End-to-end test for the Subtract method."""
    response = grpc_stub.Subtract(calculator_pb2.operands(a=10, b=4))
    assert response.value == 6, f"Expected 6, got {response.value}"
