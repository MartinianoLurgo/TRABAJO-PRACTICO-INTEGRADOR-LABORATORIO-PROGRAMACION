from controller.controladorReserva import ControladorReserva

if __name__=="__main__":
    controlador = ControladorReserva("MVC\\Archivos\\reserva.txt","MVC\\Archivos\\clientes.txt","Archivos\\fechas.txt","Archivos\\servicios.txt")
    controlador.mostrar_menu_principal()
