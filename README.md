# bcra-py

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PyPI version](https://badge.fury.io/py/bcra-py.svg)](https://badge.fury.io/py/bcra-py)

An unofficial Python wrapper to interact with the official [API of the Central Bank of the Argentine Republic (BCRA)](https://www.bcra.gob.ar/en/central-bank-api-catalog/).

`bcra-py` allows to easily query financial information, monetary statistics, exchange rates, debtors' credit risk, reported checks, and the BCRA's transparency regime. The library supports exporting the results directly to Pandas DataFrames, CSV, JSON, or Excel.

---

## Features

- **Monetary Statistics (`monetarias`)**: Query monetary variables and their methodology using dynamic properties.
- **Exchange Rates (`cambiarias`)**: Retrieve the list of supported currencies and the official exchange rates.
- **Central de Deudores (`deudores`)**: Search for credit status, historical debt reports, and rejected checks using a CUIT/CUIL/CDI.
- **Checks (`cheques`)**: Get a list of financial entities and query reported (stolen/lost) checks.
- **Transparency (`transparencia`)**: Access comparative financial data regarding savings accounts, term deposits, credit cards, and loans.
- **Data Export**: Easily convert API responses to `pandas.DataFrame`, `CSV`, `JSON`, or `Excel`.

---

## Installation

```bash
pip install bcra-py
```

Or install locally from source:

```bash
git clone https://github.com/marpeand/bcra-py.git
cd bcra-py
pip install .
```

---

## Quick Start

```python
from bcrapy.client import BCRAClient

# Initialize the client
client = BCRAClient()

# Example 1: Query the BADLAR rate (dynamically generated monetary variable)
df_badlar = client.monetarias.badlar_bancos_privados(
    desde="2023-01-01",
    hasta="2023-01-31"
).to_dataframe()
print(df_badlar.head())

# Example 2: Query the 'Central de Deudores' (Credit Risk) using a CUIT/CUIL (e.g. Banco Nación)
deudores_resp = client.deudores.deudas("30-50001091-2")
print(deudores_resp.to_dataframe())

# Example 3: Query today's exchange rates
cotizaciones = client.cambiarias.cotizaciones()
print(cotizaciones.to_dataframe())

# Export data to CSV / JSON / Excel
res = client.transparencia.plazos_fijos()
res.to_csv("plazos_fijos.csv")
res.to_excel("plazos_fijos.xlsx")
res.to_json("plazos_fijos.json")
```

---

## Module Overview

| Resource               | Description                   | Example Methods                                                                      |
| ---------------------- | ----------------------------- | ------------------------------------------------------------------------------------ |
| `client.monetarias`    | Monetary statistics           | `metodologia()`, `badlar_bancos_privados()`, `reservas_internacionales()`            |
| `client.cambiarias`    | Currencies and exchange rates | `maestros()`, `cotizaciones(fecha)`, `cotizacion(moneda)`                            |
| `client.deudores`      | Credit info and debtors       | `deudas(cuit)`, `deudas_historicas(cuit)`, `cheques_rechazados(cuit)`                |
| `client.cheques`       | Banking entities and checks   | `entidades()`, `denunciados(codigoEntidad, numeroCheque)`                            |
| `client.transparencia` | Bank products comparison      | `caja_ahorro()`, `plazos_fijos()`, `tarjetas_de_credito()`, `prestamos_personales()` |

---

## License

This project is licensed under the terms of the [MIT License](LICENSE).
