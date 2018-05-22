
fh = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
ch.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)