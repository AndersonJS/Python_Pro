"""Nesse tópico você vai aprender mais detalhes sobre os parâmetros de função: como definir valores padrão, como passar
valores pode nome em vez de justaposição. Como item extra, ainda vai aprender o básico sobre f-strings, uma cadeia de
caracteres que permite utilizar valores de variáveis em sua construção.
"""
def ola(nome):
    return f'Olá {nome}'
print(ola('Renzo'))
print(ola('Luciano'))

def ola(nome, sobrenome, idade):
    return f'Olá {nome} {sobrenome} {idade}'
print(ola('Renzo', 'Nuccitelli', 35))

def ola(nome, sobrenome='Nuccitelli'): # Definição do valor default em sobrenome.
    return f'Olá {nome} {sobrenome}'
print(ola('Renzo'))

"""Quando é passado o nome o valor sobrenome retorna junto pois foi definido como um parametro default."""

print(ola('Anderson','Jalasko'))

def ola(nome, sobrenome, idade):
    return f'Olá {nome} {sobrenome} {idade}'
print(ola('Renzo', 'Nuccitelli', 37))
print(ola(nome='Luciano', sobrenome='Ramalho', idade=37)) # Definimos por parametros com o nome e não com o valor.
print(ola(idade=22, nome='lucas', sobrenome='Souza')) # Definimos com o nome de cada parametro sem ser na posição.

"""Percebe que no último print os valor passados pelo nome do parametro não estavam na ordem, anteriormente os valores
eram passados por justapossição e não pelo nome do atributo."""