from os import scandir, remove, getlogin, system, path
from subprocess import run
from ctypes import windll
from sys import argv, executable
from platform import platform
from time import sleep
from shutil import rmtree
from requests import get
from form_text import *


def verificarpermissao(list_dir, verbose=False):
    aceitos = []
    for diretorio in list_dir:
        try:
            scandir(diretorio)
        except PermissionError:
            if verbose:
                print(color_text('red', f'Não tenho permissão para entrar nesta pasta...\n{diretorio}\n'
                                        f'Tente de novo como administrador.\n'))
        else:
            aceitos.append(diretorio)
    return aceitos


def update():
    r = get('https://api.github.com/repos/Godofcoffe/MaidOS/releases/latest')
    release = r.json()['tag_name']
    return release


def admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False


def sfc():
    if admin():
        if 'Windows-10' or 'Windows-8' in platform()[:10]:
            try:
                print(color_text('green', 'Executando DISM.EXE:'))
                sleep(1)
                saida = run(['DISM.exe', '/Online', '/Cleanup-image', '/Restorehealth'],
                            shell=True, capture_output=True, text=True)
            except WindowsError as error:
                print(color_text('red', f'Ocorreu um erro inesperado no processo DISM.EXE: {error}'))
            else:
                print(saida.stdout)
                try:
                    print(color_text('green', 'Executando sfc:'))
                    sleep(1)
                    saida = run(['sfc', '/scannow'], shell=True, capture_output=True, text=True)
                except WindowsError as error:
                    print(color_text('red', f'Ocorreu um erro inesperado no processo SFC: {error}'))
                else:
                    print(saida.stdout)
        else:
            sleep(1)
            try:
                print(color_text('green', 'Executando sfc:'))
                sleep(1)
                saida = run(['sfc', '/scannow'], shell=True, capture_output=True, text=True)
            except WindowsError as error:
                print(color_text('red', f'Ocorreu um erro inesperado no processo SFC: {error}'))
    else:
        windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv), None, 1)


def tam_dir(diretorio):
    temp = 0
    try:
        with scandir(diretorio) as d:
            for arq in d:
                temp += path.getsize(arq)
    except WindowsError:
        print(color_text('red', f'Não pude verificar o espaço de {diretorio}'))
    else:
        return temp


def chkdsk():
    if admin():
        sleep(1)
        try:
            system('chkdsk /F /R /V')
        except WindowsError as error:
            print(color_text('red', f'Ocorreu um erro inesperado no chkdsk: {error}'))
    else:
        windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv), None, 1)


def cache_dns():
    system('cls')
    system('ipconfig /flushdns')
    sleep(4)


class Maid:
    def __init__(self):
        self.__versaoAtual = 'v1.3.0'
        self.__autor = 'Godofcoffe'
        self.usr = getlogin()
        self.diretorios = [r'c:\Windows\Temp',
                           rf'C:\Users\{self.usr}\AppData\Local\Temp',
                           r'C:\Windows\Prefetch',
                           rf'C:\Users\{self.usr}\Recent',
                           rf'C:\Users\{self.usr}\AppData\Local\Google\Chrome\User Data\Default\Cache',
                           r'C:\Windows\SoftwareDistribution\Download']
        self.tamTotal = 0
        self.dirsPermitidos = verificarpermissao(self.diretorios)
        self.carregar_tamanho()

    def info(self):
        return self.__versaoAtual, self.__autor

    def carregar_tamanho(self):
        for d in self.dirsPermitidos:
            self.tamTotal += tam_dir(d)

    def maid(self):
        cont = 0
        sleep(4)
        for diretorio in self.dirsPermitidos:
            scan = scandir(diretorio)
            system('cls')
            print(f'[ / ] Abrindo {diretorio}')
            sleep(2)
            for arq in scan:
                if arq.is_file():
                    try:
                        remove(rf'{diretorio}\{arq.name}')
                    except WindowsError:
                        print(f'[ {color_text("red", "*")} ] ',
                              color_text('yellow', f'Não posso apagar o arquivo {arq.name} '
                                                   f'e/ou ela está sendo executada.'))
                        sleep(1)
                    else:
                        print(f'[ {color_text("green", "+")} ] ',
                              f'{arq.name} apagado!')
                        cont += 1

                elif arq.is_dir():
                    try:
                        rmtree(rf'{diretorio}\{arq.name}')
                    except WindowsError:
                        print(f'[ {color_text("red", "*")} ] ',
                              color_text('yellow', f'Não posso apagar a pasta {arq.name} '
                                                   f'e/ou ela está sendo executada.'))
                        sleep(1)
                    else:
                        print(f'[ {color_text("green", "+")} ] ',
                              f'{arq.name} apagada!')
                        cont += 1
            scan.close()

        system('cls')
        print('limpeza completa!')
        print(f'# {cont} arquivos e/ou pastas apagados.')
        print(f'# {self.tamTotal / 1000000:.2f}MB de memória limpa.')
        sleep(5)

    def winupdate(self):
        system('cls')
        if verificarpermissao([r'C:\Windows\SoftwareDistribution\Download'], True):
            sleep(2)
            self.dirsPermitidos = [r'C:\Windows\SoftwareDistribution\Download']
            self.carregar_tamanho()
            system('net stop wuauserv')  # para o processo de atualizações para limpeza do WinUpdate
            self.maid()
            system('net start wuauserv')  # inicia o processo de atualizações
