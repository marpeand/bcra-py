"""
La API de Estadísticas Cambiarias proporciona acceso a recursos relacionados con la
información de los tipos de cambio publicados por el BCRA.
"""


from typing import Optional
from datetime import datetime

from bcrapy.endpoints import *
from bcrapy.response import Response

class Cambiarias:
    def __init__(self, client):
        self.client = client

    def maestros(self) -> Response:
        """
        Recupera las divisas que pueden ser consultadas en la API de Tipo de Cambio.
        :return: dict con la informacion de las divisas
        """
        return self.client.get(CAMBIARIAS_DIVISAS)

    def cotizaciones(self, fecha: Optional[str] = None) -> Response:
        """
        Recupera las cotizaciones del tipo de cambio. 
        Si se proporciona un codigo, se recupera la cotizacion de esa divisa.
        Si no se proporciona un codigo, se recuperan todas las cotizaciones.
        :param codigo: Codigo de la divisa
        :return: dict con la informacion de las deudas
        """
        self._validate_date(fecha)
        params = {}
        if fecha:
            params['fecha'] = fecha
        return self.client.get(CAMBIARIAS_COTIZACIONES, params=params)

    def cotizacion(
        self, moneda: str, 
        fecha_desde: Optional[str] = None, 
        fecha_hasta: Optional[str] = None, 
        limit: Optional[int] = None, 
        offset: Optional[int] = None
        ) -> Response:
        """
        Recupera la cotizacion de una divisa en una fecha determinada.
        :param moneda: Codigo de la divisa
        :param fecha_desde: Fecha desde la cual se quiere obtener la cotizacion (YYYY-MM-DD)
        :param fecha_hasta: Fecha hasta la cual se quiere obtener la cotizacion (YYYY-MM-DD)
        :return: dict con la informacion de la cotizacion
        """
        self._validate_date(fecha_desde)
        self._validate_date(fecha_hasta)
        

        params = {}
        if fecha_desde:
            params['fechadesde'] = fecha_desde
        if fecha_hasta:
            params['fechahasta'] = fecha_hasta
        return self.client.get(CAMBIARIAS_COTIZACIONES_MONEDA.format(moneda=moneda), params=params)

    def _validate_date(self, fecha: Optional[str] = None) -> None:
        """
        Valida si la fecha es correcta.
        :param fecha: Fecha a validar
        """
        if fecha is not None:
            try:
                datetime.strptime(fecha, "%Y-%m-%d")
            except ValueError:
                raise ValueError(f"Formato de fecha incorrecto '{fecha}', debe ser YYYY-MM-DD")