def N120():
    print("\n120 Números numa matriz 10x12 \n")
    EMPTY = "-"
    Numeros = []
    for i in range(10):
        row = [EMPTY for i in range(12)]
        Numeros.append(row)

    for i in range(10):
        print("Digite os valores da linha: ")
        for j in range(12):
            Numeros[i][j] = int(input("Digite o valor da coluna: "))
    for i in range(10):
        for j in range(12):
            print (Numeros[i][j])


def N25():
    print("\n25 Números numa matriz 5x5 \n")
    EMPTY = "-"
    Numeros = []
    for i in range(5):
        row = [EMPTY for i in range(5)]
        Numeros.append(row)

    for i in range(5):
        print("Digite os valores da linha: ")
        for j in range(5):
            Numeros[i][j] = int(input("Digite o valor da coluna: "))
    for i in range(5):
        for j in range(5):
            print (Numeros[i][j])
            
def M2():
    print("\n2 Matrizes 5x5 \n")
    EMPTY = "-"
    Numeros = []
    for i in range(5):
        row = [EMPTY for i in range(5)]
        Numeros.append(row)

    print("Primeira Matriz")
    for i in range(5):
        print("Digite os valores da linha: ")
        for j in range(5):
            Numeros[i][j] = int(input("Digite o valor da coluna: "))

    Numeros2 = []
    for i in range(5):
        row = [EMPTY for i in range(5)]
        Numeros2.append(row)

    print("Segunda Matriz")
    for i in range(5):
        print("Digite os valores da linha: ")
        for j in range(5):
            Numeros2[i][j] = int(input("Digite o valor da coluna: "))

    for i in range(5):
        for j in range(5):
            print (Numeros[i][j])
            print (Numeros2[i][j])


def MAl():
    print("\nMatrizes e Vetores de média de alunos \n")
    EMPTY = "-"
    Nome = []
    for i in range(9):
        row = [EMPTY for i in range(4)]
        Nome.append(row)

    Notas = []
    for i in range(4):
        row = [EMPTY for i in range(4)]
        Notas.append(row)

    Media = []
    for i in range(4):
        row = [EMPTY for i in range(4)]
        Media.append(row)

    for i in range(4):
        Nome[i] = input("Digite o nome do aluno: ")
        soma=0
        for j in range(4):
            Notas[i][j] = int(input("Digite a nota do Bimestre: "))
            soma = soma  + Notas[i][j]

            
            
        for l in range(1):
            Media[l]= soma/4
            print("A media do aluno é: ",Nome[i], Media[l])


        

    
    
    
