def make_adder(n):
    """
    >>> make_adder(2)(3)
    >>> 5
    """
    return lambda k: n + k

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g