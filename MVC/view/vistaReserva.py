class VistaReserva:
    def mostrar_menuprincipal(self):
        print("=====================")
        print(" BIENVENIDO AL MENU ")
        print("=====================")
        print("")
        print("1 - Menu Reservas 🧉")
        print("2 - Clientes 🧑")
        print("3 - Servicios 🪄")
        print("4 - Salir del programa 😢")

    def pedir_opcion(self):
        return int(input("➡️"))
    
    def mostrar_menureserva(self):
        print("======MENU RESERVA=======")
        print("1 - Cosultar Fechas disponibles 🗓️")
        print("2 - Realizar Reserva 😄")
        print("4 - Monto Total y su Seña 💰")
        print("5 - Cancelar Reserva ❌")
    
    def mensaje_error(self):
        return print("Opcion no valida, solo Números")
    
    def mostrar_mensaje_continuar(self):
        return input("Presiona enter para continuar ➡️")
    
    def mostrar_mensaje(self):
        return print(f"Saliste del programa.Muchas gracias🙌")
    