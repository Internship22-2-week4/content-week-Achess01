def contrasenaValida(contrasena):
    return contrasena == '2Fj(jjbFsuj' or contrasena == 'eoZiugBf&g9'


if __name__ == '__main__':
    print(contrasenaValida("2Fj(jjbFsuj"))  # true
    print(contrasenaValida("eoZiugBf&g9")) # true
    print(contrasenaValida("hola")) # false
    print(contrasenaValida(""))