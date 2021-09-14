import logging

def logging_function():

    logging.basicConfig(
        # filename='test.log',
        # filemode='w',
        level=logging.DEBUG,
        format = '%(asctime)s - %(levelname)s: %(message)s',
    )
    logging.basicConfig(
        # filename='test.log',
        # filemode='w',
        level=logging.INFO,
        format = '%(asctime)s - %(levelname)s: %(message)s',
    )
    logging.basicConfig(
        # filename='test.log',
        # filemode='w',
        level=logging.WARNING,
        format = '%(asctime)s - %(levelname)s: %(message)s',
    )
    logging.basicConfig(
        # filename='test.log',
        # filemode='w',
        level=logging.ERROR,
        format = '%(asctime)s - %(levelname)s: %(message)s',
    )
    logging.basicConfig(
        # filename='test.log',
        # filemode='w',
        level=logging.CRITICAL,
        format = '%(asctime)s - %(levelname)s: %(message)s',
    )