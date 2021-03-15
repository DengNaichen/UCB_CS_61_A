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