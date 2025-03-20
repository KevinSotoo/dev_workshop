class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        texto_limpio = ""

        for letra in texto:
            if letra != " ":
                if "A" <= letra <= "Z":
                    texto_limpio += letra.lower()
                else:
                    texto_limpio += letra

        i, j = 0, len(texto_limpio) - 1
        while i < j:
            if texto_limpio[i] != texto_limpio[j]:
                return False
            i += 1
            j -= 1

        return True
    
    def invertir_cadena(self,texto):
        resultado=""
        for letra in texto:
            resultado=letra+resultado
        return resultado
    
    def contar_vocales(self,texto):
        vocales="aeiouAEIOU"
        contador=0
        for letra in texto:
            if letra in vocales:
                contador+=1
        return contador
    
    def contar_consonantes(self,texto):
        vocales="aeiouAEIOU"
        contador=0
        for letra in texto:
            es_letra='a'<=letra<='z' or 'A'<=letra<='Z'
            es_vocal=letra in vocales
            if es_letra and es_vocal==False:
                contador+=1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        texto1 = texto1.replace(" ", "").lower()
        texto2 = texto2.replace(" ", "").lower()
        
        caracteres = {}
        for letra in texto1:
            if letra in caracteres:
                caracteres[letra] += 1
            else:
                caracteres[letra] = 1
        for letra in texto2:
            if letra in caracteres:
                caracteres[letra] -= 1
            else:
                return False
        for letra in caracteres:
            if caracteres[letra] !=0:
                return False
        return True

    def contar_palabras(self,texto):
        contador=0
        en_palabra=False
        for letra in texto:
            if letra!=" ":
                if en_palabra==False:
                    contador+=1
                    en_palabra=True
            else:
                en_palabra=False
        return contador
    
    def palabras_mayus(self,texto):
        resultado=""
        mayus=True
        for letra in texto:        
            if mayus and ('a'<=letra<='z' or 'A'<=letra<='Z'):
                resultado+=letra.upper()
                mayus=False
            else:
                resultado+=letra
            if letra==" ":
                mayus=True
        return resultado
    
    def eliminar_espacios_duplicados(self,texto):
        resultado=""
        space=False
        for letra in texto:
            if letra!=" ":
                resultado+=letra
                space=False
            elif space==False:
                resultado+=letra
                space=True
        return resultado
    
    def es_numero_entero(self, texto):
        if texto=="":
            return False
    
        if texto[0]=='-':
            if texto[1:]=="":
                return False
            texto = texto[1:]
    
        for caracter in texto:
            if caracter < '0' or caracter > '9':
                return False
    
        return True
    
    def cifrar_cesar(self,texto,desplazamiento):
        resultado=""
        for simbolo in texto:
            if 'a'<=simbolo<='z':
                mayuscula=simbolo.upper()
                nueva_letra=((ord(mayuscula)-ord('A')+desplazamiento)%26)+ord('A') 
                resultado+=chr(nueva_letra)
            elif 'A'<=simbolo<='Z':
                nueva_letra=((ord(simbolo)-ord('A')+desplazamiento)%26)+ord('A')
                resultado+=chr(nueva_letra)
            else:
                resultado+=simbolo
        return resultado
    
    def descifrar_cesar(self,texto,desplazamiento):
        resultado=""
        for simbolo in texto:
            if 'a'<=simbolo<='z':
                mayuscula=simbolo.upper()
                nueva_letra=((ord(mayuscula)-ord('A')-desplazamiento)%26)+ord('A')
                resultado+=chr(nueva_letra)
            elif 'A'<=simbolo<='Z':
                nueva_letra=((ord(simbolo)-ord('A')-desplazamiento)%26)+ord('A')
                resultado+=chr(nueva_letra)
            else:
                resultado+=simbolo
        return resultado
    
    def encontrar_subcadena(self,texto,subcadena):
        posiciones=""
        i=0
        longitud_sub=0
        for caracter in subcadena:
            longitud_sub+=1
        while True:
            longitud_texto=0
            for caracter in texto[i:]:
                longitud_texto+=1
            if longitud_texto<longitud_sub:
                break
            contador=0
            while contador<longitud_sub and texto[i+contador]==subcadena[contador]:
                contador+=1
            if contador==longitud_sub:
                posiciones+=str(i)+" "
            i+=1
        return posiciones
