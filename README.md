# Funciones-R6
A continuacion se veran los 6 codigos pedidos en el reto


### 1.Dado la figura de la imagen, desarrolle:
![68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67](https://github.com/user-attachments/assets/da9e14ba-e715-4c77-834b-413466c17180)
- Una función matemática para calcular el volumen y el área superficial.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
- Revise como utilizar el valor de pi usando import math y math.pi
### 2.Dado la figura de la imagen, desarrolle:
![68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67](https://github.com/user-attachments/assets/2afc883c-f38f-408a-b4d8-8d9ab78888db)
- Una función matemática para calcular el área y el perimetro.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
- Revise como utilizar el valor de pi usando import math y math.pi
### 3.Diseñar
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
### 4.Evación de impuestos (Nah mentira, solo impuestos :c)
Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
### 5.Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
- El promedio
- La mediana
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número

## Explicacion de "reduce" y "lambda" del programa del punto 5 (Extra)
-El lambda en Python es una forma de crear funciones anónimas o funciones pequeñas de manera concisa. En lugar de definir una función con def, se puede usar lambda para crear una función en una sola línea.

-La función reduce() en Python se utiliza para aplicar una operación acumulativa a los elementos de un iterable (como una lista o tupla) de manera secuencial, reduciéndolos a un único valor

Sintaxis:
´´´python
lambda argumentos: expresión

reduce(función, iterable, [valor_inicial])
´´´
´´´python
from functools import reduce

suma = lambda x, y: x + y
print(suma(3, 4))  # Imprime 7

mi_lista = [5, 6, 7, 8, 9]
p_multiplicativo=reduce(lambda x, y: x * y, mi_lista) # "mi_lista" sera el valor iterable y "valor_inicial" sera el primer valor de esa lista
print(p_multiplicativo)
´´´
Explicación proceso "reduce":

* En la primera iteración, lambda x, y: x * y se aplica a los primeros dos números de la lista: 5 y 6. El resultado es 30.
* En la segunda iteración, se aplica la función al resultado anterior (30) y al  siguiente número de la lista (7): 30 * 7 = 210.
* Este proceso se repite para todos los elementos de la lista, y al final el resultado es 15120.
