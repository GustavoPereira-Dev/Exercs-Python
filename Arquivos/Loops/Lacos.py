from math import pow
def Pdejat15():
    print("\nCalculador de um expoente específico até a sua 15º potência \n")
    par=0
    while True:
        try:
            Exp = float(input("Digite a potência desejada: "))
        except ValueError:
            print("Só é aceitado valores inteiros e floats!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            par=1
            N=0
            while N<15:
                R = pow (Exp,N)
                print(Exp,"^",N,"= ",R)
                N=N+1
        if par!=0:
            break


def TabDej():
    print("\nCalculador de uma tabuada específica até sua multiplicação 10 \n")
    par=0
    while True:
        try:
            N2 = float(input("Digite a tabuada desejada: "))
        except ValueError:
            print("Só é aceitado valores inteiros e floats!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            par=0
            for i in range(1,11,1):
                R= i*N2
                print(N2,"X ",i,"= ",R)
        if par!=0:
            break

def Nimpatx():
    print("\nCalculador de Números ímpares até uma quantidade específica \n")
    par=0
    while True:
        try:
            NI = int(input("Digite o número inicial: "))
            NF = int(input("Digite o número final: "))
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            par=1    

            for i in range(NI,NF,1):
                if (i%2):
                    print(i)
        if par!=0:
            break



def AltFemEMasc():
    print("\n Algorítmo Calculador da Altura Masculina e Feminina \n")
    maior=0
    menor=0
    menor2=0
    maior2=0
    soma=0
    i=0
    mulheres=0
    homens=0
    media=0
    MediaPorc=0
    MediaPorc2=0
    while True:
        Sexo = input("Digite seu sexo F/M: ")
        if Sexo+'' == 'F' or Sexo+'' == 'f':
            altura= float(input("Digite sua altura: "))
            menor = altura
            soma = soma+altura
            i+=1
            mulheres+=1
            if altura>maior:
                maior = altura
        elif Sexo+'' == 'F' or Sexo+'' == 'f':
            if altura<menor:
                menor = altura
        elif Sexo+'' == 'M' or Sexo+'' == 'm':
            altura2= float(input("Digite sua altura: "))
            menor2=altura2
            i+=1
            homens+=1
            if altura2 > maior2:
                maior2 = altura2
        elif Sexo+'' == 'M' or Sexo+'' == 'm':
            if altura2 < menor2:
                menor2 = altura2
        else:
            print("ALGO ESTA INCORRETO, DIGITE F OU M NA HORA DA ESCOLHA DE SEXO")

        Cont = input("Deseja continuar? S ou N: ")
        if Cont+'' == 'N' or Cont+'' == 'n':
            break

    if homens>=1:
        MediaPorc = (homens /  i) *100
    if mulheres>=1:
        MediaPorc2 = ( mulheres/  i) *100
    if mulheres>=1:
        media = soma/mulheres
    print("A quantidade de homens e mulheres participantes são respectivamente: ",homens," e ",mulheres,"(total ",i,")")
    print ("A maior e menor altura masculina respectivamente é: ", maior2," e ", menor2)
    print ("A maior e menor altura feminina respectivamente é: ", maior," e ",menor)
    print ("A media feminina é: ", media);
    print ("A media de porcentagem masculina é: ", MediaPorc)
    print ("A media de porcentagem feminina é: ", MediaPorc2)
    if MediaPorc < MediaPorc2:
        DifPorc = ( MediaPorc2 -  MediaPorc )
        print ("A diferenca percentual e de: ", DifPorc)
    elif MediaPorc2 < MediaPorc:
        DifPorc = ( MediaPorc -  MediaPorc2  )
        print ("A diferenca percentual e de: ", DifPorc)
    else:
        print ("Nao existe nenhuma diferença percentual entre os dois! ")





	

	
        
  

