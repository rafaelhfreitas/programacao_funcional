# from functools import wraps
# from time import sleep, strftime
#
#
# def logar(f):
#     @wraps(f)
#     def executar_com_tempo(*arg, **kargs):
#         print(strftime('%H:%M:%S'))
#         return f(*arg, **kargs)
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


from functools import wraps
from time import sleep, strftime

def logar(fmt='%H:%M:%S'):
    def decorator(f):
        @wraps(f)
        def executar_com_tempo(*arg, **kargs):
            print(strftime(fmt))
            return f(*arg, **kargs)

        return  executar_com_tempo

    return decorator

@logar(fmt='%H:%M:%S')
def mochileiro():
    return 42

@logar(fmt='%H:%M:%S')
def ola(nome):
    return f'Olá {nome}'

if __name__ == '__main__':
    print(mochileiro())
    print(mochileiro.__name__)
    print(ola('Renzo'))
    print(ola.__name__)
    sleep(1)
    print((mochileiro()))
    print(ola('Rafael'))
