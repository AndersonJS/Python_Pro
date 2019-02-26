"""Nesse tópico será abordado como iterar nos diferentes elementos de um dicionário:chaves, valores e itens."""

linguas = {'br': 'portugues', 'eua': 'ingles', 'es': 'espanhol'}
print(type(linguas))

for chave in linguas:
    print(chave)
print('!'*10)

for chave in linguas.keys():
    print(chave)
print('-='*10)

for valor in linguas.values():
    print(valor)
print('#_'*10)

for chave, valor in linguas.items():
    print(chave, valor)
print('~')

"""Vamos aborda a remoção de elementos."""
print(linguas.pop('br'))  # Remove e retorna no print o valor removido
print(linguas)  # Verificação dos que ainda se encontram no dicionário
