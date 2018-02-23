#!/usr/bin/env python3

class Node:

    def __init__(s,f,child_nodes):
        s.function = f
        s.children = child_nodes
        for c in child_nodes:
            c.register_parent(s)
        s.parents = []

    def register_parent(s,parent_node):
        s.parents.append(parent_node)

    def damage(s):
        if hasattr(s,'cache'):
            del s.cache
        if not s.parents:
            return { s }
        return set.union( * (n.damage() for n in s.parents) )

    def repair(s):
        if not hasattr(s,'cache'):
            s.cache = s.function( *(c.repair() for c in s.children) )
        return s.cache

    def update(s):
        for d in s.damage():
            d.repair()


class DependencyTree:

    def __init__(s):
        s.contents = {}

    def add(s, river, *tributaries):
        if river in s.contents:
            assert(not tributaries)
            return s.contents[river]

        tributaries = [s.add(t) if callable(t) else s.add(*t) for t in tributaries]
        n = Node(river, tributaries)
        s.contents[river] = n
        return n

    def apply(s, f):
        s.contents[f].update()

if __name__ == '__main__':

    import time, random

    def f():
        return time.time()

    def g():
        return random.random()

    def h(f,g):
        return f + g

    def top(f,g,h):
        print('f',f)
        print('g',g)
        print('h',h)

    d = DependencyTree()

    structure = ( top, f, g, ( h, f, g ) )  # I think I just made a Lisp.

    d.add( *structure )

    for t in range(10):
        time.sleep(1)
        d.apply(g)
