from bcrapy.client import BCRAClient
from bcrapy.exceptions import APIError

def main():
    client = BCRAClient()

    print("--- BASE DE DATOS DE CHEQUES ---")

    # 1. Consultar entidades habilitadas (Bancos)
    print("\nEntidades Bancarias Disponibles:")
    try:
        entidades = client.cheques.entidades().to_dataframe()
        print(entidades.head())
    except APIError as e:
        print(f"Error consultando entidades: {e}")

    # 2. Consultar un cheque denunciado específico
    # codigoEntidad: 3 dígitos (Ej: Banco Galicia = '007')
    # numeroCheque: 7 dígitos (Ej: '1234567')
    codigo_banco = "007"
    nro_cheque = "1234567"
    
    print(f"\nConsultando cheque denunciado Nro {nro_cheque} del banco {codigo_banco}:")
    try:
        cheque_denunciado = client.cheques.denunciados(
            codigoEntidad=codigo_banco, 
            numeroCheque=nro_cheque
        ).to_dataframe()
        
        if not cheque_denunciado.empty:
            print(cheque_denunciado)
        else:
            print("El cheque no registra denuncias.")
    except APIError as e:
        print(f"El cheque no existe o hubo un error: {e}")

if __name__ == "__main__":
    main()
