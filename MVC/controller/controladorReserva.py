import os
from model.reserva import Reserva
from model.item import Item
from view.vistaReserva import VistaReserva
from view.vistaServicio import VistaServicio
from controller.controladorCalendario import ControladorCalendario
from controller.controladorCliente import ControladorCliente
from controller.controladorItem import ControladorItem
from controller.controladorServicio import ControladorServicio


class ControladorReserva:
    def __init__(self,archivoReservas,archivoClientes, archivoFechas, archivoServicios):
        self._archivoReservas = archivoReservas
        self._archivoClientes = archivoClientes
        self._archivoFechas = archivoFechas
        self._archivoServicios = archivoServicios
        self._archivoGastosAdministrativos = "MVC\\Archivos\\gastoAdministrativo.txt"
        self._modelo = Reserva()
        self._vista = VistaReserva()
        self._item = Item()
        self._listaReservas = []

    #Cargar archivo de reservas 
    def cargar_archivo_reservas(self):
        try:
            with open(self._archivoReservas, "r", encoding="utf-8") as archivo:
                for lineas in archivo.readlines():
                    linea = lineas.strip().split(",")
                    reserva = Reserva(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5])
                    self._listaReservas.append(reserva)
        except FileNotFoundError:
            self._vista.archivo_noEncontrado()
            
    #Cargar archivo de gastos administrativos
    def cargar_archivo_gastosAdministrativos(self):
        try:
            with open(self._archivoGastosAdministrativos , "r", encoding="utf-8") as archivo:
                for linea in archivo.readlines():
                    self._item.set_importeAdministrativo(float(linea))
        except FileNotFoundError:
            self._vista.archivo_noEncontrado()
    
    #Ingresar datos del cliente
    def ingresar_datos_cliente(self):
        self._vista.limpiar_pantalla()
        controladorCliente = ControladorCliente()
        controladorCliente.cargar_archivo_cliente()
        nuevoCliente = controladorCliente.registrar_Cliente()
        self._modelo.set_cliente(nuevoCliente)
        self._item.set_cliente(nuevoCliente)
        self._vista.mostrar_mensaje_continuar()
    #Ingresar fechas
    def ingresar_datos_fecha(self):
        controladorCalendario = ControladorCalendario()
        controladorCalendario.ingresar_dia()
        self._modelo.set_fecha(controladorCalendario._modelo.get_dia())
        self._item.set_fecha(controladorCalendario._modelo.get_dia())
        self._vista.mostrar_mensaje_continuar()
        self._vista.limpiar_pantalla()

    
    #Elegir servicios para reserva
    def elegir_servicios_reserva(self):
        controladorServicio = ControladorServicio()
        controladorServicio.cargar_archivo_servicios()
        controladorServicio.menu_lista_servicios()
        importeServicios = 0.0
        opcion = 1
        while opcion != 0:
            opcion = controladorServicio.seleccionar_servicios_reserva()
            for servicio in controladorServicio._listaServicios:
                if servicio.get_idServicio() == opcion:
                    self._modelo.set_servicios(servicio.get_tipoServicio())
                    self._item.set_servicios(f"{servicio.getTipoServicio()} - ${servicio.getPrecio()}")
                    importeServicios += servicio.get_precio()
            self._item.set_importeServicios(importeServicios)

    #Mostrar detalles de reserva
    def detalles_reserva(self):
        self._item.calcular_iva()
        self._modelo.set_totalImporte(self._item.calcular_importeTotal())
        self._item.calcular_senia()
        self._vista.mostrar_detalles(self._item)
        opcion = self._vista.preguntar_confirmacion()
        if opcion.upper() == "SI":
            self._modelo.set_nombreArchivo(f"{str(self._item.get_fecha())} - {str(self._item.get_cliente()).strip().split('_')}.txt")
            self._listaReservas.append(self._modelo)
            controladorCalendario = ControladorCalendario()
            controladorCalendario.cargar_archivo_fechas()
            controladorCalendario._listaFechas.append(self._modelo.get_fecha())
            controladorCalendario.guardar_archivo()
            self.guardar_item()
            self._vista.mostrar_mensaje_confirmar()
    
    #Guardar Item
    def guardar_item(self):
        with open(f"Archivos\\Eventos\\{str(self._item.get_fecha())} - {str(self._item.get_cliente()).strip().split('_')}.txt", 'w+') as archivo:
            archivo.write(self._item.__str__())
    
    #Cambiar gastos Administrativos
    def cambiar_precio_gastosAdministrativos(self):
        self._vista.mostrar_precio_gastoAdministrativo(self._item.get_importeAdministrativo())
        self._item.set_importeAdministrativo(float(self._vista.pedir_precio_gastoAdministrativo()))

    #Guardar archivo de reservas
    def guardar_archivo_reservas(self):
        with open(self.archivoEventos, "w") as archivo:
            for reserva in self._listaReservas:
                linea = str(reserva.get_idReserva()) + ";" + str(reserva.get_cliente()) + ";" + str(reserva.get_fecha()) + ";" + str(reserva.get_servicios()) + ";" + str(reserva.get_totalImporte()) + ";" + str(reserva.get_nombreArchivo())
                archivo.write(linea + "\n")
                
    #Menu principal
    def mostrar_menu_principal(self):
        opcion = 0
        while opcion != 4:
            self._vista.limpiar_pantalla()
            self._vista.mostrar_menuprincipal()
            try:
                opcion = self._vista.pedir_opcion()
                if opcion < 1 or opcion > 4:
                    self._vista.manejo_de_errores()
            except ValueError:
                self._vista.manejo_de_errores()
            match opcion:
                case 1:
                    while opcion != 3:
                        opcion = 0
                        self._vista.limpiar_pantalla()
                        self._vista.mostrar_menu_reservas()
                        opcion = self._vista.pedir_opcion()
                        match opcion:
                            case 1:
                                self.ingresar_datos_cliente()
                                self.ingresar_datos_fecha()
                                self.elegir_servicios_reserva()
                            case 2:
                                self._vista.limpiar_pantalla()
                            case 3:
                                self._vista.volviendo_al_menu()
                case 2:
                    opcion = 0
                    while opcion != 3:
                        self._vista.limpiar_pantalla()
                        controladorCliente = ControladorCliente()
                        controladorCliente.cargar_archivo_cliente()
                        controladorCliente._vista.mostrar_menu()
                        try:
                            opcion = self._vista.pedir_opcion()
                            if opcion < 1 or opcion > 3:
                                self._vista.manejo_de_errores()
                        except ValueError:
                            self._vista.manejo_de_errores()
                        match opcion:
                            case 1:
                                self._vista.limpiar_pantalla()
                                controladorCliente._vista.mostrar_lista_clientes()
                                controladorCliente.mostrarclientes()
                                self._vista.mostrar_mensaje_continuar()
                            case 2:
                                self._vista.limpiar_pantalla()
                                controladorCliente.cambiardatoscliente()
                            case 3:
                                self._vista.volviendo_al_menu()
                case 3:
                    opcion = 0
                    controladorServicio = ControladorServicio()
                    controladorServicio.cargar_archivo_servicios()
                    while opcion != 4:
                        self._vista.limpiar_pantalla()
                        controladorServicio._vistaServicio.mostrar_menu_servicios()
                        try:
                            opcion = self._vista.pedir_opcion()
                            if opcion < 1 or opcion > 4:
                                self._vista.manejo_de_errores()
                        except ValueError:
                            self._vista.manejo_de_errores()
                        match opcion:
                            case 1:
                                controladorServicio.menu_lista_servicios()
                                self._vista.mostrar_mensaje_continuar()
                            case 2:
                                controladorServicio.menu_lista_servicios()
                                controladorServicio.modificar_precio_servicios()
                                self._vista.mostrar_mensaje_continuar() 
                            case 3:
                                self._vista.limpiar_pantalla()
                                try:
                                    with open(self._archivoGastosAdministrativos, "r") as archivo:
                                        for linea in archivo:
                                            self._item.set_importeAdministrativo(float(linea))
                                except FileNotFoundError:
                                    self._vista.archivo_noEncontrado()
                                self._vista.mostrar_precio_gastoAdministrativo(self._item.get_importeAdministrativo())
                                self._item.set_importeAdministrativo(self._vista.pedir_precio_gastoAdministrativo())
                                with open(self._archivoGastosAdministrativos, "w") as archivo:
                                    archivo.write(str(self._item.get_importeAdministrativo()))
                                self._vista.mostrar_mensaje_continuar()
                            case 4:
                                self._vista.volviendo_al_menu()
                                self.mostrar_menu_principal()   
        self._vista.limpiar_pantalla()
        self._vista.mostrar_mensaje_final()