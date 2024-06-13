import sys
# from logger import logging
# import time
# from datetime import datetime

# whenever an exception gets raised, I want to push this on like my own custom message
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info() 
        # talks about "execution info"
        # give 3 IMP. info -> interested in "last" info
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# So, whenever you use "try...catch" -> inside the catch block just raise CustomException to use this!


# to test the logger (at timestamp intervals)
# def log_at_intervals():
#     messages = [
#         "Starting the test logging process",
#         "This is the first log message",
#         "This is the second log message",
#         "This is the third log message",
#         "This is the fourth log message",
#         "This is the fifth log message",
#         "Ending the test logging process"
#     ]

#     for message in messages:
#         logging.info(message)
#         time.sleep(5) # to wait for 5 seconds before logging the next message


# if __name__ == "__main__":
#     log_at_intervals()