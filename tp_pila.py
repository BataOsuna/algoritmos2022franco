

from cmath import pi
from pila import Pila


#! Ejercicio 19

dic = [{'titulo': 'spiderman', 'estudio': 'warner', 'año': '2014'},
{'titulo': 'matrix', 'estudio': 'warner', 'año': '2014'},
{'titulo': 'vengadores', 'estudio': 'marvel', 'año': '2014'},
{'titulo': 'dr Strange', 'estudio': 'marvel', 'año': '2016'},
{'titulo': 'black widow', 'estudio': 'marvel', 'año': '2016'},
{'titulo': 'the flash', 'estudio': 'dc', 'año': '2018'},
{'titulo': 'escudadron suicida', 'estudio': 'DC', 'año': '2018'},
{'titulo': 'batman', 'estudio': 'dc', 'año': '2019'}
]


pila1 = Pila()

''' for i in dic:
    pila1.apilar(i)
cont = 0
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    if(dato['año'] == '2014' ):
        print('Las peliculas estrenadas en 2014', dato['titulo'])
    if(dato['año'] == '2018'):
        cont += 1
    if(dato['estudio'] == 'marvel' and dato['año'] == '2016'):
        print('Las peliculas de marvel estrenadas en 2016 son', dato['titulo'])

print('en 2018 se estrenaron', cont, 'peliculas') '''
    


#!Ejercicio 24

dic = [{'Nombre' : 'Hugo', 'cantidad peliculas': '2'},
{'Nombre' : 'Pablo', 'cantidad peliculas': '4'},
{'Nombre' : 'Gabriela', 'cantidad peliculas': '5'},
{'Nombre' : 'Rocket Raccoon', 'cantidad peliculas': '1'},
{'Nombre' : 'Groot', 'cantidad peliculas': '3'},
{'Nombre' : 'Gaston', 'cantidad peliculas': '6'},
{'Nombre' : 'Daniela', 'cantidad peliculas': '7'},
{'Nombre' : 'Carlos', 'cantidad peliculas': '9'},
{'Nombre' : 'Viuda negra', 'cantidad peliculas': '3'},
]

iniciales = {'C', 'D', 'G'}

for i in dic:
    pila1.apilar(i)

cont = 0
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    if(dato['cantidad peliculas'] > '5'):
        print(dato['Nombre'])
        print('aparece en', dato['cantidad peliculas'], 'peliculas')
    if(dato['Nombre'] == 'Viuda negra'):
        print('la viuda negra participo en', dato['cantidad peliculas'], 'peliculas')
   



