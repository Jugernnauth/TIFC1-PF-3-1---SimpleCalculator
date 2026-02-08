def ingreso(dato):
    mensaje = 'ingrese ' + dato + 'numero: '
    valor= input(mensaje)
    
    #hacer esto
    try:
        valor = int(valor)
    except:
        #si no entonces la operacion
        #se generara un error    
        valor = 'Error'

    if valor == 'Error':
        print('dato erroneo')
        exit()

    return valor
      
control = 'y'

while control == 'y':
    numero_1 = ingreso('primer')
    numero_2 = ingreso('segundo')
    
    operacion = input('ingrese la operacion/simbolo')

    if operacion == '+':
        print('suma: ', numero_1 + numero_2)
    elif operacion == '-':
        print('resta', numero_1 - numero_2)
    elif operacion == '*':
        print('multiplicar', numero_1 * numero_2)
    else:
        print('el simbolo no es valido')

    control = input('quieres hacer una nueva operacion? y/n')
