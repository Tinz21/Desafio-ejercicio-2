# Ejercicio 2:  

# Basado en una matriz de R x C, entregando coordenadas de X, Y,
# se debe sumar los valores hacia las coordenadas de origen (0,0). 

# Dominio ℕ = {0, 1, 2, 3, 4, …} 
# El llenado de la matriz esta dado por Z: 
# Cuando R = 1 , completar fila con Z,  si R > 1 entonces completar fila con: Z= Z + R –1

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
    #-------------------------------------parameters
    R:int=4
    C:int=3
    Z:int=2
    #-------------------------------------coordinates
    x:int=1
    y:int=2

    if validation(R,C,x,y):
        res=run(R,C,Z,x,y)
        print(f"El resultado de una matriz {R}x{C}, cuando z={Z},x={x},y={y} es: ",res)
    else:
        print("math error")