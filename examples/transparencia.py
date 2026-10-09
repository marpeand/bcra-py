from bcrapy.client import BCRAClient
from bcrapy.exceptions import APIError

def main():
    client = BCRAClient()

    print("--- RÉGIMEN DE TRANSPARENCIA ---")

    # 1. Consultar Plazos Fijos
    print("\nPlazos Fijos Disponibles:")
    try:
        plazos_fijos = client.transparencia.plazos_fijos().to_dataframe()
        print(plazos_fijos.head())
    except APIError as e:
        print(f"Error consultando plazos fijos: {e}")

    # 2. Consultar Tarjetas de Crédito
    print("\nCostos y Tasas de Tarjetas de Crédito:")
    try:
        tarjetas = client.transparencia.tarjetas_de_credito().to_dataframe()
        print(tarjetas.head())
    except APIError as e:
        print(f"Error consultando tarjetas: {e}")
    
    # 3. Consultar resultados en crudo (raw)
    try:
        cajas_ahorro = client.transparencia.caja_ahorro().raw()
        results = cajas_ahorro.get('results', [])
        print(f"\nSe encontraron {len(results)} registros de cajas de ahorro.")
    except APIError as e:
        print(f"Error consultando cajas de ahorro: {e}")

if __name__ == "__main__":
    main()
