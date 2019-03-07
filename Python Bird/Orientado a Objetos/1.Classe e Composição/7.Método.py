"""Continuando com nosso estudo mais detalhado sobre as classes, que lhe mostra o primeiro elemento importante da classe
o primeiro atributo que é o chamado método.
    Um metodo nada mais é do que uma função que pertence a uma classe e portanto sempre esta conectada a um objeto,para
    definir o método, você vai no corpo da classe também utilizar o def."""


class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))  # Esta é uma forma não usual em Python.
    print(id(p))
    print(p.cumprimentar())  # Em geral se executa um método utilizando o proprio objeto que é p.
