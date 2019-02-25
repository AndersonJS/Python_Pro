"""Nesse tópico você vai aprender como acessar elementos de um container por indíces inteiros, calcular o número de
elementos presentes e também fatias as estruturas e sub sequẽncias."""

nome = 'Anderson'
print(len(nome))  # Retorna o número de elementos da string.

print(nome[0])

print(nome[1])

print(nome[len(nome)-1])  # Acessa o último elemento da lista, o -1 e porque nossa contagem começa em 0.

print(nome[-1])  # Para melhorar a legibilidade o Python conta de trás para frente.

print(nome[0:3])  # Fatiamento de string, pega as 3 primeiros elementos da lista.

print(nome[1:3])  # Com a mudança do 0 por 1 a contagem começa do segundo elemento da lista, pois a contagem começa em 0

print(nome[-3:len(nome)])

print(nome[-3:])

print(nome[:3])

print(nome[:4:2])  # O 2 no final indica o passo de leitura.

print(nome[::-1])  # Leitura de trás para frente.

lista = list(range(10))
print(lista[0])
print(lista[-1])
print(lista[:3])
print(lista[::-1])
print(lista)
print(len(lista))