class VistaServicio:
    def mostrar_menu_servicios(self):
        print(" 🔅================🔸🔱🔸================🔅")
        print("       BIENVENIDO AL MENU DE SERVICIOS")
        print(" 🔅================🔸⚜️🔸================🔅")
        print(" 1 - Mostrar lista y costos de servicios 📒")
        print(" 2 - Modificar precio de servicios 💴")
        print(" 3 - Modificar precio de gasto administrativo 💵")
        print(" 4 - Volver al menú principal 🔙 ")

    def mostrar_servicios(self,data):
        print(data)
    def elegir_servicio(self):
        return input("Ingrese el Numero de identificacion del Servicio🎉: ")
    
    def elegir_modificar_servicio(self):
        return input("Ingrese el Numero de identificacion del Servicio que quiere modificar🎉: ")

    def modificar_precio(self):
        return float(input("Ingresar el Nuevo Precio💵: "))

    def archivo_noEncontrado(self):
        print("------------------------------------")
        print("El Archivo no se encuenta Disponible")
        print("------------------------------------")

    def dato_invalido(self):
        print("Error, dato ingresado no válido ❌.")
    
    def mostrar_lista_servicios(self):
        print(" 🔅================🔸🔱🔸================🔅")
        print("            LISTA DE SERVICIOS")
        print(" 🔅================🔸⚜️🔸================🔅")
