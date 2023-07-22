class Calendario:
    def __init__(self, dia="", mes=7, anio=2023, estado=True):
        self._dia = dia
        self._mes = mes
        self._anio = anio
        self._estado = estado

    # Getters
    def get_dia(self):
        return self._dia
    def get_mes(self):
        return self._mes
    def get_anio(self):
        return self._anio
    def get_estado(self):
        return self._estado

    # Setters
    def set_dia(self,data):
        self._dia = data
    def set_mes(self,data):
        self._mes = data
    def set_anio(self,data):
        self._anio = data
    def set_estado(self,data):
        self._estado = data
    
    def __str__(self) -> str:
        return print(f"Dia: {self._dia}, Mes: {self._mes}, Año: {self._anio},Estado: {self._estado}")