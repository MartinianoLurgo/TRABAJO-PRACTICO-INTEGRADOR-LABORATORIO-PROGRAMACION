from model.cliente import Cliente
from view.vistaCliente import vistacliente
from view.vistaReserva import VistaReserva
class ControladorCliente:
    def __init__(self):
        self._vista = vistacliente()
        self._modelo = Cliente()
        self._vistaReserva=VistaReserva()
        self._listaCliente = []

    #Cargar archivo existente de Clientes
    def cargar_archivo_cliente(self):
        try:
            with open("MVC\\Archivos\\clientes.txt" , "r")as archivo:
                for lineas in archivo.readlines():
                    linea = lineas.strip().split(";")
                    self._modelo = Cliente(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5])
                    self._listaCliente.append(self._modelo)
        except FileNotFoundError:
            self._vista.archivo_no_encontrado()

    #Registrar Nuevo Cliente        
    def registrar_Cliente(self):
        self._vista.mostrar_registro()
        nuevoCliente = Cliente(idCliente='',nombre='', apellido="", dni='',telefono=0, metodoDePago='')
        nuevoCliente.set_nombre(self._vista.pedir_nombre())
        nuevoCliente.set_nombre(self._vista.pedir_apellido())
        nuevoCliente.set_dni(self._vista.pedir_dni())
        nuevoCliente.set_telefono(self._vista.pedir_telefono())
        nuevoCliente.set_metodoDePago(self._vista.pedir_metodo_de_pago())
        self._listaCliente.append(nuevoCliente)
        self._vista.registro_exitoso()
        

    #Mostrar Clientes
    def mostrarclientes(self):
        lista = self._listaCliente
        for cliente in lista:
            self._vista.mostrar(cliente.get_idCliente(),cliente.get_nombre(),cliente.get_apellido(),cliente.get_dni(),cliente.get_telefono(),cliente.get_metodoDePago())
     

    #Cambiar Datos del Cliente
    def cambiardatoscliente(self):
        self.mostrarclientes()
        persona = self._vista.pedir_id()
        self._vistaReserva.limpiar_pantalla()
        self._vista.cambiar_atributos()
        for cliente in self._listaCliente:
            if persona == cliente.get_nombre():
                atributos = self._vista.pedir_atributos()
                if atributos == "1":
                    cliente.set_idCliente(self._vista.pedir_id())
                elif atributos == "2":
                    cliente.set_nombre(self._vista.pedir_nombre())        
                elif atributos == "3":
                    cliente.set_apellido(self._vista.pedir_apellido())
                elif atributos == "4":
                    cliente.set_dni(self._vista.pedir_dni())
                elif atributos == "5":
                    cliente.set_telefono(self._vista.pedir_telefono())
                elif atributos == "6":
                    cliente.set_metodoDePago(self._vista.pedir_metodo_pago())

    #Guardar Archivo Clientes
    def guardar_archivo(self):
        try:
            with open("MVC\\Archivos\\clientes.txt" , "r")as archivo:
                for cliente in self._listaCliente:
                    archivo.write(str(cliente.get_idCliente()) + "," + str(cliente.get_nombre()) + "," + str(cliente.get_apellido()) + "," + str(cliente.get_dni()) + "," + str(cliente.get_telefono()) + "," + str(cliente.get_metodoDePago()))
        except FileNotFoundError:
