
class attr(object):
    def __init__(s,g): s.g = g
    def __getattribute__(s,n): return object.__getattribute__(s,'g')(n)

def chain(o):
    def f(n):
        getattr(o,n)()
        return b
    b = attr( f )
    return b

class example:
    def __init__(s): s.n = 0
    def inc(s): s.n += 1
    def sq(s): s.n = s.n ** 2

e = example()
chain(e).inc.inc.sq.sq.inc.sq
print(e.n)

a = [1,2,2,4,65,6]
chain(a).pop.pop.pop
print(a)
