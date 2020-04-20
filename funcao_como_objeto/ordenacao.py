alunos = [('Rafael', 12), ('Viviane',10), ('Masaharu', 15)]

alunos.sort(key=lambda aluno: aluno[1])

print(alunos)

def por_nome(aluno):
    return aluno[0]

print(sorted(alunos, key = por_nome))