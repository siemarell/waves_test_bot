from threading import Thread
import requests

class Puller(Thread):
    def run(self):
        while True:
            r = requests.get(URL + "?offset=%s" % (last + 1))
            if r.status_code == 200:
                for message in r.json()["result"]:
                    last = int(message["update_id"])
                    requests.post("http://localhost:8888/",
                                  data=json.dumps(message),
                                  headers={'Content-type': 'application/json',
                                           'Accept': 'text/plain'}
                                  )
            else:
                logging.warning("FAIL " + r.text)
            time.sleep(3)