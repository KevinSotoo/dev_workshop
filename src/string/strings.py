class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self,texto):
        i=0
        x=0
        for letra in texto:
            x+=1
        x-=1
        while i<x:
            if texto[i]!=texto[x]:
                return False
            i+=1
            x-=1
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
    
    def es_anagrama(self,texto1,texto2):
        caracteres={}
        for letra in texto1:
            if letra in caracteres:
                caracteres[letra]+=1
            else:
                caracteres[letra]=1
        for letra in texto2:
            if letra in caracteres:
                caracteres[letra]-=1
            else:
                return False
        for letra in caracteres:
            if caracteres[letra]!=0:
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
                resultado+=letra.upper()#sirve para convertir primer letra en mayus
                mayus=False
            else:
                resultado+=letra
            if letra==" ":
                mayus=True
        return resultado
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        pass
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        pass
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass