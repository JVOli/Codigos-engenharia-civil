#_______________________________________________________________________
#
#                      [ENG01060 - AVALIAÇÃO 3]
#
#    Programação de Métodos Numéricos Aplicados à Engenharia Civil
#
#       Universidade Federal do Rio Grande do Sul >> [UFRGS]
#       Departamento de Engenharia Civil          >> [DECIV]
#
#                                       Professor: Renato Vaz Linn
#
#  CARTÃO                            NOME                    
# [315952]   [            Joao Vitor de Oliveira Cunha            ] 
# [000002]   [                   Nome Sobrenome                   ] 
# [000003]   [                   Nome Sobrenome                   ]  
# [000004]   [                   Nome Sobrenome                   ]  
# [000005]   [                   Nome Sobrenome                   ] 
#
#                                                                              
#                           *///////////////////////////////////            
#                      .////////////////////////////////*///////            
#                  *////////////////////////////////*///////////            
#              *////////////////////////////////////////////////            
#         .////////////////////////////////*////////////////////            
#     *////////////////////////////////*////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************///////////////////////*              
#    *********************************///////////////////.                  
#    *********************************///////////////                       
#    *********************************//////////*                           
#    *********************************//////.                               
#    *********************************//                                    
#                                            
#                            AVALIAÇÃO:
#
# [FUNCIONAMENTO] - O código é capaz de solucionar o problema proposto
#                   e encontrar a solução correta (6 pts)
#    [CLAREZA]    - O código é bem escrito e claro de entender, possui
#                   informações suficientes para compreensão (1 pt)
#  [VISUALIZAÇÃO] - O código produz saídas gráficas cientificamente 
#                   adequadas e precisas (3 pts)
#_______________________________________________________________________  

#_______________________________________________________________________
#
#                      [ENG01060 - AVALIAÇÃO 3]
#
#    Programação de Métodos Numéricos Aplicados à Engenharia Civil
#
#       Universidade Federal do Rio Grande do Sul >> [UFRGS]
#       Departamento de Engenharia Civil          >> [DECIV]
#
#                                       Professor: Renato Vaz Linn
#
#  CARTÃO                            NOME                    
# [315952]   [            Joao Vitor de Oliveira Cunha            ] 
# [000002]   [                   Nome Sobrenome                   ] 
# [000003]   [                   Nome Sobrenome                   ]  
# [000004]   [                   Nome Sobrenome                   ]  
# [000005]   [                   Nome Sobrenome                   ] 
#
#                                                                              
#                           *///////////////////////////////////            
#                      .////////////////////////////////*///////            
#                  *////////////////////////////////*///////////            
#              *////////////////////////////////////////////////            
#         .////////////////////////////////*////////////////////            
#     *////////////////////////////////*////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************//////////////////////////            
#    *********************************///////////////////////*              
#    *********************************///////////////////.                  
#    *********************************///////////////                       
#    *********************************//////////*                           
#    *********************************//////.                               
#    *********************************//                                    
#                                            
#                            AVALIAÇÃO:
#
# [FUNCIONAMENTO] - O código é capaz de solucionar o problema proposto
#                   e encontrar a solução correta (6 pts)
#    [CLAREZA]    - O código é bem escrito e claro de entender, possui
#                   informações suficientes para compreensão (1 pt)
#  [VISUALIZAÇÃO] - O código produz saídas gráficas cientificamente 
#                   adequadas e precisas (3 pts)
#_______________________________________________________________________  

#Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Ler os dados e configura-los com pandas
Dados = pd.read_csv('Dados.txt',header=None, sep='\t')
Dados.columns = ['x', 'f(x)']
#Passar pala rum array
Array = Dados.to_numpy()
#Separando o array em x e fx
x = Array[:,0]
fx = Array[:,1]
#Ler os dados e configura-los sem bibliotecas
##Funcao para retornar apenas os numeros
#def only_numerics(seq):
#    seq_type= type(seq)
#    return seq_type().join(filter(seq_type.isdigit, seq))
##Abrir o arquivo e separar em linhas
#with open("Dados.txt", "r") as Valores:
#    lines = Valores.readlines()
#    x = []
#    fx = []
#    neg = []
##Separar x de fx, e unir as linhas
#for l in lines:
#    as_list = l.split("\t")
#    x.append(as_list[0])
#    fx.append(as_list[1].replace("\n",""))
##Achar os fx negativos
#for i in range(np.size(X)):
#    if(len(fx[i]) == 9):
#        neg.append(i)
##Transformar de str para int
#for i in range(np.size(X)):
#    fx[i] = int(only_numerics(fx[i]))/1000000
#    x[i] = int(only_numerics(x[i]))/1000000
##Devolver os sinais do fx
#for i in range(len(neg)):
#    fx[int(neg[i])] = fx[int(neg[i])]*(-1)
#Testes se os imputs sao validos
teste = False
Continuar = False
#Receber e testaros os inputs
while(teste == False):
    print('-----------------------------------------------------------------------')
    inicio = input('Qual o intervalo de integracao?\nDigite o primeiro valor(0-1): ')
    try:
        inicio = float(inicio)
        Continuar = True
    except:
        print('Digite um numero')
        Continuar = False
    if(Continuar == True):
        if(inicio<0 or inicio>1):
            print('Digite um numero de 0 a 1')
            Continuar = False
    if(Continuar == True):
        fim = input('Digite o segundo valor(inicio-1): ')
        try:
            fim = float(fim)
            Continuar = True
        except:
            print('Digite um numero')
            Continuar = False
        if(Continuar == True):
            if(fim<=inicio or fim>1):
                print('Digite um numero entre o primeiro valor e 1')
                Continuar = False
            else:
                teste = True
    print('-----------------------------------------------------------------------')
#Descobrir em que intervalo esta o ponto de inicio e fim
ini_pos = 0
fim_pos = 0
for i in range(0, len(x)):
    if(inicio >= x[i]):
        ini_pos = ini_pos + 1
for i in range(0, len(x)):
    if(fim > x[i]):
        fim_pos = fim_pos + 1
#Caso o inicio e fim esteja em intervalos diferentes
if(ini_pos != fim_pos): 
    #Descobrir fx do inicio e fim
    fx_ini = fx[ini_pos]+(fx[ini_pos]-fx[ini_pos-1])*(inicio-x[ini_pos])/(x[ini_pos]-x[ini_pos-1])
    fx_fim = fx[fim_pos]+(fx[fim_pos]-fx[fim_pos-1])*(fim-x[fim_pos])/(x[fim_pos]-x[fim_pos-1])
    #Somar a area do inicio
    Area = (fx[ini_pos]+fx_ini)*(x[ini_pos]-inicio)/2
    #Somar a Area do fim
    Area = Area + (fx[fim_pos-1]+fx_fim)*(fim-x[fim_pos-1])/2
    #Somar os intervalos entre o inicio e fim
    for i in range(ini_pos, fim_pos-1):
        Area = Area + (x[i+1]-x[i])*(fx[i]+fx[i+1])/2
    #plot
    fig, ax = plt.subplots(figsize=(10,10))
    ax.plot(x, fx)
    ax.set(xlabel='x', ylabel='f(x)', title='Area: '+str(round(Area,8)))
    ax.grid()
    #X e Y do inicial e final
    X0 = [x[ini_pos],x[ini_pos],inicio,inicio, x[ini_pos]]
    Y0 = [0, fx[ini_pos], fx_ini, 0, 0]
    plt.plot(X0, Y0, color = '#0BD94B',linewidth=0.5)
    X0 = [x[fim_pos-1],x[fim_pos-1],fim,fim, x[fim_pos-1]]
    Y0 = [0, fx[fim_pos-1], fx_fim, 0, 0]
    plt.plot(X0, Y0, color = '#0BD94B',linewidth=0.5)
    #Inicio e fim da integracao
    fimY = [-0.5, 1.1]
    fimX = [fim, fim]
    plt.plot(fimX, fimY, color = '#FF0000',linewidth=1)
    iniY = [-0.5, 1.1]
    iniX = [inicio, inicio]
    plt.plot(iniX, iniY, color = '#FF0000',linewidth=1)
    plt.plot([inicio, fim],[-0.45, -0.45] , color = '#FF0000', dashes=[6, 2],linewidth=1)
    #Trapezios entre o inicio e fim
    for i in range(ini_pos, fim_pos-1):
        X0 = [x[i],x[i],x[i+1],x[i+1], x[i]]
        Y0 = [0, fx[i], fx[i+1], 0, 0]
        plt.plot(X0, Y0, color = '#0BD94B',linewidth=0.5)
    plt.show()
#Caso o inicio e fim esteja no mesmo intervalo 
else:
    #Descobrir fx do inicio e fim
    fx_ini = fx[ini_pos]+(fx[ini_pos]-fx[ini_pos-1])*(inicio-x[ini_pos])/(x[ini_pos]-x[ini_pos-1])
    fx_fim = fx[fim_pos]+(fx[fim_pos]-fx[fim_pos-1])*(fim-x[fim_pos])/(x[fim_pos]-x[fim_pos-1])
    #Calculo da area
    Area = (fx_ini + fx_fim)*(fim - inicio)/2
    #plot
    fig, ax = plt.subplots(figsize=(10,10))
    ax.plot(x, fx)
    ax.set(xlabel='x', ylabel='f(x)', title='Area: '+str(round(Area,8)))
    ax.grid()
    #X e Y do inicial e final
    X0 = [fim,fim,inicio,inicio, fim]
    Y0 = [fx_fim, fx_fim, fx_ini, fx_fim, fx_fim]
    plt.plot(X0, Y0, color = '#0BD94B',linewidth=0.5)
    #Inicio e fim da integracao
    fimY = [-0.5, 1.1]
    fimX = [fim, fim]
    plt.plot(fimX, fimY, color = '#FF0000',linewidth=1)
    iniY = [-0.5, 1.1]
    iniX = [inicio, inicio]
    plt.plot(iniX, iniY, color = '#FF0000',linewidth=1)
    plt.plot([inicio, fim],[-0.45, -0.45] , color = '#FF0000', dashes=[6, 2],linewidth=1)
    plt.show()