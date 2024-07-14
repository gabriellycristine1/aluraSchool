class Pessoa:
    def __init__(self,nome, idade, profissao):
        self.nome = nome
        self.idade = idade 
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} | {self.idade} anos | {self.profissao}'
    
    def aniversario(self):
        return self.idade +1
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, meu nome é {self.nome}, sou {self.profissao} e tenho {self.idade} anos'
        else:
            return f'Ola meu nome é {self.nome}!'
    
# pessoa = Pessoa('GABY', 21, 'desenvolvedora')
# print(pessoa.__str__())
# print(pessoa.aniversario())
# print(pessoa.saudacao)

pessoa1 = Pessoa('Alice',25,'Engenheira')
pessoa2 = Pessoa('Luiza',30,'Desenvolvedor')
pessoa3 = Pessoa('Jaque',22,None)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.idade = pessoa1.aniversario()
pessoa3.idade = pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)


