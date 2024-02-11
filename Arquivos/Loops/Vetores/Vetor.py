def El10():
    print("\n Vetor com 10 números \n")
    Vetor = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,10,1):
        Vetor[i] = int(input("Digite o valor do Elemento: "))

    for i in range(0,10,1):
        print("O valor do ",i+1,"o Elemento é: ",Vetor[i])


def E110PI():
    print("\n Vetores A e B com 10 números com algorítmo ímpar/par \n")
    par=0
    impar=0
    ElementoA = [0,0,0,0,0,0,0,0,0,0]
    ElementoB = [0,0,0,0,0,0,0,0,0,0]

    for i in range(0,10,1):
        ElementoA[i] = int(input("Digite o valor do Elemento A: "))
        if ElementoA[i]==0:
            par+=1
        else:
            impar+=1

    for i in range(0,10,1):
        ElementoB[i] = int(input("Digite o valor do Elemento B: "))
        if ElementoB[i]%2==0:
            par+=1
        else:
            impar+=1

    print("O valor de quantidade de pares é: ",par)
    print("O valor de quantidade de ímpares é: ",impar)
    
    
def El10AB():
    print("\n Vetores A e B com 10 números com algorítmo ímpar/par calculador \n")
    ElementoA = [0,0,0,0,0,0,0,0,0,0]
    ElementoB = [0,0,0,0,0,0,0,0,0,0]
    i=0
    for i in range (0,10,1):
        ElementoA[i] = int(input("Digite o valor do Elemento: "))
        if i%2 == 0:
            ElementoB[i] = ElementoA[i]*5
        else:
            ElementoB[i] = ElementoA[i]+5

    for i in range (0,10,1):
        print("O valor do seguinte elemento A é: ", ElementoA[i])
        print("O valor do seguinte elemento B é: ", ElementoB[i])


def MAV():
    print("\n Vetor com a média da Sala com 4 alunos \n")
    soma=0
    media=0
    md= [0,0,0,0,0]
    for i in range (0,5,1):
        md[i] = float(input("Digite a média do Aluno: "))
        soma = soma + md[i]

    media = soma/5
    print ("A média da turma é: ", media)
    print ("A média do aluno 2 é: ", md[1])


  
