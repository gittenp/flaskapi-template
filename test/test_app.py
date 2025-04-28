"""This module contains the unittests for the Flask API."""

import os
import pprint
import unittest
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load BASE_URL from environment variables
BASE_URL = os.getenv('BASE_URL')
if not BASE_URL:
    raise ValueError("BASE_URL is not set in the environment variables.")

HEADERS = None  # Replace with actual headers if needed


class TestAPI(unittest.TestCase):
    """Unit tests for the Flask API."""

    def test_process_endpoint_valid(self):
        """Test the /process endpoint with valid input."""
        json_string = {'input': 4}

        response = requests.post(
            f"{BASE_URL}/process",
            headers=HEADERS,
            json=json_string,
            timeout=10  # Timeout set to 10 seconds
        )

        response_json = response.json()
        pprint.pprint(response_json)

        expected_response_json = {
            'error': None,
            'input': 4,
            'output': 2.0,
            'runtime': '0.000xxxxxx',
            'valid': True
        }

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response_json['error'], expected_response_json['error'])
        self.assertEqual(response_json['input'], expected_response_json['input'])
        self.assertEqual(response_json['output'], expected_response_json['output'])
        self.assertTrue(response_json['runtime'].startswith('0.0'))
        self.assertEqual(response_json['valid'], expected_response_json['valid'])


    def test_process_endpoint_keyerror(self):
        """Test the /process endpoint with keyerror input."""
        json_string = {'input': 'iiii'}

        response = requests.post(
            f"{BASE_URL}/process",
            headers=HEADERS,
            json=json_string,
            timeout=10  # Timeout set to 10 seconds
        )

        response_json = response.json()
        print(response_json)
        print(response.status_code)

        expected_response_json = {
            'error': "Invalid input type: input must be an integer or float."
            }

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response_json['error'], expected_response_json['error'])


    def test_process_endpoint_missing(self):
        """Test the /process endpoint with invalid input."""
        json_string = {}

        response = requests.post(
            f"{BASE_URL}/process",
            headers=HEADERS,
            json=json_string,
            timeout=10  # Timeout set to 10 seconds
        )

        response_json = response.json()
        print(response_json)
        print(response.status_code)

        expected_response_json = {
            'error': "Missing or incorrect input key: 'input key is missing in the request.'"
            }

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response_json['error'], expected_response_json['error'])


    def test_process_endpoint_input(self):
        """Test the /process endpoint with invalid input."""
        json_string = {'inputx': 4}

        response = requests.post(
            f"{BASE_URL}/process",
            headers=HEADERS,
            json=json_string,
            timeout=10  # Timeout set to 10 seconds
        )


        response_json = response.json()
        print(response_json)
        print(response.status_code)

        expected_response_json = {
            'error': "Missing or incorrect input key: 'input key is missing in the request.'"
            }

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response_json['error'], expected_response_json['error'])


if __name__ == "__main__":
    unittest.main()
