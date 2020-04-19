a = 5


def f(a=3):
    b = 4
    print(globals())
    print(locals())
    print(a)
    print(b)


class A:
    a = 8
    a += 1
    print(a)
    print(globals())
    print(locals())


# f()

""" 
print(globals())
{
    '__name__': '__main__', 
    '__doc__': None, 
    '__package__': None, 
    '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f5f663e6978>, 
    '__spec__': None, 
    '__annotations__': {}, 
    '__builtins__': <module 'builtins' (built-in)>, 
    '__file__': '/home/rafael/Desktop/python_projects/programacao_funcional/namespaces/namespace_global.py', 
    '__cached__': None}

def f():
    print(globals())


f()

{
    '__name__': '__main__', 
    '__doc__': None, 
    '__package__': None, 
    '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f3e892c1978>, 
    '__spec__': None, 
    '__annotations__': {}, 
    '__builtins__': <module 'builtins' (built-in)>, 
    '__file__': '/home/rafael/Desktop/python_projects/programacao_funcional/namespaces/namespace_global.py', 
    '__cached__': None, 
    'a': 5, 
    'f': <function f at 0x7f3e892fd1e0>}

"""
