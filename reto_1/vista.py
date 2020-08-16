import controlador as crl
import tkinter as tk
from tkinter import scrolledtext
#INTERFAZ DE LA VISTA
class VistaInterface:
    #METODO VACIO PARA INICIAR LA VISTA
    def iniciar(self):
        pass
    #METODO VACIO PARA EL BOTON SIMULAR
    def simular(self):
        pass
    
#CLASE VISTA
class Vista(VistaInterface):
        
    #INICIAR LA INTERFAZ
    def iniciar(self):
        
        #CREACION DE LOS ELEMENTOS DE LA INTERFAZ GRAFICA DE USUARIO
        ventana = tk.Tk()
        ventana.title("[ULTRACOM] Simulador de posiciones-v3.0")
        ventana.geometry("765x319")
        
        self.peonBlanco = scrolledtext.ScrolledText(ventana,width=20,height=9)
        self.peonBlanco.grid(column=0,row=0, padx=5, pady=5)
        
        self.peonNegro = scrolledtext.ScrolledText(ventana,width=20,height=9)
        self.peonNegro.grid(column=1,row=0, padx=5, pady=5)
        
        self.alfil = scrolledtext.ScrolledText(ventana,width=20,height=9)
        self.alfil.grid(column=2,row=0, padx=5, pady=5)
        
        self.torre = scrolledtext.ScrolledText(ventana,width=20,height=9)
        self.torre.grid(column=3,row=0, padx=5, pady=5)
        
        self.rey = scrolledtext.ScrolledText(ventana,width=20,height=9)
        self.rey.grid(column=0,row=1, padx=5, pady=5)
        
        self.reina = scrolledtext.ScrolledText(ventana,width=20,height=9)
        self.reina.grid(column=1,row=1, padx=5, pady=5)
        
        self.caballo = scrolledtext.ScrolledText(ventana,width=20,height=9)
        self.caballo.grid(column=2,row=1, padx=5, pady=5)
        
        self.botonSimular = tk.Button(ventana, text ="Simular", command = self.simular)
        self.botonSimular.grid(column=3,row=1, padx=5, pady=5)
        
        #SIMULACION INICIAL
        self.simular()
        
        #LOOP PRINCIPAL
        ventana.mainloop()
        
        
    def simular(self):
        #INICIAR UN NUEVO CONJUNTO DE TABLEROS
        self.controlador = crl.Controlador(8,8)
        self.controlador.simularMovimientos()
        #BORRAR EL CONTENIDO DE LOS CAMPOS DE TEXTO
        self.peonBlanco.delete(1.0,tk.END)
        self.peonNegro.delete(1.0,tk.END)
        self.alfil.delete(1.0,tk.END)
        self.torre.delete(1.0,tk.END)
        self.rey.delete(1.0,tk.END)
        self.reina.delete(1.0,tk.END)
        self.caballo.delete(1.0,tk.END)
        #INSERTAR EL CONTENIDO DE LOS CAMPOS DE TEXTO
        self.peonBlanco.insert(1.0,self.controlador.obtenerTableroPeonBlanco())
        self.peonNegro.insert(1.0,self.controlador.obtenerTableroPeonNegro())
        self.alfil.insert(1.0,self.controlador.obtenerTableroAlfil())
        self.torre.insert(1.0,self.controlador.obtenerTableroTorre())
        self.rey.insert(1.0,self.controlador.obtenerTableroRey())
        self.reina.insert(1.0,self.controlador.obtenerTableroReina())
        self.caballo.insert(1.0,self.controlador.obtenerTableroCaballo())
        
if __name__ == "__main__":
    vista = Vista()
    vista.iniciar()