import random

DADO_UNO = ['Fantasma', 'Alien', 'Bruja', 'Marioneta', 'Zombie', 'Vampiro', 'Pirata', 'Demonio', 'Cazador', 'Cancerbero', 'Hombre lobo', 'Momia']
DADO_DOS = ['Bosque', 'Iglesia', 'Cementerio', 'Atico', 'Cabaña abandonada', 'Fabrica abandonada', 'Egipto', 'Mansion embrujada', 'Isla desierta']
DADO_TRES = ['Boveda', 'Linterna', 'Cuchillo', 'Amuleto', 'Letra', 'Cuadro', 'Barco', 'Infierno', 'Sabana Africana', 'Mar']

def tirar_dados():
    print()
    print("1. ", random.sample(DADO_UNO, 1))
    print("2. ", random.sample(DADO_DOS, 1))
    print("3. ", random.sample(DADO_TRES, 1))

def main():
    print('\n<---🎲---🎲---🎲---🎲---🎲---🎲---🎲---🎲---🎲---🎲---🎲--🎲--🎲--🎲--🎲-->\n')
    print('\n             B I E N V E N I D     A    S T O R Y C U B E S')
    print('\n                          ')
    print('\n<---🎲---🎲---🎲---🎲---🎲---🎲---🎲---🎲---🎲---🎲---🎲--🎲--🎲--🎲--🎲-->\n')
    print('¡¡¡¡¡¡Tira los dados y escribe una historia corta usando las palabras que te salgan!!!!!!')
    print('Recuerda que "No estamos hechos de átomos, estamos hechos de historias"')
    exit = False

    while not exit:
        next = input("Tirar los dados ?  [S/N]: ")
        if next.lower() == "s":
            tirar_dados()
        else: 
            exit = True

    

if __name__ == '__main__':
    main()