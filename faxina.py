from os import scandir, chdir, remove
from time import sleep
from shutil import rmtree


def maid(os='windows', usr=''):
    """
    Aqui a um padrão de arquivos temporarios,desde do /data da memoria interna e outros que ficam em lugares...
    inconvenientes.
    """

    if os == 'windows':
        c = 'c:/Windows/Temp'
        chdir(c)
        d = scandir(c)
        print(f'[ / ] Abrindo {c}')
        for pasta in d:
            if pasta.is_file():
                sleep(0.2)
                try:
                    remove(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} '
                          f'e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'{pasta.name} apagada!')

            if pasta.is_dir():
                sleep(0.2)
                try:
                    rmtree(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} '
                          f'e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'[ + ] {pasta.name} apagado!')
        sleep(2)

        c = f'c:/Users/{usr}/AppData/Local/Temp'
        chdir(c)
        d = scandir(c)
        print(f'[ / ] Abrindo {c}')
        for pasta in d:
            if pasta.is_file():
                sleep(0.2)
                try:
                    remove(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'[ + ] {pasta.name} apagado!')

            if pasta.is_dir():
                print(f'abrindo {pasta.name}')
                sleep(0.2)
                try:
                    rmtree(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'[ + ] {pasta.name} apagado!')
        sleep(2)

        c = 'c:/Windows/Prefetch'
        chdir(c)
        d = scandir(c)
        print(f'[ / ] Abrindo {c}')
        for pasta in d:
            if pasta.is_file():
                sleep(0.2)
                try:
                    remove(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'[ + ] {pasta.name} apagado!')

            if pasta.is_dir():
                print(f'[ / ]abrindo {pasta.name}')
                sleep(0.2)
                try:
                    rmtree(c + '/' + pasta.name)
                except:
                    print(f'[ * ] Não posso apagar o arquivo {pasta.name} e/ou ele está sendo executado.')
                    sleep(0.5)
                else:
                    print(f'[ + ] {pasta.name} apagado!')
    print('limpeza completa!')


usuario = str(input('Seu nome de usuário: ')).strip()
maid(usr=usuario)
