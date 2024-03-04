import threading
import Queue
import time
class QueuePrinter(threading.Thread):
  def __init__(self, qu, *args, **kwargs):
    super(QueuePrinter, self).__init__(*args, **kwargs)
    self.qu = qu
  def run(self):
    while not self.qu.empty():
      item = self.qu.get()
      print item
      time.sleep(2)
qu = Queue()
printer = QueuePrinter(qu)
qu.put('String1')
qu.put('String2')
#etc...
printer.start()
qu.join()