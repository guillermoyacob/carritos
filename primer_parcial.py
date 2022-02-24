#Consigna 6: En función de valor de los productos. Obtener el valor promedio de los carritos abandonados

from evaluacion import datos

#generamos una lista vacia para agregar los productos abandonados

lista_productos_abandonados = []

#recorremos carritos para buscar dichos productos

for i in datos['carritos']:

#si esta abandonado (false) agregamos el id del producto a la lista de productos abandonados

	if i["finalizado"] == False:
		lista_productos_abandonados.extend(i["productos"])

#podemos visualizar la lista con 
#print(lista_productos_abandonados)

#creamos una nueva lista para ubicar solo los precios de los producto

lista_precio_final = []

#pedimos al usuario que ingrese el valor actual del dolar, para unificar el resultado final bajo ese tipo de moneda

valor_dolar = float(input("Ingrese el valor actual del dolar, por favor: "))

#recorremos cada id en nuestra lista para encontrar la coincidencia con el precio del producto
#recorremos "precio" para verificar que tipo de moneda es
#en caso de ser pesos argentinos lo pasamos a dolares para mantener coherencia en la lista

for j in lista_productos_abandonados:
        for k in datos['productos']:
                if j == k['_id']:
                            if k["precio"]["moneda"]=="ARG":
                                    lista_precio_final.append((k["precio"]["importe"])/valor_dolar)
                            else:
                                    lista_precio_final.append(k["precio"]["importe"])

print("Lista de productos abandonados: ", lista_productos_abandonados)

print("Lista del precio final: ", lista_precio_final)

#declaramos una variable para contener la suma de los valores de la lista de productos abandonados
#para luego dividirlos por el total de productos, o lo que seria lo mismo, dividirlo por el largo de la lista

suma_precio_final = 0 
for m in lista_precio_final:
    suma_precio_final += m
promedio = suma_precio_final / len(lista_precio_final)

print ("El promedio del valor total de los productos de los carritos abandonados en dolares es: U$s " + ("{0:.2f}".format(promedio)))
