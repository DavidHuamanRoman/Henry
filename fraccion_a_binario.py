if __name__ == '__main__':
    def fraccion_a_binario(decimal):
        # Inicializa la cadena binaria con el prefijo "0."
        binary = "0."

        # Repite el proceso de multiplicación sucesiva hasta que el decimal sea cero
        while decimal > 0:
            # Si el resultado de multiplicar el decimal por 2 es mayor o igual a 1,
            # agrega un "1" a la cadena binaria y resta 1 del resultado
            if decimal * 2 >= 1:
                binary += "1"
                decimal = decimal * 2 - 1
            # Si el resultado de multiplicar el decimal por 2 es menor a 1,
            # agrega un "0" a la cadena binaria y asigna el resultado a decimal
            else:
                binary += "0"
                decimal = decimal * 2
        # Devuelve la cadena binaria
        return binary
    
    print(fraccion_a_binario(1/2))
    print(fraccion_a_binario(1/3))
    print(fraccion_a_binario(1/4))
    print(fraccion_a_binario(1/5))
    print(fraccion_a_binario(1/6))
    print(fraccion_a_binario(1/7))
    print(fraccion_a_binario(1/8))
    print(fraccion_a_binario(1/9))
