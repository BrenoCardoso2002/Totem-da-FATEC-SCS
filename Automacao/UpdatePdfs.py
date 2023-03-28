# Ideia de como funciona o programa que atualiza os PDFs:
# O programa ficaria rodando de fundo;
# A pagina web ficaria aberta o tempo todo no moto tela cheia (f11 ativo);
# Ai quando o computador visse que era um horario especifico ele rodaria todos as funções que no fim realizam a atualização os PDFs de horário e calendário.

# Importações:
import time
from datetime import datetime
import pyautogui
import os

# a função a seguir é uma função que realiza um looping infinito, o looping repete a cada 1 segundo e verifica se a hora no computador é uma hora especifica se for a hora especificada é chamado algumas funções:
def verificaTempo():
    # faz um laço infinito:
    while True:
        time.sleep(1) # Espera 1 segundo
        tempo_atual = datetime.now() # pega a data atual inteira
        hora_atual = tempo_atual.hour # pega apenas a hora
        minuto_atual = tempo_atual.minute # pega apenas o minuto
        segundo_atual = tempo_atual.second # pega apenas o segundo
        # if que verifica o tempo especifico:
        if hora_atual == 2 and minuto_atual == 20 and segundo_atual == 8:
            baixaPDFs() # chama a função que baixa os novos PDFs
            apagaArquivos() # chama a função que apaga os PDFs antigos
            moveArquivos() # chama a função que move os PDFs novos para a pasta correta
            break
    verificaTempo() # chama a função de novo

# a função a seguir faz uma automação do telcado e do mouse para baixar os PDFs no site da fatec:
def baixaPDFs():
    # obs.: a pagina web do totem estara em fullScreen

    pyautogui.press('f11') # tira o fullScreen

    site_fatec = 'fatecsaocaetano.edu.br/' # link do site da fatec

    pyautogui.hotkey('ctrl', 't') # abre uma nova guia
    pyautogui.hotkey('ctrl', 'l') # foca no campo de pesquisa de link do navegador
    pyautogui.write(site_fatec) # digita o link do site fatec
    pyautogui.press('enter') # aperta no enter

    baixaCalendario() # aqui chama a função que baixa o calendario
    baixaHorario() # aqui chama a função que baixa o horario

    time.sleep(5) # Espera 5 segundo

    pyautogui.hotkey('ctrl', '9') # vai pra ultima guia do navegador
    pyautogui.hotkey('ctrl', 'w') # fecha guia
    pyautogui.hotkey('ctrl', '9') # vai pra ultima guia do navegador
    pyautogui.press('f11') # coloca o fullScreen

# essa é a função que baixa o calendario:
def baixaCalendario():
    time.sleep(5) # Espera 5 segundo

    pyautogui.click(x=710, y=430) # clica no botão do site da fatec que abre o drive que está o PDF do calendario

    time.sleep(2.5) # Espera 2.5 segundo

    pyautogui.click(x=1185, y=125) # clica no botão de baixar pdf

    time.sleep(5) # Espera 5 segundo

    pyautogui.hotkey('ctrl', 'w') # fecha a guia que está, a guia do drive com o PDF do calendario

# essa é a função que baixa o horario:
def baixaHorario():
    time.sleep(5) # Espera 5 segundo

    pyautogui.click(x=910, y=430) # clica no botão do site da fatec que abre o drive que está o PDF do horario

    time.sleep(2.5) # Espera 2.5 segundo

    pyautogui.click(x=1185, y=125) # clica no botão de baixar pdf

    time.sleep(5) # Espera 5 segundo

    pyautogui.hotkey('ctrl', 'w') # fecha a guia que está, a guia do drive com o PDF do horario

# aqui é a função que apaga os arquivos PDFs antigos:
def apagaArquivos():
    apagaHorario() # chama a função que apaga o arquivo do horario
    apagaCalendario() # chama a função que apaga o arquivo do calendario

# função que realiza a remoção do arquivo PDF do horario:
def apagaHorario():
    pasta = 'PDFs' # nome da pasta
    arquivo = 'horario.pdf' # nome do arquivo
    caminho = os.path.join(pasta, arquivo) # aqui é o caminho relativo do arquivo

    # o if abaixo verifica se o arquivo existe e apaga ele:
    if os.path.exists(caminho):
        os.remove(caminho) # remove o arquivo

# função que realiza a remoção do arquivo PDF do calendario:
def apagaCalendario():
    pasta = 'PDFs' # nome da pasta
    arquivo = 'calendario.pdf' # nome do arquivo
    caminho = os.path.join(pasta, arquivo) # aqui é o caminho relativo do arquivo

    # o if abaixo verifica se o arquivo existe e apaga ele:
    if os.path.exists(caminho):
        os.remove(caminho) # remove o arquivo

# função que moves os arquivos para a pasta correta:
def moveArquivos():
    pasta = '/home/breno/Downloads/' # esse caminho da pasta onde os arquivos baixados estão salvos

    nomeHorario = 'horario' # nome relativo do arquivo PDF com o horario
    nomeCalendario = 'calendario' # nome relativo do arquivo PDF com o calendario

    # lista todos os arquivos da pasta:
    arquivos = [arquivo for arquivo in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, arquivo))]

    # esse if abaixo passa por todos os nome dos arquivos:
    for arquivo in arquivos:
        # o if abaixo ve se o nome do arquivo contem a palavra horario:
        if nomeHorario in arquivo:
            moveHorario(pasta, arquivo, nomeHorario) # chama a função que move o arquivo do horario
        # o if abaixo ve se o nome do arquivo contem a palavra calendario:
        if nomeCalendario in arquivo:
            moveCalendario(pasta, arquivo, nomeCalendario) # chama a função que move o arquivo do calendario

# função que move o horario:
def moveHorario(pasta, arquivo, nomeHorario):
    caminho_origem = os.path.join(pasta, arquivo) # caminho que está o arquivo baixado do horario
    caminho_destino = f'PDFs/{nomeHorario}.pdf' # caminho que o arquivo deverá ser colocado
    os.rename(caminho_origem, caminho_destino) # move o arquivo pra o local determinado

# função que move o calendario:
def moveCalendario(pasta, arquivo, nomeCalendario):
    caminho_origem = os.path.join(pasta, arquivo) # caminho que está o arquivo baixado do calendario
    caminho_destino = f'PDFs/{nomeCalendario}.pdf' # caminho que o arquivo deverá ser colocado
    os.rename(caminho_origem, caminho_destino) # move o arquivo pra o local determinado

# Aqui é um if de inicialização do arquivo Python:
if __name__ == '__main__':
    verificaTempo()
