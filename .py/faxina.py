from os import scandir, remove, getlogin, system, path
from time import sleep
from shutil import rmtree
from requests import get


class Maid:
    def __init__(self):
        vs = Maid().versao()
        self.response = vs.text
        index = self.response.find('tag_name')
        versaoAtual = self.response[index:index + 22]
        with open('.version', 'w+') as arqv:
            arqv.write(versaoAtual)
        self.usr = getlogin()
        self.diretorios = ['c:/Windows/Temp', f'c:/Users/{self.usr}/AppData/Local/Temp', 'c:/Windows/Prefetch']

    def maid(self, os='windows'):
        cont = 0
        if os == 'windows':
            scan = None
            print(f'[ / ] Abrindo {self.diretorios[0]}')
            try:
                scandir(self.diretorios[0])
            except PermissionError:
                print('Não tenho permissão para entrar nesta pasta...\nTente de novo como administrador.')
            else:
                scan = scandir(self.diretorios[0])
            sleep(1)
            if scan is not None:
                for arq in scan:
                    if arq.is_file():
                        try:
                            remove(self.diretorios[0] + '/' + arq.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {arq.name} '
                                  f'e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {arq.name} apagada!')
                            cont += 1

                    if arq.is_dir():
                        print(f'[ / ] Removendo {arq.name}')
                        try:
                            rmtree(self.diretorios[0] + '/' + arq.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {arq.name} '
                                  f'e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {arq.name} apagado!')
                            cont += 1
            sleep(3)

            scan2 = None
            print(f'[ / ] Abrindo {self.diretorios[1]}')
            try:
                scandir(self.diretorios[1])
            except PermissionError:
                print('Não tenho permissão para entrar nesta pasta...\nTente de novo como administrador.')
            else:
                scan2 = scandir(self.diretorios[1])
            sleep(1)
            if scan2 is not None:
                for arq in scan2:
                    if arq.is_file():
                        try:
                            remove(self.diretorios[1] + '/' + arq.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {arq.name} e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {arq.name} apagado!')
                            cont += 1

                    if arq.is_dir():
                        print(f'[ / ] Removendo {arq.name}')
                        try:
                            rmtree(self.diretorios[1] + '/' + arq.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {arq.name} e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {arq.name} apagado!')
                            cont += 1
            sleep(3)

            scan3 = None
            print(f'[ / ] Abrindo {self.diretorios[2]}')
            try:
                scandir(self.diretorios[2])
            except PermissionError:
                print('Não tenho permissão para entrar nesta pasta...\nTente de novo como administrador.')
            else:
                scan3 = scandir(self.diretorios[2])
            sleep(1)
            if scan3 is not None:
                for arq in scan3:
                    if arq.is_file():
                        try:
                            remove(self.diretorios[2] + '/' + arq.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {arq.name} e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {arq.name} apagado!')
                            cont += 1

                    if arq.is_dir():
                        print(f'[ / ] Removendo arq {arq.name}')
                        try:
                            rmtree(self.diretorios[2] + '/' + arq.name)
                        except WindowsError:
                            print(f'[ * ] Não posso apagar o arquivo {arq.name} e/ou ele está sendo executado.')
                            sleep(1)
                        else:
                            print(f'[ + ] {arq.name} apagado!')
                            cont += 1
        print('limpeza completa!')
        print(f'# {cont} arquivos e pastas apagados.')
        sleep(3)

    def tamDir(self, diretorio):
        temp = 0
        with scandir(diretorio) as d:
            for arq in d:
                temp += path.getsize(arq)
        return temp

    def versao(self):
        return get('https://api.github.com/repos/Godofcoffe/MaidOS/releases/latest')

    def sfc(self):
        system('sfc /scannow')

    def chkdsk(self):
        system('chkdsk /R /V')

    def defrag(self):
        system('defrag /C /H /D /U')


# MENU
print(f'{"***":/^60}')
print(f'Oque eu posso fazer por você hoje {Maid().usr}?')
print('Digite "?" para exibir mais informações sobre as funções e o programa.')
print("""
[ 1 ] LIMPAR CACHE DE APPS E ARQUIVOS TEMPORÁRIOS
[ 2 ] ESCANEAR E REPARAR ARQUIVOS DO SISTEMA OPERACIONAL
[ 3 ] VERIFICAÇÃO DE DISCO
[ 4 ] DESFRAGMENTAR DISCO
[ 5 ] SAIR
""")

while True:
    on = str(input('Opção: ')).strip()[0]
    if on in '12345?':
        break

if on == '1':
    tamDir1 = Maid().tamDir(Maid().diretorios[0])
    tamDir2 = Maid().tamDir(Maid().diretorios[1])
    tamDir3 = Maid().tamDir(Maid().diretorios[2])
    print(f"""
Os Arquivos nestes diretórios serãm apagados:
'c:/Windows/Temp' - ({tamDir1 / 1000000:.1f})MB de espaço ocupado.
'c:/Users/{Maid().usr}/AppData/Local/Temp' - ({tamDir2 / 1000000:.1f})MB de espaço ocupado.
'c:/Windows/Prefetch' - ({tamDir3 / 1000000:.1f})MB de espaço ocupado.
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
elif on == '?':
    resp = Maid().response
    with open('.version', 'r') as arquivo:
        index2 = resp.find('tag_name')
        if arquivo.read() != resp[index2:index2 + 22]:
            print('A uma nova versão disponivel.')

    print(f"""
    Limpar cache de apps e arquivos temporarios:
        Apaga TODOS os aquivos POSSIVEIS em diretórios conhecidos que armazenam o cache de aplicações
        e arquivos usados anteriormente por aplicativos já desistalados.

    Escanear e reparar arquivos do sistema operacional:
        Verifica a integridade de todos os arquivos do sistema protegidos
        e repara os arquivos com problemas quando possível.

    Verificação de disco:
         Localiza setores inválidos e recupera informações legíveis.

    Desfragmentar disco:
        Executa a operação na prioridade normal e executa a desfragmentação tradicional.
        Em um volume em camadas, a desfragmentação tradicional é executada somente na camada de Capacidade.
        (Em cada volume, executa apenas as operações preferenciais da lista de operações fornecida.)
""")
