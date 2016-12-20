class nodo():
    def __init__(self,obj):
        self.obj=obj
        self.sig=None

class pilaColaBase():
    def __init__(self):
        self.nodos=None

    def insertar(self,obj):
        actual=self.nodos
        if (actual is None):
            self.nodos=nodo(obj)
        else:
            while (actual.sig is not None):
                actual=actual.sig
            actual.sig=nodo(obj)

    def __len__ (self):
        num=0
        actual=self.nodos
        while actual is not None:
            num+=1
            actual=actual.sig
        return num

    def vacio(self):
        if self.__len__()==0:
            return True
        else:
            return False

class cola(pilaColaBase):
    def __init__(self):
        pilaColaBase.__init__(self)
                    
    def sacar(self):
        primero=self.nodos
        self.nodos=primero.sig
        return primero.obj

    def mirar(self):
        return self.nodos.obj

class pila(pilaColaBase):
    def __init__(self):
        pilaColaBase.__init__(self)
            
    def sacar(self):
        actual=self.nodos
        anterior=actual
        if (actual.sig is None):
            self.nodos=None
            return actual.obj
        else:
            while actual.sig is not None:
                anterior=actual
                actual=actual.sig
            anterior.sig=None
            return actual.obj
    
    def mirar(self):
        actual=self.nodos
        if (actual.sig is None):
            return actual.obj
        else:
            while actual.sig is not None:
                actual=actual.sig
            return actual.obj
          
##class persona():
##    def __init__ (self, nombre, edad):
##        self.nombre=nombre
##        self.edad=edad
##
##if (False):
##    cp=cola()
##    print ("Cola vacía?",cp.vacio())
##    cp.insertar(persona("Jose",12))
##    cp.insertar(persona("Pedro",13))
##    cp.insertar(persona("Diego",14))
##    print ("Cola vacía?",cp.vacio())
##    print(len(cp))
##    while (not cp.vacio()):
##        ind=cp.sacar()
##        print(ind.nombre)
##        print(len(cp))
##    cp.insertar(persona("Pedro",13))
##    print(len(cp))
##    ind=cp.mirar()
##    print (ind.nombre)
##else:
##    pp=pila()
##    print ("Pila vacía?",pp.vacio())
##    pp.insertar(persona("Jose",12))
##    pp.insertar(persona("Pedro",13))
##    pp.insertar(persona("Diego",14))
##    print ("Cola vacía?",pp.vacio())
##    print(len(pp))
##    while (not pp.vacio()):
##        ind=pp.sacar()
##        print(ind.nombre)
##        print(len(pp))
##    pp.insertar(persona("Pedro",13))
##    print(len(pp))
##    ind=pp.mirar()
##    print (ind.nombre)
##    print(len(pp))
##
