class VistaItem:
    def mostrar_menu_item(self):
        print("🔅================🔸🔱🔸================🔅")
        print("       BIENVENIDO AL MENU PRINCIPAL")
        print("🔅================🔸⚜️🔸================🔅")
        print("---------Ingrese que Desea Realizar----------")
        print("[1] Mostrar Costos De Evento")
        print("[2] Calcular Devolucion")

    def mostrar_importe_servicios(self,servicio):
        return(f"Importe de servicios :{servicio}⛽")
        
    def mostrar_iva(self,iva):
        return (f" IVA total: {iva}😮")
    
    def mostrar_importe_senia(self,senia):
        return(f"La seña que dio el cliente es de: {senia}💵")
    
    def mostrar_importe_total(self,total):
        return (f"El total de servico: {total} 🛒")
    
    def mostrar_importe_devolucion(self,devolucion):
        return (f"Devolucion: {devolucion}👌")
        
