
import gevent
import random
from time import sleep
from gevent import monkey
import thread
monkey.patch_all()
def task(pid):
    """
    Some non-deterministic task
    """
    print('Task %s done start' % pid, thread.get_ident())
    sleep(random.randint(0,2))
    print('Task %s done end' % pid, thread.get_ident())

def synchronous():
    for i in range(1,10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()


