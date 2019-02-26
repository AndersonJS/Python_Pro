"""Nesse tópico será abordado o container dicionário, que também é chamado de mapas em outras linguagens.
Essa essa estrutura é utilizada para resolver problemas do tipo chave valor, como vai poder conferir ao conectar países
às suas respectivas línguas."""

linguas = {'br': 'portugues', 'eua': 'ingles'}
print(type(linguas))

print(linguas)

print(linguas['br'])  # Consultando pela chave.

print(linguas.get('es'))
print(linguas.get('es', 'nao defenida'))  # Neste caso foi passado valor se a chave não for encontrada.

"""Todos os tipos de contraines podem ser consultados para verificar se ele contém determinado valor ou chave."""

print('br' in linguas)  # A resposta sempre será um booleano.

print(6 in list(range(10)))  # Consulta de elemento na lista.

"""Também podemos adicionar e alterar elementos em um dicionário já exustnete."""

linguas['es'] = 'spanhol'  # Adicionado um novo chave e valor, novo valor esta errado então vamo arruma-lo.
print(linguas['es'])

linguas['es'] = 'espanhol'  # Pronto alterado spanhol por espanhol.
print(linguas['es'])

"""O Dicionário também permite operaçẽs com interação, mais vai fica pro tópico 8."""
