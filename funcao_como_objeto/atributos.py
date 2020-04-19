def dobro(x):
    return x * 2


"""dobro2 = lambda x: x * 2
Linter atualiza o codigo
"""


def dobro2(x): return x * 2


"""
from funcao_como_objeto.atributos import dobro
for p in dir(dobro):
    print(p)

Output : 
__annotations__
__call__
__class__
__closure__
__code__
__defaults__
__delattr__
__dict__
__dir__
__doc__
__eq__
__format__
__ge__
__get__
__getattribute__
__globals__
__gt__
__hash__
__init__
__init_subclass__
__kwdefaults__
__le__
__lt__
__module__
__name__
__ne__
__new__
__qualname__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__


>>> dobro.__name__
'dobro'
>>> dobro.__module__
'funcao_como_objeto.atributos'
>>> dobro.__
dobro.__annotations__     dobro.__delattr__(        dobro.__ge__(             dobro.__init__(           dobro.__name__            dobro.__repr__(
dobro.__call__(           dobro.__dict__            dobro.__get__(            dobro.__init_subclass__(  dobro.__ne__(             dobro.__setattr__(
dobro.__class__(          dobro.__dir__(            dobro.__getattribute__(   dobro.__kwdefaults__      dobro.__new__(            dobro.__sizeof__(
dobro.__closure__         dobro.__doc__             dobro.__globals__         dobro.__le__(             dobro.__qualname__        dobro.__str__(
dobro.__code__            dobro.__eq__(             dobro.__gt__(             dobro.__lt__(             dobro.__reduce__(         dobro.__subclasshook__(
dobro.__defaults__        dobro.__format__(         dobro.__hash__(           dobro.__module__          dobro.__reduce_ex__(      
>>> dobro.__doc__
>>> dobro.__code__
<code object dobro at 0x7faab6e19930, file "/home/rafael/Desktop/python_projects/programacao_funcional/funcao_como_objeto/atributos.py", line 1>
>>> dobro.__code__.co_c
dobro.__code__.co_cellvars  dobro.__code__.co_code      dobro.__code__.co_consts    
>>> dobro.__code__.co_c
dobro.__code__.co_cellvars  dobro.__code__.co_code      dobro.__code__.co_consts    
>>> dobro.__code__.co_code
b'|\x00d\x01\x14\x00S\x00'
>>> from dis import dis
>>> dis(dobro.__code__.co_code)
          0 LOAD_FAST                0 (0)
          2 LOAD_CONST               1 (1)
          4 BINARY_MULTIPLY
          6 RETURN_VALUE

>>> dobro.n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'n'
>>> dobro.n = 42
>>> dobro.n=
  File "<stdin>", line 1
    dobro.n=
           ^
SyntaxError: invalid syntax
>>> dobro.n
42
>>> del dobro.n
>>> dobro.n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'n'
>>> g = dobro
>>> g
<function dobro at 0x7faab6da7378>
>>> g.__name__
'dobro'



"""
