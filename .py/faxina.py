from os import scandir, remove, getlogin, system, path
from time import sleep
from shutil import rmtree
from requests import get


class Maid:
    def __init__(self):
        self.__versaoAtual = 'v1.2.0'
        self.__autor = 'Godofcoffe'
        self.usr = getlogin()
        self.diretorios = ['c:/Windows/Temp',
                           f'c:/Users/{self.usr}/AppData/Local/Temp',
                           'c:/Windows/Prefetch',
                           f'c:/Users/{self.usr}/Recent',
                           'c:/Windows/SoftwareDistribution/Download']
        self.tamTotal = 0
        self.dirsPermitidos = self.verificarpermissao(self.diretorios)
        self.carregarTamanho()

    def info(self):
        return self.__versaoAtual, self.__autor

    def upgrade(self):
        r = get('https://api.github.com/repos/Godofcoffe/MaidOS/releases/latest')
        release = r.json()['tag_name']
        return release

    def carregarTamanho(self):
        for d in self.dirsPermitidos:
            self.tamTotal += self.tamDir(d)

    def maid(self, os='windows'):
        cont = 0
        if os == 'windows':
            system('net stop wuauserv')  # para o processo de atualizações para limpeza do WinUpdate
            sleep(4)
            for diretorio in self.dirsPermitidos:
                scan = scandir(diretorio)
                system('cls')
                print(f'[ / ] Abrindo {diretorio}')
                sleep(2)
                for arq in scan:
                    if arq.is_file():
                        try:
                            remove(diretorio + '/' + arq.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {arq.name} '
                                  f'e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {arq.name} apagado!')
                            cont += 1
                            sleep(0.2)

                    elif arq.is_dir():
                        print(f'[ / ] Removendo {arq.name}')
                        try:
                            rmtree(diretorio + '/' + arq.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar a pasta {arq.name} '
                                  f'e/ou ela está sendo executada.')
                            sleep(1)
                        else:
                            print(f'[ + ] {arq.name} apagada!')
                            cont += 1
                            sleep(0.2)
        sleep(3)

        system('cls')
        self.cacheDNS()
        sleep(4)

        system('cls')
        print('limpeza completa!')
        print(f'# {cont} arquivos e/ou pastas apagados.')
        print(f'# {self.tamTotal / 1000000:.2f}MB de memória limpa.')
        system('net start wuauserv')  # inicia o processo de atualizações
        sleep(5)

    def verificarpermissao(self, list_dir, verbose=False):
        aceitos = []
        for diretorio in list_dir:
            try:
                scandir(diretorio)
            except PermissionError:
                if verbose:
                    print(f'Não tenho permissão para entrar nesta pasta...\n{diretorio}\n'
                          f'Tente de novo como administrador.\n')
            else:
                aceitos.append(diretorio)
        return aceitos

    def tamDir(self, diretorio):
        temp = 0
        try:
            with scandir(diretorio) as d:
                for arq in d:
                    temp += path.getsize(arq)
        except WindowsError:
            print(f'Não pude verificar o espaço de {diretorio}')
        else:
            return temp

    def sfc(self):
        system('sfc /scannow')

    def chkdsk(self):
        system('chkdsk /R /V')

    def cacheDNS(self):
        system('ipconfig /flushdns')


# MENU
print(f'{"MaidOS":.^55}')
print(f'{Maid().info()[0]:>55}')
print(f'Autor: {Maid().info()[1]}\n')
if Maid().upgrade() != Maid().info()[0]:
    print(f'> Há uma nova versão disponivel <\n'.center(55))
print(f'Oque eu posso fazer por você hoje {Maid().usr}?')
print('Digite "?" para exibir mais informações sobre as funções.')
print("""
[ 1 ] Limpar cache de Apps e arquivos temporarios
[ 2 ] Escanear e reparar arquivos do sistema operacional
[ 3 ] Verificação de disco
[ 0 ] Sair
""")

while True:
    on = str(input('Opção > ')).strip()[0]
    if on in '0123?':
        break

system('cls')
if on == '1':
    Maid().verificarpermissao(Maid().diretorios, True)
    print('Os arquivos serão apagados nestes seguintes diretórios:')
    for caminho in Maid().dirsPermitidos:
        if Maid().tamDir(caminho) >= 1000000000:
            print(f'{caminho} - ({Maid().tamDir(caminho) / 1000000000:.1f})GB de espaço ocupado.')
        elif Maid().tamDir(caminho) >= 1000000:
            print(f'{caminho} - ({Maid().tamDir(caminho) / 1000000:.1f})MB de espaço ocupado.')
        elif Maid().tamDir(caminho) < 1000000:
            print(f'{caminho} - ({Maid().tamDir(caminho) / 1000:.1f})kB de espaço ocupado.')

    confirm = str(input('Prosseguir [s/n]?: ')).strip().lower()[0]
    if confirm == 's':
        Maid().maid()

    elif confirm == 'n':
        print('encerrando...')
        sleep(2)

elif on == '2':
    Maid().sfc()

elif on == '3':
    Maid().chkdsk()

elif on == '0':
    print('ENCERRANDO...')
    sleep(2)

elif on == '?':
    print(f"""
        Limpar cache de apps e arquivos temporários:
            Apaga TODOS os aquivos POSSIVEIS em diretórios conhecidos que armazenam o cache de aplicações
            e arquivos usados anteriormente por aplicativos já desistalados e também incluindo o cache de
            atualizações do WindowsUpdate.
                E os diretórios são:
                    c:/Windows/Temp,
                    c:/Users/{Maid().usr}/AppData/Local/Temp,
                    c:/Windows/Prefetch,
                    c:/Users/{Maid().usr}/Recent,
                    c:/Windows/SoftwareDistribution/Download
    
        Escanear e reparar arquivos do sistema operacional:
            Verifica a integridade de todos os arquivos do sistema protegidos
            e repara os arquivos com problemas quando possível.
    
        Verificação de disco:
             Localiza setores inválidos e recupera informações legíveis.
    """)
    input('Pressione ENTER para sair...')
