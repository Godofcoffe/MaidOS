from os import scandir, remove, getlogin, system
from time import sleep
from shutil import rmtree


def maid(os='windows'):
    """
    Aqui a um padrão de arquivos temporarios,desde do /data da memoria interna e outros que ficam em lugares...
    inconvenientes.
    """
    usr = getlogin()

    if os == 'windows':
        caminho = 'c:/Windows/Temp'
        scan = None
        print(f'[ / ] Abrindo {caminho}')
        try:
            scandir(caminho)
        except PermissionError:
            print('Não tenho permissão para entrar nesta pasta...\nTente de novo como administrador.')
        else:
            scan = scandir(caminho)
        sleep(1)
        if scan is not None:
            for pasta in scan:
                if pasta.is_file():
                    try:
                        remove(caminho + '/' + pasta.name)
                    except WindowsError:
                        print(f'[ * ] Não posso apagar o arquivo {pasta.name} '
                              f'e/ou ele está sendo executado.')
                        sleep(0.5)
                    else:
                        print(f'[ + ] {pasta.name} apagada!')

                if pasta.is_dir():
                    print(f'[ / ] Removendo {pasta.name}')
                    try:
                        rmtree(caminho + '/' + pasta.name)
                    except WindowsError:
                        print(f'[ * ] Não posso apagar o arquivo {pasta.name} '
                              f'e/ou ele está sendo executado.')
                        sleep(0.5)
                    else:
                        print(f'[ + ] {pasta.name} apagado!')
        sleep(3)

        caminho2 = f'c:/Users/{usr}/AppData/Local/Temp'
        scan2 = None
        print(f'[ / ] Abrindo {caminho2}')
        try:
            scandir(caminho2)
        except PermissionError:
            print('Não tenho permissão para entrar nesta pasta...\nTente de novo como administrador.')
        else:
            scan2 = scandir(caminho2)
        sleep(1)
        if scan2 is not None:
            for pasta in scan2:
                if pasta.is_file():
                    try:
                        remove(caminho2 + '/' + pasta.name)
                    except WindowsError:
                        print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                        sleep(0.5)
                    else:
                        print(f'[ + ] {pasta.name} apagado!')

                if pasta.is_dir():
                    print(f'[ / ] Removendo {pasta.name}')
                    try:
                        rmtree(caminho2 + '/' + pasta.name)
                    except WindowsError:
                        print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                        sleep(0.5)
                    else:
                        print(f'[ + ] {pasta.name} apagado!')
        sleep(3)

        caminho3 = 'c:/Windows/Prefetch'
        scan3 = None
        print(f'[ / ] Abrindo {caminho3}')
        try:
            scandir(caminho3)
        except PermissionError:
            print('Não tenho permissão para entrar nesta pasta...\nTente de novo como administrador.')
        else:
            scan3 = scandir(caminho3)
        sleep(1)
        if scan3 is not None:
            for pasta in scan3:
                if pasta.is_file():
                    try:
                        remove(caminho3 + '/' + pasta.name)
                    except WindowsError:
                        print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                        sleep(0.5)
                    else:
                        print(f'[ + ] {pasta.name} apagado!')

                if pasta.is_dir():
                    print(f'[ / ] Removendo pasta {pasta.name}')
                    try:
                        rmtree(caminho3 + '/' + pasta.name)
                    except WindowsError:
                        print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                        sleep(0.5)
                    else:
                        print(f'[ + ] {pasta.name} apagado!')
    print('limpeza completa!')
    sleep(3)


def sfc():
    system('sfc /scannow')


def chkdsk():
    system('chkdsk')


# MENU
print(f'{"***":/^40}')
print('Oque eu posso fazer por você hoje? ')
print("""
[ 1 ] LIMPAR CACHE DE APPS E ARQUIVOS TEMPORÁRIOS
[ 2 ] ESCANEAR E REPARAR ARQUIVOS DO SISTEMA OPERACIONAL
[ 3 ] Verificação de Disco
[ 4 ] Sair
""")
while True:
    on = str(input('Opção: ')).strip()[0]
    if on in '1234':
        break
if int(on) == 1:
    print("""
Os Arquivos nestes diretórios serãm apagados:
'c:/Windows/Temp'
'c:/Users/{usr}/AppData/Local/Temp'
'c:/Windows/Prefetch'
""")
    confirm = str(input('Prosseguir [s/n]?: ')).strip().lower()[0]
    if confirm == 's':
        maid()
    if confirm == 'n':
        print('encerrando...')
        sleep(2)
elif int(on) == 2:
    sfc()
elif int(on) == 3:
    chkdsk()
elif int(on) == 4:
    print('ENCERRANDO...')
    sleep(2)
