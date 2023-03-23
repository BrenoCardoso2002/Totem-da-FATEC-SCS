import datetime
import time
import pyautogui
import os

def updatePdfs():
    pyautogui.press('f11')

    # abre o site da fatec:
    site_fatec = "fatecsaocaetano.edu.br/"

    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(site_fatec)
    pyautogui.press('enter')

    time.sleep(5)

    pyautogui.click(x=710, y=430) # botao do site da fatec que abre o drive (pdf calendario)
    time.sleep(2.5)
    pyautogui.click(x=1185, y=125) # botao de baixar pdf

    time.sleep(5)

    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2.5)

    pyautogui.click(x=910, y=430) # botao do site da fatec que abre o drive (pdf calendario)
    time.sleep(2.5)
    pyautogui.click(x=1185, y=125) # botao de baixar pdf

    time.sleep(5)
    pyautogui.hotkey('ctrl', '9')
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', '9')
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.press('f11')

def apagaArquivos():
    pasta = 'PDFs'
    arquivo = 'horario.pdf'
    caminho_completo = os.path.join(pasta, arquivo)

    if os.path.exists(caminho_completo):
        os.remove(caminho_completo)
        print(f"O arquivo {arquivo} foi removido com sucesso!")
    else:
        print(f"O arquivo {arquivo} não existe na pasta {pasta}.")

    pasta2 = 'PDFs'
    arquivo2 = 'calendario.pdf'
    caminho_completo2 = os.path.join(pasta2, arquivo2)

    if os.path.exists(caminho_completo2):
        os.remove(caminho_completo2)
        print(f"O arquivo {arquivo2} foi removido com sucesso!")
    else:
        print(f"O arquivo {arquivo2} não existe na pasta {pasta2}.")


def moveArquivos():
    pasta = '/home/user/Downloads/' # esse caminho do downlaods muda no totem tem que mudar eleeeee
    nomebase1 = 'horario'
    nomebase2 = 'calendario'

    # listar apenas arquivos na pasta
    arquivos = [arquivo for arquivo in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, arquivo))]

    # imprimir nome de cada arquivo
    for arquivo in arquivos:
        if nomebase1 in arquivo :    
            print(arquivo)
            caminho_origem = os.path.join(pasta, arquivo)
            caminho_destino = f'PDFs/{nomebase1}.pdf'
            os.rename(caminho_origem, caminho_destino)
        if nomebase2 in arquivo :    
            print(arquivo)
            caminho_origem2 = os.path.join(pasta, arquivo)
            caminho_destino2 = f'PDFs/{nomebase2}.pdf'
            os.rename(caminho_origem2, caminho_destino2)


while True:
    time.sleep(1)
    agora = datetime.datetime.now()
    hora_atual = agora.hour
    minuto_atual = agora.minute
    #colocar segundo tbm
    if hora_atual == 16 and minuto_atual == 5:
        updatePdfs()
        apagaArquivos()
        moveArquivos()
        break