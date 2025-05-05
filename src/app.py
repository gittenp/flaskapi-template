"""This module initializes a Flask application"""

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from src.main import main

# Load environment variables from a .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Define a home route
@app.route('/')
def home():
    """
    Home route that returns a welcome message.
    """
    return "Welcome to the Flask App!"

# Define a route to process input data
@app.route('/process', methods=['POST'])
def process_input():
    """
    Route to process input data from a POST request.
    The function expects a JSON payload with an input key containing
    an integer or float. It validates the input, processes it using the
    `main` function, and returns the result as a JSON response.

    Returns:
        Response: A JSON response containing the processed result or an error message.
        - 200: If the input is valid and processed successfully.
        - 400: If the input is missing or invalid.
        - 500: If an unexpected error occurs.
    """
    # Read input data from POST-request
    request_as_json = request.get_json(force=True)

    try:

        if "input" not in request_as_json:
            raise KeyError('input key is missing in the request.')

        if not isinstance(request_as_json["input"], (int, float)):
            raise TypeError('input must be an integer or float.')

        input_value = request_as_json["input"]

        # Pass the input to the main function
        result = main(input_value)
        return jsonify(result), 200
    except KeyError as e:
        # Handle missing or incorrect "input" key
        return jsonify({"error": 'Missing or incorrect input key: ' + str(e)}), 400
    except TypeError as e:
        # Handle invalid input type
        return jsonify({"error": 'Invalid input type: '+ str(e)}), 400
    except Exception as e:
        # Catch any other unexpected exceptions
        return jsonify({"error": 'An unexpected error occurred: ' + str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True,  use_reloader=False)
