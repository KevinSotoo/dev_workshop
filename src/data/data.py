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
                return x  
            x+=1
        return -1
    
    def eliminar_duplicados(self,lista):
        lista_nueva=[]
        vistos=[]
        for elemento in lista:
            existe=False
            for x in vistos:
                if elemento==x and (elemento is True)==(x is True):
                 existe=True
                 break
            if not existe:
             lista_nueva.append(elemento)
             vistos.append(elemento)
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
    
    def encuentra_numero_faltante(self,lista):
        total=0
        conteo=0
        for numero in lista:
            total+=numero
            conteo+=1
        esperado=(conteo*(conteo+1))//2
        return esperado-total



    
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
                return pila.pop()
        def peek():
            if pila:
                return pila[-1]
        def is_empty():
            return pila==[]
        return {"push":push,"pop":pop,"peek":peek,"is_empty":is_empty}
    
    def implementar_cola(self):
        cola=[]
        def enqueue(valor):
            cola+=[valor]
        def dequeue():
            if cola:
                return cola.pop(0)
        def peek():
            if cola:
                return cola[0]
        def is_empty():
            return cola==[]
        return {"enqueue":enqueue,"dequeue":dequeue,"peek":peek,"is_empty":is_empty}
    
    def matriz_transpuesta(self, matriz):
        filas=0
        for x in matriz:
            filas+=1
        columnas=0
        for y in matriz[0]:
            columnas+=1
        return [[matriz[fila][x] for fila in range(filas)] for x in range(columnas)]