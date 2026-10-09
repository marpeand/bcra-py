from bcrapy.client import BCRAClient
from bcrapy.exceptions import APIError

def main():
    client = BCRAClient()

    print("--- ESTADÍSTICAS MONETARIAS ---")
    
    # 1. Consultar una variable utilizando su método autogenerado
    print("\nTasa BADLAR Bancos Privados (Enero 2023):")
    try:
        df_badlar = client.monetarias.badlar_bancos_privados(
            desde="2023-01-01", 
            hasta="2023-02-01"
        ).to_dataframe()
        print(df_badlar.head())
    except APIError as e:
        print(f"Error consultando BADLAR: {e}")

    # 2. También puedes consultar las Reservas Internacionales
    print("\nReservas Internacionales (Principios de Enero 2023):")
    try:
        df_reservas = client.monetarias.reservas_internacionales(
            desde="2023-01-01", 
            hasta="2023-01-10"
        ).to_dataframe()
        print(df_reservas.head())
    except APIError as e:
        print(f"Error consultando Reservas: {e}")
    
    # 3. Exportar datos (envuelto en try/except para evitar fallos de red)
    print("\nExportando datos...")
    try:
        res = client.monetarias.reservas_internacionales()
        res.to_csv("reservas_historicas.csv")
        res.to_json("reservas_historicas.json")
        res.to_excel("reservas_historicas.xlsx")
        print("Exportación exitosa!")
    except APIError as e:
        print(f"Error exportando datos: {e}")

if __name__ == "__main__":
    main()
