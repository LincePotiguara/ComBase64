# encode utf-8
#from sys import argv as cmd_arguments

from base64 import decodebytes, encodebytes
import combase

# isso é a versão em 'bytes' produzida com a biblioteca base64 de :lorem_string:
# lorem_bytes = b'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4g\nRHVpcyBtYXNzYSBkaWFtLCBpbnRlcmR1bSBlZ2V0IHF1YW0gYSwgcHJldGl1bSBjb21tb2RvIGRv\nbG9yLiBNYWVjZW5hcyBuZWMgY29uc2VxdWF0IHNhcGllbiwgZXUgZGlnbmlzc2ltIG5pc2wuIFF1\naXNxdWUgY3Vyc3VzIHZlbmVuYXRpcyBsb3JlbSBhdCBsYW9yZWV0LiBQZWxsZW50ZXNxdWUgc2Vk\nIGlhY3VsaXMgbGFjdXMsIGEgdnVscHV0YXRlIG1pLiBDdXJhYml0dXIgY29udmFsbGlzIGVyYXQg\nbGFvcmVldCwgc3VzY2lwaXQgYW50ZSB1dCwgY29udmFsbGlzIGVyb3MuIE51bmMgaW4gbWF1cmlz\nIGZlbGlzLiBWZXN0aWJ1bHVtIHBoYXJldHJhIGF1Y3RvciB0aW5jaWR1bnQuIERvbmVjIGZldWdp\nYXQgbmVjIHB1cnVzIGEgbG9ib3J0aXMuIFBlbGxlbnRlc3F1ZSBuZWMgbG9yZW0gdmVsIGFyY3Ug\ndnVscHV0YXRlIGVsZWlmZW5kIG5vbiBldCBkb2xvci4=\n'
# lorem_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis massa diam, interdum eget quam a, pretium commodo dolor. Maecenas nec consequat sapien, eu dignissim nisl. Quisque cursus venenatis lorem at laoreet. Pellentesque sed iaculis lacus, a vulputate mi. Curabitur convallis erat laoreet, suscipit ante ut, convallis eros. Nunc in mauris felis. Vestibulum pharetra auctor tincidunt. Donec feugiat nec purus a lobortis. Pellentesque nec lorem vel arcu vulputate eleifend non et dolor."
lorem_bytes = b'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4g\nRHVpcw==\n'
lorem_string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis'


def paragrafo(par: bytes) -> bool:
    # _par = b'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4g\nRHVpcyBtYXNzYSBkaWFtLCBpbnRlcmR1bSBlZ2V0IHF1YW0gYSwgcHJldGl1bSBjb21tb2RvIGRv\nbG9yLiBNYWVjZW5hcyBuZWMgY29uc2VxdWF0IHNhcGllbiwgZXUgZGlnbmlzc2ltIG5pc2wuIFF1\naXNxdWUgY3Vyc3VzIHZlbmVuYXRpcyBsb3JlbSBhdCBsYW9yZWV0LiBQZWxsZW50ZXNxdWUgc2Vk\nIGlhY3VsaXMgbGFjdXMsIGEgdnVscHV0YXRlIG1pLiBDdXJhYml0dXIgY29udmFsbGlzIGVyYXQg\nbGFvcmVldCwgc3VzY2lwaXQgYW50ZSB1dCwgY29udmFsbGlzIGVyb3MuIE51bmMgaW4gbWF1cmlz\nIGZlbGlzLiBWZXN0aWJ1bHVtIHBoYXJldHJhIGF1Y3RvciB0aW5jaWR1bnQuIERvbmVjIGZldWdp\nYXQgbmVjIHB1cnVzIGEgbG9ib3J0aXMuIFBlbGxlbnRlc3F1ZSBuZWMgbG9yZW0gdmVsIGFyY3Ug\ndnVscHV0YXRlIGVsZWlmZW5kIG5vbiBldCBkb2xvci4=\n'
    _par = lorem_bytes
    par = encodebytes(par)
    return par == _par


def test_internal() -> None:
    """"Por motivos de compatibilidade há uma quebra de linha para que cada
    linha não exceda 76 caracteres de comprimento, o 77 é o \n"""
    par = lorem_string
    # par = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis massa diam, interdum eget quam a, pretium commodo dolor. Maecenas nec consequat sapien, eu dignissim nisl. Quisque cursus venenatis lorem at laoreet. Pellentesque sed iaculis lacus, a vulputate mi. Curabitur convallis erat laoreet, suscipit ante ut, convallis eros. Nunc in mauris felis. Vestibulum pharetra auctor tincidunt. Donec feugiat nec purus a lobortis. Pellentesque nec lorem vel arcu vulputate eleifend non et dolor."
    if (chr(10) in par):
        print("It has a \\n")
    else:
        pass
        # print("It does not have a \\n")
    par = bytes(par, 'ascii')
    result = paragrafo(par)
    if result:
        print("Test_Internal pass")
    else:
        print("It is a trouble in Test_Internal")


def test_codificar() -> None:
    expected = lorem_bytes
    result = combase.codificar(lorem_string)
    if (expected == result):
        print("Codificar pass")
    else:
        print("Codificar did not pass")


def test_decodificar() -> None:
    expected = lorem_string
    result = combase.decodificar(lorem_bytes)
    if (expected == result):
        print("Decodificar pass")
    else:
        print("Decodificar did not pass")


# TODO testar: arquivar()
# TODO testar: dash()
# TODO testar: ler_de_arquivo()
# TODO testar: set_parameter()

# def test_dash(par: list) -> None:
#     """it need to be in order:
#     0 -> -s
#     1 -> -d
#     2 -> -c
#     3 -> -d"""
#     lista = combase.PARAMETER
#     for arg in lista:
#         if arg.__class__ == bytes:
#             if arg == '-d':
#                 lista[arg] = par[1]
#         elif arg.__class__ == str:
#             if arg == '-s':
#                 lista[arg] = par[0]
#             elif arg == '-c':
#                 lista[arg] = par[2]
#             elif arg == '-o':
#                 lista[arg] = par[3]
#         else:
#             print("argument in PARAMETER is not str nor bytes")

def test_set_par():
    args = [lorem_string, lorem_bytes, '', '']
    argv = "-s__{}__-d__{}__-c__{}__-o__{}".format(args[0], args[1], args[2], args[3])
    argv = argv.split("__")
    # isso muda o caractere \n para um \\n por transformá-lo numa string
    # portanto isso deve ser corrigido
    argv[3] = lorem_bytes

    _par = combase.PARAMETER
    combase.set_parameter(argv, _par)
    compare = lambda a, b: a == b
    s = compare(_par["-s"], args[0])
    d = compare(_par["-d"], args[1])
    c = compare(_par["-c"], args[2])
    o = compare(_par["-o"], args[3])

    if compare(_par["-s"], args[0]) and \
            compare(_par["-d"], args[1]) and \
            compare(_par["-c"], args[2]) and \
            compare(_par["-o"], args[3]):
        print("Set_Parameter pass")
    else:
        print("Set_Parameter FAIL")
        print("with -s {} {}".format(s, _par["-s"]))
        print("with -d {} {}".format(d, _par["-d"]))
        print("with -c {} {}".format(c, _par["-c"]))
        print("with -o {} {}".format(o, _par["-o"]))



test_set_par()
test_internal()
test_codificar()
test_decodificar()

