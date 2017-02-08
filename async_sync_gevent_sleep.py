
import gevent
import random
import thread
def task(pid):
    """
    Some non-deterministic task
    """
    print('Task %s done start' % pid, thread.get_ident())

    gevent.sleep(random.randint(1,3))
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


