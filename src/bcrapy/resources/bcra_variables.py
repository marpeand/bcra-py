"""Catálogo de las 50 variables principales de la API de Estadísticas BCRA.

Cada entrada tiene `id` (idVariable en la API), `name` (identificador snake_case
apto para nombre de método) y `doc` (descripción oficial, usable como docstring).
Generado a partir de test.json.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Variable:
    id: int
    name: str
    doc: str


VARIABLES: tuple[Variable, ...] = (
    # Reservas y tipo de cambio
    Variable(
        id=1,
        name='reservas_internacionales',
        doc='Información diaria del saldo de reservas internacionales que se publica mediante Comunicación “C” (Ref. Reservas Internacionales). El saldo de las Reservas Internacionales del último día hábil de cada año calendario incorpora los ajustes que se efectúan al cierre del Balance General, con información hasta el día 31 de diciembre. Por esta razón puede diferir del dato publicado en el comunicado diario correspondiente al último día hábil del año. Excluye las asignaciones de Derechos Especiales de Giro del año 2009.',
    ),
    Variable(
        id=4,
        name='tipo_cambio_minorista',
        doc='Corresponde al tipo de cambio peso por dólar estadounidense remitido dada la Comunicación B 9791',
    ),
    Variable(
        id=5,
        name='tipo_cambio_mayorista',
        doc='Corresponde al tipo de cambio peso por dólar estadounidense calculado por el BCRA , según Comunicación A 3500 y Comunicaicón A 8359. Esta variable se publica mediante Comunicación C sobre “Tipo de Cambio de Referencia".',
    ),
    Variable(
        id=77,
        name='variacion_diaria_reservas',
        doc='Variación diaria del stock total de reservas internacionales del BCRA.',
    ),
    Variable(
        id=78,
        name='compras_divisas_bcra',
        doc='Compras y ventas de divisas del BCRA en el mercado de cambios, con excepción de las realizadas directamente al Tesoro Nacional.',
    ),
    # Tasas de interés
    Variable(
        id=7,
        name='badlar_bancos_privados',
        doc='Tasa de interés promedio ponderada por montos operados de los depósitos a plazo fijo de un millón de pesos o más, de 30 hasta 35 días de plazo, según lo informado por los bancos privados a través del SISCEN-0002, en las cuentas SISCEN 149 y 152 (plazos fijos transferibles e intransferibles con retribución fija).',
    ),
    Variable(
        id=8,
        name='tm20_bancos_privados',
        doc='Tasa de interés promedio ponderada por montos operados de los depósitos a plazo fijo de veinte millones de pesos o más, de 30 hasta 35 días de plazo, según lo informado por los bancos privados a través del SISCEN-0002, en las cuentas SISCEN 149 y 152 (plazos fijos transferibles e intransferibles con retribución fija).',
    ),
    Variable(
        id=44,
        name='tamar_bancos_privados',
        doc='Tasa de interés promedio ponderada por montos operados, correspondiente a depósitos a plazo fijo mayoristas en pesos, de 30 a 35 días de plazo, constituidos en todas las entidades bancarias privadas del país. En 2025 abarcó las operaciones de 1.000 millones de pesos y más. A partir de 2026, una vez al año, se actualiza el estrato de monto de las operaciones incluidas, según la variación del Índice de Precios al Consumidor. Los detalles metodológicos se pueden consultar en el siguiente vínculo: https://www.bcra.gob.ar/archivos//Pdfs/PublicacionesEstadisticas/tasmet.pdf',
    ),
    Variable(
        id=135,
        name='tamar_total_bancos',
        doc='Tasa de interés promedio ponderada por montos operados, correspondiente a depósitos a plazo fijo mayoristas en pesos, de 30 a 35 días de plazo, constituidos en todas las entidades bancarias del país. En 2025 abarcó las operaciones de 1.000 millones de pesos y más. A partir de 2026, una vez al año, se actualiza el estrato de monto de las operaciones incluidas, según la variación del Índice de Precios al Consumidor. Los detalles metodológicos se pueden consultar en el siguiente vínculo: https://www.bcra.gob.ar/archivos//Pdfs/PublicacionesEstadisticas/tasmet.pdf',
    ),
    Variable(
        id=138,
        name='badlar_total_bancos',
        doc='Tasa de interés promedio ponderada por montos operados de los depósitos a plazo fijo de un millón de pesos o más, de 30 hasta 35 días de plazo, según lo informado por los bancos públicos y privados a través del SISCEN-0002, en las cuentas SISCEN 149 y 152 (plazos fijos transferibles e intransferibles con retribución fija).',
    ),
    Variable(
        id=141,
        name='tm20_total_bancos',
        doc='Tasa de interés promedio ponderada por montos operados de los depósitos a plazo fijo de veinte millones de pesos o más, de 30 hasta 35 días de plazo, según lo informado por los bancos públicos y privados a través del SISCEN-0002, en las cuentas SISCEN 149 y 152 (plazos fijos transferibles e intransferibles con retribución fija).',
    ),
    Variable(
        id=12,
        name='tasa_plazo_fijo_30_dias',
        doc='Tasa de interés promedio ponderada por montos operados del total de entidades informantes en SISCEN-0002 en el segmento de operaciones de plazo fijo de 30 días en moneda nacional, informados en las cuentas SISCEN 149 y 152 (plazos fijos transferibles e intransferibles con retribución fija).',
    ),
    Variable(
        id=43,
        name='tasa_efectiva_depositos_caja_ahorro_plazo_fijo',
        doc='Serie estadística de tasa de interés en base a las tasas de caja de ahorros y de plazo fijo (Comunicado 14290). Refleja diariamente la capitalización de la tasa diaria equivalente a la tasa de interés efectiva mensual promedio ponderada de los depósitos en caja de ahorros y a plazo fijo en pesos correspondiente al segundo día hábil anterior a la fecha informada, según la encuesta SISCEN-0002 que diariamente realiza el BCRA. Los detalles metodológicos se pueden consultar en el siguiente vínculo: https://www.bcra.gob.ar/archivos//Pdfs/PublicacionesEstadisticas/tasmet.pdf',
    ),
    Variable(
        id=11,
        name='tasa_prestamos_interbancarios_privados',
        doc='Es la tasa de interés promedio ponderada por monto correspondiente a préstamos entre entidades bancarias privadas por operaciones de préstamos de efectivo hasta 15 días de plazo, a tasa de interés fija distinta de cero',
    ),
    Variable(
        id=144,
        name='tasa_prestamos_personales',
        doc='Promedio ponderada por montos otorgados de préstamos personales en pesos al sector privado no financiero a tasa de interés fija o repactable, considerando los datos informados por la totalidad de entidades financieras de todo el país, a través del SISCEN -0018 en la cuenta SISCEN 51',
    ),
    Variable(
        id=145,
        name='tasa_adelantos_cuenta_corriente',
        doc='Tasa de interés promedio ponderada por saldos pactada por el otorgamiento de préstamos a empresas del sector privado, no prestadoras de servicios financieros ni PyMEs, bajo la forma de adelantos en cuenta corriente con acuerdo, de 1 a 7 días de plazo, y de diez millones de pesos o más, en moneda nacional, según lo informado por la totalidad de entidades financieras a través del requerimiento informativo SISCEN-0018 en la cuenta SISCEN 44 (adelantos en cuenta corriente).',
    ),
    Variable(
        id=150,
        name='tasa_repo_mae_rix',
        doc='Corresponde a la tasa de interés denominada “RIX”. Se calcula como la tasa de interés promedio ponderada por monto de las operaciones en la rueda REPO entre agentes del Mercado Abierto Electrónico (MAE), de 1 día hábil, excluyendo aquellas en las que el BCRA es contraparte y las concertadas a tasa cero',
    ),
    Variable(
        id=151,
        name='monto_repo_mae',
        doc='Monto negociado de operaciones de pases en la rueda REPO del MAE, en las que el BCRA no es contraparte',
    ),
    Variable(
        id=160,
        name='tasa_politica_monetaria',
        doc='Hasta el 31 de diciembre de 2016 corresponde a la tasa de interés de la LEBAC a 35 días de plazo. A partir del 2 de enero de 2017 corresponde al centro del corredor de tasas de interés de los pases a 7 días de plazo. A partir del 8 de agosto de 2018, la tasa de referencia de la política monetaria es la de Letras de Liquidez (LELIQ). A partir del 21 de enero de 2020, corresponde a la tasa promedio ponderada de la LELIQ de menor plazo subastada en la última licitación adjudicada, la cual mantendrá su vigencia hasta el siguiente proceso de subasta. A partir del 6 de enero de 2022 es la tasa de interés anunciada por el BCRA para la LELIQ de 28 días. A partir del 18 de diciembre de 2023 es la tasa de interés de los pases pasivos a un día de plazo. A partir del 22 de julio de 2024 es la tasa de interés anunciada por el BCRA y devengada por las Letras Fiscales de Liquidez (LEFI). A partir del 11 de julio de 2025 el BCRA dejó de anunciar una tasa de política monetaria.',
    ),
    # Base monetaria y agregados
    Variable(
        id=15,
        name='base_monetaria',
        doc='Es la suma de la circulación monetaria total y los depósitos en cuenta corriente en pesos de las entidades financieras en el BCRA. Es difundida diariamente por el BCRA mediante Comunicación C.',
    ),
    Variable(
        id=16,
        name='circulacion_monetaria',
        doc='Billetes y monedas emitidos por el BCRA y puestos en circulación y cheques cancelatorios en pesos. Se difunde diariamente mediante Comunicación C del BCRA.',
    ),
    Variable(
        id=17,
        name='circulacion_en_poder_del_publico',
        doc='Circulación monetaria que no está en poder de las entidades financieras. Se obtiene calculando la diferencia entre la circulación monetaria total difundida diariamente por el BCRA mediante Comunicación “C” y el efectivo en pesos en poder de las entidades financieras',
    ),
    Variable(
        id=18,
        name='efectivo_en_entidades_financieras',
        doc='Saldo de efectivo en billetes y monedas que las entidades financieras mantienen en sus cajas y cajeros automáticos para atender las operaciones diarias con sus clientes. Se expresa en millones de pesos y se publica diariamente con dos días hábiles de rezago.',
    ),
    Variable(
        id=19,
        name='depositos_cuenta_corriente_en_bcra',
        doc='Depósitos en cuenta corriente en pesos en el BCRA que forman parte de la base monetaria, difundido diariamente mediante Comunicación “C”.',
    ),
    Variable(
        id=25,
        name='m2_privado',
        doc='El M2 privado comprende circulante en poder del público más depósitos a la vista en pesos del sector privado no financiero. Se calcula como la suma entre billetes y monedas en poder del público, cheques cancelatorios en pesos y cuentas corrientes y cajas de ahorros en pesos del sector privado no financiero.',
    ),
    # Depósitos y préstamos
    Variable(
        id=21,
        name='depositos_total',
        doc='Depósitos en efectivo del total sectores constituidos en las entidades financieras, en moneda nacional y extranjera.',
    ),
    Variable(
        id=22,
        name='depositos_cuenta_corriente',
        doc='Depósitos de efectivo constituidos por el total de sectores en las entidades financieras bajo la forma de cuenta corriente bancaria, en moneda nacional y extranjera, neto de la Utilización de Fondos Unificados de Cuentas Oficiales.',
    ),
    Variable(
        id=23,
        name='depositos_caja_ahorro',
        doc='Depósitos de efectivo constituidos bajo el sistema de caja de ahorros. Incluye depósitos de efectivo en cuentas de ahorro vinculado a préstamos, en cuentas especiales para círculos cerrados, en la cuenta Fondo de desempleo en cuentas abiertas bajo el sistema de usuras pupilares, en cuentas especiales para la acreditación de remuneraciones, en cuentas corrientes especiales para personas jurídicas y en las Cuentas especiales a las que se refiere la Ley 27.260 - Régimen de 27.260 - Régimen de sinceramiento fiscal – LIBRO II - Título I – Artículo 38, inciso c), Art. 41 y Art. 42, incisos b) y c) y Art. 41 y Art. 44 y Ley 27.613.',
    ),
    Variable(
        id=24,
        name='depositos_plazo_fijo',
        doc='Depósitos de efectivo constituidos por el total de sectores en las entidades financieras a plazo fijo (transferibles e intransferibles, con retribución fija y variable, de Unidades de Valor Adquisitivo actualizables por “CER” – Ley 25.827 -UVA- y de Unidades de Vivienda actualizables por “ICC” – Ley 27.271 -UVI-). Incluye las inversiones a plazo con retribución variable y las realizadas con cláusula que contemple la posibilidad de cancelación anticipada.',
    ),
    Variable(
        id=26,
        name='prestamos_sector_privado',
        doc='Préstamos de efectivo, en moneda nacional y extranjera, otorgados por las entidades financieras al sector privado no financiero.',
    ),
    # Inflación, expectativas e índices
    Variable(
        id=27,
        name='inflacion_mensual',
        doc='Variación mensual del índice de precios al consumidor informado por INDEC. En el período comprendido entre noviembre 2015 y abril 2016 se incluyen los valores considerados en el cálculo del Coeficiente de Estabilización de Referencia. Entre noviembre 2015 y enero 2016 corresponde a la variación del IPC de Ciudad de Buenos Aires. Entre febrero y abril de 2016 corresponde a variación del IPC de San Luis.',
    ),
    Variable(
        id=28,
        name='inflacion_interanual',
        doc='Variación interanual del índice de precios al consumidor informado por INDEC. En el período comprendido entre noviembre 2015 y abril 2016 se incluyen los valores implícitos en el cálculo del Coeficiente de Estabilización de Referencia. Entre noviembre 2015 y enero 2016 se considera el IPC de Ciudad de Buenos Aires. Entre febrero y abril de 2016 corresponde a variación del IPC de San Luis.',
    ),
    Variable(
        id=29,
        name='rem_expectativas_mercado',
        doc='Datos del Relevamiento de Expectativas de Mercado del Banco Central de la República Argentina (BCRA) que recopila los pronósticos macroeconómicos de corto y mediano plazo realizados por analistas especializados',
    ),
    Variable(
        id=30,
        name='cer',
        doc='El CER es un índice base 02/02/2002=1. Se construye en base a la tasa media geométrica calculada sobre la variación del Índice de Precios al Consumidor (IPC). Los detalles metodológicos se pueden consultar en el siguiente vínculo: https://www.bcra.gob.ar/archivos//Pdfs/PublicacionesEstadisticas/tasmet.pdf',
    ),
    Variable(
        id=31,
        name='uva',
        doc='El valor inicial de la UVA al 31/03/2016 representa el costo de la construcción de un milésimo de metro cuadrado de la vivienda a esa fecha. Su valor se actualiza según la variación del Coeficiente de Estabilización de Referencia. Los detalles metodológicos se pueden consultar en el siguiente vínculo: https://www.bcra.gob.ar/archivos//Pdfs/PublicacionesEstadisticas/tasmet.pdf',
    ),
    Variable(
        id=32,
        name='uvi',
        doc='El valor inicial en pesos de una UVI es una medida que equivale a la milésima parte del costo de la construcción de un metro cuadrado de vivienda. El mismo se ajusta por la evolución del índice de Costo de la Construcción (CAICC). Los detalles metodológicos se pueden consultar en el siguiente vínculo: https://www.bcra.gob.ar/archivos//Pdfs/PublicacionesEstadisticas/tasmet.pdf',
    ),
    Variable(
        id=40,
        name='icl_contratos_locacion',
        doc='Indicador diario que elabora el BCRA en base a la variación mensual del Índice de Precios al Consumidor (IPC) publicado por el Instituto de Estadísticas y Censos (INDEC) y de la Remuneración Imponible Promedio de los Trabajadores Estables (RIPTE), publicada por la Secretaría de Seguridad Social. Los detalles metodológicos se pueden consultar en el siguiente vínculo: https://www.bcra.gob.ar/archivos//Pdfs/PublicacionesEstadisticas/tasmet.pdf',
    ),
    # Factores de explicación de la base monetaria
    Variable(
        id=46,
        name='efecto_monetario_total',
        doc='Corresponde a la suma de los efectos monetarios correspondientes a compras netas de divisas al sector privado y otros , compras netas de divisas al tesoro nacional, e los adelantos transitorios al tesoro nacional , adelantos transitorios al tesoro nacional, transferencia de utilidades al tesoro nacional, del resto de operaciones con el tesoro nacional, de las operaciones de pases , de las LELIQ y NOTALQ, de los redescuentos y adelantos, de los intereses, primas y remuneración de cuentas corrientes asociados a op. de pases, LELIQ, NOTALQ, redescuentos y adelantos, de las operaciones con letras fiscales de liquidez y de otros operaciones.',
    ),
    Variable(
        id=47,
        name='efecto_monetario_compra_divisas_sector_privado',
        doc='Efecto monetario de las compras y ventas de divisas del BCRA en el mercado de cambios, con excepción de las realizadas directamente al Tesoro Nacional.',
    ),
    Variable(
        id=48,
        name='efecto_monetario_compra_divisas_tesoro',
        doc='Efecto monetario de las compras y ventas de divisas del BCRA al Tesoro Nacional.',
    ),
    Variable(
        id=49,
        name='efecto_monetario_adelantos_transitorios',
        doc='Variación del stock de adelantos transitorios otorgados por el BCRA al Gobierno Nacional según lo contemplado en el artículo 20 de la Carta Orgánica del BCRA',
    ),
    Variable(
        id=50,
        name='efecto_monetario_transferencia_utilidades',
        doc='Transferencia de utilidades que realiza el BCRA al Gobierno Nacional en el marco de lo dispuesto en el artículo 38 de la Carta Orgánica del BCRA.',
    ),
    Variable(
        id=52,
        name='efecto_monetario_pases',
        doc='Efecto monetario de las operaciones de pases que realizó el BCRA hasta el 14 de julio de 2025. Se muestra con signo negativo el efecto contractivo por el aumento del saldo de pases pasivos para el BCRA y la caída del saldo de pases activos para esta institución.',
    ),
    Variable(
        id=53,
        name='efecto_monetario_liquidez_leliq_notaliq',
        doc='Incluye el efecto monetario asociado a las operaciones con Letras de Liquidez5 y Notas de Liquidez a tasa variable6 (NOTALIQ) del BCRA. Se muestra con signo negativo la contracción asociada al aumento del saldo de LELIQ y/o NOTALIQ y con signo positivo la disminución de los stocks de estos títulos. Excluye la expansión vinculada al pago de intereses.',
    ),
    Variable(
        id=54,
        name='efecto_monetario_redescuentos_adelantos',
        doc='Financiamiento otorgado por el BCRA a entidades financieras mediante redescuentos o adelantos.',
    ),
    # Pasivos y stocks del BCRA
    Variable(
        id=152,
        name='stock_pases_bcra',
        doc='Stock de pases concertados por el BCRA hasta el 14 de julio de 2025.',
    ),
    Variable(
        id=155,
        name='stock_lebac_nobac',
        doc='Saldo total en circulación. No incluye las emitidas como contrapartida de operaciones de pases con el BCRA. A partir de noviembre de 2018 se dejaron de emitir LEBAC y NOBAC',
    ),
    Variable(
        id=158,
        name='stock_titulos_en_dolares_bopreal',
        doc='Stock de títulos denominados en dólares emitidos por el BCRA. A partir del 05/01/2024 se incluye el stock de BOPREAL, expresado en valor nominal residual. No se incluyen los BOPREAL emitidos como garantía de los pases acordados con bancos internacionales en 2025.',
    ),
    Variable(
        id=196,
        name='stock_lefi_entidades_financieras',
        doc='Saldo de Letras Fiscales de Liquidez en cartera de entidades financieras expresadas en valor técnico, en línea con la Com. A 8060 y Res. Conjunta secretaria de Hacienda y secretaria de finanzas 40/24.',
    ),
    Variable(
        id=198,
        name='otros_pasivos_bcra',
        doc='Otros pasivos del BCRA',
    ),
)

BY_ID: dict[int, Variable] = {v.id: v for v in VARIABLES}
BY_NAME: dict[str, Variable] = {v.name: v for v in VARIABLES}
