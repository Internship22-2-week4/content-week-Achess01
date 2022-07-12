def likes(cantidad):
    if cantidad < 1000:
        return str(cantidad)
    elif cantidad < 1000000:
        numero = cantidad // 1000
        return str(f'{numero}K')
    else:
        numero = cantidad // 1000000
        return str(f'{numero}M')
    


if __name__ == '__main__':
    # código de prueba
    print(likes(983))  # "983"
    print(likes(1900))  # "1K"
    print(likes(54000))  # "54K"
    print(likes(120800))  # "120K"
    print(likes(25222444))  # "25M"
