import gevent
import thread
from gevent import monkey
monkey.patch_all()
def foo():
    print('Running in foo', thread.get_ident())
    gevent.sleep(10)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar', thread.get_ident())
    gevent.sleep(10)
    print('Implicit context switch back to bar')
print '>>>>>',thread.get_ident()
gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
