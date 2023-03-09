BRANCHES = {
    1 : {
        1: 'SPO',
        2: 'REC',
        3: 'SSA',
        4: 'FOR',
        5: 'MCZ',
        6: 'NAT',
        7: 'JPA',
        8: 'AJU',
        9: 'VDC',
        10: 'CTG',
        11: 'GVR',
        12: 'VIX',
        13: 'TCO',
        14: 'UDI',
    },
    2: {
        1: 'CTG',
        2: 'TCO',
        3: 'UDI',
        4: 'TMA',
        5: 'VIX',
        6: 'GVR'
    },
    3: {
        1: 'BMA',
        2: 'BPE',
        3: 'BEL',
        4: 'BPB',
        5: 'SLZ',
        6: 'BAL',
        7: 'THE',
        8: 'BMG',
    },
    4: {
        1: 'FMA',
    },
}

STATUS_CHOICES = [
    ('ABERTO', 'ABERTO'),
    ('ANDAMENTO', 'ANDAMENTO'),
    ('CONCLUIDO', 'CONCLUIDO'),
    ('CANCELADO', 'CANCELADO')
]

DEPARTMENT_CHOICES = [
    ('DIRETORIA', 'DIRETORIA'),
    ('FATURAMENTO', 'FATURAMENTO'),
    ('FINANCEIRO', 'FINANCEIRO'),
    ('RH', 'RH'),
    ('FISCAL', 'FISCAL'),
    ('MONITORAMENTO', 'MONITORAMENTO'),
    ('OPERACIONAL', 'OPERACIONAL'),
    ('FROTA', 'FROTA'),
    ('EXPEDICAO', 'EXPEDICAO'),
    ('COMERCIAL', 'COMERCIAL'),
    ('JURIDICO', 'JURIDICO'),
    ('DESENVOLVIMENTO', 'DESENVOLVIMENTO'),
    ('TI', 'TI'),
    ('FILIAIS', 'FILIAIS'),
    ('COMPRAS', 'COMPRAS')
]

PAYMENT_METHOD_CHOICES = [
    ('A_VISTA', 'A VISTA'),
    ('PARCELADO-1X', 'PARCELADO 1X'),
    ('PARCELADO-2X', 'PARCELADO 2X'),
    ('PARCELADO-3X', 'PARCELADO 3X'),
    ('PARCELADO-4X', 'PARCELADO 4X'),
    ('PARCELADO-5X', 'PARCELADO 5X'),
    ('PARCELADO-6X', 'PARCELADO 6X'),
    ('PARCELADO-7X', 'PARCELADO 7X'),
    ('PARCELADO-8X', 'PARCELADO 8X'),
    ('PARCELADO-9X', 'PARCELADO 9X'),
    ('PARCELADO-10X', 'PARCELADO 10X'),
    ('PARCELADO-11X', 'PARCELADO 11X'),
]