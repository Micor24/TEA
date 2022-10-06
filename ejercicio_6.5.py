cadena = "X-DSPAM-Confidence:0.8475"
inicio = cadena.find(":") + 1 #posición
final = len(cadena) #cantidad
numero = float(cadena[inicio:final])


print(type(numero))



