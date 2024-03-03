#Parentizacion
import numpy as np
def multiplicacion_matrices_encadenadas(p):
  #Definimos el valor de n
  n = len(p)
  #Creamos la matriz donde se almacenaran los valores
  m = np.zeros((n,n),dtype=int)
  #Creamos la matriz para guardar los cortes
  s = np.zeros((n,n),dtype=int)

  #Llenamos la diagonal de la matriz con 0
  np.fill_diagonal(m,0)

  # Iteramos sobre las cadenas de longitud l
  for l in range(2, n):
      for i in range(1, n - l + 1):
          #Indicador de columna operativa
          j = i + l - 1
          #Casilla donde se asignara el numero de multiplicaciones
          m[i][j] = 999999999
          for k in range(i, j):
            #Comparación del numero de multiplicaciones
              cost = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
              if cost < m[i][j]:
                  m[i][j] = cost
                  s[i][j] = k
  #Retornamos la matriz m con la matriz s
  return m,s


# Función auxiliar para imprimir los paréntesis
def imprimir_paren(i, j, s):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        imprimir_paren(i, s[i][j],s)
        imprimir_paren(s[i][j] + 1, j, s)
        print(")", end="")


p = [5,10,3,12,5,50,6]
#Calculamos la matriz y la parentización
m,s = multiplicacion_matrices_encadenadas(p)
#Imprimimos la matriz de multiplicaciones
print("Matriz de multiplicaciones\n",m,"\n")
#Matriz de parentizacion
print("Matriz de parentesis\n",s,"\n")
#Minimo de multiplicaciones
print("Minino de multiplicaciones ",m[1,6], "\n")
#Reformamos la respuesta para colocar
#los parentesis donde corresponden
print("Solución explicita")
imprimir_paren(1, len(p)-1,s)