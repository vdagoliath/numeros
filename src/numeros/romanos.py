tupla_matriz = (
    ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
    ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
    ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
    ('', 'M', 'MM', 'MMM', '', '', '', '', '', ''),
)


def dec2romano(numero_decimal):
    if numero_decimal == 0:
        return '0'

    if numero_decimal > 3000:
        return ''

    romano = tupla_matriz[3][numero_decimal // 1000] + \
             tupla_matriz[2][numero_decimal // 100 % 10] + \
             tupla_matriz[1][numero_decimal % 100 // 10] + \
             tupla_matriz[0][numero_decimal % 10]
    return romano
