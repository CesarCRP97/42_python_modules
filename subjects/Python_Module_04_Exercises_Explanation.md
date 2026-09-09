# Módulo 04 — explicación de los ejercicios

El módulo trata operaciones con archivos, flujos de entrada/salida y manejo de
errores. Los programas deben usar Python 3.10+, cumplir `flake8`, incluir
anotaciones de tipo y gestionar excepciones sin terminar inesperadamente.

Antes del ejercicio 3 no se puede usar `with`. La estructura esencial de las
salidas de los ejemplos debe conservarse.

## Ejercicio 0 — `ft_ancient_text.py`

Objetivo: leer un archivo indicado por línea de comandos y mostrar su contenido
como `cat`.

Debe:
- Mostrar el uso si no se recibe un nombre de archivo.
- Abrir el archivo, leerlo y mostrar cabeceras y pies como en el ejemplo.
- Informar errores de apertura o acceso, como archivo inexistente o sin
  permisos.
- Cerrar el archivo explícitamente.
- Poder explicar que `open()` devuelve un flujo de archivo de texto; en tiempo
  de ejecución suele ser un `TextIOWrapper`.

## Ejercicio 1 — `ft_archive_creation.py`

Parte del ejercicio 0 y añade creación de archivos.

Debe:
- Leer y mostrar el archivo de entrada con el mismo tratamiento de errores.
- Transformar el contenido añadiendo `#` al final de cada línea y mostrarlo.
- Pedir un nombre de archivo de salida; si se deja vacío, no guardar nada.
- Si se proporciona un nombre, crear el archivo o sobrescribirlo y confirmar el
  guardado.

## Ejercicio 2 — `ft_stream_management.py`

Parte del ejercicio 1 y trabaja explícitamente con los tres flujos estándar.

Debe:
- Enviar los mensajes de error al flujo de error estándar (`stderr`) con el
  prefijo indicado en el ejemplo.
- Obtener el nombre de salida sin usar la función `input()`; debe usarse la
  entrada estándar (`stdin`).
- Mantener la lectura, transformación y guardado del ejercicio anterior.
- Usar salida estándar (`stdout`) cuando sea necesario para mensajes y prompt.

## Ejercicio 3 — `ft_vault_security.py`

Introduce el gestor de contexto `with` para cerrar archivos automáticamente,
incluso si ocurre un error.

Debe definir `secure_archive()` con:
- Un nombre de archivo obligatorio.
- Una acción opcional de lectura o escritura, representada por `int` o `str`.
- Un contenido opcional para la escritura.
- Un retorno de tipo `tuple[bool, str]`: el booleano indica éxito y el texto
  contiene el archivo leído, el contenido escrito o el mensaje de error.

Durante la evaluación pueden pedir explicar operaciones con archivos, manejo de
errores y cómo `with` evita fugas de recursos.
