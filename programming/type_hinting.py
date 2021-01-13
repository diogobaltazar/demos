# will not throw err
def f(a: int = 0) -> int:
    return a*a

# will throw err
def g(a: int = 0) -> str:
    return a*a
