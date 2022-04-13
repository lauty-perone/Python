texto = """The constants defined in this module are:The constants defined in␣
,→this module are:
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants␣
,→described below. This value is not locale-dependent.
string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not␣
,→locale-dependent and will not change.
string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not␣
,→locale-dependent and will not change.
"""

texto_sin_repetir = set(texto.lower().split())

letra = input('Ingrese una letra: ')
if letra.isalpha():
    for dato in texto_sin_repetir:
        if (dato[0].startswith(letra)):
            print(dato)
else:
    print ('Ver: módulo string')
