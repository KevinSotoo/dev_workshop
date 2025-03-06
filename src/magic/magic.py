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
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        pass
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        pass
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        pass
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        pass
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        pass
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        pass