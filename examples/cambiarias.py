from bcrapy.client import BCRAClient
from bcrapy.exceptions import APIError

def main():
    client = BCRAClient()

    print("--- ESTADÍSTICAS CAMBIARIAS ---")

    # 1. Obtener la lista de monedas maestras disponibles
    print("\nMonedas soportadas:")
    try:
        monedas = client.cambiarias.maestros().to_dataframe()
        print(monedas.head())
    except APIError as e:
        print(f"Error consultando monedas: {e}")

    # 2. Obtener las cotizaciones del día para una fecha específica
    print("\nCotizaciones del 2023-06-01:")
    try:
        cotizaciones_hoy = client.cambiarias.cotizaciones(fecha="2023-06-01").to_dataframe()
        print(cotizaciones_hoy.head())
    except APIError as e:
        print(f"Error consultando cotizaciones: {e}")

    # 3. Obtener el histórico de cotización de una moneda específica
    print("\nHistórico USD (Mayo 2023):")
    try:
        hist_usd = client.cambiarias.cotizacion(
            moneda="USD", 
            fecha_desde="2023-05-01", 
            fecha_hasta="2023-05-10"
        ).to_dataframe()
        print(hist_usd)
    except APIError as e:
        print(f"Error consultando histórico de USD: {e}")

if __name__ == "__main__":
    main()
