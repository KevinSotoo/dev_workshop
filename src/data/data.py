class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        invertida = []
        for elemento in lista:
            invertida=[elemento]+invertida 
        return invertida
    
    def buscar_elemento(self, lista, elemento):
        x=0
        for valor in lista:
            if valor==elemento:
                return x  #manda la posicion dentro de la lista
            x+=1
        return "No encontrado"
    
    def eliminar_duplicados(self, lista):
        lista_nueva=[]
        for elemento in lista:
            contador=0
            for x in lista_nueva:
                if x==elemento:
                    contador=1
                    break
            if contador==0:
                lista_nueva+=[elemento]
        return lista_nueva
    
    def merge_ordenado(self, lista1, lista2):
        resultado=[]
        x=y=0
        contador1=0
        for x in lista1:
            contador1+=1
        contador2=0
        for y in lista2:
            contador2+=1
        x=y=0
        while x<contador1 or y<contador2:
            if y==contador2 or (x<contador1 and lista1[x]<lista2[y]):
                resultado+=[lista1[x]]
                x+=1
            else:
                resultado+=[lista2[y]]
                y+=1
        return resultado
    
    def rotar_lista(self, lista, k):
        n=0
        for x in lista:
            n+=1
        if n==0:
            return lista
        k%=n
        return lista[-k:]+lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        total=0
        n=0
        for numero in lista:
            total+=numero
            n+=1
        return (n*(n+1))//2-total #se usa formula de suma de los primeros n
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            encontrado=False
            for x in conjunto2:
                if x==elemento:
                    encontrado=True
                    break
            if encontrado==False:
                return False
        return True
    
    def implementar_pila(self):
        pila=[]
        def push(valor):
            pila+=[valor]
        def pop():
            if pila:
                nueva_pila=[]
                for x in pila:
                    nueva_pila+=[x]
                valor=nueva_pila[-1]
                pila[:]=[nueva_pila[x] for x in range(nueva_pila[-1])]
                return valor
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass