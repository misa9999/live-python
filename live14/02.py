import threading

from time import sleep

def wait():
    sleep(2)
    print('Acabou')


class MyThread(threading.Thread):
    def __init__(self, target, name='MyThread'):
        super().__init__()
        self.target = target
        self.name = name

    def run(self):
        self.target()


t = MyThread(wait)
t.start()
print(t.name)