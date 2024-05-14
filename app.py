from modelos.restaurante import Restaurante

reataurante_praca = Restaurante('praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'mexicana')
restaurante_japones = Restaurante('Japa', 'japonesa')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()