import logging
import sys

def setup_logger():
    # Configure logging
    logging.basicConfig(level=logging.DEBUG, 
                        filename='app.log', 
                        filemode='a',  # 'a' means append, 'w' means overwrite
                        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s')

    # Create a logger instance
    logger = logging.getLogger(__name__)

    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)  # Use sys.stdout for console output
    console_handler.setLevel(logging.DEBUG)  # Set console handler to DEBUG level

    # Create and set formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s')
    console_handler.setFormatter(formatter)  # Corrected typo here

    # Add console handler to logger
    logger.addHandler(console_handler)

    return logger

# Initialize logger
logger = setup_logger()

# Example usage
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
