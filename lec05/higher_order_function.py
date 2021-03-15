def apply_twice(f,x):
    return f(f(x))

def square(x):
    return x * x

def triple(x):
    return x * 3

def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y+5) // 3

def make_adder(n):
    def adder (k):
        return k + n
    return adder

# add_three = make_adder(3)
# # make_adder is added in global frame
# # new frame are create call f1, contain make_adder, which parent is global
# # 
# # add_three is added in global frame
# result = add_three(4)

# # when call return, the result will show in globala frame
# print (result)

# Nested def
# why to find the current environment

# def f(x,y):
#     return g(x)

# def g(a):
#     return a + y
    # where return an error
    # local frame follow by the global
    # which don't contain y

    # function compisition

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h