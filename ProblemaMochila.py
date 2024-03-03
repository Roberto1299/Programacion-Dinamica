#Problema de la mochila
import numpy as np
def calculoMatriz(w,v,n,W):
  #Definimos el vector y lo llenamos con ceros
  V = np.zeros((n+1, W+1))

  #Comenzamos a iterar el llenado de la matriz
  #con las condiciones dadas
  for i in range(1, n+1):
    for x in range(0, W+1):
      #Marcador de peso de la mochila
      j = x-w[i-1]
      #Dependiendo del marcador existen 2 condiciones
      if j < 0:
        V[i,x] = max(V[i-1,x],0)
      else:
        V[i,x] = max(V[i-1,x], V[i-1, j] + v[i-1])
  return V

def objetosTomados(V,W,v,w,n):
  #Tomamos el valor máximo de la matriz
  max_value = V[n][W]
  objetos_tomados = []
  #Realizamos el recorrido
  for i in range(n, 0, -1):
    if max_value <= 0:
      break
    if max_value == V[i-1][W]:
      continue
    else:
      #Guardamos el indice de los objetos tomados
      objetos_tomados.append(i-1)
      max_value -= v[i-1]
      W -= w[i-1]

  #Imprimimos los objetos tomados
  for i in objetos_tomados:
    print("Tomar objeto "+str(i+1)+" con valor "+str(v[i])+ " y peso "+str(w[i]))


#Datos necesarios
w = [85,26,48,21,22,95,43,45,55,52]
v = [79,32,47,18,26,85,33,40,45,59]
n = len(v)
W = 140

#Matriz resultante
V = calculoMatriz(w,v,n,W)
print("Matriz resultante \n"+str(V) + "\n")
#Impresion de valor optimo
print("Valor optimo " +str(V[n][W]) +"\n")
#Impresión de objetos que tomar
objetosTomados(V,W,v,w,n)