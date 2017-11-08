import threading
import time
count = 0
def func(i):
    print("{} İşlemi başladı.\n".format(threading.current_thread()))
    time.sleep(i)
    print("{} İşlemi sonlandı.\n".format(threading.currentThread()))
    global count
    count += 1

tPool = list()

basla=time.time()
for i in range(3):
    tPool.append(threading.Thread(target=func, args=(3,)))
for t in tPool:
    t.start()
    t.join() # Bu satır işlemleri sıralı hale getirmektedir.

while (True):
    if (count == 3):
        break

son = time.time()
print(son - basla)