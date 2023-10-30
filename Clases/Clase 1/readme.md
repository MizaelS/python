```markdown
# Clase 1: Inputs, Variables y Prints en Python

En esta clase, aprenderemos sobre cómo obtener datos del usuario, almacenar estos datos en variables y mostrarlos en la consola utilizando la función `print`.

## Índice
1. [Variables](#variables)
2. [Inputs](#inputs)
3. [Prints](#prints)

## Variables
Las variables en Python son utilizadas para almacenar información que puede ser referenciada y manipulada en nuestro programa. La asignación de una variable se realiza utilizando el signo igual (`=`).

```python
nombre = "Juan"
edad = 25
estatura = 1.75
```

## Inputs
La función `input()` permite solicitar al usuario que ingrese datos. Por defecto, `input()` retorna los datos como una cadena de texto (str).

```python
nombre = input("Ingrese su nombre: ")
```

Para obtener datos numéricos, es necesario convertir el texto ingresado a un número utilizando `int()` para números enteros o `float()` para números de punto flotante.

```python
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en metros: "))
```

## Prints
La función `print()` se utiliza para mostrar datos en la consola. Podemos mostrar texto y también valores de variables utilizando f-strings.

```python
print("Hola, mi nombre es Juan.")
print(f"Tengo {edad} años y mido {estatura} metros.")
```

En el caso de las f-strings, las variables se colocan entre llaves `{}` y se muestran en el lugar correspondiente dentro del texto.

### Ejemplo Integrado

A continuación, se presenta un ejemplo que integra los conceptos de variables, inputs y prints:

```python
# Solicitamos datos al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en metros: "))

# Mostramos los datos en consola
print("╭────────────────────────────")
print(f"│ Su nombre es: {nombre}")
print(f"│ Su edad es: {edad}")
print(f"│ Su estatura es: {estatura}")
print("╰────────────────────────────")