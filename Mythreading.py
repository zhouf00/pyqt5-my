from threading import Thread, Event
from time import ctime
from PyQt5.QtCore import QThread, pyqtSignal


class MyThread(Thread):

    def __init__(self, target, args, name=""):
        Thread.__init__(self)
        self.name = name
        self.target = target
        self.args = args
        self._stop_event = Event()
        self._stop_event.set()

    def run(self):
        #print("starting",self.name, "at:",ctime())
        self.res = self.target(*self.args)

    def stop(self):
        self._stop_event.clear()


class RunThread(QThread):

    counter_value = pyqtSignal(int)

    def __init__(self, target, args, name=""):
        QThread.__init__(self)
        self.target = target
        self.args = args
        self.is_running = True

    def run(self):
        #print("starting",self.name, "at:",ctime())
        self.res = self.target(*self.args)

    def stop(self):
        self.terminate()