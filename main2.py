from sys import path


path.append('..\\packages')

#Calculos e Saque Parte 1
#Funções: MA, Soma, Soma4, MP, LV, CalcSal, SalNePerc, SalBase, SacarouDeposito

print("Pacote de praticamente todas (até agora) atividades feitas na linguagem C convertidas em funções do Python!")
Scon1 = int(input("Digite 1 se deseja ver alguma das funções no arquivo 'Cálculos e Saque'! \n Funções disponíveis: MA, Soma, Soma4, MP, LV, CalcSal, SalNePerc, SalBase e SacarouDeposito")


    if Scon1==1:
            from Arquivos.listagemdev.CalculosESaquePt1 import MA, Soma, Soma4, MP, LV, CalcSal, SalNePerc, SalBase, SacarouDeposito
            SEsc = int(input("Digite qual função específica deseja ver da sequência anterior: ")
            
            match SEsc:
                       case 1:
                            MA()
                       case 2:
                            Soma4()
                       case 3:
                            Soma()
                       case 4:
                            MP()
                       case 5:
                            LV()
                       case 6:
                            CalcSal()
                       case 7:
                            SalNePerc()
                       case 8:
                            SalBase()
                       case 9:
                            SacarouDeposito()
                       case _:
                            print("Não existe uma função desse valor aqui, só é aceitado de 1 a 9")




#Calculos e Saque Parte 2
#Funções: ComboLanche,AlgCarro,MacasCompradas,Intervalo100e200,Incognitas3,AlgIguais2,AlgSexo,ValorParImpar,MediaAluno,CalcSalLiqeBruto,VolEsfera,AreaExLata
from Arquivos.listagemdev.CalculosESaquePt2 import ComboLanche,AlgCarro,MacasCompradas,Intervalo100e200,Incognitas3,AlgIguais2,AlgSexo,ValorParImpar,MediaAluno,CalcSalLiqeBruto,VolEsfera,AreaExLata
ComboLanche()
AlgCarro()
MacasCompradas()
Intervalo100e200()
Incognitas3()
AlgIguais2()
AlgSexo()
ValorParImpar()
MediaAluno()
CalcSalLiqeBruto()
VolEsfera()
AreaExLata()


#Estrutura de Decisão Simples
#Funções: SomamaiorQue25,PesoIdeal,Maioridade,MaiorEMenorR,MaiorEMenorI,CalcAreaRet,AlgIdade,AlgPesc,AlgSenha
from Arquivos.DecisaoSimples.IfEElse import SomamaiorQue25,PesoIdeal,Maioridade,MaiorEMenorR,MaiorEMenorI,CalcAreaRet,AlgIdade,AlgPesc,AlgSenha
SomamaiorQue25()
PesoIdeal()
Maioridade()
MaiorEMenorR()
MaiorEMenorI()
CalcAreaRet()
AlgIdade()
AlgPesc()
AlgSenha()

#Estrutura de Decisão Composta/Homogênea
#Funções: mes1a12,AlgCaixEle,AlgOp,EstCvl,CodProd,DDataIn,HorTurn,IdadeNad,LancheMac,MeApvOuRep,OrdCresABC,PerfPessoa,TipTriang
from Arquivos.DecisaoSimples.HomogeneaEHeterogenea.ElseIfSwitch import mes1a12,AlgCaixEle,AlgOp,EstCvl,CodProd,DDataIn,HorTurn,IdadeNad,LancheMac,MeApvOuRep,OrdCresABC,PerfPessoa,TipTriang
mes1a12()
AlgCaixEle()
AlgOp()
EstCvl()
CodProd()
DDataIn()
HorTurn()
IdadeNad()
LancheMac()
MeApvOuRep()
OrdCresABC()
PerfPessoa()
TipTriang()

#Laços For, while e dowhile
#Funções: Pdejat15,TabDej,Nimpatx,AltFemEMasc
from Arquivos.Loops.Lacos import Pdejat15,TabDej,Nimpatx,AltFemEMasc
Pdejat15()
TabDej()
Nimpatx()
AltFemEMasc()

#Questionário Animais
#Função: QuAnm
from Arquivos.Loops.QuizAnimais import QuAnm
QuAnm()


#Vetores
#Funções: El10,E110PI,El10AB,MAV
from Arquivos.Loops.Vetores.Vetor import El10,E110PI,El10AB,MAV
El10()
E110PI()
El10AB()
MAV()

#Matrizes
#Funções: N120,N25,M2,MAl
from Matriz.Matrizes import N120,N25,M2,MAl
N120()
N25()
M2()
MAl()

#Biblioteca de Advocacia
#Função: ProjBibioAdv
from  Arquivos.Loops.Vetores.Advocacia.EscritorioAdvocacia import ProjBibioAdv
ProjBibioAdv()





