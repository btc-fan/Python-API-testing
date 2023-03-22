import logging

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level to INFO for the project execution
logger.setLevel(logging.DEBUG)

# Create a console handler and set the logging level to DEBUG for the CLI
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create a formatter and add it to the handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)