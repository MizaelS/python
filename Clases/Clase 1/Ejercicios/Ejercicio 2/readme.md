### Ejercicio 2: Convertidor de Temperaturas

#### Descripción:
Desarrolla un programa que permita al usuario convertir temperaturas entre grados Celsius y Fahrenheit.

#### Detalles:
1. **Selección del Tipo de Conversión**: El programa debe comenzar preguntando al usuario si desea convertir de Celsius a Fahrenheit o viceversa.
2. **Ingreso de la Temperatura**: Solicita al usuario que ingrese el valor de la temperatura a convertir.
3. **Cálculo de la Conversión**: 
    - Si es de Celsius a Fahrenheit, utiliza la fórmula \( F = C \times \frac{9}{5} + 32 \).
    - Si es de Fahrenheit a Celsius, utiliza \( C = (F - 32) \times \frac{5}{9} \).
4. **Mostrar Resultado**: Muestra la temperatura convertida en la consola.

#### Consideraciones:
- Usa `if`/`else` para manejar las diferentes opciones de conversión.
- Asegúrate de convertir el input del usuario a un número antes de realizar los cálculos.

#### Ejemplo de Salida:
```plaintext
Tipo de conversión seleccionada: Celsius a Fahrenheit
Ingrese la temperatura en Celsius: 25
La temperatura en Fahrenheit es: 77.0°F