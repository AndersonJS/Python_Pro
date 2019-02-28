"""Nesse tópico será abordado como construir uma função. Além disso também aprender o que é uma PEP, em particular a 8,
 que é um guia de estilos para escrita de código Python.


PEP 8 - Guia de Estilo para o Código Python
 https://www.python.org/dev/peps/pep-0008/
"""
"""Construção de uma função em Python"""

def ola_mundo():
    return print('Ola Mundo')
ola_mundo()

print('*'*10)

def ola_mundo():
    pass
ola_mundo()

print('*'*10)

resultado = ola_mundo()
print(type(resultado))