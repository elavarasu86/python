import logging

'''
The logging.getLogger(__name__) function is used to create a logger object that is specific to the module in which
it is called. This allows for hierarchical logging, where loggers are named according to the module hierarchy,
making it easier to track where log message originate.
'''
#conigure the root logger
logging.basicConfig(filename='example.log', level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#create a logger for the main module
main_logger = logging.getLogger('main')

#create a logger for a submodule
submodule_logger = main_logger.getChild('submodule')

def main():
    main_logger.info('Starting main function')
    submodule_function()
    main_logger.info('Finished main function')

def submodule_function():
    submodule_logger.info('Starting submodule fucntion')
    submodule_logger.info('Doing some work in submodule')
    submodule_logger.info('Finished submodule function')

if __name__=='__main__':
    main()
