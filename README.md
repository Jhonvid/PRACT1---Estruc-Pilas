# PRACT1---Estruc-Pilas
El problema pide dibujar los distintos estados de la pila después de cada operación, con el puntero que indica el tope de la pila, y determinar si hay desbordamiento (overflow) o subdesbordamiento (underflow).

Conceptos clave:
- Pila (Stack): Estructura de datos que funciona bajo el principio LIFO (Last In, First Out), es decir, el último elemento insertado es el primero en ser eliminado.
- Tope (Top): Indica la posición del último elemento en la pila. Inicialmente, el tope está en 0 porque la pila está vacía.
- Operaciones de una pila:
  - Push (Insertar): Añade un elemento al tope de la pila.
  - Pop (Eliminar): Remueve el elemento del tope de la pila.

Resultado de las operaciones:

1. Insertar (PILA, X):
   - Estado de la pila: ['X']
   - Tope: 1

2. Insertar (PILA, Y):
   - Estado de la pila: ['X', 'Y']
   - Tope: 2

3. Eliminar (PILA, Z):
   - Elimina Y (último en entrar)
   - Estado de la pila: ['X']
   - Tope: 1

4. Eliminar (PILA, T):
   - Elimina X
   - Estado de la pila: [] (vacía)
   - Tope: 0

5. Eliminar (PILA, U):
   - Error: Subdesbordamiento, no hay elementos para eliminar.
   - Estado de la pila: [] (sigue vacía)
   - Tope: 0

6. Insertar (PILA, V):
   - Estado de la pila: ['V']
   - Tope: 1

7. Insertar (PILA, W):
   - Estado de la pila: ['V', 'W']
   - Tope: 2

8. Eliminar (PILA, p):
   - Elimina W
   - Estado de la pila: ['V']
   - Tope: 1

9. Insertar (PILA, R):
   - Estado de la pila: ['V', 'R']
   - Tope: 2

Resultado final:
- Número de elementos en la pila: 2 ['V', 'R']
- Hubo un error de subdesbordamiento: Sí, ocurrió en la operación (e) cuando se intentó eliminar de una pila vacía.
- No hubo desbordamiento porque nunca se intentó insertar más de 8 elementos.
"""
