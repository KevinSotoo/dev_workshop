class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self,n):
        a,b=0,1
        contador=0
        while contador<n:
            a,b=b,a+b
            contador+=1
        return a if n>0 else 0
    
    def secuencia_fibonacci(self,n):
        a,b=0,1
        resultado=[]
        contador=0
        while contador<n:
            resultado+=[a]
            a,b=b,a+b
            contador+=1
        return resultado
    
    def es_primo(self,n):
        if n<2:
            return False
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True
    def generar_primos(self,n):
        resultado=[]
        i=2
        while i<=n:
            if self.es_primo(i):
                resultado+=[i]
            i+=1
        return resultado
    
    def es_numero_perfecto(self, n):
        suma=1
        i=2
        while i*i<=n:
            if n%i==0:
                suma+=i
                if i!=n//i:
                    suma+=n//i
            i+=1
        return suma==n and n!=1
    
    def triangulo_pascal(self, filas):
        resultado=[[1]]
        i=1
        while i<filas:
            fila=[1]
            x=1
            while x<i:
                fila+=[resultado[i-1][x-1]+resultado[i-1][x]]
                x+=1
            fila+=[1]
            resultado+=[fila]
            i+=1
        return resultado
    
    def factorial(self,n):
        resultado=1
        while n>1:
            resultado*=n
            n-=1
        return resultado
    
    def mcd(self,a,b):
        while b:
            a,b=b,a%b
        return a

    def mcm(self,a,b):
        return a*b//self.mcd(a,b)

    def suma_digitos(self,n):
        suma=0
        while n>0:
            suma+=n%10
            n//=10
        return suma

    def es_numero_armstrong(self,n):
        suma=0
        temp=n
        digitos=0
        copia=n
        while copia>0:
            digitos+=1
            copia//=10
        while temp>0:
            suma+=(temp%10)**digitos
            temp//=10
        return suma==n
    
    def es_cuadrado_magico(self,matriz):
        filas=0
        for _ in matriz:
            filas+=1
        columnas=0
        for _ in matriz[0]:
            columnas+=1
        suma=0
        i=0
        while i<columnas:
            suma+=matriz[0][i]
            i+=1
        i=0
        while i<filas:
            suma_fila=0
            x=0
            while x<columnas:
                suma_fila+=matriz[i][x]
                x+=1
            if suma_fila!=suma: return False
            i+=1
        i=0
        while i<columnas:
            suma_columna=0
            x=0
            while x<filas:
                suma_columna+=matriz[x][i]
                x+=1
            if suma_columna!=suma: return False
            i+=1
        suma_diagonal1=0
        suma_diagonal2=0
        i=0
        while i<filas:
            suma_diagonal1+=matriz[i][i]
            suma_diagonal2+=matriz[i][filas-1-i]
            i+=1
        return suma_diagonal1==suma and suma_diagonal2==suma