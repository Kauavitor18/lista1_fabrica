

class Garrafa:
    def __init__(self, tamanho, cor, marca):
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca

    def __str__(self):
        return f'tamanho: {self.tamanho}, marca: {self.marca}'

class GarrafaDeVidro(Garrafa):
    def quebrar(self):
        print('crack')


garrafa = Garrafa(200, 'preto', 'Stanley')

garrafa_de_vidro = GarrafaDeVidro(200, 'transparente', 'vidro')




print(garrafa_de_vidro.__str__())