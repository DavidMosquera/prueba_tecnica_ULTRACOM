import numpy as np
#CLASE TABLERO
class Tablero(object):
    #CONSTRUCTOR DE LA CLASE TABLERO
    #TOMA COMO ARGUMENTO LA CANTIDA DE FILAS Y COLUMNAS DEL TABLERO
    #ADEMAS SE INDICA LA UBICACION DE LA FICHA CON SU RESPECTIVA FILA Y COLUMNA
    def __init__(self, filas, columnas, filaFicha, columnaFicha):
        self.distribucion = np.zeros((filas,columnas), dtype = int)
        self.filaFicha = filaFicha
        self.columnaFicha = columnaFicha
        self.distribucion[self.filaFicha][self.columnaFicha] = 8 #LUGAR DE LA FICHA
        
    #EN ESTA CLASE EL METODO DE SIMULAR MOVIMIENTOS SE DEFINE COMO VACIO
    def simularMovimientos(self):
        pass
    
    #EN ESTA CLASE EL METODO PARA OBTENER EL TABLERO
    def obtenerTablero(self) -> str:
        return str(self.distribucion)
    
#CLASE TABLERO PEON BLANCO QUE HEREDA DE TABLERO
class TableroPeonBlanco(Tablero):
   #CONSTRUCTOR DEL TABLERO CON LA FICHA PEON BLANCO
   def __init__(self, filas, columnas, filaFicha, columnaFicha):
       Tablero.__init__(self, filas, columnas, filaFicha, columnaFicha)
   
   #EN ESTA CLASE DEFINIMOS EL METODO QUE SIMULA LOS MOVIMIENTOS DEL PEON BLANCO
   def simularMovimientos(self):
       if(self.filaFicha != 0):
           #ESTE CONDICIONAL REPRESENTA SI EL PRIMER MOVIMIENTO BASANDOSE EN 
           #LA POSICION DEL PEON BLANCO EN EL TABLERO 
           #EN ESTE CASO, EL PRIMER MOVIMIENTO PODRIA SER DE TAMANO 2
           if(self.filaFicha == (self.distribucion.shape[0] - 2)):
               self.distribucion[self.filaFicha-2][self.columnaFicha] = 1
           #EL PEON PUEDE MOVERSE UNICAMENTE HACIA ADELANTE 
           #(DESDE EL PUNTO DE VISTA DEL PEON BLANCO)
           self.distribucion[self.filaFicha-1][self.columnaFicha] = 1
   
   #RETORNAR EL TABLERO DEL PEON BLANCO
   def obtenerTablero(self) -> str:
       return "Peón blanco \n" + Tablero.obtenerTablero(self)
        

#CLASE TABLERO PEON NEGRO QUE HEREDA DE TABLERO
class TableroPeonNegro(Tablero):
   #CONSTRUCTOR DEL TABLERO CON LA FICHA PEON NEGRO
   def __init__(self, filas, columnas, filaFicha, columnaFicha):
       Tablero.__init__(self, filas, columnas, filaFicha, columnaFicha)
   
   #EN ESTA CLASE DEFINIMOS EL METODO QUE SIMULA LOS MOVIMIENTOS DEL PEON NEGRO
   def simularMovimientos(self):
       if(self.filaFicha != self.distribucion.shape[0] - 1):
           #ESTE CONDICIONAL REPRESENTA SI ES EL PRIMER MOVIMIENTO BASANDOSE EN 
           #LA POSICION DEL PEON NEGRO EN EL TABLERO 
           #EN ESTE CASO, EL PRIMER MOVIMIENTO PODRIA SER DE TAMANO 2
           if(self.filaFicha == 1):
               self.distribucion[self.filaFicha+2][self.columnaFicha] = 1
           #EL PEON PUEDE MOVERSE UNICAMENTE HACIA ADELANTE 
           #(DESDE EL PUNTO DE VISTA DEL PEON NEGRO)
           self.distribucion[self.filaFicha+1][self.columnaFicha] = 1
           
   #RETORNAR EL TABLERO DEL PEON NEGRO
   def obtenerTablero(self) -> str:
       return "Peón negro \n" + Tablero.obtenerTablero(self)

#CLASE TABLERO CABALLO QUE HEREDA DE TABLERO
class TableroCaballo(Tablero):
   #CONSTRUCTOR DEL TABLERO CON LA FICHA CABALLO
   def __init__(self, filas, columnas, filaFicha, columnaFicha):
       Tablero.__init__(self, filas, columnas, filaFicha, columnaFicha)
   
   #EN ESTA CLASE DEFINIMOS EL METODO QUE SIMULA LOS MOVIMIENTOS DEL CABALLO
   def simularMovimientos(self):
       derecha = self.columnaFicha + 2
       izquierda = self.columnaFicha - 2
       arriba = self.filaFicha - 2
       abajo = self.filaFicha + 2
       #MOVIMIENTOS A LA DERECHA
       if(derecha < self.distribucion.shape[1]):
           #MOVIMIENTO DERECHA ARRIBA
           if(self.filaFicha>0):
               self.distribucion[self.filaFicha-1][derecha] = 1
           #MOVIMIENTO DERECHA ABAJO
           if(self.filaFicha<self.distribucion.shape[0]-1):
               self.distribucion[self.filaFicha+1][derecha] = 1
       #MOVIMIENTOS A LA IZQUIERDA
       if(izquierda >= 0):
           #MOVIMIENTO A LA IZQUIERDA ARRIBA
           if(self.filaFicha>0):
               self.distribucion[self.filaFicha-1][izquierda] = 1
           #MOVIMIENTO A LA IZQUIERDA ABAJO
           if(self.filaFicha<self.distribucion.shape[0]-1):
               self.distribucion[self.filaFicha+1][izquierda] = 1
       #MOVIMIENTOS HACIA ABAJO
       if(abajo < self.distribucion.shape[0]):
           #MOVIMIENTO ABAJO IZQUIERDA
           if(self.columnaFicha>0):
               self.distribucion[abajo][self.columnaFicha-1] = 1
           #MOVIMIENTO ABAJO DERECHA
           if(self.columnaFicha<self.distribucion.shape[1]-1):
               self.distribucion[abajo][self.columnaFicha+1] = 1
       #MOVIMIENTOS HACIA ARRIBA
       if(arriba >= 0):
           #MOVIMIENTO ARRIBA IZQUIERDA
           if(self.columnaFicha>0):
               self.distribucion[arriba][self.columnaFicha-1] = 1
           #MOVIMIENTO ARRIBA DERECHA
           if(self.columnaFicha<self.distribucion.shape[1]-1):
               self.distribucion[arriba][self.columnaFicha+1] = 1
   #RETORNAR EL TABLERO CABALLO
   def obtenerTablero(self) -> str:
       return "Caballo \n" + Tablero.obtenerTablero(self)
     
#CLASE TABLERO ALFIL QUE HEREDA DE TABLERO
class TableroAlfil(Tablero):
   #CONSTRUCTOR DEL TABLERO CON LA FICHA ALFIL
   def __init__(self, filas, columnas, filaFicha, columnaFicha):
       Tablero.__init__(self, filas, columnas, filaFicha, columnaFicha)
   
   #EN ESTA CLASE DEFINIMOS EL METODO QUE SIMULA LOS MOVIMIENTOS DEL ALFIL
   def simularMovimientos(self):
       #INDICES PARA EL AVANCE DE LA DIAGONAL IZQUIERDA SUPERIOR
       filaArribaIzquierda = self.filaFicha
       columnaArribaIzquierda = self.columnaFicha
       #INDICES PARA EL AVANCE DE LA DIAGIONAL IZQUIERDA INFERIOR
       filaAbajoIzquierda = self.filaFicha
       columnaAbajoIzquierda = self.columnaFicha
       #INDICES PARA EL AVANCE DE LA DIAGIONAL DERECHA SUPERIOR
       filaArribaDerecha = self.filaFicha
       columnaArribaDerecha = self.columnaFicha
       #INDICES PARA EL AVANCE DE LA DIAGIONAL DERECHA INFERIOR
       filaAbajoDerecha = self.filaFicha
       columnaAbajoDerecha = self.columnaFicha
       #CICLIO DONDE SE ASIGNAN LOS POSIBLES MOVIMIENTOS DEPENDIENDO DE LA DIAGONAL
       while((filaArribaIzquierda >= 0 and columnaArribaIzquierda >= 0)
            or
            (filaAbajoIzquierda < self.distribucion.shape[0] and columnaAbajoIzquierda >= 0)
            or
            (filaArribaDerecha >= 0 and columnaArribaDerecha < self.distribucion.shape[1])
            or
            (filaAbajoDerecha < self.distribucion.shape[0] and columnaAbajoDerecha < self.distribucion.shape[1])):
           #AVANZAMOS EN CADA DIAGONAL
           filaArribaIzquierda -= 1
           columnaArribaIzquierda -= 1
           filaAbajoIzquierda += 1
           columnaAbajoIzquierda -= 1
           filaArribaDerecha -= 1
           columnaArribaDerecha += 1
           filaAbajoDerecha += 1
           columnaAbajoDerecha += 1
           #SI ES POSIBLE, ASIGNAR EL MOVIMIENTO A CADA UNA DE LAS DIAGONALES
           if(filaArribaIzquierda >= 0 and columnaArribaIzquierda >= 0):
               self.distribucion[filaArribaIzquierda][columnaArribaIzquierda] = 1
           if(filaAbajoIzquierda < self.distribucion.shape[0] and columnaAbajoIzquierda >= 0):
               self.distribucion[filaAbajoIzquierda][columnaAbajoIzquierda] = 1
           if(filaArribaDerecha >= 0 and columnaArribaDerecha < self.distribucion.shape[1]):
               self.distribucion[filaArribaDerecha][columnaArribaDerecha] = 1
           if(filaAbajoDerecha < self.distribucion.shape[0] and columnaAbajoDerecha < self.distribucion.shape[1]):
               self.distribucion[filaAbajoDerecha][columnaAbajoDerecha] = 1
   #RETORNAR EL TABLERO ALFIL
   def obtenerTablero(self) -> str:
       return "Alfil \n" + Tablero.obtenerTablero(self)        
               
#CLASE TABLERO TORRE QUE HEREDA DE TABLERO
class TableroTorre(Tablero):
   #CONSTRUCTOR DEL TABLERO CON LA FICHA TORRE
   def __init__(self, filas, columnas, filaFicha, columnaFicha):
       Tablero.__init__(self, filas, columnas, filaFicha, columnaFicha)
   
   #EN ESTA CLASE DEFINIMOS EL METODO QUE SIMULA LOS MOVIMIENTOS DEL CABALLO
   def simularMovimientos(self): 
       #INDICE PARA EL AVANCE HACIA ARRIBA
       arriba = self.filaFicha
       #INDICE PARA EL AVANCE HACIA ABAJO
       abajo = self.filaFicha
       #INDICE PARA EL AVANCHE HACIA LA IZQUIERDA
       izquierda = self.columnaFicha
       #INDICE PARA EL AVANCHE HACIA LA DERECHA
       derecha = self.columnaFicha
       #CICLO DONDE SE ASIGNAN LOS POSIBLES MOVIMIENTOS VERTICALES Y HORIZONTALES
       while(arriba >= 0 
             or 
             abajo < self.distribucion.shape[0] 
             or 
             izquierda >= 0
             or 
             derecha < self.distribucion.shape[1]):
           #AVANZAR EN CADA DIRECCION
           arriba -= 1
           abajo += 1
           izquierda -=1
           derecha += 1
           #SI ES POSIBLE, ASIGNAR EL MOVIMIENTO EN CADA DIRECCION
           if(arriba >= 0):
               self.distribucion[arriba][self.columnaFicha] = 1
           if(abajo < self.distribucion.shape[0]):
               self.distribucion[abajo][self.columnaFicha] = 1
           if(izquierda >= 0):
               self.distribucion[self.filaFicha][izquierda] = 1
           if(derecha < self.distribucion.shape[1]):
               self.distribucion[self.filaFicha][derecha] = 1
    #RETORNAR EL TABLERO TORRE
   def obtenerTablero(self) -> str:
       return "Torre \n" + Tablero.obtenerTablero(self)   
   
#CLASE TABLERO REY QUE HEREDA DE TABLERO
class TableroRey(Tablero):
   #CONSTRUCTOR DEL TABLERO CON LA FICHA REY
   def __init__(self, filas, columnas, filaFicha, columnaFicha):
       Tablero.__init__(self, filas, columnas, filaFicha, columnaFicha)
   
   #EN ESTA CLASE DEFINIMOS EL METODO QUE SIMULA LOS MOVIMIENTOS DEL REY
   def simularMovimientos(self):
       #ARRIBA
       if(self.filaFicha>0):
           #DIAGONAL SUPERIOR IZQUIERDA
           if(self.columnaFicha>0):
               self.distribucion[self.filaFicha-1][self.columnaFicha-1] = 1
           #DIAGONAL SUPERIOR DERECHA
           if(self.columnaFicha<self.distribucion.shape[1]-1):
               self.distribucion[self.filaFicha-1][self.columnaFicha+1] = 1
           #ASIGNAR MOVIMIENTO HACIA ARRIBA
           self.distribucion[self.filaFicha-1][self.columnaFicha] = 1
       #ABAJO
       if(self.filaFicha<self.distribucion.shape[0]-1):
           #DIAGONAL INFERIOR IZQUIERDA
           if(self.columnaFicha>0):
               self.distribucion[self.filaFicha+1][self.columnaFicha-1] = 1
           #DIAGONAL INFERIOR DERECHA
           if(self.columnaFicha<self.distribucion.shape[1]-1):
               self.distribucion[self.filaFicha+1][self.columnaFicha+1] = 1
           #ASIGNAR MOVIMIENTO HACIA ABAJO
           self.distribucion[self.filaFicha+1][self.columnaFicha] = 1
       #DERECHA
       if(self.columnaFicha<self.distribucion.shape[1]-1):
           self.distribucion[self.filaFicha][self.columnaFicha+1] = 1
       #IZQUIERDA
       if(self.columnaFicha>0):
           self.distribucion[self.filaFicha][self.columnaFicha-1] = 1
    
   #RETORNAR EL TABLERO REY
   def obtenerTablero(self) -> str:
       return "Rey \n" + Tablero.obtenerTablero(self)    

#CLASE TABLERO REINA QUE HEREDA DEl REY, TORRE Y ALFIL
class TableroReina(TableroRey, TableroTorre, TableroAlfil):
   #CONSTRUCTOR DEL TABLERO CON LA FICHA REINA
   def __init__(self, filas, columnas, filaFicha, columnaFicha):
       Tablero.__init__(self, filas, columnas, filaFicha, columnaFicha)
   
   #EN ESTA CLASE DEFINIMOS EL METODO QUE SIMULA LOS MOVIMIENTOS DE LA REINA
   def simularMovimientos(self):
       #USANDO LA HERENCIA EJECUTAMOS LAS OPERACIONES DE CADA SUPERCLASE
       #TABLERO REY
       TableroRey.simularMovimientos(self)
       #TABLERO ALFIL
       TableroAlfil.simularMovimientos(self)
       #TABLERO TORRE
       TableroTorre.simularMovimientos(self)
       
       
   #RETORNAR EL TABLERO REINA
   def obtenerTablero(self) -> str:
       return "Reina \n" + Tablero.obtenerTablero(self)  
   

    