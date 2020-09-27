# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:36:56 2020

@author: Admin
"""

import csv

lista_datos=[]

with open("synergy_logistics_database.csv","r") as archivo_csv:
    lector=csv.reader(archivo_csv)
    
    for linea in lector:
        lista_datos.append(linea)
        



totalsea=0
totalair=0
totalroad=0
totalrail=0
rutas_contadas_exp=[]
conteo_rutas_exp=[]
contador_exp=0
rutas_contadas_imp=[]
conteo_rutas_imp=[]
contador_imp=0
valores_exp=0


#ciclo for para hacer el conteo de flujo de cuántas veces se utilizó una ruta de países según su exportación  
for ruta_exp in lista_datos:
    if ruta_exp[1] == "Exports":
          ruta_actual_exp=[ruta_exp[2],ruta_exp[3]]
#Proceso para verificar que la ruta sea única y que el conteo sea correcto          
          if ruta_actual_exp not in rutas_contadas_exp:
            for movimiento_exp in lista_datos:
                if ruta_actual_exp ==[movimiento_exp[2],movimiento_exp[3]]:
                    contador_exp+=1
                    
                    
                    
            rutas_contadas_exp.append(ruta_actual_exp)
            conteo_rutas_exp.append([ruta_exp[2],ruta_exp[3],contador_exp])
            contador_exp=0
#Proceso para ordenar de mayor a menor el flujo según la ruta utilizado
            conteo_rutas_exp.sort(reverse=True,key=lambda x:x[2])
#Proceso para mostrar únicamente los 10 países con mayores flujos
            top_10_export=conteo_rutas_exp[1:11]
            

  
        
        
#ciclo for para hacer el conteo de flujo de cuántas veces se utilizó una ruta de países según su exportación          
for ruta_imp in lista_datos:
    if ruta_imp[1] == "Imports":
          ruta_actual_imp=[ruta_imp[2],ruta_imp[3]]
#Proceso para verificar que la ruta sea única y que el conteo sea correcto          
          if ruta_actual_imp not in rutas_contadas_imp:
            for movimiento_imp in lista_datos:
                if ruta_actual_imp ==[movimiento_imp[2],movimiento_imp[3]]:
                    contador_imp+=1
                    
                    
                    
            rutas_contadas_imp.append(ruta_actual_imp)
            conteo_rutas_imp.append([ruta_imp[2],ruta_imp[3],contador_imp])
            contador_imp=0

#Proceso para ordenar de mayor a menor el flujo según la ruta utilizado
            conteo_rutas_imp.sort(reverse=True,key=lambda x:x[2])
#Proceso para mostrar únicamente los 10 países con mayores flujos
            top_10_imp=conteo_rutas_imp[1:11]
            
            
#proceso con el cual se elimina el primer renglón de la lista para poder hacer la suma más sencilla

lista_datos.pop(0)
valores2=[]

#Ciclos en donde se hace la suma del monto según el transporte que utilizo
for a in lista_datos:
    if a[7]=='Air':
        totalair=totalair+int(a[9])

for a in lista_datos:
    if a[7]=='Rail':
        totalrail=totalrail+int(a[9])

for a in lista_datos:
    if a[7]=='Road':
        totalroad=totalroad+int(a[9])    
    
for a in lista_datos:
    if a[7]=='Sea':
        totalsea=totalsea+int(a[9])




    
    
  
total_imp_ext=0
totaljapon=0
totalgermany=0
totalchina=0
totalitaly=0
totalusa=0
totalrussia=0
totalsouthkorea=0
totalnetherlands=0
totalfrance=0
totalspain=0
totalunitedkingdom=0
totalcanada=0
totalbelgium=0
totalaustralia=0
totalbrazil=0
totalswitzerland=0
totalmexico=0
totalaustria=0
totalsingapore=0
totalvietnam=0
totalmalaysia=0
totalarab=0

#Ciclo for para calcular la suma de cada país según el monto de importación y exportación
for i in lista_datos:
  if i[1]=='Exports' or i[1]=='Imports' and i[2]=='Japan':
    totaljapon=totaljapon+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Germany':
    totalgermany=totalgermany+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='China':
    totalchina=totalchina+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Italy':
    totalitaly=totalitaly+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='USA':
    totalusa=totalusa+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Russia':
    totalrussia=totalrussia+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='South Korea':
    totalsouthkorea=totalsouthkorea+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Netherlands':
    totalnetherlands=totalnetherlands+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='France':
    totalfrance=totalfrance+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Spain':
    totalspain=totalspain+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='United Kingdom':
    totalunitedkingdom=totalunitedkingdom+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Canada':
    totalcanada=totalcanada+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Belgium':
    totalbelgium=totalbelgium+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Australia':
    totalaustralia=totalaustralia+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Brazil':
    totalbrazil=totalbrazil+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Switzerland':
    totalswitzerland=totalswitzerland+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Mexico':
    totalmexico=totalmexico+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Austria':
    totalaustria=totalaustria+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Singapore':
    totalsingapore=totalsingapore+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Vietnam':
    totalvietnam=totalvietnam+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='Malaysia':
    totalmalaysia=totalmalaysia+int(i[9])
  elif i[1]=='Exports' or i[1]=='Imports' and i[2]=='United Arab Emirates':
    totalarab=totalarab+int(i[9])
    


total_imp_ext=totaljapon+totalgermany+totalchina+totalitaly+totalusa+totalrussia+totalsouthkorea+totalnetherlands+totalfrance+totalspain+totalunitedkingdom+totalcanada+totalbelgium+totalaustralia+totalbrazil+totalswitzerland+totalmexico+totalaustria+totalsingapore+totalvietnam+totalmalaysia+totalarab
print(f"Total de cantidad en ventas: $ {total_imp_ext}")

porcentajejapon=totaljapon/total_imp_ext*100
porcentajegermany=totalgermany/total_imp_ext*100
porcentajechina=totalchina/total_imp_ext*100
porcentajeitaly=totalitaly/total_imp_ext*100
porcentajeusa=totalusa/total_imp_ext*100
porcentajerussia=totalrussia/total_imp_ext*100
porcentajesouthkorea=totalsouthkorea/total_imp_ext*100
porcentajenetherlands=totalnetherlands/total_imp_ext*100
porcentajefrance=totalfrance/total_imp_ext*100
porcentajespain=totalspain/total_imp_ext*100
porcentajeunitedkingdom=totalunitedkingdom/total_imp_ext*100
porcentajecanada=totalcanada/total_imp_ext*100
porcentajebelgium=totalbelgium/total_imp_ext*100
porcentajeaustralia=totalaustralia/total_imp_ext*100
porcentajebrazil=totalbrazil/total_imp_ext*100
porcentajeswitzerland=totalswitzerland/total_imp_ext*100
porcentajemexico=totalmexico/total_imp_ext*100
porcentajeaustria=totalaustria/total_imp_ext*100
porcentajesingapore=totalsingapore/total_imp_ext*100
porcentajevietnam=totalvietnam/total_imp_ext*100
porcentajemalaysia=totalmalaysia/total_imp_ext*100
porcentajearab=totalarab/total_imp_ext*100

totalporcentaje=0
#print(f"Porcentaje de Japon: {porcentajejapon}")
#print(f"Porcentaje de Alemania: {porcentajegermany}")
#print(f"Porcentaje de China: {porcentajechina}")
#print(f"Porcentaje de Italia: {porcentajeitaly}")
#print(f"Porcentaje de Usa: {porcentajeusa}")
#print(f"Porcentaje de Russia: {porcentajerussia}")
#print(f"Porcentaje de Korea del Sur: {porcentajesouthkorea}")
#print(f"Porcentaje de Holanda: {porcentajenetherlands}")
#print(f"Porcentaje de Francia: {porcentajefrance}")
#print(f"Porcentaje de España: {porcentajespain}")
#print(f"Porcentaje de Reino unido: {porcentajeunitedkingdom}")
#print(f"Porcentaje de Canada: {porcentajecanada}")
#print(f"Porcentaje de Belgica: {porcentajebelgium}")
#print(f"Porcentaje de Australia: {porcentajeaustralia}")
#print(f"Porcentaje de Brasil: {porcentajebrazil}")
#print(f"Porcentaje de Suiza: {porcentajeswitzerland}")
#print(f"Porcentaje de Mexico: {porcentajemexico}")
#print(f"Porcentaje de Austria: {porcentajeaustria}")
#print(f"Porcentaje de Singapore: {porcentajesingapore}")
#print(f"Porcentaje de Vietnam: {porcentajevietnam}")
#print(f"Porcentaje de Malasia: {porcentajemalaysia}")
#print(f"Porcentaje de Emiratos Arabes: {porcentajearab}")

totalporcentaje=porcentajejapon+porcentajegermany+porcentajechina+porcentajeitaly+porcentajeusa+porcentajerussia+porcentajesouthkorea+porcentajenetherlands+porcentajefrance+porcentajespain+porcentajeunitedkingdom+porcentajecanada+porcentajebelgium+porcentajeaustralia+porcentajebrazil+porcentajeswitzerland+porcentajemexico+porcentajeaustria+porcentajesingapore+porcentajevietnam+porcentajemalaysia+porcentajearab

#print(f"Suma de porcentaje{totalporcentaje}")  
salida=True

print("Bienvenido a Synergy Logistics")

while (salida==True):
    opcion=int(input("Elige la opción que deseas visualizar: 1.-Países con mayores flujos de exportación, 2.-Paises con mayores flujos de importación, 3.-El monto total de importación y exportación según el transporte usado, 4-El porcentaje de cada país según el monto total de importaciones y exportaciones,5-Salir "))
    
    if opcion==1:
         print("Los 10 países con mayores flujos de exportación")
         print(top_10_export)
    elif opcion==2:
         print("Los 10 países con mayores flujos de importación")
         print(top_10_imp)
    elif opcion==3:
        print(f"El monto total tranportado por aire/air es : {totalair}" )
        print(f"El monto total tranportado por tren/rail es :  {totalrail}")
        print(f"El monto total tranportado por carretera/road  es :  {totalroad}")
        print(f"El monto total tranportado por barco,mar/sea es :  {totalsea}")
        
        print("El ranking de los medios de transporte según su monto es: ")
        print("1-Barco,Mar (Sea)")
        print("2-Tren(Rail)")
        print("3-Avión(Air)")
        print("4-Carretera(Road)")
    elif opcion==4 :
        print(f"Total de cantidad en ventas: $ {total_imp_ext}")
        print(f"Porcentaje de Japon: {porcentajejapon}")
        print(f"Porcentaje de Alemania: {porcentajegermany}")
        print(f"Porcentaje de China: {porcentajechina}")
        print(f"Porcentaje de Italia: {porcentajeitaly}")
        print(f"Porcentaje de Usa: {porcentajeusa}")
        print(f"Porcentaje de Russia: {porcentajerussia}")
        print(f"Porcentaje de Korea del Sur: {porcentajesouthkorea}")
        print(f"Porcentaje de Holanda: {porcentajenetherlands}")
        print(f"Porcentaje de Francia: {porcentajefrance}")
        print(f"Porcentaje de España: {porcentajespain}")
        print(f"Porcentaje de Reino unido: {porcentajeunitedkingdom}")
        print(f"Porcentaje de Canada: {porcentajecanada}")
        print(f"Porcentaje de Belgica: {porcentajebelgium}")
        print(f"Porcentaje de Australia: {porcentajeaustralia}")
        print(f"Porcentaje de Brasil: {porcentajebrazil}")
        print(f"Porcentaje de Suiza: {porcentajeswitzerland}")
        print(f"Porcentaje de Mexico: {porcentajemexico}")
        print(f"Porcentaje de Austria: {porcentajeaustria}")
        print(f"Porcentaje de Singapore: {porcentajesingapore}")
        print(f"Porcentaje de Vietnam: {porcentajevietnam}")
        print(f"Porcentaje de Malasia: {porcentajemalaysia}")
        print(f"Porcentaje de Emiratos Arabes: {porcentajearab}")
        print(f"Suma de porcentaje{totalporcentaje}") 
        
    elif opcion==5:
       print("Gracias por visitar synergy logistics")
       salida=False
        