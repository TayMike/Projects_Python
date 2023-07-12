import webbrowser as web
from time import sleep
import pyautogui as pg
import os
import datetime

def localizarImagem(arquivo, locacao = 0):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = pg.locateCenterOnScreen(f'{dir_path}\\data\\{arquivo}', grayscale=False, confidence=0.9)    
    pg.moveTo(location[0], location[1] + locacao)
    pg.click()

def localizarArquivo(nome, usar):
    with pg.hold('ctrl'):
        pg.press('f')
    pg.write(nome)
    if usar == True:
        pg.press('enter')
        pg.press('tab',presses=3)
        pg.press('enter')

def agendarDownload(nomeArquivo):
    pg.press('tab', presses=3)
    pg.write(f'01{mes_atual}{ano_atual}')
    pg.press('tab')
    pg.write(f'{dia_atual}{mes_atual}{ano_atual}')
    localizarImagem('Arquivo_DadosDownload.png')
    sleep(1)
    localizarImagem('Arquivo_Arquivo.png')
    sleep(1)
    localizarImagem('Arquivo_Separador.png', -50)
    pg.write(f'{nomeArquivo}')
    pg.press('tab')
    sleep(1)
    localizarImagem('Arquivo_RelatorioEmail.png')
    sleep(2)
    localizarImagem('Arquivo_Texto.png', 50)
    pg.write(f'{nomeArquivo}')
    localizarImagem('Arquivo_Compactar.png')
    sleep(2)
    pg.press(['tab','enter'])
    sleep(2)
    localizarImagem('Arquivo_OK.png')
    sleep(1)
    #pg.press('tab', presses=19)
    #pg.press('enter')

def processo(nome, imagem1, boolean, valor):
    localizarArquivo(nome, boolean)
    sleep(1)
    if valor == 1:
        pg.press('tab', presses=2)
        pg.press('enter')
        pg.press(['tab','enter'])
    elif valor == 2:
        pg.press('tab',presses=3)
        pg.press('enter')
    localizarImagem(imagem1)
    sleep(2)
    localizarImagem('Arquivo_Agendar.png')
    agendarDownload(nome)

def main():
    # Logar no forponto RUMO
    web.open(r'https://forpontoweb.rumolog.com/ForpontoWeb/Login.aspx?ReturnUrl=%2fforpontoweb%2fFormularios%2fPainelAdministracao2.aspx')
    sleep(6)
    pg.write('123456')
    pg.press(['tab','enter'])
    sleep(6)

    # Entrar na area de consultas de relatorios
    pg.press(['tab','enter','tab','enter'])
    sleep(2)
    localizarImagem('Rumo_Consultas.png')
    sleep(1)

    # Localizar o arquivo -- Solicitacoes Listar por Status -- e baixar
    processo('Solicitacoes Listar por Status','Arquivo1.png',True,0)

    # Localizar o arquivo -- lote por motivo de ocor_Ocor -- e baixar
    processo('lote por motivo de ocor_Ocor','Arquivo2.png',True,0)

    # Localizar o arquivo -- Marcacoes Analisadas -- e baixar
    processo('Marcacoes Analisadas','Arquivo3.png',False,1)

    # Localizar o arquivo -- MAQ - Lista Atividades Gestor -- e baixar
    processo('MAQ - Lista Atividades Gestor','Arquivo4.png',True,0)

    # Localizar o arquivo -- lote mot ocor rel semanal -- e baixar
    processo('lote mot ocor rel semanal','Arquivo5.png',False,2)

    # Fechar aba depois que finalizar todo o processo
    with pg.hold('ctrl'):
        pg.press('w')

# Definir as datas
dia_atual = str(datetime.datetime.now().day)
mes_atual = str(datetime.datetime.now().month)
ano_atual = str(datetime.datetime.now().year)

if len(dia_atual) == 1: dia_atual = "0" + dia_atual
if len(mes_atual) == 1: mes_atual = "0" + mes_atual

main()