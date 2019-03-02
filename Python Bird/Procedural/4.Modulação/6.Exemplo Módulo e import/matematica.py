def soma(parcela, parcela_2):
    return parcela + parcela_2

"""Iremos importa este script no executa_matematica e para que não imprima o print deste script usamos o dander name que
é o __name__ ."""
#print(__name__)
#print(soma(1, 2))

"""Quando executamos vemos que o script assima retorna __main__ e o print da soma. então com o retorno do __name 
sabemos que o script esta sendo executado do diretorio principal que é o nosso __main__ entáo podemos colocar no lugar
do print(__name ) uma condição de if"""

if __name__ == '__main__':
    print(soma(1, 2))
