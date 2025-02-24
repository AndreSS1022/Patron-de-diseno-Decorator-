
class Bebida:
    def obtener_descripcion(self):
        pass
    
    def calcular_precio(self):
        pass


class CafeSimple(Bebida):
    def obtener_descripcion(self):
        return "Café simple"
    
    def calcular_precio(self):
        return 1000


class ComplementoBebida(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida
    
    def obtener_descripcion(self):
        return self.bebida.obtener_descripcion()
    
    def calcular_precio(self):
        return self.bebida.calcular_precio()


class Leche(ComplementoBebida):
    def obtener_descripcion(self):
        return f"{self.bebida.obtener_descripcion()}, con leche"
    
    def calcular_precio(self):
        return self.bebida.calcular_precio() + 500

class Azucar(ComplementoBebida):
    def obtener_descripcion(self):
        return f"{self.bebida.obtener_descripcion()}, con azúcar"
    
    def calcular_precio(self):
        return self.bebida.calcular_precio() + 250

class Canela(ComplementoBebida):
    def obtener_descripcion(self):
        return f"{self.bebida.obtener_descripcion()}, con canela"
    
    def calcular_precio(self):
        return self.bebida.calcular_precio() + 250


mi_cafe = CafeSimple()
print(f"{mi_cafe.obtener_descripcion()} - ${mi_cafe.calcular_precio()}")

mi_cafe_con_leche = Leche(mi_cafe)
print(f"{mi_cafe_con_leche.obtener_descripcion()} - ${mi_cafe_con_leche.calcular_precio()}")

mi_cafe_completo = Canela(Azucar(Leche(mi_cafe)))
print(f"{mi_cafe_completo.obtener_descripcion()} - ${mi_cafe_completo.calcular_precio()}")

