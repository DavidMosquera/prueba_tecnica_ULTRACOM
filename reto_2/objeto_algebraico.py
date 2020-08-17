import numpy as np

#INTERFACE DE OBJETO ALGEBRAICO
class ObjetoAlgebraicoInterface:
    #OPERACION SUMAR
    def sumar(self, polinomio = np.poly1d([0])):
        pass
    #OPERACION RESTAR
    def restar(self, polinomio = np.poly1d([0])):
        pass
    #OPERACION MULTIPLICAR POR ESCALAR
    def multiplicarPorEscalar(self, escalar = 1):
        pass
    #OPERACION MULTIPLICAR POR POLINOMIO
    def multiplicarPorPolinomio(self, polinomio = np.poly1d([1])):
        pass
    #OPERACION EVALUAR POLINOMIO
    def evaluarPoliniomio(self, x=0) -> float:
        pass

#CLASE OBJETO ALGEBRAICO QUE IMPLEMENTA LA INTERFAZ DE OBJETO ALGEBRAICO
class ObjetoAlgebraico(ObjetoAlgebraicoInterface):
    #CONSTRUCTOR DONDE SE INICIA EL OBJETO ALGEBRAICO
    #POR DEFECTO SE INICIA COMO EL POLINIMOMIO f(x) = 0
    def __init__(self, polinomio = np.poly1d([0])):
        self.polinomio = polinomio
    
    #OPERACION PARA SUMA ENTRE POLINOMIOS: f(x) + g(x)
    def sumar(self, polinomio = np.poly1d([0])):
        if isinstance(polinomio, ObjetoAlgebraico):
            polinomio = polinomio.polinomio
        self.polinomio = np.polyadd(self.polinomio, polinomio)

    #OPERACION PARA RESTA ENTRE POLINIMIOS: f(x) - g(x)
    def restar(self, polinomio = np.poly1d([0])):
        if isinstance(polinomio, ObjetoAlgebraico):
            polinomio = polinomio.polinomio
        self.polinomio = np.polysub(self.polinomio, polinomio)
    
    #OPERACION PARA MULTIPLICACION POR ESCALAR: f(x) * escalar
    def multiplicarPorEscalar(self, escalar = 1):
        self.polinomio = np.polymul(self.polinomio, escalar)
        
    #OPREACION PARA MULTIPLICACION DE POLINIMOOS: f(x) * g(x)
    def multiplicarPorPolinomio(self, polinomio = np.poly1d([1])):
        if isinstance(polinomio, ObjetoAlgebraico):
            polinomio = polinomio.polinomio
        self.polinomio = np.polymul(self.polinomio, polinomio)
    
    #OPERACION PARA EVALUACION DE POLINIMIO: f(val)
    def evaluarPoliniomio(self, x=0) -> float:
        return np.polyval(self.polinomio, x)
    
#HILO PRINCIPAL PARA DEMOSTRAR FUNCIONAMIENTO
if __name__ == "__main__":
    #REALIZAREMOS OPERACIONES PARA CONSTRUIR EL OBJETO ALGEBRAICO:
    #       f(x) = -16x^3 + 28x^2 + 76x + 20
    
    #CREAMOS EL OBJETO ALGEBRAICO COMO VACIO, OBTENIENDO EL POLINIMO:
    #       f(x) = 0
    objetoAlgebraico = ObjetoAlgebraico()
    print("Polinomio inicial:", objetoAlgebraico.polinomio)
    
    #SUMAMOS AL OBJETO g(x) = x^2 + 4x + 5, OBTENIENDO EL POLINIMIO:
    #       f(x) = x^2 + 4x + 5
    objetoAlgebraico.sumar([1,4,5])
    print("Polinomio luego de sumar g(x) = x^2 + 4x + 5:\n", objetoAlgebraico.polinomio)
    
    #RESTAMOS AL OBJETO g(x) = 2x^2 + x + 4, OBTENIENDO EL POLINIMIO:
    #       f(x) = -x^2 + 3x + 1
    objetoAlgebraico.restar([2,1,4])
    print("Polinomio luego de restar g(x) = 2x^2 + x + 4:\n",objetoAlgebraico.polinomio)
    
    #MULTIPLICAMOS AL OBJETO POR EL ESCALAR 4, OBTENIENDO EL POLINIMIO:
    #       f(x) = -4x^2 + 12x + 4
    objetoAlgebraico.multiplicarPorEscalar(4)
    print("Polinomio luego de multiplicar por el escalar 4:\n",objetoAlgebraico.polinomio)
    
    #MULTIPLICAMOS AL OBJETO POR g(x) = 4x + 5, OBTENIENDO EL POLINIMIO:
    #       f(x) = -16x^3 + 28x^2 + 76x + 20
    objetoAlgebraico.multiplicarPorPolinomio([4,5])
    print("Polinomio luego de multiplicar g(x) = 4x + 5:\n",objetoAlgebraico.polinomio)
    
    #EVALUAMOS EL POLINIMIO EN f(5), OBTENIENDO COMO RESULTADO -900.0
    print("Polinomio luego de evaluar f(5):\n",objetoAlgebraico.evaluarPoliniomio(5))
    
    #TAMBIEN SE PERMITE OPERACIONES ENTRE OBJETOS ALGEBRAICOS
    #SUMAMOS AL OBJETO g(x) = x^2 + 2x + 3, OBTENIENDO EL POLINIMIO:
    #       f(x) = -16x^3 + 29x^2 + 78x + 23
    objetoAlgebraico.sumar(ObjetoAlgebraico([1,2,3]))
    print("Polinomio luego de sumar g(x) = x^2 + 2x + 3:\n",objetoAlgebraico.polinomio)