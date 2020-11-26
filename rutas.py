def contar_rutas_mas_cortas(C):
    result=C
    x=len(result)
    # lleno todas las columnas 1
    for i in range(x): 
        result[i][0] = 1
     # lleno toda las filas con 1
    for j in range(x): 
        result[0][j]= 1

    for i in range(1,x):
        for j in range(1,x):
            if(result[i][j]==0):
                if(result[i-1][j]>0):# suma el valor de la izq
                    result[i][j]+=result[i-1][j]
                if(result[i][j-1]>0):# suma el valor en la pos superior
                    result[i][j]+=result[i][j-1]
            else:
                result[i][j]=0# si encontro la restriccion sume 0 
            
    return result[x-1][x-1]
