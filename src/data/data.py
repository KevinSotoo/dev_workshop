class Data:
    def invertir_lista(self, lista):
        resultado = []
        for i in lista:
            resultado = [i] + resultado
        return resultado

    def buscar_elemento(self, lista, elemento):
        indice = 0
        for i in lista:
            if i == elemento:
                return indice
            indice += 1
        return -1

    def eliminar_duplicados(self, lista):
        resultado = []
        for item in lista:
            encontrado = False
            for r in resultado:
                if r == item:
                    encontrado = True
                    break
            if not encontrado:
                resultado += [item]
        return resultado

    def merge_ordenado(self, lista1, lista2):
        resultado = []
        while lista1 or lista2:
            if not lista1:
                resultado += [lista2[0]]
                lista2 = lista2[1:]
            elif not lista2:
                resultado += [lista1[0]]
                lista1 = lista1[1:]
            elif lista1[0] < lista2[0]:
                resultado += [lista1[0]]
                lista1 = lista1[1:]
            else:
                resultado += [lista2[0]]
                lista2 = lista2[1:]
        return resultado

    def rotar_lista(self, lista, k):
        if not lista:
            return []
        while k > 0:
            lista = [lista[-1]] + lista[:-1]
            k -= 1
        return lista

    def encuentra_numero_faltante(self, lista):
        n = 1
        while True:
            encontrado = False
            for num in lista:
                if num == n:
                    encontrado = True
                    break
            if not encontrado:
                return n
            n += 1

    def es_subconjunto(self, conjunto1, conjunto2):
        for item in conjunto1:
            encontrado = False
            for c in conjunto2:
                if c == item:
                    encontrado = True
                    break
            if not encontrado:
                return False
        return True

    def implementar_pila(self):
        pila = []
        def push(x):
            pila[:] = pila + [x]
        def pop():
            if pila:
                ultimo = pila[-1]
                pila[:] = pila[:-1]
                return ultimo
        def peek():
            if pila:
                return pila[-1]
        def is_empty():
            return not pila
        return {"push": push, "pop": pop, "peek": peek, "is_empty": is_empty}

    def implementar_cola(self):
        cola = []
        def enqueue(x):
            cola[:] = cola + [x]
        def dequeue():
            if cola:
                primero = cola[0]
                cola[:] = cola[1:]
                return primero
        def peek():
            if cola:
                return cola[0]
        def is_empty():
            return not cola
        return {"enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty}

    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        filas = 0
        for _ in matriz:
            filas += 1
        columnas = 0
        for _ in matriz[0]:
            columnas += 1
        resultado = []
        for _ in range(columnas):
            resultado += [[0] * filas]
        i = 0
        for fila in matriz:
            j = 0
            for valor in fila:
                resultado[j][i] = valor
                j += 1
            i += 1
        return resultado