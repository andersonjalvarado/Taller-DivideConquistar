## =========================================================================
## @author Anderson Jair Alvarado (andersonjalvarado@javeriana.edu.co)
## =========================================================================
import math

'''
    @inputs:S, una secuencia de n-elementos.
    @outputs: max, el valor de la maxima i diferencia.
'''
def maxima_i_diferencia(secuencia):
    max = -math.inf
    for i in range (len(secuencia)):
        if (i == 0):
            sum_izquierda = 0
            sum_derecha = suma(secuencia,i+1,len(secuencia)-1)
        elif (i == len(secuencia)):
            sum_izquierda = suma(secuencia,0,i-1)
            sum_derecha = 0
        else:
            sum_izquierda = suma(secuencia,0,i-1)
            sum_derecha = suma(secuencia,i+1,len(secuencia)-1)
            
        diferencia = sum_izquierda - sum_derecha
        
        if(diferencia > max):
            max = diferencia
        #print(f'index : {i}, valor: {secuencia[i]}, result: {sum_izquierda} - {sum_derecha} = {diferencia}')        
    return max

'''
    @inputs:S, una secuencia de n-elementos.
            b, inicio de la secuencia
            e, final de la secuencia
    @outputs: suma de los valores de la secuencia.
'''
def suma(secuencia, b, e):
    if (b>e):
        return 0
    else:
        q = math.floor( ( b + e )/2 )
        return suma(secuencia, b, q-1) + secuencia[q] + suma(secuencia, q+1, e)
    


#secuencia = [-97.69512693467526, 30.815347601947565]
#max = maxima_i_diferencia(secuencia)
#print(f'maxima diferencia de la secuencia: {max}')