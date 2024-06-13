import logging
import os
from datetime import datetime

# update: I want to save all the logs of one day into the same log file.
LOG_FILE_DATE = datetime.now().strftime('%Y_%m_%d')
LOG_FILE_NAME = f"{LOG_FILE_DATE}.log"


logs_dir = os.path.join(os.getcwd(), "logs") # to define the path where the Log file should be appended
os.makedirs(logs_dir, exist_ok=True) # to actually create a directory for logs

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE_NAME) # to get the Log file path

# now, to write/configure the CONTENT of the Log file
logging.basicConfig(
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # conventional format (best practice)
    datefmt="%Y-%m-%d %H:%M:%S",
    level = logging.INFO,
        handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()  # adds logging to the console
    ]
)

# to test the logger
    # this condition ensures that the code block is executed only if the script is run directly, not when it is imported as a module in another script.
# if __name__== "__main__":
#     logging.info("Logging has started")
#     logging.debug("This is a debug message")
#     logging.warning("This is a warning message")
#     logging.error("This is an error message")
#     logging.critical("This is a critical message")