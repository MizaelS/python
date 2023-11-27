# Clase 2: Estructuras de Control de Flujo en Python

En esta clase, profundizaremos en las estructuras de control de flujo en Python, que son cruciales para la creación de programas dinámicos y funcionales. Nos centraremos en las sentencias condicionales y los bucles, herramientas esenciales para que los programas tomen decisiones y repitan acciones bajo ciertas condiciones.

## Índice
1. [Sentencias Condicionales](#sentencias-condicionales)
2. [Bucles `for`](#bucles-for)
3. [Bucles `while`](#bucles-while)

## Sentencias Condicionales
Las sentencias condicionales (`if`, `elif`, `else`) permiten dirigir el flujo de un programa basándose en la evaluación de condiciones. Son esenciales para la toma de decisiones en la programación.

### `if`, `elif`, y `else`
- **`if`**: Es la estructura básica para evaluar una condición. Si la condición es verdadera, se ejecuta el bloque de código que sigue.
- **`elif` (else if)**: Se utiliza después de un `if` para evaluar otra condición, en caso de que la condición del `if` sea falsa.
- **`else`**: Se usa después de un `if` o `elif` para definir un bloque de código que se ejecuta cuando las condiciones anteriores no se cumplen.

### Ejemplo de uso:
```python
numero = int(input("Ingrese un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
```
Este código evalúa si un número es positivo, negativo o cero.

## Bucles `for`
Los bucles `for` son una forma eficiente de ejecutar un bloque de código repetidamente para cada elemento en una secuencia, como un rango, una lista o una cadena de texto.

### Conceptos Clave:
- **Iteración**: Es el proceso de ejecutar un conjunto de instrucciones repetidamente.
- **Secuencia**: Puede ser cualquier objeto en Python sobre el que se pueda iterar, como listas, tuplas, diccionarios, conjuntos y cadenas.
- **Rango**: El uso de `range()` en bucles `for` es común para generar secuencias de números.

### Ejemplos de uso:
- **Iterar sobre una lista**:
  ```python
  colores = ["rojo", "verde", "azul"]
  for color in colores:
      print(color)
  ```
  Este código recorre cada elemento en la lista `colores` y lo imprime.

- **Uso del rango**:
  ```python
  for i in range(10):
      print(i)
  ```
  Imprime los números del 0 al 9.

## Bucles `while`
Los bucles `while` repiten un bloque de código mientras una condición especificada sea verdadera. Son ideales para situaciones donde no se conoce de antemano el número de veces que se repetirá el bloque.

### Conceptos Clave:
- **Condición de Control**: El bucle se ejecuta mientras esta condición sea verdadera.
- **Potencial de bucle infinito**: Es importante modificar la variable de control dentro del bucle para evitar repeticiones infinitas.

### Ejemplos de uso:
- **Estructura básica**:
  ```python
  contador = 0
  while contador < 5:
      print(contador)
      contador += 1
  ```
  Imprime los números del 0 al 4. La condición `contador < 5` controla el número de iteraciones.

### Ejemplo Integrado
Utilizamos tanto bucles como sentencias condicionales en un ejemplo práctico:

```python
# Solicitamos un número al usuario
numero = int(input("Ingrese un número: "))

# Verificamos si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Contamos hasta el número ingresado con un bucle while
contador = 1
while contador <= numero:
    print(contador)
    contador += 1
```