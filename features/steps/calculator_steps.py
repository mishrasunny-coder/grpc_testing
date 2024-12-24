import grpc
import calculator_pb2
import calculator_pb2_grpc
from behave import given, when, then

# Shared resources
channel = None
stub = None
response = None

@given("the Calculator gRPC server is running")
def step_given_server_running(context):
    global channel, stub
    # Connect to the gRPC server
    channel = grpc.insecure_channel("localhost:50051")
    stub = calculator_pb2_grpc.CalculatorStub(channel)

@when('I send numbers {a:d} and {b:d} to the Add method')
def step_when_add(context, a, b):
    global response
    # Call the Add method
    response = stub.Add(calculator_pb2.operands(a=a, b=b))

@when('I send numbers {a:d} and {b:d} to the Subtract method')
def step_when_subtract(context, a, b):
    global response
    # Call the Subtract method
    response = stub.Subtract(calculator_pb2.operands(a=a, b=b))

@then('I should get the result {expected_result:d}')
def step_then_validate_result(context, expected_result):
    assert response.value == expected_result, f"Expected {expected_result}, but got {response.value}"
