class VistaCalendario:
    def pedir_dia(self):
        return int(input("Ingrese el día a realizar el evento: "))
    
    def mostrar_calendario(self,dia):
        print(f"Reserva:|{dia}/07/2023|")

    def estado(self,estado):
        return (f"La Fecha esta:{estado}🪄")