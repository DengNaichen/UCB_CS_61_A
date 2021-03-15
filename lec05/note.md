### Environment 

High-order function
```python
def apply_twice(f,x):
    return f(f(x))

def square(x):
    return x * x
```

Applying a user-defined fucntions:
- Create a new frame
- Bine formal parameters
- Execute the body

```python 
def make_adder(n):
    def adder (k):
        return k + n
    return adder

add_three = make_adder(3)
# make_adder is added in global frame
# new frame are create call f1, contain make_adder, which parent is global
# 
# add_three is added in global frame
result = add_three(4)
```

- every user-defined functions has a parent frame
- the parent of a fucntion is the frame in which it was defined
- Every local frame has a parent frame
- the parent of a frame is the parent of the fucntion called.

Local Names
Lambad Functions

```python
>>> x = 10
>>> square = x * x
>>> square
100
>>> square = lambda x: x * x
>>> square(10)
100
>>> (lambda x: x * x)(3)

>>> square
<function <lambda> at 0x7f7f781055e0>
>>> def square(x):
...     return x * x
... 
>>> square
<function square at 0x7f7f78105670>
```

Lambda Expression vs. Def
- Both create a function with the same domain, range, and behavior.
- Both bind that function to the name square.
- Only the def statement gives the function an intrinsic name, which shows  up in environment diagrams but doesn't affect execution (unless the function is printed).

Environment Example:


