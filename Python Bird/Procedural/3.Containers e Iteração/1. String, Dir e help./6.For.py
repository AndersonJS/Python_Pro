"""Nesse tópico será apresentado o For. Ele é o tipo de laço de iteração mais utilizado em Python. Para melhor
intendimento ele será utilizado para acessar todos os elementos de um container e pode compartilhar o codigo gerado com
o do tópico anterior, feito com laço while."""

nome = 'Anderson'
i = 0

while i < len(nome):
    print(nome[i])
    i += 1

print('-' * 10)

for v in nome:
    print(v)

print('¨'*10)

for i in range(len(nome)):
    print(i, nome[i])

print('='*10)

for i, v in enumerate(nome):
    print(i, v)
print()
print('FIM FOR.')