"""O método que vimos na aula 7 é um tipo de atributo da classe, mais ele não é o único, existem também os chamados
atributos de dados e na documentação original em inglês ele são chamados deary atributs e algumas outras linguagens eles
são chamados também de campos ou ainda quando falam em atributos a turma costuma a referir ao atributo de dado e quando
é método chamamos efetivamente de métodos, para criar então os atributos durante a criação na realidade eu tenho de
falar para você de um método especial, que o chamado dander init que é de inicialização em inglês.

Para criar então um atributo de objeto você vai utilizar o self e vai criar o seu atributo, uma forma de definir que um
campo existe mais não tem nem um valor que foi atribuido a ele é utilizar o valor nome de nulo."""




class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome

    def cumprimentar(self):
        return f'Olá{id(self)}'


if __name__ == '__main__':
    p = Pessoa('luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Renzo'
    print(p.nome)
