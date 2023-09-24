
def main():

    #Entrada de dados.
    print("Digite três nûmeros.")
    x = int(input(""))
    y = int(input(""))
    z = int(input(""))

    #Condicionais ordenando os números em ordem
    #crescente.
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    else:
        print("Digite um número válido.") 
    
    #Exibe os números na tela.
    print(x)
    print(y)
    print(z)

if __name__ == '__main__':
    main()
