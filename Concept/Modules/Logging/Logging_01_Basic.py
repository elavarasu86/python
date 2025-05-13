import logging
''' Refer : https://docs.python.org/3/howto/logging.html
Basic Logging:  Logging is a means of tracking events that happen when some software runs. 
                The software’s developer adds logging calls to their code to indicate that certain events have occurred. 

DEBUG:		Detailed information, typically of interest only when diagnosing problems.
INFO:		Confirmation that things are working as expected.
WARNING:	An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR:		Due to a more serious problem, the software has not been able to perform some function.
CRITICAL:	A serious error, indicating that the program itself may be unable to continue running.

The default level is WARNING, which means that only events of this severity and higher will be tracked, unless the logging package is configured to do otherwise.
'''

#A simple example
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything as default level is WARNING.

# OUTPUT is: WARNING:root:Watch out!
# in the above output python printing level(WARNING) and description(Watch out!)
