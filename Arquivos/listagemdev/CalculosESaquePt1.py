def MA():
    class MediaError(ValueError):
        pass
    par=0
    while True:
        try:
            print("\nCalculador da Média Aritmética \n")
            N1 = int(input("Digite o valor da 1º Nota: "))
            if N1<0 or N1>10:
                raise MediaError
            N2 = int(input("Digite o valor da 2º Nota: "))
            if N2<0 or N2>10:
                raise MediaError
            N3 = int(input("Digite o valor da 3º Nota: "))
            if N3<0 or N3>10:
                raise MediaError
            N4 = int(input("Digite o valor da 4º Nota: "))
            if N4<0 or N4>10:
                raise MediaError
            par=1
            Media = (N1 + N2 + N3 + N4)/4;
            print("O valor da media eh:", Media)
        except MediaError:
            print("Ops! Parece que houve algum erro, veja se houve uma digitacao menor que 0 ou \n maior que 10 na nota")
        except ValueError:
            print("Só é aceitado valores inteiros e flutuantes!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break


def Soma():
    par=0
    print("\nCalculador da Soma de dois números \n")
    while True:
        try:
            N1 = int(input("Digite o valor do primeiro número: "))
            N2 = int(input("Digite o valor do segundo número: "))
            par=1
            Soma = N1 + N2
            print("O valor da soma eh:", Soma)
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break

def Soma4():
    print("\nCalculador da Soma de quatro números \n")
    while True:
        try:
            N1 = int(input("Digite o valor do primeiro número: "))
            N2 = int(input("Digite o valor do segundo número: "))
            N3 = int(input("Digite o valor do terceiro número: "))
            N4 = int(input("Digite o valor do quarto número: "))
            par=1
            Soma = N1+N2+N3+N4
            print("O valor da soma dos quatro números é:", Soma)
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break
    


def MP ():
    class MediaError(ValueError):
        pass
    par=0
    print("\nCalculador da Média Ponderada \n")
    while True:
        try:
            No1 = int(input("Digite o valor da 1º nota: "))
            if No1<0 or No1>10:
                raise MediaError
            P1 = float(input("Digite o peso da 1º nota: "))
            No2 = int(input("Digite o valor da 2º nota: "))
            if No2<0 or No2>10:
                raise MediaError
            P2 = float(input("Digite o peso da 2º nota: "))
            No3 = int(input("Digite o valor da 3º nota: "))
            if No3<0 or No3>10:
                raise MediaError
            P3 = float(input("Digite o peso da 3º nota: "))
            MP = (No1 * P1 + No2 * P2 + No3 * P3) / (P1+ P2+ P3)
            par=1
            print("A Média Ponderada será:", MP)
        except MediaError:
            print("Ops! Parece que houve algum erro, veja se houve uma digitacao menor que 0 ou \n maior que 10 na nota")
        except ZeroDivisionError:
            print("Os pesos não podem conter o valor zero!")
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break
    


def LV():
    print("\nCalculador da quantidade de litros pela velocidade por hora \n")
    while True:
        try:
            Tempo = int(input("Digite o tempo pecorrido: "))
            Vel = float(input("Digite o valor da velocidade média: "))
            Dis = Tempo * Vel
            Litros = Dis /12
            print("A Distância é: ", Dis), print("\n O valor de Litro utilizado é: ", Litros)
        except ValueError:
            print("Só é aceitado valores inteiros no tempo e flutuantes & inteiro na Velocidade!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break


def CalcSal():
    print("\nCalculador de Salário \n")
    par=0
    while True:
        try:
            Salario = float(input("Digite o valor do Salário: "))
            NovoSal = (Salario * 25)/100 + Salario
            par=1
            print("O valor do novo salário será: ", NovoSal)
        except ValueError:
            print("Só é aceitado flutuantes & inteiro na Velocidade!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break

def SalNePerc():
    print("\nCalculador da Porcentagem Salarial \n")
    par=0
    while True:
        try:
            Salario = float(input("Digite o valor do Salário: "))
            PercSal = int(input("Digite o percentual salarial: "))
            NovoSal = (Salario * PercSal)/100 + Salario
            print("O valor do novo salário será: ", NovoSal)
        except ValueError:
            print("Só é aceitado valores inteiros na Porcentagem Salarial e flutuantes & inteiro no Salário!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break

def SalBase():
    print("\nCalculador de Salário Base \n")
    par=0
    while True:
        try:
            SalarioBase = float(input("Digite o valor do Salário Base: "))
            Gratificacao = (SalarioBase * 10)/100
            Imposto = (SalarioBase * 15)/100
            Salario = SalarioBase - Imposto
            par=1
            print(" O valor da Gratificação será: ", Gratificacao)
            print("\n O valor do Imposto Será: ", Imposto)
            print("\n O valor do Salário será: ", Salario)
        except ValueError:
            print("Só é aceitado valores inteiros na Porcentagem Salarial e flutuantes & inteiro no Salário!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break   


def SacarouDeposito():
    print("\nAlgorítmo do Saque ou Depósito \n")
    par=0
    while True:
        try:
            Operacao = int(input("Será feito deposito ou saque?: "))
            valor = float(input("Escreva qual valor deseja: "))
            par=1
            if Operacao==0:
                soma=valor+500
                print("Seu valor atual é: ", soma)
            else:
                soma=500-valor
                print("Seu valor atual é: ", soma)
        except ValueError:
            print("Só é aceitado valores inteiros na escolha da operação e flutuantes & inteiro no valor!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break   


