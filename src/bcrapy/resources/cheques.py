from bcrapy.endpoints import *
from bcrapy.response import Response

class Cheques:
    def __init__(self, client):
        self.client = client

    def entidades(self) -> Response:
        """
        Consultas las entidades del BCRA.
        :return: dict con listado de las entidades disponibles
        """
        return self.client.get(CHEQUES_ENTIDADES)


    def denunciados(self, codigoEntidad: str, numeroCheque: str) -> Response:
        """
        Consultas un cheque de una entidad
        :param codigoEntidad: Código de la entidad consultada
        :param numeroCheque: Número del cheque consultado
        :return: dict con la informacion de las deudas
        """
        self._validate_codigo_entidad(codigoEntidad)
        self._validate_numero_cheque(numeroCheque)
        return self.client.get(CHEQUES_DENUNCIADOS.format(codigoEntidad=codigoEntidad, numeroCheque=numeroCheque))
    

    def _validate_codigo_entidad(self, codigoEntidad: str):
        """
        Valida que el codigo de la entidad sea correcto
        :param codigoEntidad: Codigo de la entidad a validar
        :return: None
        """
        if not codigoEntidad or len(codigoEntidad) != 3:
            raise ValueError("Debe proporcionar el codigo de la entidad")

    def _validate_numero_cheque(self, numeroCheque: str):
        """
        Valida que el numero del cheque sea correcto
        :param numeroCheque: Numero del cheque a validar
        :return: None
        """
        if not numeroCheque or len(numeroCheque) != 7:
            raise ValueError("Debe proporcionar el numero del cheque")