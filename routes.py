from flask import Blueprint, request, current_app
from waves import waves
import bot
api = Blueprint('simple_page', __name__)


@api.route('/', methods=['POST'])
def msg_handler():
    current_app.logger.info("Got request: %s" % request)
    current_app.logger.info("Request json is: %s" % request.json)
    data = request.json
    address = data['message']['text']
    chat_id = data['message']['chat']['id']
    if not waves.validate_address(address):
        bot.send_message(chat_id, f'Invalid waves testnet address: "{address}"')
    else:
        waves.transfer_asset(address)
    return "OK", 200
