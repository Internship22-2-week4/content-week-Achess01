def bmi(peso, altura):
    bmi = peso / altura**2
    if bmi < 18.5:
        return 'Bajo peso'
    elif bmi >= 18.5 and bmi <= 24.9:
        return 'Normal'
    elif bmi >= 25 and bmi <= 29.9:
        return 'Sobrepeso'
    else:
        return 'Obeso'


if __name__ == '__main__':
    # código de prueba
    print(bmi(65, 1.8))  # "Normal"
    print(bmi(72, 1.6))  # "Sobrepeso"
    print(bmi(52, 1.75))  # "Bajo de peso"
    print(bmi(135, 1.7))  # "Obeso"
