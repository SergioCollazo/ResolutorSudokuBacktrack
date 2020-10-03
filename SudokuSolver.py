#!/usr/bin/env python
# coding: utf-8

# # Resolutor de Sudokus mediante algortimo de backtracking

# In[1]:


tablero_inicial =[[6,0,3,0,5,0,2,0,4],
           [0,4,5,0,0,0,6,9,0],
           [0,8,0,9,6,4,0,1,0],
           [0,0,0,5,8,1,0,0,0],      
           [0,0,9,3,0,6,7,0,0],
           [0,0,0,7,9,2,0,0,0],
           [0,7,0,2,1,5,0,3,0],
           [0,5,4,0,0,0,1,2,0],
           [2,0,8,0,3,0,5,0,6]];


# In[2]:


def imprimir_tablero(t):
    for f in range(len(t)):
        print(t[f])
    print(" ")    


# In[3]:


imprimir_tablero(tablero_inicial)


# In[4]:


def sudoku(i,j,inicial,solucion):
    if inicial[i][j] == False:
        for k in range(1,10):
            solucion[i][j] = k
            if es_factible(i,j,solucion):
                if i == 8 and j == 8: imprimir_tablero(solucion)
                if i < 8 and j == 8: sudoku(i+1, 0, inicial, solucion)
                if i <= 8 and j < 8: sudoku(i, j+1, inicial ,solucion)
            solucion[i][j] = 0
    else:
        if i == 8 and j == 8: imprimir_tablero(solucion)
        if i < 8 and j == 8: sudoku(i+1, 0, inicial, solucion)
        if i <= 8 and j < 8: sudoku(i, j+1, inicial ,solucion)


# In[5]:


def es_factible(i,j,solucion):
    valido = True
    k = 0
    while k <= 8 and valido:  #Comprobamos la columna
        if solucion[i][j] == solucion [k][j] and k != i:
            valido = False
        k = k + 1
    l = 0
    while l <= 8 and valido: #comprobamos la fila
        if solucion[i][j] == solucion[i][l] and l != j:
            valido = False
        l = l +1
    k = correspondencia3x3(i);
    l = correspondencia3x3(j);
    #Comrpobamos el subgrupo 3x3
    while k < correspondencia3x3(i) + 3 and valido:
        while l < correspondencia3x3(j) + 3 and valido:
            if solucion[i][j] == solucion[k][l] and i != k and j != l:
                valido = False
            l = l + 1
        k = k + 1
        l = correspondencia3x3(j)
    return valido    


# In[6]:



def correspondencia3x3(i):
    resultado = (i//3)*3
    return resultado    


# In[7]:


tablero_solucion = [[0 for x in range(9)] for y in range(9)] 
for n in range(len(tablero_inicial)):
    for m in range(len(tablero_inicial[n])):
        tablero_solucion[n][m] = tablero_inicial[n][m]
        
sudoku(0,0,tablero_inicial,tablero_solucion)

