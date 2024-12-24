from server import CalculatorServicer
import calculator_pb2


def test_add():
    """Test the Add method of the Calculator service."""
    servicer = CalculatorServicer()
    request = calculator_pb2.operands(a=5, b=3)
    response = servicer.Add(request, None)
    assert response.value == 8, f"Expected 8, but got {response.value}"


def test_subtract():
    """Test the Subtract method of the Calculator service."""
    servicer = CalculatorServicer()
    request = calculator_pb2.operands(a=10, b=4)
    response = servicer.Subtract(request, None)
    assert response.value == 6, f"Expected 6, but got {response.value}"
