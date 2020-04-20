"""
Construa uma função de ordenação que ordene os alunos por nota. Se houver empate em nota, o nome deverá definir a ordem
>>> alunos = [('Renzo',0), ('Luciano', 10), ('Renzo Santos', 10), ('Renzo Nucitelli',10)]
>>> alunos.sort(key=ordernar_por_nota_e_nome)
>>> alunos
[('Renzo',0), ('Luciano', 10), ('Renzo Nucitelli',10), ('Renzo Santos', 10)]
"""

alunos = [('Renzo',0), ('Luciano', 10), ('Renzo Santos', 10), ('Renzo Nucitelli',10)]


def ordernar_por_nota_e_nome(aluno):
    nome, nota = aluno
    return nota, nome

print(alunos

alunos.sort(key=ordernar_por_nota_e_nome)

print(alunos)
