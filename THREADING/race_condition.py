import logging
import time
import concurrent.futures
class FakeDatabase:
    def __init__(self):
        self.val=0
    def update(self,name):
        logging.info(f"Starting update for thread:: {name}")
        local_copy=self.val
        local_copy+=1
        time.sleep(0.1)
        self.val=local_copy
        logging.info(f"Finishing update for thread:: {name}")

if __name__=="__main__":
    format="%(asctime)s: %(name)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    db= FakeDatabase()
    logging.info(f"FDB starting value is :: {db.val}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for id in range(2):
            executor.submit(db.update, id)
    logging.info(f"Ending update. Updated value is :: {db.val}")

