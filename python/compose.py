#!/usr/bin/env python3

def compose(*fs):
    if len(fs) == 1: return fs[0]
    return lambda x:fs[0](compose(*fs[1:])(x))

def forward_compose(*fs):
    if len(fs) == 1: return fs[-1]
    return lambda x:fs[-1](forward_compose(*fs[:-1])(x))

inc = lambda x : x + 1
sq = lambda x : x ** 2

compose(print,sq,inc,sq,sq,inc,inc)(0)

forward_compose(inc,inc,sq,sq,inc,sq,print)(0)
