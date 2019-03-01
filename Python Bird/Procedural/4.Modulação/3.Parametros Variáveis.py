"""Nesse tópico você vai aprender a criar uma função com um número variável de argumentos, tanto por justaposição quanto
 por nome.
 Suponha que você queira criar uma função soma na qual você quer aceitar um número variável de parcelas, para fazer isso
 você pode encontrar utilizar o *, na maioria das vezes você vai encontrar dessa maneira *args, mais o args é uma
 convenção, você pode utilizar a nomeação que quiser depois do *.
 """
def soma(*parcelas):
    print(parcelas)
    print(type(parcelas))
print(soma())
"""()  Nosso print vai retorna nossa tupla vazia pois não foi passado valor
<class 'tuple'>  Tipo de nossa parcelas é uma tupla"""
print(soma(1,2))
"""(1, 2)
<class 'tuple'>
None
"""
"""Para implementar de verdade nossa função soma, podemos utiliza uma variavel como a aux = 0"""
def soma(*parcelas):
    aux=0
    for valor in parcelas:
        aux += valor
    return aux
print(soma())
# 0
print(soma(2))
# 2
print(soma(2, 4))
# 6
print(soma(2, 4, 10))  # Recebemos um numero arbitrário de parametros justa postos ou seja de acordo com sua posição.
# 16

"""Também é possivel faze-lo para parametros nomeados"""
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
print(f())
"""{}
<class 'dict'>
None"""

print(f(nome='Anderon'))
"""{'nome': 'Anderon'}
<class 'dict'>
None"""

print(f(nome='Anderson', sobrenome='Jalasko'))
"""{'nome': 'Anderson', 'sobrenome': 'Jalasko'}
<class 'dict'>
None"""

"""Algo que costuma acontecer e que você pode já ter uma tupla com três elementos e derepente já ter um dicionario
construido com alguns argumentos kwargs."""
args=(2, 4, 10)
kwargs={'nome': 'Anderson', 'sobrenome': 'Jalasko'}

def f(*args, **kwargs):
    print(args)
    print(kwargs)
print(f())
"""()
{}
None"""
print(f(1, 2, nome='Renzo', sobrenome='Nuccitelli'))
# (1, 2)
# {'nome':'Renzo','sobrenome':'Nuccitelli'
"""Podemos passar argumentos tanto por justapossição quanto por argumentos nomeados, os por justapossição serão 
inseridos na tupla args e os por nomeação sera atribuido no kwargs."""

"""Agora vamos tenta passar as variaveis args e a kwargs para nossa função f."""
print(f(args, kwargs))

"""((2, 4, 10), {'nome': 'Anderson', 'sobrenome': 'Jalasko'})  # Foi empacotado tanto o args quanto o kwargs.
{}
None"""

# Vamos desempacotar nossa função
print(f(*args, **kwargs))
"""(2, 4, 10)
{'nome': 'Anderson', 'sobrenome': 'Jalasko'}
None
"""