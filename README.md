# Transformador de Sistemas de Numeración

Programa de consola en Python para convertir números entre distintos sistemas de numeración: **binario**, **decimal** y **hexadecimal**. Incluye un historial de conversiones realizadas durante la sesión.

## Características

- Conversión **Binario → Decimal** (8 bits)
- Conversión **Decimal → Binario** (0 a 255)
- Conversión **Hexadecimal → Decimal** (2 dígitos)
- Conversión **Binario → Hexadecimal** (4 bits)
- Conversión **Decimal → Hexadecimal** (0 a 255)
- Historial de conversiones (ver y borrar)
- Validación de entradas (longitud y caracteres permitidos)

## Requisitos

- Python 3
- No necesita librerías externas

## Uso

```bash
python3 binario.py
```

Al ejecutarlo verás un menú interactivo:

```
1. Binario -> Decimal
2. Decimal -> Binario
3. Hexadecimal -> Decimal
4. Binario -> Hexadecimal
5. Decimal -> Hexadecimal
6. Historial
7. Borrar Historial
8. Salir
```

Ingresa el número de la opción deseada y sigue las instrucciones en pantalla.

### Ejemplo

```
Ingrese una de las opciones enumeradas; 1

_____Convertidor de Binario a Decimal._____
Ingrese un número binario: 00001010
Tú número binario 00001010, pasado a decimal es 10.
```

## Estructura del código

Todo el programa vive en un único archivo `Transformador_Sistemas_Númericos.py`, con un bucle principal `while True` que despacha la opción elegida a un bloque `if/elif` por cada conversión. Las conversiones usan tuplas de valores posicionales (`Prefijo_bin`, `prefijo_bin`) y diccionarios de mapeo (`prefijo_hexa`, `prefijo_Hexa`) para traducir entre sistemas.

## Limitaciones conocidas

- Las opciones 1 y 3 exigen longitudes fijas (8 y 2 caracteres respectivamente), por lo que no aceptan números binarios/hexadecimales con menos dígitos aunque sean válidos (ej. `101` no se acepta, hay que escribir `00000101`).
- El historial usa el valor de entrada como clave, así que una misma entrada repetida en distintas opciones se sobrescribe.

## Autor

Proyecto personal — Matias EF 🐍.
