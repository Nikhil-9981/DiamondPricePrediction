import sys
from logger import logging

def error_message_detail(error , error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
     # division by zero division by zero <traceback object at 0x000001D2D5AAA7C0>
    file_name = exc_tb.tb_frame.f_code.co_filename
    # [c:\Users\NIKHIL SINGH\Documents\Projects\Diamond_price_prediction\src\exception.py]
    print(exc_tb.tb_lineno)
    error_message = "Error occured in python script name [{0}] line numer [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)

    )

    return error_message


class CustomeException(Exception):


    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail= error_detail)
      
    
    def __str__(self):
        return self.error_message   

if __name__ == "__main__":
    logging.info("Logging has started")

    try :
        27/0
    except Exception as e:
        logging.info("Zero division error")
        logging.info(CustomeException(e,sys))
        # [2023-08-27 03:25:16,842] 35 root - INFO - Error occured in python script name [c:\Users\NIKHIL SINGH\Documents\Projects\Diamond_price_prediction\src\exception.py] line numer [32] error message [division by zero]




# Function Definition: You define a function named error_message_detail that takes two parameters: error and error_detail. The error parameter is expected to be an error object, and error_detail is expected to be a tuple of exception information obtained using sys.exc_info().

# Extracting Exception Information: In the line _, _, exc_tb = error_detail.exc_info(), you use the exc_info() method from the error_detail tuple (presumably, this should be an instance of sys.exc_info()) to extract information about the current exception. The result is a tuple containing three elements: (exception_type, exception_value, traceback).

# _: This is a convention to indicate that you're not interested in the first element, which is the exception type.

# _: Similarly, you're not interested in the second element, which is the exception value (the error message).

# exc_tb: This variable is assigned the traceback object, which contains information about the stack frames and where the error occurred.

# Getting the File Name: You retrieve the file name where the error occurred using exc_tb.tb_frame.f_code.co_filename. The tb_frame attribute of the traceback object represents the frame where the error occurred, and co_filename is one of its attributes that holds the file name.

# Creating the Error Message: You construct an error message string using string formatting. This message includes the following information:

# The file name where the error occurred (file_name).
# The line number in the file where the error occurred (exc_tb.tb_lineno).
# The error message itself, converted to a string using str(error).
# Returning the Error Message: Finally, the function returns the error message as a string.

# This function is designed to be used when you catch an exception and want to provide a more detailed error message that includes the file name and line number where the error occurred in addition to the original error message. It can be helpful for debugging and understanding the context of an error in your code.