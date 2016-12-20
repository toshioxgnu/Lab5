#Jose Gonzalez Riquelme CI: 18247430-4

import cola
import time
import random

class cliente(object):
    def __init__(self,numeroDeItems, horaActual, minutoActual):
        self.numeroDeItems=numeroDeItems
        self.horaActual=horaActual
        self.minutoActual=minutoActual

class caja(cola.cola):
    # Las cajas heredan de cola
    def __init__ (self):
        cola.cola.__init__(self)
        self.clientesAtendidos=0
        self.minutosDeAtencion=0

def crearClientes(horaActual,minutoActual):
    # probabilidad que llegue un cliente a esta hora
    if (random.random()>0.35):
        # buscar la caja mas vacia
        cajaMasVacia=caja1
        cantidadClientesCajaMasVacia=len(caja1)
        if cantidadClientesCajaMasVacia>len(caja2):
            cajaMasVacia=caja2
            cantidadClientesCajaMasVacia=len(caja2)
        if cantidadClientesCajaMasVacia>len(caja3):
            cajaMasVacia=caja3
            cantidadClientesCajaMasVacia=len(caja3)
        if cantidadClientesCajaMasVacia>len(caja4):
            cajaMasVacia=caja4
            cantidadClientesCajaMasVacia=len(caja4)

        # Cargar un cliente nuevo a la caja mas vacia
        cantidadDeItems=random.randint(20,100)
        cajaMasVacia.insertar(cliente(cantidadDeItems, horaActual, minutoActual))

def atenderClientes(cajaActual):
    if len(cajaActual) > 0:
        cajaActual.mirar().numeroDeItems -= 10
        cajaActual.minutosDeAtencion += 1
        if cajaActual.mirar().numeroDeItems <= 0 :
            cajaActual.sacar()
            cajaActual.clientesAtendidos += 1
    return cajaActual.clientesAtendidos

# Crear las cajas del supermercado
caja1=caja()
caja2=caja()
caja3=caja()
caja4=caja()

# Horario de funcionamiento
horaActual=9
horaCierre=21
minutoActual=0

# Ciclo principal, funciona mientras estén las puertas abiertas
# y hayan todavía clientes en alguna de las colas
while horaActual<horaCierre or len(caja1)>0 or len(caja2)>0 or len(caja3)>0 or len(caja4)>0:
    # cargar clientes a la cola mas corta
    if horaActual<horaCierre:
        crearClientes(horaActual, minutoActual)

    # atender clientes
    c1=atenderClientes(caja1)
    c2=atenderClientes(caja2)
    c3=atenderClientes(caja3)
    c4=atenderClientes(caja4)

    #Clientes totales
    ct=c1+c2+c3+c4

    # incremento de la hora
    minutoActual+=1
    if minutoActual==60:
        horaActual+=1
        minutoActual=0

    # Impresion de la hora y de la cantidad de clientes por caja
    print("%i:%i\t%i\t%i\t%i\t%i" % (horaActual,minutoActual,len(caja1),len(caja2),len(caja3),len(caja4)))
    #time.sleep(0.1)

    # fin de la simulación forzoso
    if (horaActual==24):
        break

# Resultado de la simulacion
if len(caja1)==0 and len(caja2)==0 and len(caja3)==0 and len(caja4)==0:
    print ("Clientes atendidos en el dia" ,ct )
    print("La caja1 vendio ",caja1.minutosDeAtencion*10, "productos")
    print ("La caja2 vendio",caja2.minutosDeAtencion*10, "productos")
    print ("La caja3 vendio",caja3.minutosDeAtencion*10, "productos")
    print ("La caja4 vendio",caja4.minutosDeAtencion*10, "productos")

    print ("Cada cliente espero en la caja1.",int(caja1.minutosDeAtencion/caja1.clientesAtendidos), "minutos")
    print ("Cada cliente espero en la caja2.",int(caja2.minutosDeAtencion/caja2.clientesAtendidos), "minutos")
    print ("Cada cliente espero en la caja3.",int(caja3.minutosDeAtencion/caja3.clientesAtendidos), "minutos")
    print ("Cada cliente espero en la caja4.",int(caja4.minutosDeAtencion/caja4.clientesAtendidos), "minutos")
    print ("Su supermercado es muy eficiente y la gente está feliz")
else:
    print("Su supermercado no sirve, ya que todavía queda gente sin atender")
