from bcrapy.client import BCRAClient
from bcrapy.exceptions import APIError

def main():
    client = BCRAClient()

    print("--- CENTRAL DE DEUDORES ---")
    
    # Usamos el CUIT de una entidad pública (ej: Banco Nación) para el ejemplo
    cuit = 30500010912
    
    # 1. Consultar el estado de deuda actual de un CUIT/CUIL
    print(f"\nConsultando deudas de: {cuit}")
    try:
        deudas = client.deudores.deudas(cuit).to_dataframe()
        if not deudas.empty:
            print(deudas.head())
        else:
            print("El sujeto no registra deudas en la central.")
    except APIError as e:
        print(f"Error consultando deudas: {e}")

    # 2. Historial de deudas (hasta 2 años de antiguedad)
    print(f"\nConsultando deudas históricas de: {cuit}")
    try:
        historicas = client.deudores.deudas_historicas(cuit).to_dataframe()
        if not historicas.empty:
            print(historicas.head())
    except APIError as e:
        print(f"Error consultando deudas históricas: {e}")
        
    cuit_cheques = 30717283186
    # 3. Cheques Rechazados
    print(f"\nConsultando cheques rechazados de: {cuit_cheques}")
    try:
        cheques_rech = client.deudores.cheques_rechazados(cuit_cheques).to_dataframe()
        if not cheques_rech.empty:
            print(cheques_rech.head())
        else:
            print("No posee cheques rechazados.")
    except APIError as e:
        print(f"Error consultando cheques rechazados: {e}")

if __name__ == "__main__":
    main()
