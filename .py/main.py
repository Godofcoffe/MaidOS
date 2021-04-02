from faxina import *

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

    print("""
    [ 1 ] Somente diretórios cache
    [ 2 ] Somente diretório cache do Windows Update
    [ 3 ] Somente cache DNS
    [ 4 ] Limpeza completa
    [ 0 ] Cancelar
    """)
    while True:
        confirm = str(input('Opção > ')).strip()[0]
        if '12340' in confirm:
            break

    if confirm == '1':
        Maid().maid()

    elif confirm == '2':
        Maid().winupdate()

    elif confirm == '3':
        Maid().cacheDNS()

    elif confirm == '4':
        Maid().diretorios.append(r'C:\Windows\SoftwareDistribution\Download')
        Maid().maid()
        Maid().winupdate()
        Maid().cacheDNS()

    elif confirm == '0':
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
    print(rf"""
        Limpar cache de apps e arquivos temporários:
            Apaga TODOS os aquivos POSSIVEIS em diretórios conhecidos que armazenam o cache de aplicações
            e arquivos usados anteriormente por aplicativos já desistalados e também incluindo o cache de
            atualizações do WindowsUpdate.
                E os diretórios são:
                    C:\Windows\Temp,
                    C:\Users\{Maid().usr}\AppData\Local\Temp,
                    C:\Windows\Prefetch,
                    C:\Users\{Maid().usr}\Recent,
                    C:\Windows\SoftwareDistribution\Download

        Escanear e reparar arquivos do sistema operacional:
            Verifica a integridade de todos os arquivos do sistema protegidos
            e repara os arquivos com problemas quando possível.

        Verificação de disco:
             Executa o comando nativo do windows CHKDSK, ele verifica a integridade do sistema de arquivos e
             metadados do sistema operacional em um volume de disco. Alguns desses erros podem ser entradas
             corrompidas na tabela mestre de arquivos (MFT), descritores de segurança incorretos associados
             a arquivos ou até informações de tamanho de arquivo ou carimbo de hora desalinhados sobre arquivos
             individuas.
             
             Usos:
                * Chkdsk pode digitalizar, opcionalmente, todos os setores em um volume de disco em busca de
                setores defeituosos. Os setores defeituoso podem apresentar-se de 2 formas: soft bad sectors,
                que podem ocorrer quando os dados são mal escritos, e os hard bad sectors, quando há danos
                fisico no disco.
                    
                A ferramenta tenta corrigir separando os soft bad sectors, e marcando os hard bad sectors
                para eles não serem usados.
                
                * Em casos de problemas com aplicativos não carregando ou falhando.
            
            Recomendações:  
                * Executar-lo a cada poucos meses como parte da manutenção de rotina.
                
                * Também pode considerar usar-lo sempre quando o Windows é desligado
                de maneira anormal (Queda de energia, Falha no sistema).
    """)
    input('Pressione ENTER para sair...')
