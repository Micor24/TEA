try:
    entrada = input("Ingrese nombre del archivo: ")
    archivo = open(entrada, "r", encoding="UTF-8") 
    for linea in archivo:
        print(linea.upper())
except:
    print("Error, no existe el")




#print(archivo.read())
#encoding: f_8 normalmente usado r read a applicate 
#por cada línea en el archivo ,,entrada,"r", "names.txt", "a", encoding="UTF-8"