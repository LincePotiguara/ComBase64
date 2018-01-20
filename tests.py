# encode utf-8
from base64 import decodebytes, encodebytes
import combase

# isso é a versão em 'bytes' produzida com a biblioteca base64 de :lorem_string:
lorem_bytes = b'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4g\nRHVpcyBtYXNzYSBkaWFtLCBpbnRlcmR1bSBlZ2V0IHF1YW0gYSwgcHJldGl1bSBjb21tb2RvIGRv\nbG9yLiBNYWVjZW5hcyBuZWMgY29uc2VxdWF0IHNhcGllbiwgZXUgZGlnbmlzc2ltIG5pc2wuIFF1\naXNxdWUgY3Vyc3VzIHZlbmVuYXRpcyBsb3JlbSBhdCBsYW9yZWV0LiBQZWxsZW50ZXNxdWUgc2Vk\nIGlhY3VsaXMgbGFjdXMsIGEgdnVscHV0YXRlIG1pLiBDdXJhYml0dXIgY29udmFsbGlzIGVyYXQg\nbGFvcmVldCwgc3VzY2lwaXQgYW50ZSB1dCwgY29udmFsbGlzIGVyb3MuIE51bmMgaW4gbWF1cmlz\nIGZlbGlzLiBWZXN0aWJ1bHVtIHBoYXJldHJhIGF1Y3RvciB0aW5jaWR1bnQuIERvbmVjIGZldWdp\nYXQgbmVjIHB1cnVzIGEgbG9ib3J0aXMuIFBlbGxlbnRlc3F1ZSBuZWMgbG9yZW0gdmVsIGFyY3Ug\ndnVscHV0YXRlIGVsZWlmZW5kIG5vbiBldCBkb2xvci4=\n'
lorem_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis massa diam, interdum eget quam a, pretium commodo dolor. Maecenas nec consequat sapien, eu dignissim nisl. Quisque cursus venenatis lorem at laoreet. Pellentesque sed iaculis lacus, a vulputate mi. Curabitur convallis erat laoreet, suscipit ante ut, convallis eros. Nunc in mauris felis. Vestibulum pharetra auctor tincidunt. Donec feugiat nec purus a lobortis. Pellentesque nec lorem vel arcu vulputate eleifend non et dolor."

def paragrafo(par: bytes) -> bool:
    _par = b'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4g\nRHVpcyBtYXNzYSBkaWFtLCBpbnRlcmR1bSBlZ2V0IHF1YW0gYSwgcHJldGl1bSBjb21tb2RvIGRv\nbG9yLiBNYWVjZW5hcyBuZWMgY29uc2VxdWF0IHNhcGllbiwgZXUgZGlnbmlzc2ltIG5pc2wuIFF1\naXNxdWUgY3Vyc3VzIHZlbmVuYXRpcyBsb3JlbSBhdCBsYW9yZWV0LiBQZWxsZW50ZXNxdWUgc2Vk\nIGlhY3VsaXMgbGFjdXMsIGEgdnVscHV0YXRlIG1pLiBDdXJhYml0dXIgY29udmFsbGlzIGVyYXQg\nbGFvcmVldCwgc3VzY2lwaXQgYW50ZSB1dCwgY29udmFsbGlzIGVyb3MuIE51bmMgaW4gbWF1cmlz\nIGZlbGlzLiBWZXN0aWJ1bHVtIHBoYXJldHJhIGF1Y3RvciB0aW5jaWR1bnQuIERvbmVjIGZldWdp\nYXQgbmVjIHB1cnVzIGEgbG9ib3J0aXMuIFBlbGxlbnRlc3F1ZSBuZWMgbG9yZW0gdmVsIGFyY3Ug\ndnVscHV0YXRlIGVsZWlmZW5kIG5vbiBldCBkb2xvci4=\n'
    par = encodebytes(par)
    return par == _par

def test_internal() -> None:
    """"Por algum motivo essa codificação vem com uma quebra de linha
    sempre depois de um ponto quando a string é assimilada numa variável"""
    par = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis massa diam, interdum eget quam a, pretium commodo dolor. Maecenas nec consequat sapien, eu dignissim nisl. Quisque cursus venenatis lorem at laoreet. Pellentesque sed iaculis lacus, a vulputate mi. Curabitur convallis erat laoreet, suscipit ante ut, convallis eros. Nunc in mauris felis. Vestibulum pharetra auctor tincidunt. Donec feugiat nec purus a lobortis. Pellentesque nec lorem vel arcu vulputate eleifend non et dolor."
    if(chr(10) in par):
        print("It has a \\n")
    else:
        print("It does not have a \\n")
    par = bytes(par, 'ascii')
    result = paragrafo(par)
    if result:
        print("Test_Internal pass")
    else:
        print("It is a trouble in Test_Internal")

def test_codificar() -> None:
    expected = lorem_bytes
    result = combase.codificar(lorem_string)
    if(expected == result):
        print("Codificar pass")
    else:
        print("Codificar did not pass")

def test_decodificar() -> None:
    expected = lorem_string
    result = combase.decodificar(lorem_bytes)
    if(expected == result):
        print("Decodificar pass")
    else:
        print("Decodificar did not pass")


test_internal()
test_codificar()
test_decodificar()