import sys 
import logging

def error_message_detail(error, error_detail:sys):
    __,__, exc_tb=error_detail.exc_info()   #execution information
    file_name=exc_tb.tb_frame.f_code.co_filename  #given in custom exception handling document, on google
    error_message = "error occured in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

#function which will show how your error will look 

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
    
#common throughout
