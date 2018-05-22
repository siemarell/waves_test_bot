from threading import Thread
import requests
from config import URL
import logging
import time
import json


class Puller(Thread):
    def run(self):
        last = -1
        while True:
            r = requests.get(URL + "getUpdates?offset=%s" % (last + 1))
            if r.status_code == 200:
                for message in r.json()["result"]:
                    last = int(message["update_id"])
                    requests.post("http://localhost:5000/",
                                  data=json.dumps(message),
                                  headers={'Content-type': 'application/json',
                                           'Accept': 'text/plain'}
                                  )
            else:
                logging.warning("FAIL " + r.text)
            time.sleep(3)
