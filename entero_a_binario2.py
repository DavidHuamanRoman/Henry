if __name__ == '__main__':
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    def aBinario(decimal):
        if isinstance(decimal, int) and decimal >= 0:
            # Creando una cadena para almacenar el binario
            binary = ""
            numero = decimal
            while numero > 0:
                binary = str(numero % 2) + binary
                numero //= 2
            return f'{decimal} en binario es: {binary}'
        else:
            return None
        
    print(aBinario('50'))
    print(aBinario(50))
    print(aBinario(-50))
