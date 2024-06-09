class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurante_praca.nome = 'Bistro'
restaurante_praca.categoria = 'Italiana'

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True


restaurantes = [restaurante_praca,restaurante_pizza]

print(vars(restaurante_praca))
print(restaurante_praca.nome)

if restaurante_praca.ativo:
    print(f'{restaurante_praca.nome} esta ativo')
else:
    print(f'{restaurante_praca.nome} esta inativo')

print(vars(restaurante_pizza))

