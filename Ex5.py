# 5) Escreva um programa que inverta os caracteres de um string.


def inverte_string(texto: str) -> str:
    texto_invertido = ""
    
    for letra in texto:
        texto_invertido = letra + texto_invertido
    
    return texto_invertido


texto = "testando"
print(inverte_string(texto))