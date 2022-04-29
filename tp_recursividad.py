#! Ejercicio 5: convertir un numero romano a decimal.


''' romanos = {'M': 1000, 'D': 500, 'C': 100,'L': 50, 'X': 10, 'V': 5, 'III': 3, 'II': 2, 'I': 1}



def romano_a_decimal(num_romano):
    if(len(num_romano) == 1):
        return romanos[num_romano]
    else:
        if(romanos[num_romano[0]] >= romanos[num_romano[1]]):
            return romanos[num_romano[0]] + romano_a_decimal(num_romano[1:])
        else:
            return - romanos[num_romano[0]] + romano_a_decimal(num_romano[1:])
        
print(romano_a_decimal('XVL')) '''



#! Ejercicio 22: la mochila del Jedi.

''' mochila = ['capa', 'escudo','sable de luz', 'pistola laser', 'granadas', 'casco', 'comida' ]


def usar_la_fuerza(vector, buscado):
    if(len(vector) == 0):
        return -1
    elif(buscado == vector[-1]):
        return len(vector)-1
    else:
        return usar_la_fuerza(vector[:-1], buscado)


print(usar_la_fuerza(mochila, 'sable de luz')) '''

''' mochila = ['Pan', 'Capa', 'Sable de luz', 'otro']

def usar_fuerza(mochila, pos):
    if(pos< len(mochila)):
        if(mochila[pos] == 'Sable de luz'):
            return ('Fueron sacados', pos, 'objetos hasta encontrar el Sable de luz')
        else:
            return usar_fuerza(mochila, pos+1)
    else:
        return -1

print(usar_fuerza(mochila, 0)) '''


#!Ejercicio 23 

''' def salida_laberinto(matriz, x, y, caminos=[]):
    """Salida del laberinto."""
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 2):
            caminos.append([x, y])
            print("Saliste del laberinto")
            print(caminos)
            caminos.pop()
        elif(matriz[x][y] == 1):
            matriz[x][y] = 3
            caminos.append([x, y])
            # print("mover este")
            salida_laberinto(matriz, x, y+1, caminos)
            # print("mover oeste")
            salida_laberinto(matriz, x, y-1, caminos)
            # print("mover norte")
            salida_laberinto(matriz, x-1, y, caminos)
            # print("mover sur")
            salida_laberinto(matriz, x+1, y, caminos)
            caminos.pop()
            matriz[x][y] = 1


lab = [[1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 1],
       [0, 1, 1, 0, 1, 0, 1],
       [1, 0, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 2]]

salida_laberinto(lab, 0, 0) '''

