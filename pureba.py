class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pila = []
        self.tope = 0

    def insertar(self, elemento):
        if self.tope < self.capacidad:
            self.pila.append(elemento)
            self.tope += 1
            print(f"Insertar({elemento}) -> Pila: {self.pila}, Tope: {self.tope}")
        else:
            print(f"Error: Desbordamiento al intentar insertar {elemento}")

    def eliminar(self):
        if self.tope > 0:
            elemento = self.pila.pop()
            self.tope -= 1
            print(f"Eliminar() -> Se eliminó: {elemento}, Pila: {self.pila}, Tope: {self.tope}")
        else:
            print("Error: Subdesbordamiento, no hay elementos para eliminar")

# Crear la pila con capacidad de 8 elementos
pila = Pila(8)

# Operaciones
pila.insertar('X')  # Insertar X
pila.insertar('Y')  # Insertar Y
pila.eliminar()     # Eliminar Z (elimina Y)
pila.eliminar()     # Eliminar T (elimina X)
pila.eliminar()     # Eliminar U (pila vacía - error)
pila.insertar('V')  # Insertar V
pila.insertar('W')  # Insertar W
pila.eliminar()     # Eliminar p (elimina W)
pila.insertar('R')  # Insertar R
