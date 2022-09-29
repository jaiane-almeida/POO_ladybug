
class Herois:

    def __init__(self, nome, idade, poder, miraculous):
        self.nome = nome
        self.idade = idade
        self.poder = poder
        self.miraculous = miraculous
        self.__ID_vilao = 'Gabriel Agreste' #encapsulamento


    def bichinho (self, kwami, idade_k):
        self.kwami = kwami
        self.idade_k = idade_k
        return('os kwamis são as criaturas magicas mais fofas de todas! Principalmente o: ')

    # herança
class Ladybug(Herois):
    def __init__(self):
        super().__init__('marinette', 14, 'poder da criação','joaninha') #polimorfismo
        self.kwami = 'Tikki'
        self.idade_k = 5000 #podemos fazer assim ou do jeito que vou colocar no catnoir

    def objeto(self):
        print('meu miraculous é disfarçado de brinco')
        return super().bichinho('tikki', 5000) + (f'{self.kwami}')


portador1 = Ladybug()
print(portador1.objeto())

class Catnoir(Herois):
     def __init__(self):
         super().__init__('Adrien', 14,'poder da destruição', 'gato')
         self.kwami = 'blag'


     def objeto2(self):
         print('meu miraculous é disfarçado de anel')
         return super().bichinho('blag', 5000) + (f'{self.kwami}') #polimorfismo

portador2 = Catnoir()
print(portador2.objeto2())

class Vilao(Herois):
    def __init__(self):
        print('Gabriel Agreste é o portador do miraculous da borboleta')
        print(self.__ID.Vilao)

portador3 = Herois('hawk moth', '??', 'manipulação', 'borboleta')
print(f'o vilão é atendido por {portador3.nome} e não sabemos sua identidade')

