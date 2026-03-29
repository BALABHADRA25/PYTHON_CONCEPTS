import logging
import threading
import time

def thread_func(name):
    logging.info(f"The thread:: {name} starting")
    time.sleep(2)
    logging.info(f"The thread:: {name} finishing")


if __name__ == "__main__":
    format="%(asctime)s: %(name)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Before creating Thread")
    #x= threading.Thread(target=thread_func, args=(1,))
    x= threading.Thread(target=thread_func, args=(1,), daemon=True)
    logging.info("Before starting Thread")
    x.start()
    x.join()
    logging.info("Waiting for thread to finish")
    logging.info("All done")




