import abc
import time
from manager import Manager
from observer import Observer

class Consumer(Observer):
    def __init__(self, delay=0):
       self.manager = Manager
       self.manager.attach(self)
       self.delay = delay

    def notify(self, message):
        time.sleep(self.delay)
        print message.text.encode('utf8')
