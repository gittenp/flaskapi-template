"""This module provides a utility function to set up logging for the application."""

import os
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter


def setup_logging(log_level, log_file_path=None):
    """
    Configures logging for the application.
    Args:
        log_level (int): The logging level (e.g., logging.INFO, logging.DEBUG).
        log_file_path (str, optional): The path to the log file. If not provided, a default
            log file named 'system_log_file.log' will be created in the project's root directory.
    Returns:
        None
    """
    # Clear existing handlers to avoid duplicates
    root_logger = logging.getLogger()
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # Default log file path
    if not log_file_path:
        file_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        log_file_path = os.path.join(file_path, 'system_log_file.log')

    # File handler
    file_handler = RotatingFileHandler(filename=log_file_path, maxBytes=2 * 1024 * 1024, backupCount=2)
    file_formatter = Formatter(fmt='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # Stream handler
    stream_handler = logging.StreamHandler()
    stream_formatter = Formatter(fmt='%(levelname)s: %(message)s')
    stream_handler.setFormatter(stream_formatter)

    # Add handlers to the root logger
    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)
    root_logger.setLevel(log_level)  # Set the global log level


if __name__ == '__main__':
    # Initialize logging with INFO level
    setup_logging(logging.INFO) # Set the log level to INFO
    logger = logging.getLogger(__name__)  # Get the module-specific logger

    # Log messages
    logger.info("Logging setup complete.")
    logger.error("This is an error message.")

    # Change log level dynamically
    logger.setLevel(logging.DEBUG)  # Change the log level to DEBUG
    logger.debug("This is a debug message.")
