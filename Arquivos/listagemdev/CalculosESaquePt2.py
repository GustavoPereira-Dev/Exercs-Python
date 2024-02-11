import math
def ComboLanche():
    print("\nAlgorítmo de Combo do Lanche \n")
    class LunchError(ValueError):
        pass
    par=0
    while True:
        try:
            Lanche = int(input("Digite a escolha: 1 para Bigmac com Refrigerante ou 2 para Bigmac sem: "))
            par=1
            if Lanche==1:
                print("Você escolheu a opção BigMac com Refrigerante; Valor: 25$")
            elif Lanche==2:
                print("Você escolheu a opção BigMac sem Refrigerante; Valor: 20$")
            else:
                par=0
                raise LunchError
        
        except LunchError:
            print("Ops! Parece que houve algum erro, veja se houve uma digitação incorreta que ultrapassou os valores pedidos ")
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break



def AlgCarro():
    print("\nCalculador do valor real do carro \n")
    par=0
    while True:
        try:
            CarroNovo = int(input("Digite o valor de preço do carro: R$ "))
            Escolha = int(input("Você tem alguma necessidade especial? 1 para sim"))
            par=1
            if Escolha==1:
                Imposto = (CarroNovo * 45)/100
                PorcDistri= (CarroNovo*28)/100
                ValorReal = CarroNovo-Imposto
                print("O valor do imposto que será cortado é: ", Imposto)
                print("O valor da Porcentagem de Distribuição é:", PorcDistri)
                print("O valor real do carro será: ", ValorReal)
            else:
                Imposto = (CarroNovo * 45)/100
                PorcDistri= (CarroNovo*28)/100
                ValorReal = CarroNovo+Imposto
                print("O valor do imposto que será cortado é: ", Imposto)
                print("O valor da Porcentagem de Distribuição é:", PorcDistri)
                print("O valor real do carro será: ",)
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break
                

                
def MacasCompradas():
    print("\nAlgorítmo das Maças compradas \n")
    par=0
    while True:
        try:
            QuantMacas = int(input("Digite a quantidade de maças: "))
            if QuantMacas >=12:
                ValorMacas = QuantMacas * 0.25
                print ("O valor será: R$ ", ValorMacas)
            else:
                ValorMacas = QuantMacas *0.30
                print ("O valor será: R$ ", ValorMacas)
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break

def Intervalo100e200():
    print("\Algorítmo do Intervalo de 100 à 200 \n")
    par=0
    while True:
        try:
            N1 = int(input("Digite o valor de um número: "))
            par=1
            if 100>=N1 and N1<=200:
                print("O valor está entre 100 e 200")
            else:
                print("O valor não está entre 100 e 200")
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break

def Incognitas3():
    print("\nAlgorítmo de intervalo entre 3 incógnitas \n")
    par=0
    while True:
        try:
            x = int(input("Digite o valor da incógnita x: "))
            y = int(input("Digite o valor da incógnita y: "))
            z = int(input("Digite o valor da incógnita z: "))
            par=0
            if x <= z and z <= y:
                print("O valor está entre o intervalo x e y")
            else:
                print("O valor não está entre x e y")
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break

def AlgIguais2():
    print("\nAlgorítmo de 2 Valores Iguais \n")
    while True:
        try:
            x = int(input("Digite o valor da incógnita x: "))
            y = int(input("Digite o valor da incógnita y: "))
            par=1
            if x == y:
                print ("Ambos os valores são iguais")
            else:
                print ("Os valores não são iguais")
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break
        
def AlgSexo():
    print("\nAlgorítmo de Sexo \n")
    par=0
    class SexError(ValueError):
        pass
    while True:
        try:
            S = input("Digite o seu Sexo")
            par=1
            if S+""=="M" or S+""=="m":
                print("Seja bem-vindo, Senhor!")
            elif S+"" =="F" or S+''=='f':
                print("Seja bem-vinda, Senhora!")
            else:
                par=0
                raise SexError
        except SexError:
            print("Só é aceito valores com uma letra, por exemplo F para feminino e M para Masculino")
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break
    

def ValorParImpar ():
    print("\nAlgorítmo do Valor Par ou Ímpar \n")
    while True:
        try:
            Num = int(input("Digite o valor de um número: "))
            if Num%2 == 0:
                print("O valor é par: ", Num)
            else:
                print("O valor é ímpar ", Num)
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break

def MediaAluno ():
    print("\nCalculador da média ponderada de aluno \n")
    class MediaError(ValueError):
        pass
    while True:
        try:
            N1 = int(input("Digite o valor da 1º nota: "))
            if N1<0 or N1>10:
                raise MediaError
            P1 = int(input("Digite o peso da 1º nota: "))
            N2 = int(input("Digite o valor da 2º nota: "))
            if N2<0 or N2>10:
                raise MediaError
            P2 = int(input("Digite o peso da 2º nota: "))
            N3 = int(input("Digite o valor da 3º nota: "))
            if N3<0 or N3>10:
                raise MediaError
            P3 = int(input("Digite o peso da 3º nota: "))
            MP = (N1 * P1 + N2 * N2 + N3 * P3) / (P1 + P2 + P3)
            par=1
            if MP>=7:
                print("O Aluno foi aprovado; (Media) = ", MP)
            else:
                print("O Aluno foi aprovado; (Media) = ", MP)
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


def CalcSalLiqeBruto ():
    print("\nCalculador do Salário Líquido e Bruto \n")
    while True:
        try:
            HrTrab = int(input("Digite a quantidade de hotas: "))
            ValorPHr = float(input("Digite o valor por hora: "))
            Depedente = int(input("Digite a quantidade de Dependentes: "))
            ValorBruto = HrTrab * ValorPHr
            ValorLiquido = ValorBruto + (Depedente * 300)
            par=1
            print("Seu salário bruto é: R$ ", ValorBruto), print("Seu salário líquido é: R$", ValorLiquido)
        except ValueError:
            print("Só é aceitado valores inteiros em horas trabalhadas e Dependente e flutuantes em Valor por Hora!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break
    
def VolEsfera():
    print("\nCalculador do Volume de uma Esfera \n")
    while True:
        try:
            Raio = float(input("Digite o valor de Raio da Esfera: "))
            Volume = 4 * math.pow(Raio,3)/3
            print("O valor do volume é: ", Volume)
        except ValueError:
            print("Não é aceito valores string/carácteres!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break


def AreaExLata():
    print("\nCalculador da Area Externa de uma Lata \n")
    Raio = float(input("Digite o valor de Raio da Lata: "))
    Alt = float(input("Digite o valor da altura da Lata: "))
    AreaExterna = 2*math.pi*Raio*(Raio+Alt)
    return print("A área externa da lata é: ", AreaExterna)



