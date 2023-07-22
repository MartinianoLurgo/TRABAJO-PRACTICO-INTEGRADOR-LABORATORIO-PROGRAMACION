class Servicio:
    def __init__(self,idServicio = 0,tipoServicio ="",descripcion ="",costo=0,estado=None):
        self._idServicio = idServicio
        self._tipoServicio = tipoServicio
        self._descripcion = descripcion
        self._costo = costo
        self._estado = estado
    
    #Getters
    def get_idServicio(self):
        return self._idServicio
    def get_tipoServicio(self):
        return self._tipoServicio
    def get_descripcion(self):
        return self._descripcion
    def get_costo(self):
        return self._costo
    def get_estado(self):
        return self._estado

    
    #Setters
    def set_idServicio(self,data):
        self._idServicio = data
    def set_tipoServicio(self,data):
        self._tipoServicio = data
    def set_descripcion(self,data):
        self._descripcion = data
    def set_costo(self,data):
        self._costo = data
    def set_estado(self,data):
        self._estado = data
    
    def __str__(self) -> str:
        return print(f"Id: {self._idServicio}, Tipo de servicio: {self._tipoServicio}, Descripcion: {self._descripcion}, Costo: {self._costo}, Estado: {self._estado}")