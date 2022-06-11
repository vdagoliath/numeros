_MIL = 'mil'

tupla_unidades = (
    {
        'comun': 'cero'
    },
    {
        'comun': 'uno',
        'apocopado': 'un',
        'genero': {
            'femenino': 'una',
            'masculino': 'uno',
        },
    },
    {
        'comun': 'dos'
    },
    {
        'comun': 'tres'
    },
    {
        'comun': 'cuatro'
    },
    {
        'comun': 'cinco'
    },
    {
        'comun': 'seis'
    },
    {
        'comun': 'siete'
    },
    {
        'comun': 'ocho'
    },
    {
        'comun': 'nueve'
    },

)

tupla_decenas = (
    {
        'comun': ''
    },
    {
        'comun': 'diez',
        'especiales': ('', 'once', 'doce', 'trece', 'catorce', 'quince',
                       'dieciseis', 'diecisiete', 'dieciocho', 'diecinueve'),
    },
    {
        'comun': 'veinte',
        'prefijo': 'veinti'
    },
    {
        'comun': 'treinta'
    },
    {
        'comun': 'cuarenta'
    },
    {
        'comun': 'cincuenta'
    },
    {
        'comun': 'sesenta'
    },
    {
        'comun': 'setenta'
    },
    {
        'comun': 'ochenta'
    },
    {
        'comun': 'noventa'
    },

)

tupla_centenas = (
    {
        'comun': ''
    },
    {
        'comun': 'cien',
        'prefijo': 'ciento'
    },
    {
        'comun': 'doscientos',
    },
    {
        'comun': 'trescientos',
    },
    {
        'comun': 'cuatrocientos'
    },
    {
        'comun': 'quinientos'
    },
    {
        'comun': 'seiscientos'
    },
    {
        'comun': 'setecientos'
    },
    {
        'comun': 'ochocientos'
    },
    {
        'comun': 'novecientos'
    },

)

apellidos = [
    {
        'singular': 'cuatrillón',
        'plural': 'cuatrillones'
    },
    _MIL,
    {
        'singular': 'trillón',
        'plural': 'trillones'
    },
    _MIL,
    {
        'singular': 'billón',
        'plural': 'billones'
    },
    _MIL,
    {
        'singular': 'millón',
        'plural': 'millones'
    },
    _MIL,
    '']


def lee3dig(numero, contexto_final=True, usar_apocopado=False):
    if 0 <= numero < 1000:
        unidad = numero % 10
        decena = numero // 10 % 10
        centena = numero // 100
        ultima_union_anulada = False

        if numero == 0:
            return ''

        if unidad == decena == 0:
            return tupla_centenas[centena].get('comun')

        lista = []
        lista.append(tupla_centenas[centena].get('prefijo') if tupla_centenas[centena].get('prefijo') else
                     tupla_centenas[centena].get('comun'))

        if unidad == 0:
            lista.append(tupla_decenas[decena].get('comun'))
            return ' '.join(lista) if str(lista[0]).__len__() > 1 else lista[lista.__len__() - 1]

        if tupla_decenas[decena].get('especiales'):
            lista.append(tupla_decenas[decena].get('especiales')[unidad])
            return ' '.join(lista) if str(lista[0]).__len__() > 1 else lista[lista.__len__() - 1]

        if tupla_decenas[decena].get('prefijo'):
            lista.append(tupla_decenas[decena].get('prefijo') + tupla_unidades[unidad].get(
                'apocopado' if usar_apocopado and tupla_unidades[unidad].get('apocopado') else 'comun'))
            ultima_union_anulada = True
        else:
            lista.append(tupla_decenas[decena].get('comun'))
            lista.append(tupla_unidades[unidad].get(
                'apocopado' if usar_apocopado and tupla_unidades[unidad].get('apocopado') else 'comun'))
        ultima_union = ' ' if not contexto_final or ultima_union_anulada else ' y '
        lista_decena = [' '.join(lista[:-1]), lista[lista.__len__() - 1]]
        lectura = ultima_union.join(lista_decena) if ''.join(lista[1]).__len__() > 1 else ''.join(lista_decena)
        lectura = lectura.lstrip()
        return lectura
    else:
        return False


def _es_ape1_mayor_ape2(ape1, ape2):
    idx1 = -1 if ape1 == _MIL else 0
    idx2 = -1 if ape2 == _MIL else 0
    if idx1 + idx2 == -1:
        return idx1 > idx2
    for idx, ape in enumerate(apellidos):
        idx1 = idx if isinstance(ape, dict) and (ape.get('singular') == ape1 or ape.get('plural') == ape1) else idx1
        idx2 = idx if isinstance(ape, dict) and (ape.get('singular') == ape2 or ape.get('plural') == ape2) else idx2
    return idx1 < idx2


def num2letras(numero, separador_miles=',', separador_decimales='.'):
    numero_str = numero
    if isinstance(numero, int) or isinstance(numero, float):
        numero_str = str(numero)
        if numero < 0:
            raise 'El número especificado debe ser mayor o igual que 0'
    numero_str_sin_separador_miles = str.join('', numero_str.split(separador_miles))
    numero_str_sin_separador_miles_splitted = numero_str_sin_separador_miles.split(separador_decimales)
    numero_entero = numero_str_sin_separador_miles_splitted[0]
    if int(numero_entero) < 0:
        raise 'El número especificado debe ser mayor o igual que 0'
    numero_decimal = numero_str_sin_separador_miles_splitted[1] \
        if numero_str_sin_separador_miles_splitted.__len__() > 1 else '0'
    numero_grupos_de_tres = []
    pila = []
    for idx in range(1, numero_entero.__len__() + 1):
        if pila.__len__() == 3:
            numero_grupos_de_tres.insert(0, ''.join(pila))
            pila.clear()
        pila.insert(0, numero_entero[-idx])
    if pila.__len__() > 0:
        numero_grupos_de_tres.insert(0, ''.join(pila))

    indice = numero_entero.__len__() // 3
    indice += 1 if numero_entero.__len__() % 3 > 0 else 0
    lectura = ''
    seccion_apellidos = apellidos[-indice:]
    ultima_apellido_leido = ''
    for idx, apellido in enumerate(seccion_apellidos):
        ape = apellido
        if isinstance(ape, dict):
            ape = ape.get('singular') if int(numero_grupos_de_tres[idx]) == 1 else ape.get('plural')
        n3 = int(numero_grupos_de_tres[idx])
        if n3 == 1:
            leido = lee3dig(n3,
                            usar_apocopado=(idx < seccion_apellidos.__len__() - 1 and n3 == 1)) if ape != _MIL else ''
            cond = ape.__len__() > 0
            lectura += leido + ' ' + ape if cond else leido
            ultima_apellido_leido = ape if cond else ultima_apellido_leido
            lectura += ' '
        if n3 > 1:
            lectura += lee3dig(n3, usar_apocopado=ape.__len__() > 0)
            lectura += ' ' + ape + ' '
            ultima_apellido_leido = ape
        if n3 == 0:
            cond = ape.__len__() > 0 and \
                   idx < seccion_apellidos.__len__() - 1 and \
                   _es_ape1_mayor_ape2(ape, ultima_apellido_leido)
            lectura += ' ' + ape + ' ' if cond else ''
            ultima_apellido_leido = ape if cond else ultima_apellido_leido

    lectura = lectura.strip()
    lectura_splitted = lectura.split(' ')
    nueva_lectura_splitted = []
    for split in lectura_splitted:
        if split.__len__() > 0:
            nueva_lectura_splitted.append(split.strip())
    lectura = str.join(' ', nueva_lectura_splitted)

    lectura_decimal = numero_decimal + '0' if numero_decimal.__len__() == 1 else numero_decimal
    lectura_decimal += '/1' + ''.zfill(lectura_decimal.__len__())
    return lectura + ' ' + lectura_decimal
