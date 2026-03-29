import time
import logging
import threading

def thread_func(name):
    logging.info(f"Thread ::{name} starting")
    time.sleep(2)
    logging.info(f"Thread:: {name} finishing")

if __name__=="__main__":
    format = "%(asctime)s: %(name)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%h:%M:%S")

    threads=[]
    for id in range(3):
        logging.info(f"Create and start thread:: {id}")
        x= threading.Thread(target=thread_func, args=(id,))
        threads.append(x)
        x.start()
    for id, thread in enumerate(threads):
        logging.info(f"Before joining thread:: {id}")
        x.join()
        logging.info(f"Thread done :: {id}")
