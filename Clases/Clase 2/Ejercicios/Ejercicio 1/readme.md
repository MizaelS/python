### Ejercicio 1: Verificador de Palabras Palíndromas

#### Descripción:
Un palíndromo es una palabra o frase que se lee igual hacia adelante y hacia atrás, ignorando los espacios, signos de puntuación y mayúsculas. Desarrolla un programa que determine si una palabra o frase ingresada por el usuario es un palíndromo.

#### Tareas Detalladas:
1. Solicita al usuario que ingrese una cadena de texto.
2. Elimina los espacios y convierte el texto a minúsculas (o mayúsculas) para una comparación uniforme.
3. Invierte el texto y compáralo con el original.
4. Usa sentencias condicionales para determinar si el texto es un palíndromo.
5. Imprime el resultado.

#### Ejemplo de Salida:
```plaintext
╭────────────────────────────
│ Texto ingresado: Anilina
│ 'Anilina' es un palíndromo.
╰────────────────────────────
```

#### Consejos:
- Recuerda que en Python, el slicing `[::-1]` puede usarse para invertir una cadena.
- Es importante normalizar la cadena (espacios, mayúsculas/minúsculas) antes de la comparación.