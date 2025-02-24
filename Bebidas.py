# Componente base
class Bebida:
    def obtener_descripcion(self):
        pass
    
    def calcular_precio(self):
        pass

# Componente concreto
class CafeSimple(Bebida):
    def obtener_descripcion(self):
        return "Café simple"
    
    def calcular_precio(self):
        return 1000

# Decorador base
class ComplementoBebida(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida
    
    def obtener_descripcion(self):
        return self.bebida.obtener_descripcion()
    
    def calcular_precio(self):
        return self.bebida.calcular_precio()

# Decoradores concretos
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

# Uso
mi_cafe = CafeSimple()
print(f"{mi_cafe.obtener_descripcion()} - ${mi_cafe.calcular_precio()}")
# Café simple - $1.000

mi_cafe_con_leche = Leche(mi_cafe)
print(f"{mi_cafe_con_leche.obtener_descripcion()} - ${mi_cafe_con_leche.calcular_precio()}")
# Café simple, con leche - $1.500

mi_cafe_completo = Canela(Azucar(Leche(mi_cafe)))
print(f"{mi_cafe_completo.obtener_descripcion()} - ${mi_cafe_completo.calcular_precio()}")
# Café simple, con leche, con azúcar, con canela - $2.000
