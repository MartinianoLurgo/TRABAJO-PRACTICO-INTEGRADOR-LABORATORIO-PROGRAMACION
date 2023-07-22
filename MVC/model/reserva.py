class Reserva:
    def __init__(self,idReserva=0, cliente="",fecha="",servicios="",importe="",nombreArchivo=""):
        self._idReserva = idReserva
        self._cliente = cliente
        self._fecha = fecha
        self._servicios = servicios
        self._importe = importe
        self._nombreDeArchivo = nombreArchivo

    # GETTERS
    def get_idReserva(self):
        return self._idReserva
    def get_cliente(self):
        return self._cliente
    def get_fecha(self):
        return self._fecha
    def get_servicios(self):
        return self._servicios
    def get_totalImporte(self):
        return self._totalImporte
    def get_nombreArchivo(self):
        return self._nombreDeArchivo
    
    #Setters
    def set_id(self,data):
        self._idReserva = data
    def set_cliente(self,data):
        self._cliente = data
    def set_fecha(self,data):
        self._fecha = data
    def set_servicios(self,data):
        self._servicios = data
    def set_totalImporte(self,data):
        self._totalImporte = data
    def set_nombreArchivo(self,data):
        self._nombreDeArchivo = data
    
    def __str__(self) -> str:
        return print(f"IdReserva: {self._idReserva}, Cliente: {self._cliente}, Fecha: {self._fecha}, Servicios: {self._servicios}, Total del importe: {self._totalImporte}")
    