def fabrica_de_multiplicadores():
    def dobro(n):
        return n * 2

    return dobro

dobro_externo = fabrica_de_multiplicadores()
dobro_externo2 = fabrica_de_multiplicadores()

print(dobro_externo is dobro_externo2)
print(dobro_externo(3))


def fabrica_de_multiplicadores_new(multiplicador):
    def multiplicar(n):
        return n * multiplicador

    return multiplicar

dobro = fabrica_de_multiplicadores_new(2)
triplo = fabrica_de_multiplicadores_new(3)

print(dobro(3))
print(triplo(4))