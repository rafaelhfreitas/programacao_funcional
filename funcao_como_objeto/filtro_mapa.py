import operator

alunos = [('Rafael', 0), ('Viviane',10), ('Masaharu', 15), ('Alessandra', 5)]

print([(nome, nota) for nome, nota in alunos if nota > 5])

print([nome for nome, nota in alunos if nota > 5])


def possui_nota_maior_cinco(aluno):
    _, nota = aluno
    return  nota > 5

print(list(filter(possui_nota_maior_cinco, alunos)))

def extrair_nome(aluno):
    nome, _ =  aluno
    return nome

print(list(map(extrair_nome, alunos)))

print(list(map(extrair_nome, filter(possui_nota_maior_cinco, alunos))))

print(list(map(operator.itemgetter(0), filter(possui_nota_maior_cinco, alunos))))