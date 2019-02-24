"""Nesse tópico será apresentado o container cadeia de caracteres, do inglês string. Ele é utilizado para representar
texto dentro do código. Além disso você vai aprender as funções dir e help paara poder investigar os elementos que
constituem qualquer objeto diretamente no console.
    Container, se chama assim pois ele pode conter uma seguência de objetos.
    Vamos começar por uma string ou a chamada. cadeia de caracteres, pode ser definida com aspas simples.
        Ex:
       # >>>'Anderson'
        'Anderson'

    Para pular uma linha na frase, se usa o \n, mais a legibilidade de nosso código fica comprometido, para ficar mais
    legivel nosso código, podemos usar 3 aspas."""

p = ('python \npro')
print(p)
print(' ')             # Tanto o \n quanto as 3 aspas permitem o salto de linha, mais com as 3 aspas fica mais legivel.
p_2 = '''python  
pro'''
print(p_2)

print('''Python     
pro''')               # Podemos fazer com ou sem atribuição a uma variavél.

"""Também podemos concatenar nossa strings com expressão matemática"""
print('')
print('Python '+('Pro'))
print('')
print('a'*4)
print('Ipsum Loren '*7)

"""Agora teremos duas funções muito importante quando estamos trabalhando no console.
A primeira delas é o dir, ele vai fornecer uma lista de operações e atributos que esse objeti possui."""

dir('')

"""A segunda é o Help, que é usado quando você não sabe ou não se lembra o que um elemento faz ai você usa  o help"""

help('anderson'.lower) #Ele te apresenta um texto de ajuda.

#Obs: No console para sair do modo help aperte a letra Q.