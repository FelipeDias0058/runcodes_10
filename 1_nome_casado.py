#A função lê o nome e estado civil da pessoa(e do cônjuge,
#se aplicável), e exibe quantos caracteres estão no nome
def f_nome_char(nome, est_civil):
    if '1' in est_civil:
        conjuge = input("Digite o nome de seu cônjuge: ").strip()
        print(f'{len(nome) + len(conjuge)} caracteres.')
    elif '2' in est_civil:
        print(f'{len(nome)} caracteres.')


def main():
    #Entrada de nome e estado civil
    nome = input("Digite seu nome: ").strip()
    print("Digite '1' se for casado, '2' se for solteiro.")
    est_civil = input("Digite seu estado civil: ").strip()
    
    #Chama a função 'f_nome_char'
    f_nome_char(nome, est_civil)


if __name__ == '__main__':
    main()
