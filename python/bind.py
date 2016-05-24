
def bind(f,*a,**k):
    """Does the same thing as functools.partial"""
    def g(*b,**l):
        return f(*a+b, **{**k,**l})
    return g

p = bind(print, 'I like', sep='... ', end='.\n')

p("pie")
p("cake")
p("generic functions")
