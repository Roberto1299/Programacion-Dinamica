#Problema de la cuerda
def resolverCorte(n, p):
  #Declaramos los arreglos que usaremos
  #los llenamos con cero
  max_ganancia = [0] * (n + 1)
  cortes_optimos = [0] * (n + 1)

  for j in range(1, n+1):
    #Declaramos nuestras variables temporales
    #serán de utilidad a lo largo del código
    temporal = 0
    corte = 0
    for i in range(1, j+1):
      #Hacemos el calculo de la ganancia máxima
      if temporal < p[i] + max_ganancia[j - i]:
        temporal = p[i] + max_ganancia[j - i]
        corte = i
    #Guardamos el máximo valor
    max_ganancia[j] = temporal
    #Guardamos el índice del corte
    cortes_optimos[j] = corte
  return max_ganancia, cortes_optimos

def corteOptimo(n, s):
  print("Tamaño de cuerda ", n)
  while(n>0):
    print("Se debe hacer un corte de "+ str(cortes_optimos[n]))
    n = n - cortes_optimos[n]

def imprimirTabla(p,l):
  print("Tabla")
  for i in range(0,l+1):
    print("Cuerda ["+str(i) + "] máximo valor "+str(p[i]))
  print("\n")


precios = [0, 1, 4, 10, 12, 15, 20, 21, 32, 31, 41, 51]
longitud_cuerda = 11
#Comenzamos a calcular los precios
precio_maximo, cortes_optimos = resolverCorte(longitud_cuerda, precios)

#Imprimimos la tabla
imprimirTabla(precio_maximo,longitud_cuerda)
#Encontrar el corte optimo del largo 11
n = 11
corteOptimo(n, cortes_optimos)