"""
El servicio Api de Central de deudores, permite obtener un informe consolidado por clave de
identificación fiscal (CUIT, CUIL o CDI) para una persona humana o jurídica respecto de
financiaciones otorgadas por entidades financieras, fideicomisos financieros, entidades no
financieras emisoras de tarjetas de crédito / compra, otros proveedores no financieros de
créditos, sociedades de garantía recíproca, fondos de garantía de carácter público y proveedores
de servicios de crédito entre particulares a través de plataformas. 
Además, cheques rechazados.
Su difusión no implica conformidad por parte de este Banco Central.

"""

from bcrapy.endpoints import *
from bcrapy.response import Response

class Deudores:
    def __init__(self, client):
        self.client = client

    def deudas(self, identificacion: str | int) -> Response:
        """
        Consultas las deudas del sujeto consultado en el BCRA.
        Se puede consultar hasta con 2 años de antiguedad.
        :param identificacion: CUIT/CUIL/CDI del sujeto consultado
        :return: Response con la informacion de las deudas
        """
        identificacion = self._validate_identification(identificacion)
        response = self.client.get(CENTRAL_DEUDORES_DEUDAS.format(identificacion=identificacion))
        return response


    def deudas_historicas(self, identificacion: str | int) -> Response:
        """
        Consultas las deudas del sujeto consultado en el BCRA. 
        Se puede consultar hasta con 2 años de antiguedad.
        :param identificacion: CUIT del sujeto consultado
        :return: dict con la informacion de las deudas
        """
        identificacion = self._validate_identification(identificacion)
        response = self.client.get(CENTRAL_DEUDORES_DEUDAS_HISTORICAS.format(identificacion=identificacion))
        return response
    
    def cheques_rechazados(self, identificacion: str | int) -> Response:
        """
        Consultas los cheques rechazados del sujeto consultado en el BCRA. 
        Se puede consultar hasta con 2 años de antiguedad.
        :param identificacion: CUIT/CUIL/CDI del sujeto consultado
        :return: dict con la informacion de los cheques rechazados
        """
        identificacion = self._validate_identification(identificacion)
        response = self.client.get(CENTRAL_DEUDORES_CHEQUES_RECHAZADOS.format(identificacion=identificacion))
        return response


    def _validate_identification(self, identificacion: str | int) -> str:
        """
        Valida que la identificacion sea correcta tanto para CUIL/CUIT/CDI.
        Retorna la identificacion sin formato
        :param identificacion: CUIT/CUIL/CDI del sujeto consultado
        :return: str con la identificacion
        """
        import re
        identificacion = str(identificacion)
        
        # Mantiene únicamente los caracteres numéricos
        identificacion = re.sub(r"\D", "", identificacion)

        if len(identificacion) != 11:
            raise ValueError("La identificacion debe tener 11 digitos numericos")
        return identificacion