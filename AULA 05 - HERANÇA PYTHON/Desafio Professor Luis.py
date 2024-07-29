usuario = input("Informe seu nome de usuário: ")
senha = input("Informe sua senham, lembrando que a senha deve conter no minimo 1 letra maiuscula, 1 letra minuscula e um numero : ")

if any(letraa.isupper() for letraa in senha) and any(letra.islower() for letra in senha) and any(letras.isdigit() for letras in senha):
    print("Senha forte")

else:
    print("Senha Fraca, por favor digite novamente!")
    while True:
        senha = input("Informe sua senham, lembrando que a senha deve conter no minimo 1 letra maiuscula, 1 letra minuscula e um numero : ")
        if any(letraa.isupper() for letraa in senha) and any(letra.islower() for letra in senha) and any(letras.isdigit() for letras in senha):
            print("Senha forte")
            break