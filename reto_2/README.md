# Reto 2: Objeto algebraico

### Requisitos para ejecución 🔧

Para ejecutar el resultado de este reto, es necesario instalar Python junto con
numpy.

Si aún no tienes una versión de Python disponible en tu equipo, dirígete al siguiente 
link: https://www.python.org/downloads/

Si cuentas con una versión de Python pero no tiene instalado el paquete de numpy, ejecuta
en una línea de comandos (CMD) la siguiente sentencia

```
pip install --upgrade numpy
```

### Explicación de la implementación

El script 'objeto_algebraico.py' contiene la interfaz y la clase concreta del objeto algebraico.
Allí, se implementan las operaciones de suma, resta, multiplicación escalar, multiplicación
entre polinomios y evaluación de polinomios para un objeto algebraico. Estas operaciones
se implementan a través de los objetos poly1d de numpy. Además, se permite realizar
operaciones suma, resta y multiplicación entre objetos algebraicos. 

Finalmente, el script 'objeto_algebraico.py' puede ejecutarse para desplegar un caso de prueba
donde se muestra el funcionamiento de cada una de las operaciones. Los resultados de este caso de prueba se muestran en la siguiente imagen:

![alt text](https://github.com/DavidMosquera/prueba_tecnica_ULTRACOM/blob/v4_reto2/reto_2/caso_de_prueba.png)
