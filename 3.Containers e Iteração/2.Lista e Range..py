"""Nesse tópico será abordado o container lista. Essa estrutura é utilizado em larga escala na esmagadora maioria dos
programas escritos em Python, por isso é importante conhcê-la em detalhes. Além disso  será visto a função range para
gerar listas com progressões aritmeticas.

A lista de Python pode ser definido como um vetor dinâmico em outras linguagens, isso significa que vocẽ pode acrescenta
e remove elementos da mesma, para criar uma lista você vei utilizar os colcletes [ ], uma lista pode ter vários elementos
 que podem ser separados por virgula."""

print([1, 2, 3])
print(type([])) #Lista
print(type({})) #Dicionário, vai ser abordado mais a frente.

n1 = (1, 3)     #Tupla, vai ser abordado mais a frente.
print(type(n1))

"""A criação de listas com números consecutivos é muito comum em python, por isso o python forneceu uma função chamada
range, que te permite definir uma progressão aritmetica na hora de criar uma lista."""

lista = list(range(10))  # Aqui estamos definindo que o range começa em 0 e termina em 9.
print(lista)
#[0,1,2,3,4,5,6,7,8,9]

lista = list(range(1, 10))  # Definimos o range que começa em 1 e termina em 10.
print(lista)
#[1,2,3,4,5,6,7,8,9,10]

lista = list(range(1, 10, 2))  # Definimos o range que começa em 1 até 10 com um salto de leitura de 2 em 2.
print(lista)
#[1,3,5,7,9]

lista = list(range(10, 1, -2))  # Podemos definir que a leitura seja de trás para frente com -2 com salto de 2 em 2.
print(lista)
#[10,8,6,4,2]

lista.sort()  # Com o sort reordenamos os elementos da lista.
print(lista)
#[2,4,6,8,10]

lista.append(12)  # Com o append inclui o elemento no final da lista.
print(lista)
#[2,4,6,8,10,12]

lista.pop()  # Com o pop remove o último elemento da lista.
print(lista)
#[2,4,6,8,10]

lista.extend([12, 14])  # Com o extend podemos adicionar mais de um elementos a lista.
print(lista)
#[2, 4, 6, 8, 10, 12, 14]

print(lista + [16, 18])  # Também podemos concatena listas
#[2, 4, 6, 8, 10, 12, 14, 16, 18]

print([1, 3]*3)
#[1, 3, 1, 3, 1, 3]


"""Strings e listas tem uma semelhança muito grande, muitas vezes temos uma string e queremos separar essa string em 
um lista."""

print('Python Pro')  # Consideramos o espaço vazio como separador.

print('Python Pro'.split())  # Com o split podemos passar de string para lista.

print( '#'.join(['Python', 'Pro'])) # Com o join fazemos o inverso, de lista para string e podemos definir o separador.


"""Podemos colocar qualquer coisa dentro de uma lista, até mesmo outra lista ou objeto de Python."""

print([1, 1.0, {'br', 'portugues', 'eua', 'ingles'}, (1, 2), 'Anderson', [1, 2, 3]])