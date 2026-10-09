"""Endpoints del BCRA"""

BASE_API_URL="https://api.bcra.gob.ar"

# Deudas www.bcra.gob.ar/en/api-documentation/?fileName=central-deudores-v1

CENTRAL_DEUDORES_DEUDAS="/centraldedeudores/v1.0/deudas/{identificacion}"
CENTRAL_DEUDORES_DEUDAS_HISTORICAS="/centraldedeudores/v1.0/deudas/historicas/{identificacion}"
CENTRAL_DEUDORES_CHEQUES_RECHAZADOS="/centraldedeudores/v1.0/deudas/chequesrechazados/{identificacion}"

# Cheques www.bcra.gob.ar/en/api-documentation/?fileName=cheques-v1
CHEQUES_ENTIDADES="/cheques/v1.0/entidades"
CHEQUES_DENUNCIADOS="/cheques/v1.0/denunciados/{codigoEntidad}/{numeroCheque}"

# Estadisticas Cambiarias www.bcra.gob.ar/en/api-documentation/?fileName=estadisticascambiarias-v1
CAMBIARIAS_DIVISAS="/estadisticascambiarias/v1.0/maestros/divisas"
CAMBIARIAS_COTIZACIONES="/estadisticascambiarias/v1.0/cotizaciones"
CAMBIARIAS_COTIZACIONES_MONEDA="/estadisticascambiarias/v1.0/cotizaciones/{moneda}"

# Estadísticas Monetarias 4.0 www.bcra.gob.ar/en/api-documentation/?fileName=estadisticas-monetarias-v3
METODOLOGIA="/estadisticas/v4.0/Metodologia"
METODOLOGIA_VARIABLE="/estadisticas/v4.0/Metodologia/{codigo}"

MONETARIAS="/estadisticas/v4.0/Monetarias"
MONETARIAS_VARIABLE="/estadisticas/v4.0/Monetarias/{codigo}"

# Regimen Transparencia www.bcra.gob.ar/en/api-documentation/?fileName=regimen-transparencia-v1
CAJAS_AHORROS="/transparencia/v1.0/cajasahorros/"
PAQUETES_PRODUCTOS="/transparencia/v1.0/paquetesproductos/"

PLAZOS_FIJOS="/transparencia/v1.0/plazosfijos/"

PRESTAMOS_PRENDARIOS="/transparencia/v1.0/prestamos/prendarios"
PRESTAMOS_HIPOTECARIOS="/transparencia/v1.0/prestamos/hipotecarios"
PRESTAMOS_PERSONALES="/transparencia/v1.0/prestamos/personales"

TARJETAS_DE_CREDITO="/transparencia/v1.0/tarjetascredito"
