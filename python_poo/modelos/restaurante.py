from modelos.avaliacao import Avaliacao

class Restaurante:
    """
     Representa um restaurante e suas características.
    """

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self.categoria}'
    
    @classmethod 
    def list_restaurant(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)} | Avaliação')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {restaurante.media_avaliacoes}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '[x]' if self._ativo else '[]' 
    
    def alternar_status(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5:
            avaliacao =  Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
             

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return 'Sem avaliação'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_nota = len(self._avaliacao)
        media = round(soma_das_notas / qtd_nota,1)
        return media



    


