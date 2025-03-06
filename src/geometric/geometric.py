class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def area_rectangulo(self, base, altura):
        resultado=base*altura
        return resultado

    def perimetro_rectangulo(self, base, altura):
        resultado=2*(base+altura)
        return resultado

    def area_circulo(self, radio):
        resultado=math.pi*radio**2
        return resultado

    def perimetro_circulo(self, radio):
        resultado=2*math.pi*radio
        return resultado

    def area_triangulo(self, base, altura):
        resultado=(base*altura)/2
        return resultado

    def perimetro_triangulo(self, lado1, lado2, lado3):
        resultado=lado1+lado2+lado3
        return resultado

    def es_triangulo_valido(self, lado1, lado2, lado3):
        resultado=lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1
        return resultado
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        resultado=((base_mayor+base_menor)*altura)/2
        return resultado

    def area_rombo(self, diagonal_mayor, diagonal_menor):
        resultado=(diagonal_mayor*diagonal_menor)/2
        return resultado

    def area_pentagono_regular(self, lado, apotema):
        resultado=(5*lado*apotema)/2
        return resultado

    def perimetro_pentagono_regular(self, lado):
        resultado=5*lado
        return resultado

    def area_hexagono_regular(self, lado, apotema):
        resultado=(6*lado*apotema)/2
        return resultado

    def perimetro_hexagono_regular(self, lado):
        resultado=6*lado
        return resultado

    def volumen_cubo(self, lado):
        resultado=lado**3
        return resultado

    def area_superficie_cubo(self, lado):
        resultado=6*lado**2
        return resultado

    def volumen_esfera(self, radio):
        resultado=(4/3)*math.pi*radio**3
        return resultado
    
    def area_superficie_esfera(self, radio):
        """
        Calcula el área de la superficie de una esfera.
        
        Args:
            radio (float): Radio de la esfera
            
        Returns:
            float: Área de la superficie de la esfera
        """
        pass
    
    def volumen_cilindro(self, radio, altura):
        """
        Calcula el volumen de un cilindro.
        
        Args:
            radio (float): Radio de la base del cilindro
            altura (float): Altura del cilindro
            
        Returns:
            float: Volumen del cilindro
        """
        pass
    
    def area_superficie_cilindro(self, radio, altura):
        """
        Calcula el área de la superficie de un cilindro.
        
        Args:
            radio (float): Radio de la base del cilindro
            altura (float): Altura del cilindro
            
        Returns:
            float: Área de la superficie del cilindro
        """
        pass
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        """
        Calcula la distancia euclidiana entre dos puntos en un plano 2D.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            float: Distancia entre los dos puntos
        """
        pass
    
    def punto_medio(self, x1, y1, x2, y2):
        """
        Calcula el punto medio entre dos puntos en un plano 2D.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coordenadas (x, y) del punto medio
        """
        pass
    
    def pendiente_recta(self, x1, y1, x2, y2):
        """
        Calcula la pendiente de una recta que pasa por dos puntos.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            float: Pendiente de la recta
        """
        pass
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        """
        Obtiene los coeficientes de la ecuación de una recta en la forma Ax + By + C = 0.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coeficientes (A, B, C) de la ecuación de la recta
        """
        pass
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        """
        Calcula el área de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            apotema (float): Longitud de la apotema
            
        Returns:
            float: Área del polígono regular
        """
        pass
    
    def perimetro_poligono_regular(self, num_lados, lado):
        """
        Calcula el perímetro de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            
        Returns:
            float: Perímetro del polígono regular
        """
        pass
