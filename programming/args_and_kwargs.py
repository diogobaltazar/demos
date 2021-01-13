def f(*args):
    for arg in args:
        print(f'> {arg}')

print('*args are wrapped as an array: f(1, 2, 3):')
f(1, 2, 3)

def g(**args):
    for (key, value) in args.items():
        print(f'> key: {key}, value: {value}')


print('**args are wrapped as a dict: g(a=1, b=2, c=3):')
g(a=1, b=2, c=3)



