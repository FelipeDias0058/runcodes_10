    
def main():

    #Entrada e formatação de dados.
    txt = (input("Digite um número: "))
    lista = [txt[0], txt[1]]
    lista1 = [int(x) for x in lista] 
    n_par, n_impar = 0, 0

    #Cndicional determinando a quantidade
    #pares ou ímpares.
    for num in lista1:
 
        if num % 2 == 0:
            n_par += 1
 
        else:
            n_impar += 1

    #Condicionais determinando a mensagem a ser
    #exibida.
    if n_impar == 0:
        print("Nenhum dígito é ímpar.")
    if n_impar == 1:
        print("Apenas um dígito é ímpar.")
    if n_impar == 2:
        print("Os dois dígitos são ímpares.")
 

if __name__ == '__main__':
    main()
    
