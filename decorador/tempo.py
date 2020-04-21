# from functools import wraps
# from time import sleep, strftime
#
#
# def logar(f):
#     @wraps(f)
#     def executar_com_tempo(*args, **kwargs):
#         print(strftime('%H:%M:%S'))
#         return f(*args, **kwargs)
#
#     return  executar_com_tempo
#
# @logar
# def mochileiro():
#     return 42
#
# @logar
# def ola(nome):
#     return f'Olá {nome}'
#
# if __name__ == '__main__':
#     print(mochileiro())
#     print(mochileiro.__name__)
#     print(ola('Renzo'))
#     print(ola.__name__)
#     sleep(1)
#     print((mochileiro()))
#     print(ola('Rafael'))


# from functools import wraps
# from time import sleep, strftime
#
#
# def logar(fn=None, *, fmt='%H:%M:%S'):
#     if fn is not None:
#         return logar(fmt=fmt)(fn)
#
#     def decorator(f):
#         @wraps(f)
#         def executar_com_tempo(*args, **kwargs):
#             print(strftime(fmt))
#             return f(*args, **kwargs)
#
#         return executar_com_tempo
#
#     return decorator
#
#
# @logar
# def mochileiro():
#     return 42
#
#
# @logar(fmt='%H:%M:%S')
# def ola(nome):
#     return f'Olá {nome}'
#
#
# if __name__ == '__main__':
#     print(mochileiro())
#     print(mochileiro.__name__)
#     print(ola('Renzo'))
#     print(ola.__name__)
#     sleep(1)
#     print((mochileiro()))
#     print(ola('Rafael'))

from functools import wraps
from time import sleep, strftime
from decorator import getfullargspec, decorator

@decorator
def logar(f, fmt='%H:%M:%S', *args, **kwargs):
    print(strftime(fmt))
    return f(*args, **kwargs)

@logar
def mochileiro():
    return 42


@logar(fmt='%H:%M:%S')
def ola(nome):
    return f'Olá {nome}'


if __name__ == '__main__':
    print(getfullargspec(mochileiro))
    print(getfullargspec(ola))
    print(mochileiro())
    print(mochileiro.__name__)
    print(ola('Renzo'))
    print(ola.__name__)
    sleep(1)
    print((mochileiro()))
    print(ola('Rafael'))
