
class Asiento:
    def __init__ (self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self,cambio):
        if cambio == "blanco" or cambio == "negro" or cambio == "amarillo" or cambio == "verde" or cambio == "rojo":
            self.color = cambio

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,num):
        self.registro = num

    def asignarTipo(self,Tipo):
        if Tipo == "electrico" or Tipo == "gasolina":
            self.tipo = Tipo

class Auto:
    cantidadCreados = 0
    def __init__ (self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        contador = 0
        for n in range(0, len(self.asientos), 1):
            if self.asientos[n] != None:
                contador = contador + 1
        return contador
    
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for l in range (0, len(self.asientos),1):
                if self.asientos[l] != None:
                    if self.asientos[l].registro != self.registro:
                        print("Las piezas no son originales")
                    else:
                        print("Auto original")
        else:
            print("Las piezas no son originales")