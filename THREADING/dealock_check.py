import threading
l=threading.Lock()
print(f"Accquiring lock 1")
l.acquire()
print("Accquiring lock2")
l.acquire()
print("Accquired 2 locks")