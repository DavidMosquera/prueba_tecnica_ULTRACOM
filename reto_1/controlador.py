import modelo as md
import random as rnd

#INTERFAZ DEL CONTROLADOR
class ControladorInterface:
    #METODO PARA OBTENER EL STRING DE LOS TABLEROS
    def obtenerString(self) -> str:
        pass
    #METODO PARA SIMULAR LOS MOVIMIENTOS DE LOS TABLEROS
    def simularMovimientos(self):
        pass
    #METODO PARA OBTENER LA FILA DE LA POSICION ALEATORIA
    def obtenerFilaFicha(self) -> str:
        pass
    #METODO PARA OBTENER LA COLUMNA DE LA POSICION ALEATORIA
    def obtenerColumnaFicha(self) -> str:
        pass

#CLASE DEL CONTROLADOR QUE IMPLEMENTA LA INTERFAZ
class Controlador(ControladorInterface):
    
    #CONSTRUCTOR DEL CONTROLADOR QUE RECIBE LA CANTIDAD DE FILAS Y COLUMNAS DE
    #LOS TABLEROS
    def __init__(self, filas, columnas):
        #GENERAMOS EL ESTADO ALEATORIO INICIAL
        self.filaFicha = rnd.randint(0,filas-1)
        self.columnaFicha = rnd.randint(0,columnas-1)
        #LISTA DE TABLEROS
        self.tableros = []
        #AGREGAMOS CADA TABLERO A LA LISTA
        self.tableros.append(md.TableroAlfil(filas, columnas, self.filaFicha, self.columnaFicha))
        self.tableros.append(md.TableroCaballo(filas, columnas, self.filaFicha, self.columnaFicha))
        self.tableros.append(md.TableroPeonBlanco(filas, columnas, self.filaFicha, self.columnaFicha))
        self.tableros.append(md.TableroPeonNegro(filas, columnas, self.filaFicha, self.columnaFicha))
        self.tableros.append(md.TableroTorre(filas, columnas, self.filaFicha, self.columnaFicha))
        self.tableros.append(md.TableroRey(filas, columnas, self.filaFicha, self.columnaFicha))
        self.tableros.append(md.TableroReina(filas, columnas, self.filaFicha, self.columnaFicha))
    
    #SIMULA LOS MOVIMIENTOS DE TODOS LOS TABLEROS EN LA LISTA DE TABLEROS
    def simularMovimientos(self):
        for tablero in self.tableros:
            tablero.simularMovimientos()
            
    #OBTIENE EL VALOR COMO STRING DE LA COLUMNA ALEATORIA DE LA FICHA
    def obtenerColumnaFicha(self) -> str:
        return str(self.columnaFicha)
    
    #OBTIENE EL VALOR COMO STRING DE LA FILA ALEATORIA DE LA FICHA
    def obtenerFilaFicha(self) -> str:
        return str(self.filaFicha)
    
    #OBTIENE EL ESTRING DE TODOS LOS TABLEROS
    def obtenerString(self) -> str:
        tableroStr = ""
        for tablero in self.tableros:
            tableroStr += tablero.obtenerTablero() + " \n"
        return tableroStr
