import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import statistics as st
from colorama import*

# Este codigo analiza un datasets de spotify
# El objetivo es crear una base de datos funcional
#El siguiente apartado es solamente para inicializar los archivos de excel
tabla= "spotify_artist_data.xlsx"
tabla= pd.read_excel(tabla)
tabla2= "100_million.xlsx"
tabla2= pd.read_excel(tabla2)
tabla3= "feats.xlsx"
tabla3= pd.read_excel(tabla3)
tabla4= "tracks_artistas.xlsx"
tabla4= pd.read_excel(tabla4)
tabla5= "onebillion_artistas.xlsx"
tabla5= pd.read_excel(tabla5)
tabla6= "feats_artistas.xlsx"
tabla6= pd.read_excel(tabla6)
tabla7= "spotify_artist_data_un_espacio.xlsx"
tabla7= pd.read_excel(tabla7)
tabla8= "mas_escuchadas_mujeres.xlsx"
tabla8= pd.read_excel(tabla8)
tabla9= "mas_escuchados_hombres.xlsx"
tabla9= pd.read_excel(tabla9)
tabla10='mas_escuchados_grupos.xlsx'
tabla10= pd.read_excel(tabla10)

#En este submenu se enseñarán diferentes tipos de estadísticas:
def estadisticas(): 
#El contador servira en este caso para acumular las veces que el usuario utilizo este submenu
    contador_estadisticas = 0
    while True:
        try:
            print(" ")
            print(Back.BLUE+"Menu de Estadísticas                        "+Back.RESET)
            print(Back.BLUE+"1 "+Back.GREEN+" Top 10 artistas más exitosos        "+Back.RESET)
            print(Back.BLUE+"2 "+Back.GREEN+" Top 10 artistas menos escuchados    "+Back.RESET)
            print(Back.BLUE+"3 "+Back.GREEN+" Top 10 artistas con más canciones   "+Back.RESET)
            print(Back.BLUE+"4 "+Back.GREEN+" Top 10 artistas con menos canciones "+Back.RESET)
            print(Back.BLUE+"5 "+Back.GREEN+" Regresar al menú principal          "+Back.RESET)
            contador_estadisticas = contador_estadisticas + 1
            op = int(input("\nInserte la opción de su preferencia: "))
            if op == 1:
                print(tabla7.loc[1:10, ('Artist Name','Lead Streams')]) 
            elif op == 2:
                print(tabla.loc[999:1008, ('Artist Name','Lead Streams')])
            elif op == 3:
                print(tabla4.nlargest(10, ['Tracks']))
            elif op == 4:
                print(tabla4.nsmallest(10, ['Tracks']))
            elif op == 5:  
                contador_estadisticas = contador_estadisticas - 1
                print("Las veces que se utilizó este submenú fueron:",contador_estadisticas,"veces.")
                break
#Los except son utilizados para evitar errores en el programa
        except TypeError:
            print("Favor de introducir una opción valida.")
        except NameError: 
            print("El nombre de la variable es incorrecto, ejem, programador, bucate otra chambita.")
        except ValueError:
            print("Intruduce el tipo de dato correcto, son solo numeros owo ")      
#-----------------------------------------------------------------------------------------------------------------------------
#En este submenu se enseñarán diferentes tipos de reportes:
def reportes():
#El contador servira en este caso para acumular las veces que el usuario utilizo este submenu
    contador_reportes = 0

    while True:
            print(" ")
            print(Back.BLUE+"                       Menú de Reportes                                 "+Back.RESET)
            print(Back.BLUE+"1 "+Back.GREEN+" Artista con más reproducciones                         "+Back.RESET)
            print(Back.BLUE+"2 "+Back.GREEN+" Artista con las colaboraciones mas reproducidas        "+Back.RESET)
            print(Back.BLUE+"3 "+Back.GREEN+" Artista con la mayor cantidad de canciones publicadas  "+Back.RESET)
            print(Back.BLUE+"4 "+Back.GREEN+" Artista con la mayor cantidad de canciones llegadas    "+Back.RESET)
            print(Back.BLUE+"  "+Back.GREEN+"                al millón de reproducciones             "+Back.RESET)
            print(Back.BLUE+"5 "+Back.GREEN+" Artista con la mayor cantidad de canciones llegadas    "+Back.RESET)
            print(Back.BLUE+"  "+Back.GREEN+"                al billón de reproducciones             "+Back.RESET)                       
            print(Back.BLUE+"6 "+Back.GREEN+" Regresar al menú principal                             "+Back.RESET)
            contador_reportes = contador_reportes + 1
            try:
                op = int(input("\nInserte la opción de su preferencia: "))
                if op == 1:
                    print(tabla7.nlargest(1,'Lead Streams')) 
                elif op == 2:
                    print(tabla7.nlargest(1,'Feats'))
                elif op == 3:
                    print(tabla7.nlargest(1,'Tracks'))
                elif op == 4:
                    print(tabla7.nlargest(1,'100 Million'))
                elif op == 5:
                    print(tabla7.nlargest(1,'One Billion'))
                elif op == 6:
                    contador_reportes = contador_reportes - 1
                    print("/nLas veces que se utilizó este submenú fueron:",contador_reportes,"veces.")
                    break
            except TypeError:
                print("Favor de introducir una opción valida.")
            except NameError: 
                print("El nombre de la variable es incorrecto, ejem, programador, bucate otra chambita.")
            except ValueError:
                print("Intruduce el tipo de dato correcto, son solo numeros owo ")
#-----------------------------------------------------------------------------------------------------------------------------
#En este submenu se enseñarán diferentes tipos de gráficas:
def graficas():

    contador_graficas = 0

    #El siguiente ciclo servirá para generar cada una de las gráficas del menú anterior y más
    while True:
            print(" ")
            print(Back.BLUE+"Menú de Gráficas                                                 "+Back.RESET)
            print(Back.BLUE+"1 "+Back.GREEN+" Top 10 artistas y su ultimas actualizaciones                  "+Back.RESET)
            print(Back.BLUE+"2 "+Back.GREEN+" Top 10 artistas y canciones con 100 mill de reproducciones    "+Back.RESET)
            print(Back.BLUE+"3 "+Back.GREEN+" Top 10 artistas y canciones con un billón de reproducciones   "+Back.RESET)
            print(Back.BLUE+"4 "+Back.GREEN+" Top 10 Artistas con menos actualizaciones                     "+Back.RESET)
            print(Back.BLUE+"5 "+Back.GREEN+" Top 10 artistas con menos num# de tracks                      "+Back.RESET)
            print(Back.BLUE+"6 "+Back.GREEN+" Top 10 Artistas con menor # de canciones con 100mill reprod.  "+Back.RESET)
            print(Back.BLUE+"7 "+Back.GREEN+" Regresar al menú principal                                    "+Back.RESET)
            contador_graficas = contador_graficas + 1
#Solo se usan los primeros 10 valores para las siguientes graficas
            try:
                tabla= "spotify_artist_data.xlsx"
                tabla= pd.read_excel(tabla)
                op = int(input("\nInserte la opción de su preferencia: "))
                if op == 1:
                    artista=tabla.loc[0:9, ("Artist Name")]
                    fecha=tabla.loc[0:9, ('Last Updated')]
                    plt.figure(figsize=(9,3))
                    plt.scatter(artista,fecha,alpha=.75,facecolor='m')
                    plt.title('Top 10 Artistas y sus ultimas actualizaciones')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 2:
                    artista=tabla.loc[0:9, ("Artist Name")]
                    cienm=tabla.loc[0:9, ('100 Million')]
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,cienm,alpha=.75,facecolor='g')
                    plt.title('Top 10 Artistas y el numero de canciones con 100 millones de reproducciones')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 3:
                    artista=tabla.loc[0:9, ("Artist Name")]
                    oneb=tabla.loc[0:9, ('One Billion')]
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,oneb,alpha=.75)
                    plt.title('Top 10 Artistas y el numero de canciones con 1 billon de reproducciones')
                    plt.xticks(rotation=45)
                    plt.show()

# A partir de estas graficas utilizamos los ultimos valores para los top

                elif op == 4:
                    artista=tabla.loc[999:1008, ("Artist Name")]
                    fecha=tabla.loc[999:1008, ('Last Updated')]
                    plt.figure(figsize=(9,3))
                    plt.scatter(artista,fecha,alpha=.75,facecolor='r')
                    plt.title('Top 10 Artistas con menos actualizaciones')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 5:
                    tracks="tracks_artistas.xlsx"
                    tracks = pd.read_excel(tracks)
                    artista=tracks.loc[990:1008, ("Artist Name")]
                    tracks1=tracks.loc[990:1008, ('Tracks')]
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,tracks1,alpha=.75,facecolor='g')
                    plt.title('Top 10 artistas con menos num# de tracks')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 6:
                    artista=tabla.loc[999:1008, ("Artist Name")]
                    cienm=tabla.loc[999:1008, ('100 Million')]
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,cienm,alpha=.75,facecolor='r')
                    plt.title('Top 10 Artistas con menor numero de canciones con 100 millones de reproducciones')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 7:
                    contador_graficas = contador_graficas - 1
                    print("Las veces que se utilizó este submenú fueron:",contador_graficas,"veces.")
                    break
            except TypeError:
                print("Favor de introducir una opción valida.")
            except NameError: 
                print("El nombre de la variable es incorrecto, ejem, programador, bucate otra chambita.")
            except ValueError:
                print("Intruduce el tipo de dato correcto, son solo numeros owo ")

def graficas2():
    
    contador_graficas2 = 0
    #El siguiente ciclo servirá para generar cada una de las gráficas del menú anterior y más
    while True:
            print(" ")
            print(Back.BLUE+"Menú de Gráficas Mujeres                                         "+Back.RESET)
            print(Back.BLUE+"1 "+Back.GREEN+" Top 10 artistas mujeres y su ultima publicacion               "+Back.RESET)
            print(Back.BLUE+"2 "+Back.GREEN+" Top 10 artistas mujeres y el # de canciones publicadas        "+Back.RESET)
            print(Back.BLUE+"3 "+Back.GREEN+" Top 10 artistas mujeres y canciones con 100 mill de reprod.   "+Back.RESET)
            print(Back.BLUE+"4 "+Back.GREEN+" Top 10 artistas mujeres y canciones con un billón de reprod.  "+Back.RESET)
            print(Back.BLUE+"5 "+Back.GREEN+" Regresar al menú principal                                    "+Back.RESET)
            contador_graficas2 = contador_graficas2 + 1

# Se utiliza un archivo de excel diferente debido a que buscamos un grupo especifico
            try:
                artfemlist="mas_escuchadas_mujeres.xlsx"
                artfemlist = pd.read_excel(artfemlist)
                op = int(input("\nInserte la opción de su preferencia: "))
                if op == 1:
                    artista=artfemlist["Artist Name"]
                    tracks=artfemlist['Tracks']
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,tracks,alpha=.75,facecolor='m')
                    plt.title('Top 10 artistas mujeres en Spotify y su ultima actualizacion')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 2:
                    artista=artfemlist["Artist Name"]
                    cienmill=artfemlist['100 Million']
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,cienmill,alpha=.75,facecolor='m')
                    plt.title('Top 10 artistas mujeres y su # de tracks')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 3:
                    artista=artfemlist["Artist Name"]
                    cienmill=artfemlist['100 Million']
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,cienmill,alpha=.75,facecolor='m')
                    plt.title('Top 10 Artistas mujeres y el numero de canciones con 100 millones de reprod.')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 4:
                    artista=artfemlist["Artist Name"]
                    onebill=artfemlist['One Billion']
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,onebill,alpha=.75,facecolor='m')
                    plt.title('Top 10 Artistas mujeres y el numero de canciones con 1 billon de reprod.')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 5:
                    contador_graficas2 = contador_graficas2 - 1
                    print("Las veces que se utilizó este submenú fueron:",contador_graficas2,"veces.")
                    break
            except TypeError:
                print("Favor de introducir una opción valida.")
            except NameError: 
                print("El nombre de la variable es incorrecto, ejem, programador, bucate otra chambita.")
            except ValueError:
                print("Intruduce el tipo de dato correcto, son solo numeros owo ")


def graficas3():
    contador_graficas3 = 0
    #El siguiente ciclo servirá para generar cada una de las gráficas del menú anterior
    while True:
            print(" ")
            print(Back.BLUE+"Menú de Gráficas Hombres                                         "+Back.RESET)
            print(Back.BLUE+"1 "+Back.GREEN+" Top 10 artistas hombres y su ultima publicacion               "+Back.RESET)
            print(Back.BLUE+"2 "+Back.GREEN+" Top 10 artistas hombres y el # de canciones publicadas        "+Back.RESET)
            print(Back.BLUE+"3 "+Back.GREEN+" Top 10 artistas hombres y canciones con 100 mill de reprod.   "+Back.RESET)
            print(Back.BLUE+"4 "+Back.GREEN+" Top 10 artistas hombres y canciones con un billón de reprod.  "+Back.RESET)
            print(Back.BLUE+"5 "+Back.GREEN+" Regresar al menú principal                                    "+Back.RESET)
            contador_graficas3 = contador_graficas3 + 1  
            # #El contador servira en este caso para acumular las veces que el usuario utilizo este submenu
            #Se utiliza la tabla art_masc
            try:
                art_masc="mas_escuchados_hombres.xlsx"
                art_masc = pd.read_excel(art_masc)
                op = int(input("\nInserte la opción de su preferencia: "))
                if op == 1:
                    artista=art_masc["Artist Name"]
                    fecha=art_masc['Last Updated']
                    plt.figure(figsize=(9,3))
                    plt.scatter(artista,fecha,alpha=.75,facecolor='g')
                    plt.title('Top 10 artistas masculinos y sus ultimas actualizaciones')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 2:
                    artista=art_masc["Artist Name"]
                    tracks=art_masc['Tracks']
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,tracks,alpha=.75,facecolor='g')
                    plt.title('Top 10 artistas hombres y su # de tracks')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 3:
                    artista=art_masc["Artist Name"]
                    cien_mill=art_masc['100 Million']
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,cien_mill,alpha=.75,facecolor='g')
                    plt.title('Top 10 Artistas hombres y el numero de canciones con 100 millones de reprod.')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 4:
                    artista=art_masc["Artist Name"]
                    one_bill=art_masc['One Billion']
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,one_bill,alpha=.75,facecolor='g')
                    plt.title('Top 10 Artistas mujeres y el numero de canciones con 1 billon de reprod.')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 5:
                    contador_graficas3 = contador_graficas3 -1
                    print("Las veces que se utilizó este submenú fueron:",contador_graficas3,"veces.")
                    break
            except TypeError:
                print("Favor de introducir una opción valida.")
            except NameError: 
                print("El nombre de la variable es incorrecto, ejem, programador, bucate otra chambita.")
            except ValueError:
                print("Intruduce el tipo de dato correcto, son solo numeros owo ")

def graficas4():
    contador_graficas4 = 0
    #El siguiente ciclo servirá para generar cada una de las gráficas del menú anterior
    while True:
            print(" ")
            print(Back.BLUE+"Menú de Gráficas de grupos                                       "+Back.RESET)
            print(Back.BLUE+"1 "+Back.GREEN+" Top 10 grupos y su ultima publicacion                         "+Back.RESET)
            print(Back.BLUE+"2 "+Back.GREEN+" Top 10 grupos y el # de canciones publicadas                  "+Back.RESET)
            print(Back.BLUE+"3 "+Back.GREEN+" Top 10 grupos y canciones con 100 mill de reprod.             "+Back.RESET)
            print(Back.BLUE+"4 "+Back.GREEN+" Top 10 grupos y canciones con un billón de reprod.            "+Back.RESET)
            print(Back.BLUE+"5 "+Back.GREEN+" Regresar al menú principal                                    "+Back.RESET)
            contador_graficas4 = contador_graficas4 + 1
            # Se utiliza la tabla de los grupos
            try:
                grupos="mas_escuchados_grupos.xlsx"
                grupos = pd.read_excel(grupos)
                op = int(input("\nInserte la opción de su preferencia: "))
                if op == 1:
                    artista=grupos["Artist Name"]
                    fecha=grupos['Last Updated']
                    plt.figure(figsize=(9,3))
                    plt.scatter(artista,fecha,alpha=.75,facecolor='r')
                    plt.title('Top 10 grupos en Spotify y su ultima actualizacion')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 2:
                    artista=grupos["Artist Name"]
                    tracks=grupos['Tracks']

                    plt.figure(figsize=(9,3))
                    plt.bar(artista,tracks,alpha=.75,facecolor='r')
                    plt.title('Top 10 grupos y su # tracks ')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 3:
                    artista=grupos["Artist Name"]
                    cienmillg=grupos['One Billion']
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,cienmillg,alpha=.75,facecolor='r')
                    plt.title('Top 10 grupos y el numero de canciones con 100 millones de reprod.')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 4:
                    artista=grupos["Artist Name"]
                    one_bill=grupos['One Billion']
                    plt.figure(figsize=(9,3))
                    plt.bar(artista,one_bill,alpha=.75,facecolor='r')
                    plt.title('Top 10 grupos y el numero de canciones con 1 billon de reprod.')
                    plt.xticks(rotation=45)
                    plt.show()
                elif op == 5:
                    contador_graficas4 = contador_graficas4 - 1
                    print("Las veces que se utilizó este submenú fueron:",contador_graficas4,"veces.")
                    break
            except TypeError:
                print("Favor de introducir una opción valida.")
            except NameError: 
                print("El nombre de la variable es incorrecto, ejem, programador, bucate otra chambita.")
            except ValueError:
                print("Intruduce el tipo de dato correcto, son solo numeros owo ")
#-----------------------------------------------------------------------------------------------------------------------------
#Este submenu explica brevemente el beneficio de hacer un programa como este:
def beneficios():
    contador_beneficios = 0
# Se agrego submenus a los objetivos adornando con colorama
    while True:
            print(" ")
            print(Back.BLUE+"Menú de Benefic                              "+Back.RESET)
            print(Back.BLUE+"1 "+Back.GREEN+" Objetivos                   "+Back.RESET)
            print(Back.BLUE+"2 "+Back.GREEN+" Beneficios principales      "+Back.RESET)
            print(Back.BLUE+"3 "+Back.GREEN+" Regresar al menú principal  "+Back.RESET)
            contador_beneficios = contador_beneficios + 1
            try:
                op = int(input("\nInserte la opción de su preferencia: "))
                if op == 1:
                    print("\n                       OBJETIVOS                           ")
                    print("Desarrollar un programa que permita generar información")
                    print(" a partir de los datos que contiene un dataset, de un")
                    print("         tema en particular y de tu interés.\n")
                elif op == 2:
                    print("\n                     BENEFICIOS PRINCIPALES"                   )
                    print("       1.-Simplificar la busqueda de los datos analiticos")
                    print("\n 2.-Utilizar herramientas de programacion y adaptarlos a usos")
                    print("                  de trabajos de analisis.")
                    print("\n       3.-Ayuda a la imaginacion o a la estrategia logica")
                    print("              para resolver problemas matematicos.\n")
                elif op == 3:
                    contador_beneficios = contador_beneficios - 1
                    print("Las veces que se utilizó este submenú fueron:",contador_beneficios,"veces.")
                    break
            except TypeError:
                print("Favor de introducir una opción valida.")
            except NameError: 
                print("El nombre de la variable es incorrecto, ejem, programador, bucate otra chambita.")
            except ValueError:
                print("Intruduce el tipo de dato correcto, son solo numeros owo ")
#-----------------------------------------------------------------------------------------------------------------------------
#Este es el menu principal el cual tienen el importante papel de mostrar las primeras opciones y llevarnos a los submenus
def menu_principal():
# Funcion De ciclo para el menu principal donde se agrega colorama par adornar
    while True:
        try:
            print(" ")
            print(Back.WHITE+"  Base de datos Spotify  "+Back.RESET)
            print(Back.BLUE+"      Menu principal     "+Back.RESET)
            print(Back.BLUE+"1 "+Back.GREEN+" Estadisticas          "+Back.RESET)
            print(Back.BLUE+"2 "+Back.GREEN+" Reportes              "+Back.RESET)
            print(Back.BLUE+"3 "+Back.GREEN+" Graficas              "+Back.RESET)
            print(Back.BLUE+"4 "+Back.GREEN+" Graficas de mujeres   "+Back.RESET)
            print(Back.BLUE+"5 "+Back.GREEN+" Graficas de hombres   "+Back.RESET)
            print(Back.BLUE+"6 "+Back.GREEN+" Graficas de grupos    "+Back.RESET)
            print(Back.BLUE+"7 "+Back.GREEN+" Beneficios            "+Back.RESET)
            print(Back.BLUE+"8 "+Back.GREEN+" Terminar              "+Back.RESET)

            op = int(input("Inserte la opción de su preferencia: "))
            if op == 1:
                estadisticas()
            elif op == 2:
                reportes()
            elif op == 3:
                graficas()
            elif op == 4:
                graficas2()
            elif op == 5:
                graficas3()
            elif op == 6:
                graficas4()
            elif op == 7:
                beneficios()
            elif op == 8:
                break
        except TypeError:
            print("Favor de introducir una opción valida.")
        except NameError: 
            print("El nombre de la variable es incorrecto, ejem, programador, bucate otra chambita.")
        except ValueError:
            print("Intruduce el tipo de dato correcto, son solo numeros owo ")
    
menu_principal()