class Pessoa:
    def __init__(self):
        self.nome = None

    def cumprimentar(self):
        return f'Olá Mundo {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    p.nome = 'Paulo'
    print(p.nome)