from flask import Blueprint, request, current_app

api = Blueprint('simple_page', __name__)


@api.route('/', methods=['POST'])
def msg_handler():
    current_app.logger.warning("Got request: %s" % request)
    current_app.logger.info("Got request info: %s" % request)
    return "OK", 200
