from faxina import Maid
from os import system
from time import sleep

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
