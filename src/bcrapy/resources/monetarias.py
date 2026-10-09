from bcrapy.endpoints import METODOLOGIA, METODOLOGIA_VARIABLE, MONETARIAS, MONETARIAS_VARIABLE
from .bcra_variables import VARIABLES
from bcrapy.response import Response


class Monetarias:
    def __init__(self, client):
        self._client = client

    def metodologia(self) -> Response:
        """
        Consulta la lista de metodologias de estadísticas monetarias publicadas por el BCRA.
        :return: Response con la informacion
        """
        return self._client.get(METODOLOGIA)

    def metodologia_codigo(self, codigo) -> Response:
        """
        Consulta la metodología de una variable específica.
        :param codigo: Codigo de la variable
        :return: Response con la informacion
        """
        return self._client.get(METODOLOGIA_VARIABLE.format(codigo=codigo))

    def monetarias(self) -> Response:
        """
        Consulta las variables monetarias publicadas por el BCRA.
        :return: Response con la lista de variables
        """
        return self._client.get(MONETARIAS)

    def monetarias_codigo(self, codigo, desde: str = "", hasta: str = "" ) -> Response:
        """
        Consulta los valores históricos de una variable monetaria.
        :param codigo: Codigo de la variable
        :param desde: Fecha inicial (YYYY-MM-DD) opcional
        :param hasta: Fecha final (YYYY-MM-DD) opcional
        :return: Response con los datos de la variable
        """
        params = {}
        if desde:
            params['desde'] = desde
        if hasta:
            params['hasta'] = hasta
        return self._client.get(MONETARIAS_VARIABLE.format(codigo=codigo), params=params)


def create_method(codigo, name):
    def method(self, desde: str = "", hasta: str = ""):
        return self.monetarias_codigo(codigo, desde, hasta)
    method.__name__ = name
    return method


for var in VARIABLES:
    setattr(
        Monetarias,
        var.name,
        create_method(var.id, var.name),
    )