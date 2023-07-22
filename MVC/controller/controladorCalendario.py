from model.calendario import Calendario
from view.vistaCalendario import VistaCalendario
from view.vistaReserva import VistaReserva


class ControladorCalendario:
    def __init__(self):
        self._modelo = Calendario()
        self._vistaCalendario = VistaCalendario()
        self._vistaReserva = VistaReserva()
        self._archivo = "MVC\\Archivos\\fechas.txt"
        self._listaFechas = []

    #Cargar archivo de fechas
    def cargar_archivo_fechas(self):
        try:
            with open(self._archivo, "r") as archivo:
                for lineas in archivo.readlines():
                    linea = lineas.strip().split("/")
                    fecha = Calendario(int(linea[0]), int(linea[1]), int(linea[2]),linea[3])
                    self._listaFechas.append(fecha)
        except FileNotFoundError:
            self._vistaReserva.archivo_noEncontrado()

    #Ingresar dia
    def ingresar_dia(self):
        opcion = 1
        while opcion !=0 :
            try:
                self._modelo.set_dia(self._vistaCalendario.pedir_dia())
                while self._modelo.get_dia() < 1 or self._modelo.get_dia() > 31:
                    self._vistaReserva.manejo_de_errores()
                    self._modelo.set_dia(self._vistaCalendario.pedir_dia())
                opcion = 0
            except ValueError:
                self._vistaReserva.manejo_de_errores()
    
    #Guardar archivo
    def guardar_archivo(self):
        try:
            with open(self._archivo, "w") as archivo:
                for fechas in self._listaFechas:
                    archivo.write(str(fechas))
                    archivo.write("\n")
        except FileNotFoundError:
            self._vistaReserva.archivo_noEncontrado()