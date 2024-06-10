import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # to define the name of the Log File
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # to define the path where the Log file should be appended

os.makedirs(logs_path, exist_ok=True) # to actually create a directory for logs

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # to get the Log file path

# now, to write/configure the CONTENT of the Log file
logging.basicConfig(
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # conventional format (best practice)
    level = logging.INFO,
        handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()  # Adds logging to the console
    ]
)

# to test the logger
    # this condition ensures that the code block is executed only if the script is run directly, not when it is imported as a module in another script.
if __name__== "__main__":
    logging.info("Logging has started")
    logging.debug("This is a debug message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")