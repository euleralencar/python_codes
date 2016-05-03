# Carregando pacotes essenciais
import webbrowser, pyautogui, time

## Obs.: a posição no pyautogui é coluna, linha

# Introdução para a execução do programa
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
print('Coloque o Webbrower aberto na Tela Principal')

input() # press Enter to begin
print('Started.')

#Schedule a time
#Implementar um roteiro para dizer o tempo que quero para bater o ponto
prog = int(input('Quanto tempo (em segundos) para execução do programa? '))

#Abrindo Browser simplificado
webbrowser.open('http://sistemasnet/sarh/horarioflexivelNovo/lancamento/LancamentoHoras.asp?SISQSmodulo=18384&excel=true')
time.sleep(15) # espera para ser carregada a página

# não utilizarei o comando abaixo
# time.sleep(int(prog)) # tempo de espera até o programa ser rodado

time_for = 5*prog/9.71+1

for i in range(int(time_for)):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

#Posição do Botão de Saída
pyautogui.click(1862, 388) #Tela1
#pyautogui.click(3787, 385) #Tela2

#Clicar na posição do botão de Ok
pyautogui.click(1039, 167)

#Clicar na posição de Ok (segundo botão)
pyautogui.click(1113, 167)

# COMO ACHAR POSICAO DESEJADA
# import pyautogui
# pyautogui.position()

# Criar um roteiro para colocar o computador em Sleep
import os
os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')
