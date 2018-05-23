from flask import Flask
from log_handlers import ch, fh
from config import BOT_TOKEN
import routes
import logging
import poller

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(routes.api)
app.logger.addHandler(ch)
app.logger.addHandler(fh)
app.logger.setLevel(logging.INFO)

if __name__ == '__main__':
    pollerobj = poller.Poller()
    pollerobj.daemon = True
    pollerobj.start()
    app.run(host='0.0.0.0', port=5000, threaded=True)
    pollerobj.join()
