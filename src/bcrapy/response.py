import pandas as pd

class Response:
    """
    Clase para manejar la respuesta de la API.
    """
    def __init__(self, response: dict):
        self.response = response
        self.data = response.get('results', response)

    def raw(self) -> dict:
        """
        Retorna la respuesta cruda de la API.
        :return: dict con la respuesta de la API
        """
        return self.response
    
    def to_dataframe(self) -> pd.DataFrame:
        """
        Convierte la respuesta de la API a un DataFrame de Pandas.
        :return: pd.DataFrame con la respuesta de la API
        """
        if isinstance(self.data, dict):
            json_data = self._normalize_dict(self.data)
            return pd.DataFrame([json_data])
        elif isinstance(self.data, list):
            flattened_data = []
            for item in self.data:
                if isinstance(item, dict) and 'detalle' in item and isinstance(item['detalle'], list):
                    base_info = {k: v for k, v in item.items() if k != 'detalle'}
                    for det in item['detalle']:
                        if isinstance(det, dict):
                            flattened_data.append(self._normalize_dict({**base_info, **det}))
                        else:
                            flattened_data.append(self._normalize_dict({**base_info, 'valor': det}))
                else:
                    flattened_data.append(self._normalize_dict(item) if isinstance(item, dict) else item)
            return pd.DataFrame(flattened_data)
        return pd.DataFrame()

    def _normalize_dict(self, d: dict, parent_key: str = '', sep: str = '_') -> dict:
        """
        Normaliza un diccionario anidado.
        :param d: Diccionario a normalizar
        :param parent_key: Clave padre
        :param sep: Separador
        :return: dict normalizado
        """
        items = []
        for k, v in d.items():
            if isinstance(v, dict):
                items.extend(self._normalize_dict(v, parent_key, sep=sep).items())
            elif isinstance(v, list):
                for item in v:
                    items.extend(self._normalize_dict(item, parent_key, sep=sep).items())
            else:
                items.append((k, v))
        return dict(items)
    
    def to_csv(self, filename: str) -> bool:
        """
        Convierte la respuesta de la API a un archivo CSV.
        :param filename: Nombre del archivo CSV
        :return: True si se escribió correctamente, False en caso contrario
        """
        try:
            self.to_dataframe().to_csv(filename, index=False)
            return True
        except Exception:
            return False
    
    def to_json(self, filename: str) -> bool:
        """
        Convierte la respuesta de la API a un archivo JSON.
        :param filename: Nombre del archivo JSON
        :return: True si se escribió correctamente, False en caso contrario
        """
        try:
            self.to_dataframe().to_json(filename, orient='records')
            return True
        except Exception:
            return False
    
    def to_excel(self, filename: str) -> bool:
        """
        Convierte la respuesta de la API a un archivo Excel.
        :param filename: Nombre del archivo Excel
        :return: True si se escribió correctamente, False en caso contrario
        """
        try:
            self.to_dataframe().to_excel(filename, index=False)
            return True
        except Exception:
            return False

    def __str__(self) -> str:
        return str(self.data)
    