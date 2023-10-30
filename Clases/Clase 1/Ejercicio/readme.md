### Problema: Calculadora de Índice de Masa Corporal (IMC)

El Índice de Masa Corporal (IMC) es una manera simple y comúnmente utilizada para categorizar a las personas en grupos de peso: bajo peso, peso normal, sobrepeso u obesidad. El IMC se calcula utilizando la siguiente fórmula:

#### Tarea:

Desarrolla un programa en Python que realice lo siguiente:

1. Solicita al usuario que ingrese su nombre.
2. Solicita al usuario que ingrese su peso en kilogramos.
3. Solicita al usuario que ingrese su altura en metros.
4. Calcula el IMC utilizando la fórmula proporcionada.
5. Muestra el IMC del usuario en la consola, junto con un mensaje que indique la categoría de peso correspondiente según el IMC calculado:

   - Bajo peso: IMC < 18.5
   - Peso normal: 18.5 ≤ IMC < 24.9
   - Sobrepeso: 25 ≤ IMC < 29.9
   - Obesidad: IMC ≥ 30

#### Ejemplo de Salida:

```plaintext
╭────────────────────────────
│ Nombre: Juan
│ Peso: 70 kg
│ Altura: 1.75 m
│ IMC: 22.86
│ Categoría: Peso normal
╰────────────────────────────
```

#### Consejos:

- Recuerda convertir las entradas de texto a números para poder realizar cálculos.
- Utiliza f-strings para formatear la salida en la consola.
- Para mantener el formato y la precisión de los números, puedes utilizar la función `round()` para redondear el IMC a dos decimales, por ejemplo: `imc = round(imc, 2)`.