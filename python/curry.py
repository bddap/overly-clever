#!/usr/bin/env python3

def curry( f, *a ,**k ):
    def j( *b, **l ):
        if b or l:
            return curry( f, *a+b, **{**k,**l} )
        else:
            return f( *a, **k )
    return j

@curry
def g(*a,**k):
    print(*a,**k)

f = g("forts")("under")("the")("sea")

f(sep='! ')()
f(sep='')()
f(end='?\n')()

@curry
def pipe(x,*fs):
    for f in fs:
        x = f(x)
    return x

def add1(x):
    print(x,'+ 1 =',x + 1)
    return x + 1

def double(x):
    print(x,'* 2 =',x * 2)
    return x * 2

y = pipe(1,double)(add1,double)
y = y(double)(add1)

print('Functions have not been called yet. curry() is lazy.')
print(y())
