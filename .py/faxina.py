from os import scandir, remove, getlogin, system, path
from time import sleep
from shutil import rmtree


class Maid:
    def __init__(self):
        self.usr = getlogin()
        self.caminho = 'c:/Windows/Temp'
        self.caminho2 = f'c:/Users/{self.usr}/AppData/Local/Temp'
        self.caminho3 = 'c:/Windows/Prefetch'
        self.dir1 = path.getsize(self.caminho)
        self.dir2 = path.getsize(self.caminho2)
        self.dir3 = path.getsize(self.caminho3)

    def maid(self, os='windows'):
        """
        Aqui a um padrão de arquivos temporarios,desde do /data da memoria interna e outros que ficam em lugares...
        inconvenientes.
        """
        cont = 0
        if os == 'windows':
            scan = None
            print(f'[ / ] Abrindo {self.caminho}')
            try:
                scandir(self.caminho)
            except PermissionError:
                print('Não tenho permissão para entrar nesta pasta...\nTente de novo como administrador.')
            else:
                scan = scandir(self.caminho)
            sleep(1)
            if scan is not None:
                for pasta in scan:
                    if pasta.is_file():
                        try:
                            remove(self.caminho + '/' + pasta.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {pasta.name} '
                                  f'e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {pasta.name} apagada!')
                            cont += 1

                    if pasta.is_dir():
                        print(f'[ / ] Removendo {pasta.name}')
                        try:
                            rmtree(self.caminho + '/' + pasta.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {pasta.name} '
                                  f'e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {pasta.name} apagado!')
                            cont += 1
            sleep(3)

            scan2 = None
            print(f'[ / ] Abrindo {self.caminho2}')
            try:
                scandir(self.caminho2)
            except PermissionError:
                print('Não tenho permissão para entrar nesta pasta...\nTente de novo como administrador.')
            else:
                scan2 = scandir(self.caminho2)
            sleep(1)
            if scan2 is not None:
                for pasta in scan2:
                    if pasta.is_file():
                        try:
                            remove(self.caminho2 + '/' + pasta.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {pasta.name} apagado!')
                            cont += 1

                    if pasta.is_dir():
                        print(f'[ / ] Removendo {pasta.name}')
                        try:
                            rmtree(self.caminho2 + '/' + pasta.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {pasta.name} apagado!')
                            cont += 1
            sleep(3)

            scan3 = None
            print(f'[ / ] Abrindo {self.caminho3}')
            try:
                scandir(self.caminho3)
            except PermissionError:
                print('Não tenho permissão para entrar nesta pasta...\nTente de novo como administrador.')
            else:
                scan3 = scandir(self.caminho3)
            sleep(1)
            if scan3 is not None:
                for pasta in scan3:
                    if pasta.is_file():
                        try:
                            remove(self.caminho3 + '/' + pasta.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {pasta.name} apagado!')
                            cont += 1

                    if pasta.is_dir():
                        print(f'[ / ] Removendo pasta {pasta.name}')
                        try:
                            rmtree(self.caminho3 + '/' + pasta.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {pasta.name} apagado!')
                            cont += 1
        print('limpeza completa!')
        print(f'# {cont} arquivos e pastas apagados.')
        print(f'# {(self.dir1 + self.dir2 + self.dir3) / 1000000:.2f}MB limpos do sistema.')
        sleep(3)

    def sfc(self):
        system('sfc /scannow')

    def chkdsk(self):
        system('chkdsk')

    def defrag(self):
        system('defrag /C /H /D /U')


# MENU
print(f'{"***":/^40}')
print(f'Oque eu posso fazer por você hoje {Maid().usr}?')
print("""
[ 1 ] LIMPAR CACHE DE APPS E ARQUIVOS TEMPORÁRIOS
[ 2 ] ESCANEAR E REPARAR ARQUIVOS DO SISTEMA OPERACIONAL
[ 3 ] VERIFICAÇÃO DE DISCO
[ 4 ] DESFRAGMENTAR DISCO
[ 5 ] SAIR
""")

while True:
    on = str(input('Opção: ')).strip()[0]
    if on in '12345':
        break

if on == '1':
    print(f"""
Os Arquivos nestes diretórios serãm apagados:
'c:/Windows/Temp' - ({Maid().dir1 / 1000000:.2f})MB de espaço ocupado.
'c:/Users/{Maid().usr}/AppData/Local/Temp' - ({Maid().dir2 / 1000000:.2f})MB de espaço ocupado.
'c:/Windows/Prefetch' - ({Maid().dir3 / 1000000:.2f})MB de espaço ocupado.
""")
    confirm = str(input('Prosseguir [s/n]?: ')).strip().lower()[0]
    if confirm == 's':
        Maid().maid()
    if confirm == 'n':
        print('encerrando...')
        sleep(2)

elif on == '2':
    Maid().sfc()

elif on == '3':
    Maid().chkdsk()

elif on == '4':
    Maid().defrag()
    print('finalizado')

elif on == '5':
    print('ENCERRANDO...')
    sleep(2)
