# from decorador.registrador import get_marcadas, marcar
#
# def primeira():
#     pass
#
# marcar(primeira)
#
# def segunda():
#     pass
#
# marcar(segunda)
#
# if __name__ == '__main__':
#     for f in get_marcadas():
#         print((f.__name__))


from decorador.registrador import get_marcadas, marcar

def primeira():
    pass

primeira = marcar(primeira)

@marcar
def segunda():
    pass

if __name__ == '__main__':
    for f in get_marcadas():
        print((f.__name__))
    primeira()
    segunda