# Explicación de `ft_ancient_text.py`

`ft_ancient_text.py` recibe la ruta de un archivo por terminal, lo abre,
muestra su contenido y maneja errores sin cerrar el programa inesperadamente.

## 1. Importaciones

```python
import sys
import typing
```

- `sys.argv` contiene los argumentos recibidos al ejecutar el programa.
- `typing` se usa para indicar el tipo del archivo abierto.

## 2. Comprobación de argumentos

```python
if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
```

`sys.argv` siempre incluye el nombre del propio script. Por ejemplo:

```sh
python3 ft_ancient_text.py archivo.txt
```

produce:

```python
sys.argv == ["ft_ancient_text.py", "archivo.txt"]
```

Por eso deben existir exactamente dos elementos. Si falta la ruta, se muestra
cómo usar el programa.

## 3. Función principal

```python
def recover_file(file_name: str) -> None:
```

- `file_name: str`: recibe una ruta como texto.
- `-> None`: la función no devuelve un valor; muestra información en pantalla.

## 4. Variable del archivo

```python
file: typing.IO[str] | None = None
```

Antes de abrirlo no hay archivo, así que vale `None`.

Si `open()` funciona, `file` pasa a contener un objeto de archivo de texto,
representado aquí como `typing.IO[str]`.

## 5. Apertura y lectura

```python
file = open(file_name, "r")
content: str = file.read()
```

- `"r"` significa modo lectura.
- `read()` obtiene todo el contenido y lo guarda en `content`.
- Si el archivo no existe o no hay permisos, `open()` lanza un error de tipo
  `OSError`.

## 6. Mostrar el contenido

```python
print(content, end="" if content.endswith("\n") else "\n")
```

Si el texto ya termina con salto de línea, no añade otro. Si no lo tiene,
añade uno para que el mensaje posterior no quede pegado a la última línea del
archivo.

## 7. Gestión de errores

```python
except OSError as error:
    print(f"Error opening file '{file_name}': {error}")
```

Si no se puede abrir o leer el archivo, el programa muestra el error y no se
cierra de forma inesperada.

## 8. Cierre garantizado

```python
finally:
    if file is not None:
        file.close()
        print(f"File '{file_name}' closed.")
```

`finally` se ejecuta tanto si todo sale bien como si ocurre un error.

La condición evita intentar cerrar un archivo que nunca se abrió. Si se abrió
correctamente, `close()` libera el recurso.

## 9. Punto de entrada

```python
if __name__ == "__main__":
```

Este bloque se ejecuta solo cuando lanzas el archivo directamente con Python,
no cuando otro archivo lo importa.
