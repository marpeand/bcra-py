from .endpoints import BASE_API_URL

from .resources.deudores import Deudores
from .resources.cheques import Cheques
from .resources.transparencia import Transparencia
from .resources.cambiarias import Cambiarias
from .resources.monetarias import Monetarias

from .requester import Requester


class BCRAClient:
    def __init__(self):

        client = Requester(BASE_API_URL)

        self.deudores = Deudores(client)
        self.cheques = Cheques(client)
        self.cambiarias = Cambiarias(client)
        self.monetarias = Monetarias(client)
        self.transparencia = Transparencia(client)
