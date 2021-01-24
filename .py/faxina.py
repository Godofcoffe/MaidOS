from os import scandir, chdir, remove, getlogin
from time import sleep
from shutil import rmtree


def maid(os='windows'):
    """
    Aqui a um padrão de arquivos temporarios,desde do /data da memoria interna e outros que ficam em lugares...
    inconvenientes.
    """
    usr = getlogin()

    if os == 'windows':
        c = 'c:/Windows/Temp'
        chdir(c)
        d = scandir(c)
        print(f'[ / ] Abrindo {c}')
        for pasta in d:
            if pasta.is_file():
                try:
                    remove(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} '
                          f'e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'[ + ] {pasta.name} apagada!')

            if pasta.is_dir():
                try:
                    rmtree(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} '
                          f'e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'[ + ] {pasta.name} apagado!')
        sleep(3)

        c = f'c:/Users/{usr}/AppData/Local/Temp'
        chdir(c)
        d = scandir(c)
        print(f'[ / ] Abrindo {c}')
        for pasta in d:
            if pasta.is_file():
                try:
                    remove(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'[ + ] {pasta.name} apagado!')

            if pasta.is_dir():
                print(f'abrindo {pasta.name}')
                try:
                    rmtree(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'[ + ] {pasta.name} apagado!')
        sleep(3)

        c = 'c:/Windows/Prefetch'
        chdir(c)
        d = scandir(c)
        print(f'[ / ] Abrindo {c}')
        for pasta in d:
            if pasta.is_file():
                try:
                    remove(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'[ + ] {pasta.name} apagado!')

            if pasta.is_dir():
                print(f'[ / ]abrindo {pasta.name}')
                try:
                    rmtree(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'[ + ] {pasta.name} apagado!')
    print('limpeza completa!')
    sleep(3)


print(f'{"***":/^40}')
print("""
Os Arquivos nestes diretórios seram apagados:
'c:/Windows/Temp'
'c:/Users/{usr}/AppData/Local/Temp'
'c:/Windows/Prefetch'
""")
while True:
    on = str(input('Prosseguir [s/n]: ')).strip().lower()[0]
    if on in 'sn':
        break
if on == 's':
    maid()
if on == 'n':
    print('encerrando...')
    sleep(0.5)

