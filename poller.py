from threading import Thread
import requests
from config import BOT_URL
import logging
import time
import json
#import db


class Poller(Thread):
    def run(self):
        last = 0
        while True:
            #last = db.get_last_update_index()
            r = requests.get(BOT_URL + "getUpdates?offset=%s" % (last + 1))
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
