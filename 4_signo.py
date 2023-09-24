#A função determina o signo astrológico de acordo com
#os parâmetros.
def f_signo(d, m):
    if (22 <= d <= 31 and m == 12) or (1 <= d <= 19 and m == 1):
        return "Capricórnio"
    elif (20 <= d <= 31 and m == 1) or (1 <= d <= 18 and m == 2):
        return "Aquário"
    elif (19 <= d <= 29 and m == 2) or (1 <= d <= 20 and m == 3):
        return "Peixes"
    elif (21 <= d <= 31 and m == 3) or (1 <= d <= 19 and m == 4):
        return "Áries"
    elif (20 <= d <= 30 and m == 4) or (1 <= d <= 20 and m == 5):
        return "Touro"
    elif (21 <= d <= 31 and m == 5) or (1 <= d <= 21 and m == 6):
        return "Gêmeos"
    elif (22 <= d <= 30 and m == 6) or (1 <= d <= 22 and m == 7):
        return "Câncer"
    elif (23 <= d <= 31 and m == 7) or (1 <= d <= 22 and m == 8):
        return "Leão"
    elif (23 <= d <= 31 and m == 8) or (1 <= d <= 22 and m == 9):
        return "Virgem"
    elif (23 <= d <= 30 and m == 9) or (1 <= d <= 22 and m == 10):
        return "Libra"
    elif (23 <= d <= 31 and m == 10) or (1 <= d <= 21 and m == 11):
        return "Escorpião"
    elif (22 <= d <= 31 and m == 11) or (1 <= d <= 21 and m == 12):
        return "Sagitário"
    else:
        return "Digite um Dia e Mês."


def main():
    #Digita dia e mês de nascimento.
    d = int(input("Digite seu dia de nascimento: "))
    m = int(input("Digite seu mês de nascimento: "))

    #Exibe na tela qual o signo do usuário.
    print(f'Seu signo é {f_signo(d, m)}.')


if __name__ == '__main__':
    main()

 
