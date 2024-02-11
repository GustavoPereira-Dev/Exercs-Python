def QuAnm():
    print("\n Quiz dos Animais Akinator versão Python \n")
    acertos=0
    erros=0
    tentativas=0
    
    while True:
        Herbivoro=0
        Carnivoro=0
        Mamifero=0
        Quadrupede=0
        Terrestre=0
        Repteis=0
        Escolha=0
        tentativas+=1
        Mamifero= int(input("1o O animal eh um mamífero?: "))
        Quadrupede = int(input("2o O animal eh quadrúpede?: "))
        Carnivoro = int(input("3o O animal eh carnívoro?: "))
        Herbivoro = int(input("4o O animal eh herbívoro?: "))
        Terrestre = int(input("5o O animal eh um ser terrestre?: "))
        Repteis = int(input("6o O animal eh um réptel?: "))

	
        if Mamifero==1 and Quadrupede==1 and Carnivoro==1 and Herbivoro==0 and Terrestre==1 and Repteis==0:
            Escolha = int(input("O animal eh um leao? 1 para sim ou 2 para nao: "))
	
        elif Mamifero==1 and Quadrupede==1 and Carnivoro==0 and Herbivoro==1 and Terrestre==1 and Repteis==0:
            Escolha = int(input("O animal eh um Cavalo? 1 para sim ou 2 para nao: "))
	
        elif Mamifero==1 and Quadrupede==0 and Carnivoro==1 and Herbivoro==1 and Terrestre==1 and Repteis==0:
    	    Escolha = int(input("O animal eh um ser humano? 1 para sim ou 2 para nao: "))
	
        elif Mamifero==1 and Quadrupede==1 and Carnivoro==1 and Herbivoro==1 and Terrestre==1 and Repteis==0:
            Escolha = int(input("O animal eh um macaco? 1 para sim ou 2 para nao: "))
    
        elif Mamifero==1 and Quadrupede==1 and Carnivoro==1 and Herbivoro==1 and Terrestre==0 and Repteis==0:
            Escolha = int(input("O animal eh um morcego? 1 para sim ou 2 para nao: "))
    
        elif Mamifero==1 and Quadrupede==0 and Carnivoro==1 and Herbivoro==0 and Terrestre==0 and Repteis==0:
            Escolha = int(input("O animal eh uma baleia? 1 para sim ou 2 para nao: "))
	
        elif Mamifero==0 and Quadrupede==1 and Carnivoro==1 and Herbivoro==1 and Terrestre==1 and Repteis==0:
            Escolha = int(input("O animal eh um avestruz? 1 para sim ou 2 para nao: "))
	
        elif Mamifero==0 and Quadrupede==0 and Carnivoro==1 and Herbivoro==0 and Terrestre==1 and Repteis==0:
            Escolha = int(input("O animal eh um pinguim? 1 para sim ou 2 para nao: "))
	
        elif Mamifero==0 and Quadrupede==1 and Carnivoro==1 and Herbivoro==1 and Terrestre==0 and Repteis==0:
            Escolha = int(input("O animal eh um pato? 1 para sim ou 2 para nao: "))
	
        elif Mamifero==0 and Quadrupede==0 and Carnivoro==1 and Herbivoro==0 and Terrestre==0 and Repteis==0:
            Escolha = int(input("O animal eh uma aguia? 1 para sim ou 2 para nao: "))
	
        elif Mamifero==0 and Quadrupede==1 and Carnivoro==1 and Herbivoro==1 and Terrestre==1 and Repteis==1:
            Escolha = int(input("O animal eh uma tartaruga? 1 para sim ou 2 para nao: "))
	
        elif Mamifero==0 and Quadrupede==1 and Carnivoro==1 and Herbivoro==0 and Terrestre==1 and Repteis==1:
            Escolha = int(input("O animal eh um crocodilo? 1 para sim ou 2 para nao: "))
	
        elif Mamifero==0 and Quadrupede==0 and Carnivoro==1 and Herbivoro==0 and Terrestre==1 and Repteis==1:
            Escolha = int(input("O animal eh uma cobra? 1 para sim ou 2 para nao: "))
	
        else:
            print ("Ops! algo deu errado, tente novamente se puder \n")

        match Escolha:
            case 1:
                acertos+=1

            case 2:
                erros+=1


            case _:
                print ("Algo foi digitado errado nesse! so eh aceitado 1 ou 2 nessa questao")
                erros+=1
    

        Continuar= int(input("Deseja continuar? 1 para sim 0 para nao: "))
        if Continuar!=1:
            break
	
	
    MediaPorcAcertos = (acertos/tentativas) *100
    MediaPorcErros = ( erros/tentativas) *100
	
    if acertos>=1:
        print ("Hehehe, acertei novamente ")
        print ("Valor de tentativas: ", tentativas)
        print ("Valor de acertos: ", acertos)
        print ("Valor de erros: ", erros)
        print ("Valor percentual de acertos: ", MediaPorcAcertos)
        print ("Valor percentual de erros: ", MediaPorcErros)
	
    else:
        print ("Ops.... \n");
        print ("Valor de tentativas: ", tentativas)
        print ("Valor de acertos: ", acertos)
        print ("Valor de erros: ", erros)
        print ("Valor percentual de acertos: ", MediaPorcAcertos)
        print ("Valor percentual de erros: ", MediaPorcErros)



