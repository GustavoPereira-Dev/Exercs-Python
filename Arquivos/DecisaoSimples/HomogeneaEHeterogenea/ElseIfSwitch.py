import math
import numpy 



def mes1a12():
    print("\nAlgorítmo de meses \n")
    class MounthError(ValueError):
        pass
    par=0
    while True:
            try:
                No = int(input("Digite um número entre 1 e 12: "))
                if No<=0 or No>12:
                    raise MounthError
            except MounthError:
                print('Algo no seu comando esta errado, digite um No entre 1 e 12')
            except ValueError:
                print("Só é aceitado valores inteiros!")
            except KeyboardInterrupt:
                print("Não utilize o control c control v na hora de mandar os dados!")
            except:
                print("Algo ocorreu errado, tente novamente")
            else:
                par+=1
                match No:
                    case 1:
                        print("O mês é Janeiro")
                    case 2:
                        print("O mês é Fevereiro")
                    case 3:
                        print('O mês é Março')
                    case 4:
                      print('O mês é Abril')
                    case 5:
                      print('O mês é Junho')
                    case 6:
                      print('O mês é Junho')
                    case 7:
                      print('O mês é Julho')
                    case 8:
                      print('O mês é Agosto')
                    case 9:
                      print('O mês é Setembro')
                    case 10:
                      print('O mês é Outubro')
                    case 11:
                      print('O mês é Novembro')
                    case 12:
                      print('O mês é Dezembro')
            if par!=0:
                break
        
           
def AlgCaixEle():
    print("\nAlgorítmo do Caixa Eletrônico \n")
    class ChoiceError(ValueError):
        pass
    class PasswordError(ValueError):
        pass
    par=0
    par1=0
    par2=0
    ConfSenha=0
    ContCont=0
    for i in range(4):
        try:
            par1=0
            Senha = input("Digite a senha que deseja colocar de 4 carácteres: ")
            for letter in range(len(Senha)):
                par1+=1
            if par1==4:
                ConfSenha=1
            else:
                ConfSenha=0
                raise PasswordError
            par2=0
            Conf = input("Digite a senha novamente para confirmar: ")
            for letter in range(len(Conf)):
                par2+=1
            if par2==4:
                ConfCont=1
            else:
                ConfCont=0
                raise PasswordError
            if Senha + "" == Conf + "" and ConfSenha==1 and ConfCont:
                par+=1
                print("A senha está correta!")
                escolha = int(input("Digite a escolha que deseja fazer: "))
                match escolha:
                    case 1:
                        print ("O valor para seu emprestimo sera:  R$ 10000")
                    case 2:
                        print ("Seu saldo eh: R$ 10000")
                    case 3:
                        print ("O valor para sacar serah R$ 10000")
                    case _:
                        par=0
                        raise ChoiceError
                if par!=0:
                    break
                
            else:
                print ("Senha incorreta, tente novamente")
        except ChoiceError:
            print('Opção invalida, tente novamente.')
        except PasswordError:
            print("Só é aceito uma senha com 4 carácteres!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
               


    if par==0:
        print("O Algorítmo foi bloqueado devido as diversas tentativas falhas, tente novamente em meia hora")
        
            
  	
 
    

	
def AlgOp():
    print("\nAlgorítmo de Operações \n")
    par=0
    Esc=0
    class ChoiceError(ValueError):
        pass
    while True:
        try:
            Operacao = int(input("Digite a operação desejada: 1 soma, 2 subtração, 3 divisão, 4 multiplicação \n5  Módulo, 6 Divisão Inteira, 7 Exponenciação ou 8 Radiciação: "))
            if Operacao<8:
                N1 = float(input("Digite o primeiro número: "))
                N2 = float(input("Digite o segundo número: "))
            else:
                N1 = float(input("Digite o numero que será radiciado: "))
            par=1
            match Operacao:
                case 1:
                    Res = N1+N2
                    print("O valor de soma é: ", Res)
                case 2:
                    Res = N1 - N2
                    print ("O valor de subtração é: ", Res)
                case 3:
                    Res = N1 / N2
                    print ("O valor de divisão é: ", Res)
                case 4:
                    Res = N1 * N2
                    print ("O valor de multiplicação é: ", Res)
                case 5: 
                    Res = N1 % N2
                    print ("O valor de módulo é: ", Res)
                case 6: 
                    Res = N1 // N2
                    print ("O valor de divisão int é: ", Res)
                case 7: 
                    Res = N2 ** N1
                    print ("O valor de exponenciação é: ", Res)
                case 8:
                    Esc = int(input("Deseja uma raiz quadrada ou cúbica? Digite 1 para qd e 2 para cbc "))
                    if Esc==1:
                        Res = math.sqrt(N1)
                        print ("O valor da raiz quadrada é: ", Res)
                    else:
                        Res = numpy.cbrt(N1)
                        print ("O valor da raiz cúbica é: ", Res)
                case _:
                    par=0
                    raise ChoiceError
        except ChoiceError:
            print('Opção invalida, tente novamente.')
        except ZeroDivisionError:
            par=0
            print("Não é possível dividir com um denominador zero!")
        except ValueError:
            par=0
            print("Só é aceitado valores inteiros na escolha e não strings nos números!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break



def EstCvl():
    print("\nAlgorítmo do Estado Cívil \n")
    par=0
    class ChoiceError(ValueError):
        pass
    while True:
        try:
            EstCv = input("Digite o seu Estado Cívil (S Solteiro, C Casado, D Divorciado ou Viúvo): ")
            par=1
            match EstCv:
                case 'S':
                    print ("Seu Estado Cívil é solteiro(a)")
                case 'C':
                    print ("Seu Estado Cívil é casado(a) ")
                case 'D':
                    print ("Seu Estado Cívil é divorciado(a) ")
                case 'V':
                    print ("Seu Estado Cívil é viúvo(a) ")
                case _:
                    par=0
                    raise ChoiceError
        
        except ChoiceError:
            print("Ops! Algo está errado na digitação, tente novamente ")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        
        if par!=0:
            break

            
def CodProd():
    print("\nAlgorítmo do Código de Produto \n")
    class ChoiceError(ValueError):
        pass
    par=0
    while True:
        try:
            Codigo = int(input("Digite o Código do produto: "))
            par=1
            if Codigo == 1:
                print("O produto é um alimento não perecível")
            elif Codigo >= 2 and Codigo <=4:
                print("O produto é um alimento perecível")
            elif Codigo == 5 or Codigo == 6:
                print("O produto faz parte de um vestuário")
            elif Codigo == 7:
                print("O produto é de Higiene pessoal")
            elif Codigo >=8 and Codigo <=15:
                print("O produto é de limpeza e utensílios domésticos")
            else:
                par=0
                raise ChoiceError
        except ChoiceError:
            print('Opção invalida,só é aceito valores de código até 15, tente novamente.')
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break
        


def DDataIn():
    print("\nCalculador da diferença entre 2 data informadas \n")
    par=0
    class YearError(ValueError):
        pass
    class MounthError(ValueError):
        pass
    class DayError(ValueError):
        pass
    while True:
        try:
            Ano = int(input("Digite o primeiro ano: "))
            if Ano<0 or Ano>2022:
                raise YearError
            Mes = int(input("Digite o primeiro mês: "))
            if Mes<0 or Mes >12:
                raise MounthError
            Dia = int(input("Digite o primeiro dia: "))
            if Dia<0 or Dia>31:
                raise DayError
            
            Ano2 = int(input("Digite o segundo ano: "))
            if Ano2<0 or Ano2>2022:
                raise YearError
            Mes2 = int(input("Digite o segundo mês: "))
            if Mes2<0 or Mes2 >12:
                raise MounthError
            Dia2 = int(input("Digite o segundo dia: "))
            if Dia2<0 or Dia2>31:
                raise DayError
            
        except YearError:
            print("O valor de ano está ilógico ou não existente ainda!")
        except MounthError:
            print("O valor de Mês está ilógico!")
        except DayError: 
            print("O valor de dia está ilógico ou não existente ainda!")
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
             
        else:
            print("A")
            if Ano<Ano2:
                print("O primeiro ano é mais antigo que o segundo")
            elif Ano>Ano2:
                print("O segundo ano é mais antigo que o primeiro")
            elif Mes<Mes2:
                print("O primeiro mês é mais antigo que o segundo")
            elif Mes>Mes2:
                print("O segundo mês é mais antigo que o primeiro")
            elif Dia<Dia2:
                print("O primeiro dia é mais antigo que o segundo")
            elif Dia<Dia2:
                print("O segundo dia é mais antigo que o primeiro")
            else:
                print("As datas são iguais! ")
        if par!=0:
            break

def HorTurn():
    print("\nAlgorítmo do Horário de turno \n")
    class TurnError(ValueError):
        pass
    par=0
    while True:
        try:
            Turno = float(input("Digite a hora do início do turno de trabalho: "))
            par=1
            if Turno>=5.00 and Turno<=12.59:
                print("O turno é de manhã")
            elif Turno>=13.00 and Turno<=20.59:
                print("O turno é de tarde")
            elif Turno>=21.00 and Turno<=24.00 or Turno>=00.01 and Turno<=04.59:
                print("O turno é da noite")
            else:
                par=0
                raise TurnError
        except TurnError:
            print("Só é aceito um valor entre 00.00 e 24.00!")
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break


def IdadeNad():
    print("\nAlgorítmo da idade do nadador e sua categoria \n")
    class SwimmerError(ValueError):
        pass
    while True:
        try:
            Idade = int(input("Digite a Idade completa do Nadador(a): "))
            par=1
            if Idade>=5 and Idade<=7:
                print("O nadador(a) é Infantil A")
            elif Idade>=8 and Idade<=10:
                print("O nadador(a) é Infantil B")
            elif Idade>=11 and Idade<=13:
                print("O nadador(a) é Juvenil A")
            elif Idade>=14 and Idade<=17:
                print("O nadador(a) é Juvenil B")
            elif Idade>=18:
                print("O nadador é Sênior")
            else:
                par=0
                raise SwimmerError
            
        except SwimmerError:
            print("Algo nessa Idade esta errada, digite um numero inteiro maior/igual que 5")
        except ValueError:
            print("Só é aceitado valores inteiros!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break
        

def LancheMac():
    print("\nAlgorítmo de escolha de um Lanche do Mc \n")
    class LunchError(IndexError):
        pass
    par=0
    while True:
        try:
            Cliente = input("Digite seu nome: ")
            Opcao = int(input("Digite a opcao do Lanche (1 BigMac, 2 Quarteirao, 3 MacChicken, 4 MacMelt \n e 5 MacMax): "))
            par=1
            match Opcao:
                case 1:
                    print("Entendido, 1 Bigmac para o cliente ", Cliente)
                case 2:
                    print("Entendido, 1 Quarteirão para o cliente ", Cliente)
                case 3:
                    print("Entendido, 1 Macchicken para o cliente ", Cliente)
                case 4:
                    print("Entendido, 1 MacMelt para o cliente ", Cliente)
                case 5:
                    print("Entendido, 1 MacMax para o cliente´", Cliente)
                case _:
                    par=0
                    raise LunchError

        except LunchError:
            print("Algo está incorreto em seu pedido, por favor tente novamente")
        except ValueError:
            print("Só é aceitado valores inteiros na opção de lanche!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")

        if par!=0:
            break



def MeApvOuRep():
    print("\nCalculador da média do aluno e da provação ou reprovação \n")
    class NoteError(ValueError):
        pass
    par=0
    while True:
        try:
            Nota1 = float(input("Digite o valor da primeira nota: "))
            if Nota1<0 or Nota1>10:
                raise NoteError
            Nota2 = float(input("Digite o valor da segundo nota: "))
            if Nota2<0 or Nota2>10:
                raise NoteError
            Nota3 = float(input("Digite o valor da terceira nota: "))
            if Nota3<0 or Nota3>10:
                raise NoteError
            Nota4 = float(input("Digite o valor da quarta nota: "))
            if Nota4<0 or Nota4>10:
                raise NoteError
            Media = (Nota1+Nota2+Nota3+Nota4)/4
            par+=1
            if Media>=9 and Media<=10:
                print("A nota é A, o aluno foi aprovado; (Media): ", Media)
            elif Media>=7 and Media<=8.9:
                print("A nota é B, o aluno foi aprovado; (Media): ", Media)
            elif Media>=5 and Media<=6.9:
                print("A nota é C, o aluno precisará fazer recuperação; (Media): ", Media)
            elif Media>=2.6 and Media<=4.9:
                print("A nota é D, o aluno será reprovado; (Media): ", Media)
            elif Media>=0 and Media<=2.5:
                print("A nota é E, o aluno está completamente reprovado...; (Media): ", Media)
        except NoteError:
            print("Ops! Parece que houve algum erro, veja se houve uma digitacao menor que 0 ou \n maior que 10 na nota")
        except ValueError:
            print("Só é aceitado valores inteiros e flutuantes!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break



def OrdCresABC():
    print("\nAlgorítmo Calculador da ordem crescente ABC \n")
    par=0
    while True:
        try:
            A = float(input("Digite o valor A: "))
            B = float(input("Digite o valor B: "))
            C = float(input("Digite o valor C: "))
        except ValueError:
            print("Só é aceitado valores inteiros e flutuantes!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        else:
            par=1
            if A<B and B<C:
                print("A sequência crescente é: ", A,"A, ", B ,"B,", C ,"C")
            elif B<C and C<A:
                print("A sequência crescente é: ", B, "B, ", C, "C, ", A, "A")
            elif C<A and A<B:
                print("A sequência crescente é: ", C,"C, ", A, "A, ", B,"B")
            elif B<A and A<C:
                print("A sequência crescente é: ", B, "B, ", A, "A, ", C, "C")
            elif C<B and B<A:
                print("A sequência crescente é: ", C, "C, ", B, "B, ", A, "A")
            elif A<C and C<B:
                print("A sequência crescente é: ", A, "A, ", C, "C, ", B, "B")
            else:
                print("Os números são iguais! ")
        if par!=0:
            break
    

def PerfPessoa():
    print("\nAlgorítmo de perfil pessoal pelos 2 dígitos do ano de nascimento \n")
    par=0
    class DigitError(ValueError):
        pass
    while True:
        try:
            AnoNasc1 = int(input("Digite o primeiro dígito do seu ano de nasciento (Ex: *19*87): "))
            if AnoNasc1>9 and AnoNasc1<21:
                ConfDig1=1
            else:
                ConfDig1=0
                raise DigitError    
            AnoNasc2 = int(input("Digite o segundo dígito do seu ano de nasciento (Ex: 19*87*): "))
            if AnoNasc2>9 and AnoNasc2<100:
                ConfDig2=1
            else:
                ConfDig2=0
                raise DigitError
            Perfil = (AnoNasc1+AnoNasc2)%5
        except DigitError:
            print("É necessário ter o primeiro digito, e depois o segundo dígito!")
        except ValueError:
            print("Só é aceitado valores inteiros e flutuantes!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente") 
        else:
            par=1
            if Perfil==0:
                print("Seu perfil é Tímido(a)")
            elif Perfil==1:
                print("Seu perfil é Sonhador(a)")
            elif Perfil==2:
                print("Seu perfil é Paquerador(a)")
            elif Perfil==3:
                print("Seu perfil é Atraente")
            elif Perfil==4:
                print("Seu perfil é Irresistível")
        if par!=0:
            break



def TipTriang():
    print("\nAlgorítmo do Tipos de triângulos \n")
    class TriangleError(ValueError):
        pass
    par=0
    while True:
        try:
            A = float(input("Digite um valor do lado A do triângulo em cm: "))
            B = float(input("Digite um valor do lado B do triângulo em cm: "))
            C = float(input("Digite um valor do lado C do triângulo em cm: "))

            if A==B and A==C and A+B==C:
                print("O triângulo é Equilátero")
            elif A==B and A+B>C or A==C and A+B>C:
                print("O triângulo é Isósceles")
            elif A!=B and A!=C and A+B>C:
                print("O triângulo é Escaleno")
            else:
                raise TriangleError
                
        except TriangleError:
            print("Os números não compusem um triângulo")
        except ValueError:
            print("Só é aceitado valores inteiros e flutuantes!")
        except KeyboardInterrupt:
            print("Não utilize o control c control v na hora de mandar os dados!")
        except:
            print("Algo ocorreu errado, tente novamente")
        if par!=0:
            break




            
                   

