# Ejercicio 2:  

import os

def run(R,C,Z,x,y): # This function calculates the final result
    matrix=[]
    array=[]
    for i in range(1,R+1):
        for j in range(1,C+1):
            if i==1:
                array.append(Z)
            else:
                array.append(Z+i-1)
            if j==C:
                matrix.append(array)
                array=[]
    count=0
    for i in range(y+1):
        count=matrix[i][0]+count
    result=count*(x+1)
    return result


def validation(R,C,x,y): # This function validate that the input parameters are correct
    if R and C > 0:
        if x<C and y<R:
            return True
    return False


if __name__=="__main__":
    os.system("cls")
    print(
        """ Basado en una matriz de R x C, entregando coordenadas de X, Y,
        se debe sumar los valores hacia las coordenadas de origen (0,0). 

        Dominio N = {0, 1, 2, 3, 4, …} 
        El llenado de la matriz esta dado por Z: 
        Cuando R = 1 , completar fila con Z,  si R > 1 
        entonces completar fila con: Z= Z + R –1

        Ejemplo:  

        Matriz R x C = 4, 3   
        Z = 2    X = 1     Y = 2 

        Por tanto, se obtiene la siguiente matriz:  
                C=1    C=2    C=3 
        R = 1    2      2      2 
        R = 2    3      3      3
        R = 3    4      4      4
        R = 4    5      5      5 

        Dada las coordenadas X e Y la matriz da como resultado 18 : 
               x0      x1 
        y0     2       2  
        y1     3       3
        Y2     4       4
        """)
    #-------------------------------------parameters
    R=int(input('Ingrese el valor de R: '))
    C=int(input('Ingrese el valor de C: '))
    Z=int(input('Ingrese el valor de Z: '))
    #-------------------------------------coordinates
    x=int(input('Ingrese el valor de x: '))
    y=int(input('Ingrese el valor de y: '))

    if validation(R,C,x,y):
        res=run(R,C,Z,x,y)
        print(f"El resultado de una matriz {R}x{C}, cuando z={Z},x={x},y={y} es: ",res)
    else:
        print("math error")