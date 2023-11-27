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
Los bucles `for` permiten iterar sobre una secuencia, como una lista, un rango o una cadena de texto, ejecutando un bloque de código un número determinado de veces.

### Ejemplos de uso:
- **Iterando sobre un rango**:
  ```python
  for i in range(1, 6):
      print(i)
  ```
  Imprime los números del 1 al 5.

- **Iterando sobre una lista**:
  ```python
  frutas = ["manzana", "banana", "cereza"]
  for fruta in frutas:
      print(fruta)
  ```
  Recorre la lista de frutas e imprime cada elemento.

## Bucles `while`
El bucle `while` ejecuta un conjunto de instrucciones repetidamente mientras una condición sea verdadera. Es útil cuando no sabes cuántas veces necesitarás repetir una acción.

### Ejemplo de uso:
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```
Imprime los números del 0 al 4.

### Ejemplo Integrado
Combinamos sentencias condicionales y bucles en un programa práctico:

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