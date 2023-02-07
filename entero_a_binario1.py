if __name__ == '__main__':
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    # Verificando que ingrese un número entero
    while True:
        try:
            numero = int(input('Ingrese un número entero para convertirlo a binario: '))
            # Si no hay un error se almacena el número y se rompe el ciclo while
            break 
        except ValueError:
            # Si existe un error se solicita que vuelva a ingresar
            print('Debe ingresar un número entero válido.')

    def aBinario(decimal):
        # Si decimal en negativo, return None
        if decimal < 0:
            return None
        # Si no es negativo se continua.
        num = decimal # Para no modificar el valor de decimal
        binary = 0
        power = 1
        while num > 0:
            binary += (num % 2) * power
            num //= 2
            power *= 10
        return f'{decimal} convertido en binario es {binary}'

    print(aBinario(numero))
