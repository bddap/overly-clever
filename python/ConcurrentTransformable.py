
from threading import Lock
from queue import Queue

class ConcurrentTransformable:
    """Non blocking transforms."""

    def __init__(s,thing):
        s.thing = thing
        s.lock = Lock()
        s.transforms = Queue()
        #rule: must have lock before removing items from s.transforms.

    def transform(s,f):
        """Transform thing lazily."""
        s.transforms.put( f )

    def get(s):
        """Evaluate thing, then return thing."""
        with s.lock:
            while not s.transforms.empty():
                s.thing = s.transforms.get()( s.thing )
            return s.thing

if __name__ == '__main__':

    from threading import Thread
    import time, random

    n = ConcurrentTransformable( 0 )

    def inc():
        while True:
            time.sleep( random.random() )
            n.transform( lambda x : x + 1 )

    def dec():
        while True:
            time.sleep( random.random() )
            n.transform( lambda x : x - 1 )

    def watch():
        a = n.get()
        while True:
            b = n.get()
            if b != a:
                a = b
                print(a)

    Thread( target=inc  , daemon=True ).start()
    Thread( target=dec  , daemon=True ).start()
    Thread( target=watch, daemon=True ).start()

    while True:
        time.sleep(10)
        n.transform(lambda x:x*2//1)
