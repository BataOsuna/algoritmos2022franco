from lista import Lista
from cola import Cola
from jurassic_park import dinosaurs

class Dinosaurios:

    def __init__(self,time, zone_code, dino_number, alert_level, nombre):
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level= alert_level
        self.nombre = nombre
        
    def __str__(self):
        return f"{self.time} | {self.zone_code} | {self.dino_number} | {self.alert_level} | {self.nombre}"


lista_dinosaurios = Lista()
lista_dinosaurios2 = Lista()
cola_herbi = Cola()
cola_carni = Cola()



file = open('C:/Users/franc/Desktop/Facultad 2022/Algoritmos/Algoritmos 2022/algoritmos_2022-main/alerts.txt')
lineas = file.readlines()



def busqueda(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name']
    



lineas.pop(0) 
for linea in lineas:
    datos = linea.split(';')
    datos[3] = datos[3][:-1]
    datos.append(busqueda(datos[2]))
    """ print(datos) """
    lista_dinosaurios.insertar(Dinosaurios(datos[0],
                                        datos[1],
                                        datos[2],
                                        datos[3],
                                        datos[4],),
                                campo = 'time')
    
    lista_dinosaurios2.insertar(Dinosaurios(datos[0],
                                           datos[1],
                                           datos[2],
                                           datos[3],
                                           datos[4],),
                                campo = 'nombre')
    

#!Determinar cual fue el ultimo dinosaurio descubierto  
print()                      
dato = 0
for dino in dinosaurs:
    dato_2 = int(dino['named_by'][-4:])
    if dato_2 > dato:
        dato = int(dino['named_by'][-4:])

for dino in dinosaurs:
    if dino['named_by'][-4:] == str(dato):
        print('El ultimo dinosaurio descubierto fue', dino['name'], 'y lo hizo', dino['named_by'])
print()


#!Listado ordenado por hora
print('Listado ordenado por hora')
lista_dinosaurios.barrido()
print()
#!Listado ordenado por nombre
print('Listado ordenado por nombre')
lista_dinosaurios2.barrido()



#! Eliminar la informacion de las siguientes zonas y modificar la zona de 'HYD195'
dato = lista_dinosaurios.busqueda('WYG075', 'zone_code')
lista_dinosaurios.eliminar(dato.info)
lista_dinosaurios.eliminar('SXH966', 'zone_code')
lista_dinosaurios.eliminar(dato.info)
lista_dinosaurios.eliminar('LYF010', 'zone_code')
lista_dinosaurios.eliminar(dato.info)
dato = lista_dinosaurios.busqueda('HYD195', 'zone_code')
dato.info.nombre = 'Mosasaurus'


dato = lista_dinosaurios2.busqueda('WYG075', 'zone_code')
lista_dinosaurios2.eliminar(dato.info)
lista_dinosaurios2.eliminar('SXH966', 'zone_code')
lista_dinosaurios2.eliminar(dato.info)
lista_dinosaurios2.eliminar('LYF010', 'zone_code')
lista_dinosaurios2.eliminar(dato.info)
dato = lista_dinosaurios2.busqueda('HYD195', 'zone_code')
dato.info.nombre = 'Mosasaurus'


#! Listado filtrado de los datos que solo incluya datos de los dinosaurios: Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con nivel critical o high.
print()
print('Listado de los dinosaurios Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con level critical o high')
lista_dinosaurios.barrido_level()
print()

#! Listado de toda la información de los dinosaurios Raptors y Carnotaurus; y los códigos de las zonas donde puedo encontrar dinosaurios Compsognathus.
print('Listado de los dinosaurios Raptors y Carnotaurus y los codigos de las zonas donde puedo encontrar Compsognathus')
lista_dinosaurios.barrido_zona()
print()        


#! Datos de los dinosaurios carnívoros en una cola y otra con los herbívoros, descartar las de nivel 'low' y 'medium'. Y la info de la zona EPC944
for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda(dato[2]))
    if (dato[3] != 'low' and dato[3] != 'medium'):
        aux = dato[4]
        for dino in dinosaurs:
            if (aux == dino['name'] and dino['type'] == 'carnívoro '):
                cola_carni.arribo(Dinosaurios(dato[0],
                                        dato[1],
                                        dato[2],
                                        dato[3],
                                        dato[4]))
            else:
                if (aux == dino['name'] and dino['type'] == 'herbívoro '):
                    cola_herbi.arribo(Dinosaurios(dato[0],
                                            dato[1],
                                            dato[2],
                                            dato[3],
                                            dato[4]))

print('Dinosaurios carnivoros a excepcion de los de nivel low o medium y los que pertenecen a la zona EPC944')
while (not cola_carni.cola_vacia()):
    dato = cola_carni.atencion()
    if (dato.zone_code != 'EPC944'):
        print(dato)
print()


print('Dinosaurios herbivoros a excepcion de los de nivel low o medium')
while (not cola_herbi.cola_vacia()):
    dato = cola_herbi.atencion()
    
    print(dato)
