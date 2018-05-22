import logging
from logging.handlers import RotatingFileHandler
fh = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)