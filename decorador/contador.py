# def fabrica_de_contador():
#     contador = 0
#
#     def contar():
#         nonlocal contador
#         contador += 1
#         return contador
#
#     return  contar
#
#
# contador = fabrica_de_contador()
# contador2 = fabrica_de_contador()

# print(contador())
# print(contador())
# print(contador())
# print(contador2())
# print(contador2())

_contador = 0

def fabrica_de_contador():

    def contar():
        global _contador
        _contador += 1
        return _contador

    return contar


contador = fabrica_de_contador()
contador2 = fabrica_de_contador()

print(contador())
print(contador())
print(contador())
print(contador2())
print(contador2())