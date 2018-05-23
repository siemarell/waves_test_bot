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
    if address.startswith('/'):
        return "OK", 200
    chat_id = data['message']['chat']['id']
    if not waves.validate_address(address):
        current_app.logger.info(f'Invalid waves testnet address: "{address}"')
        bot.send_message(chat_id, f'Invalid waves testnet address: "{address}"')
    else:
        tx_id = waves.transfer_asset(address)
        if tx_id:
            current_app.logger.info(f'I\'ve sent 0.01 waves to "{address}". txId: "{tx_id}"')
            bot.send_message(chat_id, f'I\'ve sent 0.01 waves to "{address}". txId: "{tx_id}"')
        else:
            current_app.logger.info(f'Failed to send waves to "{address}"')
            bot.send_message(chat_id, f'Failed to send waves to "{address}"')
    return "OK", 200
