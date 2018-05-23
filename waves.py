import requests
from config import API_KEY, NODE_ADDRESS
from flask import current_app


class Waves:
    def __init__(self, node_address, api_key):
        self.node_address = node_address
        self._s = requests.Session()
        self._s.headers.update({'API_KEY': api_key})

    def validate_address(self, address):
        resp = self._s.get(f'{self.node_address}/addresses/validate/{address}')
        return resp.status_code == 200 and resp.json()['valid']

    def transfer_asset(self, recipient, amount=1000000, fee=100000, asset_id=None):
        data = {
            "sender": "3N3Cn2pYtqzj7N9pviSesNe8KG9Cmb718Y1",
            "recipient": recipient,
            "fee": fee,
            "amount": amount,
            "attachment": ""
        }
        resp = self._s.post(f'{self.node_address}/assets/transfer', json=data)
        current_app.logger.info(resp.json())
        if resp.status_code == 200:
            return resp.json()['id']
        else:
            return None

waves = Waves(NODE_ADDRESS, API_KEY)
