#PASO 1
#Para importar saludos de nuestro modulos.py...
'''
import b44_Modulos  #poner import y el nombre de tu archivo

saludar()
'''
#Sin embargo así no funciona, debido a que no es posible utilizar directamente la función
#Tenemos que hacerlo como si se tratase de una clase y sus métodos
#Es decir, imaginar que queremos decir de saludos el método saludar

from b44_Modulos import saludar

saludar()

#si hubiéramos importado así: from saludos import*
#hubiera importado todo lo de ese fichero

#PASO 2
#Nota importante: no hace falta importar constantemente, solo es para visualizar los ejemplos y pasos
import b44_Modulos

b44_Modulos.Saludo()




