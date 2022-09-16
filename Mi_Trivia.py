import random  # Importamos la librería random para crear un numero aleatorio 
import time  # Importamos la librería time para hacer pausas en el codigo
import os #Importamos la librería os para limpiar pantalla

def clean(): #Definimos la función para limpiar pantalla segun el SO
  if os.name == "posix":
   os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   os.system ("cls")

# Codigos para dar colores a las lineas de codigo
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 10)

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print (f"{YELLOW}BIENVENIDO A MI TRIVIA".center(55))
print("----------------------".center(50))
print ("\nPondremos a prueba tus conocimientos\n")

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable
nombre = input("Ingresa tu nombre: ").capitalize()

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el 
# contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla
# OJO, el \n al final o al inicio de la línea es para dar un "salto de línea"
print(f"""\nHola {nombre}, lee con atencion las intrucciones de la trivia: 
 1.- Hay diferentes preguntas con múltiples respuestas
 2.- Responde con la letra de la alternativa correcta y presiona 'Enter' para pasar al siguiente nivel
 3.- Inicias con {puntaje} puntos, hay respuestas que duplicarán, restarán, sumarán o te harán perder la mitad de tu puntaje
 Buena suerte!{RESET}""")

game = True
contador = 0

while game == True:
  contador += 1
  # Agregamos un timer para iniciar la trivia
  print("\nLa trivia inicia en..\n")
  for timer in range(5, 0, -1):
    time.sleep(1.2)
    print(RED+str(timer)+RESET)
    time.sleep(1.2)
  print(f"{RED}\nGo!\n{RESET}")
  time.sleep(1.5)

  clean() #Limpiamos pantalla

  # Categoria Deporte
  # Pregunta 1
  print(f"\n{GREEN}Nivel 1\n")
  print("¿Que país ha ganado mas copas del mundo en fútbol?\n")
  print ("a) Brasil") # Respuesta correcta
  print ("b) Alemania") 
  print ("c) Inglaterra") 
  print (f"d) Argentina{RESET}") 
  # Solicitamos la respuesta del usuario y la almacenamos en una variable
  respuesta_1 = input("\nTu respuesta: ")
  # Evaluamos la respuesta ingresada
  while respuesta_1 not in ("a", "b", "c", "d", "h"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_1 == "a":
    puntaje += 10
    print(f"{GREEN}Correcto {nombre}, Brasil es pentacampeon mundial!{RESET}")
  elif respuesta_1 == "b":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, Alemania es tetracampeon{RESET}")
  elif respuesta_1 == "c":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, Inglaterra solo tiene un título{RESET}")
  elif respuesta_1 == "d":
    puntaje /= 2
    print(f"{RED}Respuesta incorrecta {nombre}, Argentina ganó 2 mundiales{RESET}")
  # Agregamos una respuesta secreta
  elif respuesta_1 == "h":
    puntaje += 10
    print(f"{RED}Oh! no es la respuesta correcta pero te regalo 10 puntos{RESET}")

  print(f"{nombre} llevas {puntaje} puntos")
  time.sleep(2)
  clean() #Limpiamos pantalla

  # Hacemos una pausa para leer y entender el mensaje de la respuesta  
  # inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

  #  Pregunta 2
  print(f"\n{GREEN}Nivel 2\n")
  print("¿Quién es el atleta mas rápido a nivel mundial en 100 metros?\n")
  print ("a) Michael Jordan")
  print ("b) Tyson Gay")
  print ("c) Gareth Bale")
  print (f"d) Usain Bolt{RESET}") # Respuesta correcta
  # Solicita la respuesta del usuario y la almacenamos en una variable
  respuesta_2 = input("\nTu respuesta: ")
  # Evaluamos la respuesta ingresada
  while respuesta_2  not in ("a", "b", "c", "d", "e"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_2 == "a":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, Michael Jordan es basquetbolista{RESET}")
  elif respuesta_2 == "b":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, Tyson Gay no es el atleta mas rápido{RESET}")
  elif respuesta_2 == "c":
    puntaje /= 2
    print(f"{RED}Respuesta incorrecta {nombre}, Gareth Bale es un jugador de fútbol{RESET}")
  elif respuesta_2 == "d":
    puntaje += 10
    print(f"{GREEN}Asi es {nombre}, Usain Bolt es el hombre mas rápido del mundo{RESET}")
  # Agregamos una respuesta secreta
  elif respuesta_2 == "e":
    puntaje += 10
    print(f"{RED}No soy ninguna de las alternativas pero te doy 10 puntos extras{RESET}")

  print(f"{nombre} llevas {puntaje} puntos")
  time.sleep(2)
  clean() #Limpiamos pantalla
  # Hacemos una pausa para leer y entender el mensaje de la respuesta  
  # inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

  #  Pregunta 3
  print(f"\n{GREEN}Nivel 3\n")
  print("¿Que es un decatlón?\n")
  print ("a) Un deporte olímpico")
  print ("b) Una competencia atlética de 10 pruebas combinadas") # Respuesta correcta
  print ("c) Una maraton de 40 km")
  print (f"d) Un juego entre 2 equipos{RESET}")
  # Solicita la respuesta del usuario y la almacenamos en una variable
  respuesta_3 = input("\nTu respuesta: ")
  # Evaluamos la respuesta ingresada
  while respuesta_3  not in ("a", "b", "c", "d", "f"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_3 == "a":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, el decatlón no es un deporte{RESET}")
  elif respuesta_3 == "b":
    puntaje += 10
    print(f"{GREEN}Respuesta correcta {nombre}, el declatlón es una competencia de 10 pruebas{RESET}")
  elif respuesta_3 == "c":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, el decatlon no incluye maraton de 40 km{RESET}")
  elif respuesta_3 == "d":
    puntaje /= 2
    print(f"{RED}Respuesta incorrecta {nombre}, no es un juego entre 2 equipos{RESET}")
  # Agregamos una respuesta secreta
  elif respuesta_3 == "f":
    puntaje += 10
    print(f"{RED}Me descubriste! ten 10 puntos por eso{RESET}")

  print(f"{nombre} llevas {puntaje} puntos")
  time.sleep(2)
  clean() #Limpiamos pantalla

  # Hacemos una pausa para leer y entender el mensaje de la respuesta  
  # inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

  # Categoria Cine
  # Pregunta 4
  print(f"\n{GREEN}Nivel 4\n")
  print("¿Quien es el protagonista de la película 'Thor'?\n")
  print ("a) Robert Downey Jr.")
  print ("b) Chris Evans")
  print ("c) Chris Hemsworth") # Respuesta correcta
  print (f"d) Tom Hiddleston{RESET}") 
  # Solicita la respuesta del usuario y la almacenamos en una variable
  respuesta_4 = input("\nTu respuesta: ")
  # Evaluamos la respuesta ingresada
  while respuesta_4  not in ("a", "b", "c", "d", "j"):
    respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_4 == "a":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, Robert Downey Jr. es Iron Man{RESET}")
  elif respuesta_4 == "b":
    puntaje /= 2
    print(f"{RED}Respuesta incorrecta {nombre}, él es otro Chris{RESET}")
  elif respuesta_4 == "c":
    puntaje += 10
    print(f"{GREEN}Respuesta correcta {nombre}, Chris Hemsworth interpreta a Thor{RESET}")
  elif respuesta_4 == "d":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, Tom Hiddleston interpreta a Loki{RESET}")
  # Agregamos una respuesta secreta
  elif respuesta_4 == "j":
    puntaje += 10
    print(f"{RED}Vaya! acepta estos 10 puntos extras{RESET}")

  print(f"{nombre} llevas {puntaje} puntos")
  time.sleep(2)
  clean() #Limpiamos pantalla

  # Hacemos una pausa para leer y entender el mensaje de la respuesta  
  # inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

  # Pregunta 5
  print(f"\n{GREEN}Nivel 5\n")
  print("¿En que año se estrenó Corazon Valiente?\n")
  print ("a) 1998")
  print ("b) 2000")
  print ("c) 2005")
  print (f"d) 1995{RESET}") # Respuesta correcta
  # Solicita la respuesta del usuario y la almacenamos en una variable
  respuesta_5 = input("\nTu respuesta: ")
  # Evaluamos la respuesta ingresada
  while respuesta_5  not in ("a", "b", "c", "d", "l"):
    respuesta_5 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_5 == "a":
    puntaje /= 2
    print(f"{RED}Respuesta incorrecta {nombre}, en 1998 se estrenó Armageddon{RESET}")
  elif respuesta_5 == "b":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, en el año 2000 terminó el siglo XX{RESET}")
  elif respuesta_5 == "c":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, en el 2005 se estrenó Harry Potter y el cáliz de fuego{RESET}")
  elif respuesta_5 == "d":
    puntaje += 10
    print(f"{GREEN}Respuesta correcta {nombre}, Corazon Valiente con Mel Gibson se estrenó en 1995{RESET}")
  # Agregamos una respuesta secreta
  elif respuesta_5 == "l":
    puntaje += 10
    print(f"{RED}Buen intento! no vienen mal 10 puntos mas{RESET}")

  print(f"{nombre} llevas {puntaje} puntos")
  time.sleep(2)
  clean() #Limpiamos pantalla

  # Hacemos una pausa para leer y entender el mensaje de la respuesta  
  # inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

  # Pregunta 6
  print(f"\n{GREEN}Nivel 6\n")
  print("¿Hasta el 2018 cuantas peliculas tiene la saga 'Piratas del Caribe'?\n")
  print ("a) 5") # Respuesta correcta
  print ("b) 6")
  print ("c) 4")
  print (f"d) 7{RESET}")
  # Solicita la respuesta del usuario y la almacenamos en una variable
  respuesta_6 = input("\nTu respuesta: ")
  # Evaluamos la respuesta ingresada
  while respuesta_6  not in ("a", "b", "c", "d", "p"):
    respuesta_6 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_6 == "a":
    puntaje += 10
    print(f"{GREEN}Correcto {nombre}, Piratas del Caribe tiene 5 películas y un cortometraje{RESET}")
  elif respuesta_6 == "b":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, Piratas del Caribe solo tiene 5 películas y un cortometraje{RESET}")
  elif respuesta_6 == "c":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, Piratas del Caribe no tiene 4 películas{RESET}")
  elif respuesta_6 == "d":
    puntaje /= 2
    print(f"{RED}Respuesta incorrecta {nombre}, 7 es demasiado{RESET}")
  # Agregamos una respuesta secreta
  elif respuesta_6 == "p":
    puntaje += 10
    print(f"{RED}No soy la respuesta correcta pero tampoco perdiste puntos{RESET}")

  print(f"{nombre} llevas {puntaje} puntos")
  time.sleep(2)
  clean() #Limpiamos pantalla

  # Hacemos una pausa para leer y entender el mensaje de la respuesta  
  # inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

  # Categoria Historia
  # Pregunta 7
  print(f"\n{GREEN}Nivel 7\n")
  print("¿Quien gobernaba en el antiguo Egipto?\n")
  print ("a) El emperador") 
  print ("b) El zar") 
  print ("c) El faraon") # Respuesta correcta
  print (f"d) El presidente{RESET}")
  # Solicita la respuesta del usuario y la almacenamos en una variable
  respuesta_7 = input("\nTu respuesta: ")
  # Evaluamos la respuesta ingresada
  while respuesta_7  not in ("a", "b", "c", "d", "m"):
    respuesta_7 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_7 == "a":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, el emperador gobernó Roma{RESET}")
  elif respuesta_7 == "b":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, los zares eran rusos{RESET}")
  elif respuesta_7 == "c":
    puntaje += 10
    print(f"{GREEN}Respuesta correcta {nombre}, los faraones gobernaban en Egipto{RESET}")
  elif respuesta_7 == "d":
    puntaje /= 2
    print(f"{RED}Respuesta incorrecta {nombre}, no habian presidentes en el antiguo Egipto{RESET}")
  # Agregamos una respuesta secreta
  elif respuesta_7 == "m":
    puntaje += 10
    print(f"{RED}Soy una respuesta secreta que te obsequia 10 puntos{RESET}")

  print(f"{nombre} llevas {puntaje} puntos")
  time.sleep(2)
  clean() #Limpiamos pantalla

  # Hacemos una pausa para leer y entender el mensaje de la respuesta  
  # inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

  # Pregunta 8
  print(f"\n{GREEN}Nivel 8\n")
  print("Quien fue el ultimo inca?\n")
  print ("a) José de San Martín") 
  print ("b) Manco Cápac")
  print ("c) Atahualpa") # Respuesta correcta
  print (f"d) Tupac Amaru II{RESET}")
  # Solicita la respuesta del usuario y la almacenamos en una variable
  respuesta_8 = input("\nTu respuesta: ")
  # Evaluamos la respuesta ingresada
  while respuesta_8  not in ("a", "b", "c", "d", "i"):
    respuesta_8 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_8 == "a":
    puntaje /= 2
    print(f"{RED}Respuesta incorrecta {nombre}, José de San Martín proclamó la independencia{RESET}")
  elif respuesta_8 == "b":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, Manco Cápac no fue el último inca{RESET}")
  elif respuesta_8 == "c":
    puntaje += 10
    print(f"{GREEN}Respuesta correcta {nombre}, Atahualpa fue el útlimo inca{RESET}")
  elif respuesta_8 == "d":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, Tupac Amaru II se rebeló contra los españoles{RESET}")
  # Agregamos una respuesta secreta
  elif respuesta_8 == "i":
    puntaje += 10
    print(f"{RED}Casi nadie me descubre, para celebrar llevate 10 puntos{RESET}")

  print(f"{nombre} llevas {puntaje} puntos")
  time.sleep(2)
  clean() #Limpiamos pantalla

  # Hacemos una pausa para leer y entender el mensaje de la respuesta  
  # inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

  # Pregunta 9
  print(f"\n{GREEN}Nivel 9\n")
  print("La guerra de los 100 años duró:\n")
  print ("a) 100 años") 
  print ("b) 116 años") # Respuesta correcta
  print ("c) 10 años")
  print (f"d) 50 años{RESET}")
  # Solicita la respuesta del usuario y la almacenamos en una variable
  respuesta_9 = input("\nTu respuesta: ")
  # Evaluamos la respuesta ingresada
  while respuesta_9  not in ("a", "b", "c", "d", "y"):
    respuesta_9 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_9 == "a":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, coincidente con 100 pero no{RESET}")
  elif respuesta_9 == "b":
    puntaje += 10
    print(f"{GREEN}Respuesta correcta {nombre}, una guerra de 116 años? quien lo diría{RESET}")
  elif respuesta_9 == "c":
    puntaje /= 2
    print(f"{RED}Respuesta incorrecta {nombre}, no duró 10 años{RESET}")
  elif respuesta_9 == "d":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, 50 es casi la mitad de lo que duró{RESET}")
  # Agregamos una respuesta secreta
  elif respuesta_9 == "y":
    puntaje += 10
    print(f"{RED}Por poco adivinas, no te preocupes igual ganas 10 puntos extras{RESET}")

  print(f"{nombre} llevas {puntaje} puntos")
  time.sleep(2)
  clean() #Limpiamos pantalla

  # Hacemos una pausa para leer y entender el mensaje de la respuesta  
  # inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel\n")

  # Damos las instrucciones sobre la pregunta final
  print(f"""{YELLOW}{nombre} has llegado al nivel final, este es mi nivel favorito porque te doy la opción de triplicar tu puntaje si respondes correctamente o de lo contrario puedes perder la mitad de tu puntaje.
  Estas listo?{RESET}""")

  # Hacemos una pausa para leer y entender las instrucciones
  inicio = input("\nPresiona 'Enter' para continuar")

  # Categoria Matemáticas
  # Pregunta 10
  print(f"\n{GREEN}Nivel 10\n")
  print("¿A cuántas unidades equivale 10 decenas de millar?\n")
  print ("a) 100000 unidades") # Respuesta correcta
  print ("b) 10000 unidades") 
  print ("c) 100 centenas")
  print (f"d) 100000 decenas{RESET}")
  # Solicita la respuesta del usuario y la almacenamos en una variable
  respuesta_10 = input("\nTu respuesta: ")
  # Evaluamos la respuesta ingresada
  while respuesta_10  not in ("a", "b", "c", "d", "q"):
    respuesta_10 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_10 == "a":
    puntaje += (abs(puntaje) * 2)
    print(f"{GREEN}Excelente {nombre}, has triplicado tu puntaje{RESET}")
  elif respuesta_10 == "b":
    puntaje += 5
    print(f"{RED}Estuvo cerca {nombre}, te faltó un 0 pero igual te obsequio 5 puntos{RESET}")
  elif respuesta_10 == "c":
    puntaje -= 5
    print(f"{RED}Respuesta incorrecta {nombre}, por esta vez te restaré solo 5 puntos{RESET}")
  elif respuesta_10 == "d":
    puntaje /= 2
    print(f"{RED}{nombre} 100000 decenas es demasiado, perdiste la mitad de tu puntaje{RESET}")
  # Agregamos una respuesta secreta
  elif respuesta_10 == "q":
    print(f"{RED}Sorpresa! mantienes tu puntaje {nombre}{RESET}")

  print(f"{nombre} llevas {puntaje} puntos")
  time.sleep(2)
  clean() #Limpiamos pantalla

  # Hacemos una pausa para leer y entender el mensaje de la respuesta  
  # inicio = input("\nPresiona 'Enter' para continuar")
  
  # Oportunidad de duplicar puntaje aleatoriamente
  print(F"""\n{YELLOW}  Duplicas o Divides?\n 
  Tienes un ultima oportunidad de duplicar tu puntaje
  1.- Escogerás un número entre 1 y 6 y lanzaremos el dado
  2.- Si te toca el número que elegiste duplicas tus puntos
  3.- Si me toca el número que elija me llevo la mitad de tus puntos{RESET}""")

  # Condicionamos a solo ingresar número entre 1 y 6
  num_player = int(input(f"\n{GREEN}Ingresa tu número: "))
  while num_player not in range(1, 7):
    num_player = int(input("Ingresa un número entre 1 y 6: "))
  # Lanzamiento de dados para duplicar o dividir puntaje
  print(input("\nLanza el dado con 'Enter'"))
  dado_player= random.randint(1, 6)
  time.sleep(1)
  print(f"Tu dado es: {dado_player}")
  if num_player == dado_player:
    time.sleep(1)
    puntaje *= 2
    print("\nBien jugado! Duplicaste tu puntaje")
  else:
    time.sleep(1.5)
    num_pc = random.randint(1, 6)
    print(f"\nEs mi turno: {num_pc}\n")
    time.sleep(1)
    dado_pc = random.randint(1, 6)
    print(f"Mi dado es: {dado_pc}")
    if num_pc == dado_pc:
      puntaje /= 2
      time.sleep(1)
      print("\nTe gané, me llevo la mitad de tu puntaje")
    else:
      time.sleep(1)
      print(f"\nMantienes tu puntaje{RESET}")
  time.sleep(2)
  clean() #Limpiamos pantalla

  # Mostramos en pantalla el mensaje de despedida 
  print(f"\n{MAGENTA}Felicitaciones! has finalizado la trivia {nombre}, tienes un puntaje de {puntaje} puntos{RESET}") 
  
  # Preguntamos si desea volver a jugar la trivia
  print(f"\n{RED}Quieres seguir jugando?")
  answer = input("Ingresa Y para iniciar o N para finalizar: ").upper()
  if answer == f"Y{RESET}":
      game = True
      time.sleep(2)
      clean() #Limpiamos pantalla
  else:
      game = False
if game == False:
  print(f"\n{MAGENTA}Intentos realizados: {contador}")
  print(f"Gracias por jugar esta trivia, espero te hayas divertido {nombre}{RESET}\n")