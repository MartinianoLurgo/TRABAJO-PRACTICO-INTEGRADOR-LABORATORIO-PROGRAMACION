class vistacliente:
    def mostrar_menu(self):
        print(" 🔅================🔸🔱🔸================🔅")
        print("       BIENVENIDO AL MENU DE CLIENTES")
        print(" 🔅================🔸⚜🔸================🔅") 
        print(" 1 - Mostrar Lista de Clientes 🧑‍💻")
        print(" 2 - Cambiar Datos del Cliente 💱")
        print(" 3 - Volver al menú principal 🔙 ")
    def mostrar_lista_clientes(self):
        print(" 🔅================🔸🔱🔸================🔅")
        print("             LISTA DE CLIENTES")
        print(" 🔅================🔸⚜🔸================🔅")

    def mostrar_registro(self):
        print(" 🔅================🔸🔱🔸================🔅")
        print("          COMIENZO DE REGISTRO CLIENTE")
        print(" 🔅================🔸⚜🔸================🔅")

    def mostrar(self,id,nombre,apellido,dni,telefono,pago):
        print(f"{id} - {nombre} - {apellido} - {dni} - {telefono} - {pago}")
    
    def cambiar_atributos(self):
        print(" 🔅================🔸🔱🔸================🔅")
        print("              CAMBIAR ATRIBUTOS")
        print(" 🔅================🔸⚜🔸================🔅")
        print(" 1 - ID")
        print(" 2 - nombre")
        print(" 3 - apellido ")
        print(" 4 - dni")
        print(" 5 - telefono")
        print(" 6 - metodo de pago ")
        return input("Ingrese la opción que desee cambiar ➡️ ")

    def pedir_id(self):
        return int(input("Ingrese el ID de la persona que desee cambiar ➡️ "))
    
    def pedir_nombre(self):
        return input("Ingrese el Nombre: ")

    def pedir_apellido(self):
        return input("Ingrese el Apellido: ")

    def pedir_dni(self):
        return int(input("Ingrese el número de DNI del cliente: ")) 

    def pedir_telefono(self):
        return int(input("Ingrese el teléfono 📞: "))

    def pedir_metodo_de_pago(self):
        return input("Ingrese el Metodo de Pago del Cliente💲: ")

    def dato_invalido(self):
        return("Error, dato ingresado no válido ❌.")

    def registro_exitoso(self):
        return("Se Registro el cliente ✅.")

    def cliente_no_encontrado(self):
        return("No se encontró el cliente ❌.")
    
    def archivo_no_encontrado(self):
        return print("Archivo de Clientes no encontrado")