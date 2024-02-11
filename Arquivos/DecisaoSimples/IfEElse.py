def SomamaiorQue25():
    print ("\nAlgorítmo do cálculo de soma maior que 25 \n")
    par=0
    while True:
        try:
            N1 = int(input("Digite o 1º número: "))
            N2 = int(input("Digite o 2º número: "))
            Soma = N1 + N2
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            par+=1
            if Soma>25:
                print ("A soma é maior que 25")
            elif Soma==25:
                print ("A soma é igual a 25")
            else:
                print("A soma é menor que 25")
        if (par!=0):
            break


def PesoIdeal():
    print ("\nCalculadora do Peso Ideal \n")
    par=0
    while True:
        try:
            Sexo = input("Digite o seu sexo: ")
            Altura = float(input("Digite a sua altura: "))
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            if Sexo + "" == "Masculino" or Sexo + "" == "masculino":
                par+=1
                Peso = (72.2 * Altura) -58
                print ("O seu peso ideal é: ", Peso)
            elif Sexo + "" == "Feminino" or Sexo + "" == "feminino":
                par+=1
                Peso = (62.1 * Altura) - 44.7
                print ("O seu peso ideal é: ", Peso)
            else:
                print("Só é aceitado o valor 'Masculino' ou \'Feminino\'")
        if par!=0:
            break



def Maioridade():
    print(" \nCalculadora da maioridade \n")
    par=0
    while True:
        try:
            AnoNascimento = int(input("Digite em que ano nasceu: "))
            Idade = 2022 - AnoNascimento
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            if Idade>=18:
                print ("A maioridade está atingida; (Idade) = ", Idade)
            else:
                print ("A maioridade não está atingida (Idade) = ", Idade)
        if par!=0:
            break

def MaiorEMenorR():
    print ("\nAlgorítmo do maior e menor número flutuante ou real\n")
    par=0
    class FloatError(ValueError):
        pass
    while True:
        try:
            Num1 = float(input("Digite o primeiro Número float: "))
            Num2 = float(input("Digite o segundo Número float: "))
            n = int(Num1)
            m = Num1 * 10
            s = n * 10
            n2 = int(Num2)
            m2 = Num2 * 10
            s2 = n2 * 10
            if m == s or m2==s2:
                raise FloatError
        except ValueError:
            print("Não é aceitado valores strings/carácteres!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except FloatError:
            print("Só é aceitado valores flutuantes ou não específicos!") 
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            par+=1
            if Num1>Num2:
                print("O Numero 1 (",Num1, ") é maior que o 2 (",Num2,")")
                print("O Numero 2 (",Num1,") é menor que o 1 (",Num2,")")
            else:
                print("O Numero 1 (",Num1,") é menor que o 2 (",Num2,")")
                print("O Numero 2 (",Num1,") é maior que o 1 (",Num2,")")
        if par!=0:
            break
        

 

def MaiorEMenorI():
    print ("\nAlgorítmo do maior e menor número Inteiro ou Natural \n")
    par=0
    while True:
        try:
            Num1 = int(input("Digite o primeiro Número float: "))
            Num2 = int(input("Digite o segundo Número float: "))
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            par+=1
            if Num1>Num2:
                print("O Numero 1 (",Num1, ") é maior que o 2 (",Num2,")")
                print("O Numero 2 (",Num1,") é menor que o 1 (",Num2,")")
            else:
                print("O Numero 1 (",Num1,") é menor que o 2 (",Num2,")")
                print("O Numero 2 (",Num1,") é maior que o 1 (",Num2,")")
        if par!=0:
            break

      
def CalcAreaRet():
    print ("\nCalculador da área do retângulo \n")
    class AreaError(ValueError):
        pass
    par=0
    while True:
        try:
            Base = float(input("Digite a base de um triângulo: "))
            Altura = float(input("Digite a altura de um triângulo: "))
            Area = (Base *Altura)/2
            if Base <=0 or Altura<=0:
                raise AreaError
        except AreaError:
            print ("Deve ser digitado um valor positivo maior que zero!")
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            par+=1
            print ("O resultado é: ", Area)
        if par!=0:
            break


def AlgIdade():
    print ("\n Algorítmo da Idade \n")
    par=0
    class YearError(ValueError):
        pass
    class NextYearError(ValueError):
        pass
    while True:
        try:
            AnoAtual = int(input("Digite o ano atual: "))
            AnoNasc = int(input("Digite o seu ano de nascimento: "))
            if AnoAtual<=AnoNasc or AnoAtual<=0 or AnoNasc<=0 or AnoAtual>=2023 or AnoNasc>=2023:
                raise YearError
            Idade = AnoAtual - AnoNasc
            print("Sua idade é: ", Idade)
            AnoASeComp = int(input("Digite um ano para saber quanto de idade terá nele: "))
            Idade2 = AnoASeComp - AnoNasc
            if Idade2<=0:
                raise NextYearError
        except YearError:
            print("Algo está errado na digitação, veja se colocou um ano indefinido ou se \n o AnoAtual está menor que o de Nascimento")
        except NextYearError:
            print("Algo está errado na digitação, veja se o Ano em comparação está menor \n que o de Nascimento")
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            par+=1
            print ("Você téra ",Idade2," Anos")
        if par!=0:
            break



def AlgPesc():
    print ("\nAlgorítmo do Pescador \n")
    class FishError(IndexError):
        pass
    par=0
    while True:
        try:
            KgPeixe = float(input("Digite a quantidade de quilos de peixe: "))
            if KgPeixe<=0:
                raise FishError
        except FishError:
            print("Algo está errado na digitação, só é aceito valores positivos")
        except ValueError:
            print("Não é aceito valores strings/caractéres!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            par+=1
            if KgPeixe<=50:
                print("O valor de peixe por pessoa está correto, parábens")
            else:
                PesoExc = KgPeixe-50
                Multa = PesoExc * 4
                print("O peso passou mais do que devia, valor excedente: ", PesoExc)
                print("Precisará ser pago esse valor de multa:  R$ ", Multa)
        if par!=0:
            break



def AlgSenha():
    print("\n Algorítmo de Senha\n")
    par=0
    for i in range(4):
        Senha = input("Digite a senha que deseja colocar: ")
        Conf = input("Digite a senha novamente para confirmar: ")
        if Senha + "" == Conf + "":
            par+=1
            print("A senha está correta!")
        else:
            print("A senha está incorreta, tente novamente")
        if par!=0:
            break
    if par==0:
        print("O Algorítmo foi bloqueado devido as diversas tentativas falhas, tente novamente em meia hora")

    
    
