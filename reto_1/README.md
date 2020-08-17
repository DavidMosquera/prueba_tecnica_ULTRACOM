# Reto 1: Simulador de posiciones

### Requisitos para ejecución 🔧

Para ejecutar el resultado de este reto, es necesario instalar Python junto con
numpy y tkinter.

Si aún no tienes una versión de Python disponible en tu equipo, dirígete al siguiente 
link: https://www.python.org/downloads/

Si cuentas con una versión de Python pero no tiene instalado el paquete de numpy, ejecuta
en una línea de comandos (CMD) la siguiente sentencia

```
pip install --upgrade numpy
```

### Explicación de la implementación
Para implementar el simulador de posiciones se diseñó el siguiente diagrama de clases de UML:

![alt text](https://github.com/DavidMosquera/prueba_tecnica_ULTRACOM/blob/v4_reto2/reto_1/uml_clases.png)

Las clases ubicadas en el scrpit 'modelo.py' se implementan siguiendo el modelo anterior. Luego, se realiza la conexión entre el modelo y la vista del usuario utilizando un controlador ubicado en el script 'controlador.py'. Finalmente se implementa la vista en el script 'vista.py' donde se muestran los resultados de cada simulación al usuario utilizando interfaces de tkinter. El resultado de la implementación se muestra en la siguiente imagen: 

![alt text](https://github.com/DavidMosquera/prueba_tecnica_ULTRACOM/blob/v4_reto2/reto_1/resultado_caso_de_prueba.png)

