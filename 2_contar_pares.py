#A Função retorna a quantidade de dígitos pares
#no número digitado.
def num_pares(x):
    return len([ y for y in str(x) if int(y) % 2 == 0])

    
def main():

    #Digita um número.
    x = int(input("Digite um número: "))

    #Exibe a quantidade de números pares.
    print(f'Este número possui {num_pares(x)} dígito(s) par(es).')

if __name__ == '__main__':
    main()
    
