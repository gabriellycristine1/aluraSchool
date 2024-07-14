
from modelos.restaurante import Restaurante

# restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
resturante_japones = Restaurante('Japa', 'Japonesa')

resturante_japones.receber_avaliacao('Gui', 10)
resturante_japones.receber_avaliacao('lais', 8)
resturante_japones.receber_avaliacao('emy', 5)



def main():
    Restaurante.list_restaurant()


if __name__ == '__main__':
    main()