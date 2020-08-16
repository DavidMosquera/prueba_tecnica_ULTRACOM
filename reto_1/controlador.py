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
    #METODO PARA OBTENER EL ALFIL
    def obtenerTableroAlfil(self) -> str:
        pass
    #METODO PARA OBTENER EL CABALLO
    def obtenerTableroCaballo(self) -> str:
        pass
    #METODO PARA OBTENER LA TORRE
    def obtenerTableroTorre(self) -> str:
        pass
    #METODO PARA OBTENER EL PEON NEGRO
    def obtenerTableroPeonNegro(self) -> str:
        pass
    #METODO PARA OBTENER EL PEON BLANCO
    def obtenerTableroPeonBlanco(self) -> str:
        pass
    #METODO PARA OBTENER LA REINA
    def obtenerTableroReina(self) -> str:
        pass
    #METODO PARA OBTENER EL REY
    def obtenerTableroRey(self) -> str:
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
        #CREAMOS CADA TABLERO
        self.tableroAlfil = md.TableroAlfil(filas, columnas, self.filaFicha, self.columnaFicha)
        self.tableroCaballo = md.TableroCaballo(filas, columnas, self.filaFicha, self.columnaFicha)
        self.tableroPeonBlanco = md.TableroPeonBlanco(filas, columnas, self.filaFicha, self.columnaFicha)
        self.tableroPeonNegro = md.TableroPeonNegro(filas, columnas, self.filaFicha, self.columnaFicha)
        self.tableroTorre = md.TableroTorre(filas, columnas, self.filaFicha, self.columnaFicha)
        self.tableroRey = md.TableroRey(filas, columnas, self.filaFicha, self.columnaFicha)
        self.tableroReina = md.TableroReina(filas, columnas, self.filaFicha, self.columnaFicha)
        #AGREGAMOS CADA TABLERO A LA LISTA
        self.tableros.append(self.tableroAlfil)
        self.tableros.append(self.tableroCaballo)
        self.tableros.append(self.tableroPeonBlanco)
        self.tableros.append(self.tableroPeonNegro)
        self.tableros.append(self.tableroTorre)
        self.tableros.append(self.tableroRey)
        self.tableros.append(self.tableroReina)
    
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
    
    #METODO PARA OBTENER EL ALFIL
    def obtenerTableroAlfil(self) -> str:
        return self.tableroAlfil.obtenerTablero()
    #METODO PARA OBTENER EL CABALLO
    def obtenerTableroCaballo(self) -> str:
        return self.tableroCaballo.obtenerTablero()
    #METODO PARA OBTENER LA TORRE
    def obtenerTableroTorre(self) -> str:
        return self.tableroTorre.obtenerTablero()
    #METODO PARA OBTENER EL PEON NEGRO
    def obtenerTableroPeonNegro(self) -> str:
        return self.tableroPeonNegro.obtenerTablero()
    #METODO PARA OBTENER EL PEON BLANCO
    def obtenerTableroPeonBlanco(self) -> str:
        return self.tableroPeonBlanco.obtenerTablero()
    #METODO PARA OBTENER LA REINA
    def obtenerTableroReina(self) -> str:
        return self.tableroReina.obtenerTablero()
    #METODO PARA OBTENER EL REY
    def obtenerTableroRey(self) -> str:
        return self.tableroRey.obtenerTablero()
