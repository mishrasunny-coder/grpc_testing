Feature: Calculator Service
  As a user of the Calculator gRPC service
  I want to perform basic addition and subtraction operations
  So that I can validate the service functionality

  Scenario: Add two numbers
    Given the Calculator gRPC server is running
    When I send numbers 5 and 3 to the Add method
    Then I should get the result 8

  Scenario: Subtract two numbers
    Given the Calculator gRPC server is running
    When I send numbers 10 and 4 to the Subtract method
    Then I should get the result 6
