class Cliente:
<<<<<<< Updated upstream
    def __init__(self,idCliente=0,nombre="" , apellido="" , dni=0 , telefono=0,metododepago=""):
=======
    def __init__(self, idCliente, nombre, apellido, dni, telefono, metodoDePago):
>>>>>>> Stashed changes
        self._idCliente = idCliente
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._telefono = telefono
<<<<<<< Updated upstream
        self._metodoDePago = metododepago
=======
        self._metodoDePago = metodoDePago
>>>>>>> Stashed changes

    #GETTERS
    def get_idCliente(self):
        return self._idCliente
    def get_nombre(self):
        return self._nombre
    def get_apellido(self):
        return self._apellido
    def get_dni(self):
        return self._dni
    def get_telefono(self):
        return self._telefono
    def get_metodoDePago(self):
        return self._metodoDePago
    
    #SETTERS 
    def set_idCliente(self, data):
        self._idCliente = data
    def set_nombre(self,data):
        self._nombre = data
    def set_apellido(self,data):
        self._apellido = data
    def set_dni(self,data):
        self._dni = data
    def set_telefono(self,data):
        self._telefono = data
    def set_metodoDePago(self,data):
        self._metodoDePago = data
    
    def __str__(self) -> str:
        return print(f"IdCliente: {self._idCliente}, Nombre: {self._nombre}, Apellido: {self._apellido}, DNI: {self._dni}, Telefono: {self._telefono}, Metodo de pago: {self._metodoDePago}")