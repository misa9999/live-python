import threading

from time import sleep

def wait():
    sleep(2)
    print('Acabou')


t1 = threading.Thread(target=wait, name='wait', daemon=True)
t1.start()
print(t1.is_alive())
print(t1.name)

t2 = threading.Thread(target=wait, name='wait')
t2.start()
print(t2.is_alive())
print(t2.name)


# print(threading.active_count())
# print(threading.enumerate())
# print(threading.enumerate()[0].name)
# print(threading.enumerate()[0].is_alive())