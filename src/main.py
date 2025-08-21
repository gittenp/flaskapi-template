"""This module contains the main processing function for the Flask API."""

import time
import logging
from helpers.system_logging import setup_logging

# Initialize logging and set the log level
setup_logging(logging.INFO)

# setup_logging(logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("Starting Logging")

def main(input_value):
    """
    Main function that processes the input and returns a dictionary with the result and metadata.
    Args:
        input_value: The input value to be processed.
    Returns:
        Dict: A dictionary containing the processed output, error info, validity, and runtime.
    """
    logger.info("Entering main function.")
    starttime = time.time()

    result = {
        "input": input_value,
        "output": None,
        "error": None,
        "valid": False,
        "runtime": None
    }

    try:
        result["output"] = input_value / 2
        result["valid"] = True
    except Exception as e:
        result["error"] = 'Error occurred in main function' + str(e)  # Store error as string for easier debugging

    result["runtime"] = f"{time.time() - starttime:.10f}"
    logger.debug("Execution time: %s seconds.", result["runtime"])

    logger.info("Exiting main function.")

    return result


if __name__ == '__main__':
    # Test cases for quick validation
    print(main(4))  # Valid input
    print(main('4'))  # Invalid input (should raise a Error)
    print(main(None))  # Invalid input (should raise a Error)

#test