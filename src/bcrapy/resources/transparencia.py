from bcrapy.endpoints import (
    CAJAS_AHORROS, 
    PAQUETES_PRODUCTOS, 
    PLAZOS_FIJOS, 
    PRESTAMOS_HIPOTECARIOS, 
    PRESTAMOS_PERSONALES, 
    PRESTAMOS_PRENDARIOS, 
    TARJETAS_DE_CREDITO
)
from bcrapy.response import Response

class Transparencia:
    def __init__(self, client):
        self.client = client

    def caja_ahorro(self) -> Response:
        """
        Consulta las tasas de interés de cajas de ahorro.
        :return: Response con la informacion de cajas de ahorro
        """
        return self.client.get(CAJAS_AHORROS)

    def paquetes_productos(self) -> Response:
        """
        Consulta las comisiones de paquetes de productos.
        :return: Response con la informacion de paquetes de productos
        """
        return self.client.get(PAQUETES_PRODUCTOS)
    
    def plazos_fijos(self) -> Response:
        """
        Consulta las tasas de interés de plazos fijos.
        :return: Response con la informacion de plazos fijos
        """
        return self.client.get(PLAZOS_FIJOS)

    def prestamos_prendarios(self) -> Response:
        """
        Consulta las tasas y comisiones de préstamos prendarios.
        :return: Response con la informacion de prestamos prendarios
        """
        return self.client.get(PRESTAMOS_PRENDARIOS)

    def prestamos_hipotecarios(self) -> Response:
        """
        Consulta las tasas y comisiones de préstamos hipotecarios.
        :return: Response con la informacion de prestamos hipotecarios
        """
        return self.client.get(PRESTAMOS_HIPOTECARIOS)

    def prestamos_personales(self) -> Response:
        """
        Consulta las tasas y comisiones de préstamos personales.
        :return: Response con la informacion de prestamos personales
        """
        return self.client.get(PRESTAMOS_PERSONALES)

    def tarjetas_de_credito(self) -> Response:
        """
        Consulta las tasas y comisiones de tarjetas de crédito.
        :return: Response con la informacion de tarjetas de credito
        """
        return self.client.get(TARJETAS_DE_CREDITO)