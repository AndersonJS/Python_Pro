"""Nesse tópico será abordado o container tupla. Apesar de muito parecida com a lista, a tupla é imutavél, o que
significa não ser possivel alterar as referências depois de tê-la criado. Também será visto como utiliza a função id
para identificar unicamente objetos durante a execução de um programa Python."""

tpl = (1, 2)
print(type(tpl))
#<class 'tuple'>

print(tuple(range(6)))  # A tupla imprime dentro de parentes.
#(0, 1, 2, 3, 4, 5)

tpl1 = (5,)  #Tupla com um unico número.tem de colocar a virgula no final pois se não colocar o python acha que é um int
print(tpl1)
print(type(tpl1))

registro = ('Anderson', 30)
nome, idade = registro  #Aqui é feito o desempacotamento por sua forte semantica.
print(nome)
print(idade)

"""Veremos como é criada uma nova tupla que agrega os dados de duas tuplas em apenas uma, mais não saberemos o seu id."""
registro_2 = ('Renzo', 35)
print(registro + registro_2)
print(id('_'))  #Quando perguntado o id do último valor impresso com '_' dentro do id ele retorna o id da soma das tuplas
