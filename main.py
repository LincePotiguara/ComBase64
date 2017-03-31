# encode utf-8
import base64
import io
import sys

PARAMETER = {'-s': '',  # parâmetro para o local do arquivo a ser escrito
             '-d': '',  # parâmetro da string que armazena o que deve ser decodificado
             '-c': '',  # parâmetro da string que armazena o que deve ser codificado
             '-o': ''}  # parâmetro para o local onde será escrito a string codificada ou decodificada


# lê os parâmetros passados e os armazena nas devidas chaves
def set_parameter():
    for i in range(len(sys.argv)):
        dash = sys.argv[i]
        if dash in PARAMETER.keys():
            PARAMETER[dash] = sys.argv[i + 1]

# isso remove o \n no final de um texto
def remove(pos, total):
    if total[len(total)-2:len(total)] == '\n':
        total = total[:len(total) - 2]


# função retorna os bytes codificados
def codificar(codigo):
    temp = bytes(codigo, 'utf8')
    return base64.encodebytes(temp)


# função que retorna os bytes decodificados
def decodificar(codigo):
    ss = codigo[len(codigo)-5:len(codigo)]
    if codigo.__class__.__name__ == "str":
        remove(ss, codigo)
        # ss tem função elucidativa quando em debbuger
        print(codigo[len(codigo)-5:len(codigo)])
    if codigo.__class__.__name__!= "bytes":
        codigo = bytes(codigo, 'utf8')

    return base64.decodebytes(codigo)


# salva os bytes do parâmetro "codigo" para o arquivo do parâmetro "local" que é o lugar do arquivo
def arquivar(local, codigo):
    file = io.open(local, "wb+")
    file.write(codigo)
    print("escrito")
    file.close()


# lê a primeiro linha do arquivo "local" e retorna o que encontrou supondo que seja algo a ser utilizado
def ler_de_arquivo(local):
    file = io.open(local, "rb+")
    codigo = file.readline()
    return codigo


def main():
    if PARAMETER['-s'] == '':
        if PARAMETER['-o'] == '':
            if PARAMETER['-c'] == '':
                print(decodificar(PARAMETER['-d']))
            else:
                print(codificar(PARAMETER['-c']))
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


if __name__ == "__main__":
    if len(sys.argv) == 0 or len(sys.argv) == 1:
        print(sys.argv)
        sys.exit(0)
    elif sys.argv[1] == 'help' or sys.argv[1] == 'ajuda' or sys.argv[1] == 'help()' or sys.argv[1] == 'ajuda()':
        print("use -s para salvar no destino")
        print("use -o para abrir o arquivo")
        print("use -c para encriptar")
        print("use -d para decodificar")
        print(sys.argv)
        sys.exit(0)
    else:
        set_parameter()

        main()
