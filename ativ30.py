# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notdef calcula_media(nota1, nota2, nota3):
def calcule_media(nota1, nota2, nota3):
    média =  (nota1+nota2+nota3)/3
    if média >=7:
        return f"media: {média:.2f} - aprovado"
    else:
        return f"media: {média:.2f} - reprovado"
nota1 =float(input(f"digite a primeira nota "))
nota2 =float(input(f"digite a segunda nota  "))
nota3 =float(input(f"digite a terceira nota "))
resultado = calcule_media(nota1, nota2, nota3)
print(resultado)