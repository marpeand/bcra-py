import httpx
from .response import Response
from .exceptions import APIError

class Requester:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(
            timeout=10
        )

    def get(self, url: str, params: dict = None) -> dict:
        """
        Hace una peticion GET a la URL especificada.
        La misma ya crea la Session usando httpx
        :param url: URL a consultar
        :param params: Diccionario de parametros para la peticion GET
        :return: dict con la respuesta de la API
        """
        try:
            response = self.client.get(f"{self.base_url}{url}", params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            error_msg = e.response.text if e.response else str(e)
            raise APIError(f"Error HTTP {e.response.status_code} al consultar la API: {error_msg}")
        except Exception as e:
            raise APIError(f"Error inesperado al consultar la API: {str(e)}")
        
        return Response(response.json())

    