# Lab_Criptografia

## hash.py


El programa hash.py recibe como entrada un string o un archivo txt y luego muestra por consola el hash obtenido. Es necesario importar fileinput.
Este progrma fue probado en ubuntu.
La funcion hash acepta caracteres Unicode, sin embargo, el caracter \ no es aceptado solo al final de una palabra unica. Esto es debido a que resulta ser un caracter especial, con la funcionalidad de realizar saltos de linea o para agregar rutas.

**Ejemplos:**

Se debe ingresar el siguiente comando en una terminal ubicada en la direccion donde se encuentre hash.py.

``python3 hash.py -h palabra``

En el caso de ingresar un archivo de texto, seria el siguiente comando.

``python3 hash.py -a archivo.txt ``

En el caso de calcular la entropia de una palabra unica.

``python3 hash.py -e -h palabra ``

En el caso de calcular la entropia de un archivo txt.

``python3 hash.py -e -a archivo.txt ``
