# encode utf-8
import base64
import io
import sys

PARAMETER = {'-s': '', # parâmetro para o local do arquivo a ser escrito
             '-d': b'', # parâmetro da string que armazena o que deve ser decodificado
             '-c': '', # parâmetro da string que armazena o que deve ser codificado
             '-o': ''} # parâmetro para o local onde será escrito a string codificada ou decodificada


# lê os parâmetros passados e os armazena nas devidas chaves
def set_parameter(args: list, container: dict) -> None:
    for i in range(len(args)):
        dash = args[i]
        if dash in container.keys():
            container[dash] = args[i + 1]


# função retorna os bytes codificados
def codificar(codigo: str) -> bytes:
    return base64.encodebytes(
        bytes(codigo, 'utf-8')
    )


# função que retorna os bytes decodificados
def decodificar(codigo) -> str:
    if codigo.__class__.__name__ == "str":
        codigo.replace(chr(10), '')
        codigo.replace(chr(13), '')

    if codigo.__class__.__name__ != "bytes":
        codigo = bytes(codigo, 'utf-8')


    return str(
        base64.decodebytes(codigo), 'utf-8'
    )


# salva os bytes do parâmetro "codigo" para o arquivo do parâmetro "local" que é o lugar do arquivo
def arquivar(local, codigo) -> None:
    file = io.open(local, "wb+")
    file.write(codigo)
    print("escrito")
    file.close()


# lê a primeiro linha do arquivo "local" e retorna o que encontrou supondo que seja algo a ser utilizado
def ler_de_arquivo(local: str) -> bytes:
    file = io.open(local, "rb+")
    codigo = file.readline()
    return codigo


def dash() -> None:
    if PARAMETER['-s'] == '':
        if PARAMETER['-o'] == '':
            if PARAMETER['-c'] == '':
                print(decodificar(PARAMETER['-d']))
            else:
                print(
                    str(codificar(PARAMETER['-c']), 'utf8')
                )
        else:
            if PARAMETER['-c'] == '':
                print(decodificar(ler_de_arquivo(PARAMETER['-o'])))
            else:
                print(codificar(ler_de_arquivo(PARAMETER['-o'])))
    else:
        if PARAMETER['-o'] == '':
            if PARAMETER['-c'] == '':
                arquivar(PARAMETER['-s'], decodificar(PARAMETER['-d']))
            else:
                arquivar(PARAMETER['-s'], codificar(PARAMETER['c']))
        else:
            if PARAMETER['-c'] == '':
                arquivar(PARAMETER['-s'], decodificar(ler_de_arquivo(PARAMETER['-o'])))
            else:
                arquivar(PARAMETER['-s'], codificar(ler_de_arquivo(PARAMETER['-o'])))

def run(args: list) -> None:
    if len(args) == 0 or len(args) == 1:
        print(args)
        input("nenhum parâmetro dado")  # no given parameter
        sys.exit(0)
    elif args[1] == 'help' or args[1] == 'ajuda' or args[1] == 'help()' or args[1] == 'ajuda()':
        print("use -s para salvar no destino")
        print("use -o para abrir o arquivo")
        print("use -c para encriptar")
        print("use -d para decodificar")
        print(args)
        sys.exit(0)
    else:
        # this will remove the archive name from args
        args.reverse()
        args.pop()
        args.reverse()

        set_parameter(args, PARAMETER)
        dash()

def prepare() -> None:
    open_from = ""
    save_in = ""
    deal_with = input("""Obtenha o resultado em base 64 usando -c [caracteres]
Obtenha o resultado em ascii usando -d [caracteres] """)
    print("")
    _dash = deal_with[:2]
    code = deal_with[3:]
    files = input("""Use -o [arquivo] para ler do arquivo
Use -s [arquivo] para salvar no arquivo
Aperte Enter ser escrito no console """)
    set_parameter([_dash, code], PARAMETER)
    dash()


# prepare()
# run(sys.argv)