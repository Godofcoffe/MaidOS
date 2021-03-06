from faxina import *
from form_text import *
from colorama import init

init()
M = Maid()
print(color_text('white', f'{"MaidOS":.^55}'))
print(f'{M.info()[0]:>55}')
print(f'Autor: {M.info()[1]}\n')
if update() != M.info()[0]:
    print(color_text('yellow', f'> Há uma nova versão disponivel <\n'.center(55)))
print(f'O que eu posso fazer por você hoje {M.usr}?')
print('Digite', color_text('white', '"?"'), 'para exibir mais informações sobre as funções.')
print(f"""
{color_text('yellow', '[ 1 ]')} Limpar cache de Apps e arquivos temporários
{color_text('yellow', '[ 2 ]')} Escanear e reparar arquivos do sistema operacional
{color_text('yellow', '[ 3 ]')} Verificação de disco
{color_text('yellow', '[ 0 ]')} Sair
""")

while True:
    print(color_text('green', 'Opção > '), end='')
    on = str(input()).strip()[0]
    if on in '0123?':
        break

system('cls')
if on == '1':
    verificarpermissao(M.diretorios, True)
    print(color_text('yellow', 'Os arquivos serão apagados nestes seguintes diretórios!:'))
    for caminho in M.dirsPermitidos:
        if tam_dir(caminho) >= 1000000000:
            print(f'{caminho} - ({tam_dir(caminho) / 1000000000:.1f})GB de espaço ocupado.')
        elif tam_dir(caminho) >= 1000000:
            print(f'{caminho} - ({tam_dir(caminho) / 1000000:.1f})MB de espaço ocupado.')
        elif tam_dir(caminho) < 1000000:
            print(f'{caminho} - ({tam_dir(caminho) / 1000:.1f})kB de espaço ocupado.')

    print(f"""
{color_text('yellow', '[ 1 ]')} Somente diretórios cache
{color_text('yellow', '[ 2 ]')} Somente diretório cache do Windows Update
{color_text('yellow', '[ 3 ]')} Somente cache DNS
{color_text('yellow', '[ 4 ]')} Limpeza completa
{color_text('yellow', '[ 0 ]')} Cancelar
    """)
    while True:
        print(color_text('green', 'Opção > '), end='')
        confirm = str(input()).strip()[0]
        if confirm in '01234':
            break

    if confirm == '1':
        M.dirsPermitidos.pop()
        M.maid()

    elif confirm == '2':
        M.winupdate()

    elif confirm == '3':
        cache_dns()

    elif confirm == '4':
        M.maid()
        M.winupdate()
        cache_dns()

    elif confirm == '0':
        print(color_text('white', 'Encerrando...'))
        sleep(2)

elif on == '2':
    sfc()

elif on == '3':
    chkdsk()

elif on == '0':
    print(color_text('white', 'ENCERRANDO...'))
    sleep(2)

elif on == '?':
    print(rf"""
        Limpar cache de apps e arquivos temporários:
            Apaga TODOS os aquivos POSSIVEIS em diretórios conhecidos que armazenam o cache de aplicações
            e arquivos usados anteriormente por aplicativos já desistalados e também incluindo o cache de
            atualizações do WindowsUpdate.
                E os diretórios são:
                    C:\Windows\Temp,
                    C:\Users\{M.usr}\AppData\Local\Temp,
                    C:\Windows\Prefetch,
                    C:\Users\{M.usr}\Recent,
                    C:\Windows\SoftwareDistribution\Download

        Escanear e reparar arquivos do sistema operacional:
            Se algumas funções do Windows não estiverem funcionando ou se o Windows falhar,
            use o Verificador de Arquivos do Sistema para examinar o Windows e restaurar os arquivos.
            
            Se você estiver executando o Windows 10, o Windows 8.1 ou o Windows 8,
            será executato primeiro a ferramenta DISM (Gerenciamento e Manutenção de Imagens de Implantação)
            
            Importante: Quando for executado esse comando,
            o DISM usa o Windows Update para fornecer os arquivos necessários para corrigir as corrupções.
            
            Já no Windows 7:
            Será usado o comando sfc /scannow para verificar todos os arquivos protegidos do sistema, 
            substituindo os arquivos corrompidos por uma cópia em cache que está localizada em uma pasta compactada
            em %WinDir%\System32\dllcache.
            O espaço reservado %WinDir% representa a pasta do sistema operacional Windows.
            Por exemplo, C:\Windows.

            Observação Não feche esta janela do Prompt de Comando até que a verificação esteja 100% concluída.
            Os resultados da verificação serão mostrados depois que esse processo for concluído.

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
