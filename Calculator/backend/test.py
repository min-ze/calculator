import unittest
from server import app  # Import your Flask app
import json

class CalculatorTestCase(unittest.TestCase):

    # Set up the testing client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test the addition endpoint
    def test_add(self):
        response = self.app.post('/add', data={"num1": 5, "num2": 3}, content_type='application/x-www-form-urlencoded')
        data = json.loads(response.data)
        
        # Check that the response contains the correct result
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 8)

    # Test the subtraction endpoint
    def test_subtract(self):
        response = self.app.post('/subtract', data={"num1": 5, "num2": 3}, content_type='application/x-www-form-urlencoded')
        data = json.loads(response.data)
        
        # Check that the response contains the correct result
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 2)

    # Test when one number is missing (blank input)
    def test_add_with_blank_input(self):
        # Send an empty string for num1 (simulating blank input)
        response = self.app.post('/add', data={"num1": "", "num2": "3"}, content_type='application/x-www-form-urlencoded')
        data = json.loads(response.data)

        # Check that it returns the correct result (assumes missing inputs as 0)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 3)

        
    # Test when invalid input (non-numeric) is sent
    def test_invalid_input(self):
        response = self.app.post('/add', data={"num1": "abc", "num2": 3}, content_type='application/x-www-form-urlencoded')
        data = json.loads(response.data)

        # Check for error response
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
