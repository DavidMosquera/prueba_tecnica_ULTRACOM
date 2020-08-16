import controlador as crl

#INTERFAZ DE LA VISTA
class VistaInterface:
    #METODO VACIO PARA INICIAR LA VISTA
    def iniciar(self):
        pass
    
#CLASE VISTA
class Vista(VistaInterface):
    #INICIA EL CONTROLADOR
    def __init__(self):
        self.controlador = crl.Controlador(8,8)

    #INICIA LA EJECUCION DE LA VISTA
    def iniciar(self):
        while(input("Simular [1]\nSalir [0]\n") == "1"):
            self.controlador = crl.Controlador(8,8)
            print("Posición de la ficha (fila,columna): (",self.controlador.obtenerFilaFicha(), ",", self.controlador.obtenerColumnaFicha(),")")
            self.controlador.simularMovimientos()
            print(self.controlador.obtenerString())
        