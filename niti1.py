import time
import _thread

def f():
    for i in range(10):
        print(i)
        time.sleep(1)

_thread.start_new_thread(f,())
_thread.start_new_thread(f,())
print("Idemo dalje...")
time.sleep(20)