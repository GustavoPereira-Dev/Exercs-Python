def ProjBibioAdv():
    prof = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
    area = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
    senha = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
    cod = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    devo = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    livro = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    aux=0
    a=0
    Adv=0
    Est=0
    Sec=0
    acessos=0
    falhas=0
    tam=1
    MediaPorcAcessos= 0.0
    MediaPorcAdv = 0.0
    MediaPorcEst = 0.0
    MediaPorcSec = 0.0
    MediaPorcFalhas = 0.0
    i=0
    k=0
    j=0
    quant=0
         
    for i in range (0, 20, 1):
        acessos+=1
        print("Escreva sua categoria:")
        print("1-Advogado")
        print("2-Estagiario")
        print("3-Secretaria")
        prof[i] = int(input())


        match prof[i]:
            case 1:
                Adv+=1
                cod[i] = int(input("Digite a matricula: "))
                area[i] = input("Que area atua: ")
    
            case 2:
                Est+=1
                cod[i] = int(input("\nInforme a Matricula: "))

            case 3:
                Sec+=1
                senha[i] = int(input("Digite a senha: "))
                if senha[i]==832:
                    print ("Acesso aceito")
                    devo[i] = int(input(" Qual livro deseja devolver: "))   
                else:
                    print("Acesso negado \n")
                    falhas+=1
   

   
            case _:
              print("Algo esta errado na digitacao, tente novamente ")
              falhas+=1
 


    



        if prof[i]==1 or prof[i]==2:
            livro[i] = int(input("Escreva o codigo do livro: "))
            for k in range(0 + a, acessos+2, 1):
                aux=0
                for j in range (k - 1 + a , acessos+2, 1):
                    if livro[k] == livro[j] and livro[k]>0 and livro[j]>0:
                        aux+=1
                if aux==3:
                    print ("A quantidade de copias emprestadas desse livro ja passou do suficiente!" )
                    aux+=1
                    a = a + 2
                    falhas+=1
        
        print(tam) 
        cont = int(input("Deseja continuar com o codigo? digite 1 para sim e 2 para nao "))
        print(cont)
        if cont!=1:
            break
            


        




    while True:
        imprimir = int(input("Digite se quer imprimir os resultados do dia na tela (1 para sim 0 para nao) \n"))
        match imprimir:
            case 0:
                print("Finalizando o programa... ")
            case 1:
                for i in range(0, acessos, 1):
                    match prof[i]:
                        case 1:
                            if livro[i]!=0:
                                print (i+1,"o adicao: Advogado do código", cod[i]," e da area ", area[i]," coletou o livro ", livro[i])
                            else:
                                print (i+1,"o adicao: Advogado do código", cod[i]," e da area ", area[i]," coletou o livro indisponível ", livro[i])
                        case 2:
                            if livro[i]!=0:
                                print (i+1,"o adicao: Estagiário do código", cod[i]," coletou o livro ", livro[i])
                            else:
                                print (i+1,"o adicao: Estagiário do código", cod[i]," coletou o livro indidisponível ", livro[i]);
                        case 3:
                            if devo[i]!=0:
                                print (i+1,"o adicao: Secretária devolveu o livro ", devo[i])
                            else:
                                print (i+1,"o adicao: Houve uma tentativa de acessar a area da Secretaria falhada, veja se foi algum erro de alguma secretaria ou \n alguem de má fé tentando burlar algo \n")


        if imprimir==1:
            if Adv>0:
                MediaPorcAdv = ( Adv/acessos ) *100
            if Est>0:
                MediaPorcEst = (    Est/ acessos ) *100
            if Sec>0:
                MediaPorcSec = ( Sec/ acessos ) *100
            if falhas>0 and acessos>0:
                MediaPorcFalhas =  (falhas/acessos) *100
            MediaPorcAcessos =   100  - MediaPorcFalhas
            print ("Valor de acessos: \n Advogados" , Adv,"( ", MediaPorcAdv,"%) \nEstagiarios ", Est,"( ",MediaPorcEst,"%) \nSecretarias ",Sec, "( ",MediaPorcSec,"%) \ne geral ",acessos )
            print ("Valor de acesso bem-sucedidos: ", acessos-falhas,"( ", MediaPorcAcessos,"%)")
            print ("Valor de acessos mal-sucedidos: ",falhas,"( ", MediaPorcFalhas,"%)" )
            imprimir= int(input("Deseja finalizar o programa? 0 para sim \n"))
            if imprimir==0:
                print("Finalizando... \n")

        if imprimir==0:
            break
 

   





