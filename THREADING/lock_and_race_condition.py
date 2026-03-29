import logging
import time
import concurrent.futures
import threading

class FakeDatabase:
    def __init__(self):
        self.val=0
        self._loc= threading.Lock()
    
    def lock_update(self, name):
        logging.info(f"Starting thread:: {name}")
        logging.debug(f"Thread:: {name} about to lock")
        with self._loc:
            logging.debug(f"Thread:: {name} has lock")
            local_copy= self.val
            local_copy+=1
            time.sleep(0.2)
            self.val=local_copy
            logging.debug(f"Thread:: {name} about to release lock")
        logging.debug(f"Thread:: {name} after release lock")
        logging.info(f"Thread:: {name} is done")

if __name__=="__main__":
    format= "%(asctime)s: %(name)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

    db= FakeDatabase()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for id in range(2):
            executor.submit(db.lock_update, id)
    logging.info(f"The final value in FDB is :: {db.val}")


