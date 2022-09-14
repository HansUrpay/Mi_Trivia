import random  # Importamos la librería random para crear un numero aleatorio 

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 10)

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("\nBienvenido a mi trivia sobre cultura general")
print ("Pondremos a prueba tus conocimientos\n")


# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable
nombre = input("Ingresa tu nombre: ")

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla
# OJO, el \n al final o al inicio de la línea es para dar un "salto de línea"
print(f"\n Hola {nombre}, lee con atencion las intrucciones de la trivia:\n" 
"\n 1.- Hay diferentes preguntas con múltiples respuestas"
"\n 2.- Responde con la letra de la alternativa correcta y presiona 'Enter' para pasar al siguiente nivel"
f"\n 3.- Inicias con {puntaje} puntos, hay respuestas que restaran, sumaran o te haran perder la mitad de tu puntaje pero la respuesta correcta duplicará tus puntos"
"\n Buena suerte!\n")

# Hacemos una pausa para leer y entender las instrucciones
inicio = input("Presiona 'Enter' para iniciar")

# Categoria Deporte

# Pregunta 1
print("\nNivel 1")
print("¿Que país ha ganado mas copas del mundo en fútbol?")
print ("a) Brasil") # Respuesta correcta
print ("b) Alemania") 
print ("c) Inglaterra") 
print ("d) Argentina") 
# Solicitamos la respuesta del usuario y la almacenamos en una variable
respuesta_1 = input("\nTu respuesta: ")
# Evaluamos la respuesta ingresada
while respuesta_1 not in ("a", "b", "c", "d", "h"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
# Ahora verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_1 == "a":
  puntaje *= 2
  print(f"Correcto {nombre}, Brasil es pentacampeon mundial!")
elif respuesta_1 == "b":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, Alemania es tetracampeon")
elif respuesta_1 == "c":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, Inglaterra solo tiene un título")
elif respuesta_1 == "d":
  puntaje /= 2
  print(f"Respuesta incorrecta {nombre}, Argentina ganó 2 mundiales")
# Agregamos una respuesta secreta
elif respuesta_1 == "h":
  puntaje += 10
  print(f"Oh! no es la respuesta correcta pero te regalo 5 puntos")

print(f"{nombre} llevas {puntaje} puntos")
# Hacemos una pausa para leer y entender el mensaje de la respuesta  
inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

#  Pregunta 2
print("\nNivel 2")
print("¿Quién es el atleta mas rápido a nivel mundial en 100 metros?")
print ("a) Michael Jordan")
print ("b) Tyson Gay")
print ("c) Gareth Bale")
print ("d) Usain Bolt") # Respuesta correcta
# Solicita la respuesta del usuario y la almacenamos en una variable
respuesta_2 = input("\nTu respuesta: ")
# Evaluamos la respuesta ingresada
while respuesta_2  not in ("a", "b", "c", "d", "e"):
  respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_2 == "a":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, Michael Jordan es basquetbolista")
elif respuesta_2 == "b":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, Tyson Gay no es el atleta mas rápido")
elif respuesta_2 == "c":
  puntaje /= 2
  print(f"Respuesta incorrecta {nombre}, Gareth Bale es un jugador de fútbol")
elif respuesta_2 == "d":
  puntaje *= 2
  print(f"Asi es {nombre}, Usain Bolt es el hombre mas rápido del mundo")
# Agregamos una respuesta secreta
elif respuesta_2 == "e":
  puntaje += 10
  print(f"Has obtenido 5 puntos extras")

print(f"{nombre} llevas {puntaje} puntos")
# Hacemos una pausa para leer y entender el mensaje de la respuesta  
inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

#  Pregunta 3
print("\nNivel 3")
print("¿Que es un decatlón?")
print ("a) Un deporte olímpico")
print ("b) Una competencia atlética de 10 pruebas combinadas") # Respuesta correcta
print ("c) Una maraton de 40 km")
print ("d) Un juego entre 2 equipos")
# Solicita la respuesta del usuario y la almacenamos en una variable
respuesta_3 = input("\nTu respuesta: ")
# Evaluamos la respuesta ingresada
while respuesta_3  not in ("a", "b", "c", "d", "f"):
  respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_3 == "a":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, no es un deporte")
elif respuesta_3 == "b":
  puntaje *= 2
  print(f"Respuesta correcta {nombre}, el declatlón es una competencia de 10 pruebas")
elif respuesta_3 == "c":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, el decatlon no incluye maraton de de 40 km")
elif respuesta_3 == "d":
  puntaje /= 2
  print(f"Respuesta incorrecta {nombre}, no es un juego entre 2 equipos")
# Agregamos una respuesta secreta
elif respuesta_3 == "f":
  puntaje += 10
  print(f"Me descubriste! ten 5 puntos por eso")

print(f"{nombre} llevas {puntaje} puntos")
# Hacemos una pausa para leer y entender el mensaje de la respuesta  
inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

# Categoria Cine
# Pregunta 4
print("\nNivel 4")
print("¿Quien es el protagonista de la película 'Thor'?")
print ("a) Robert Downey Jr.")
print ("b) Chris Evans")
print ("c) Chris Hemsworth") # Respuesta correcta
print ("d) Tom Hiddleston") 
# Solicita la respuesta del usuario y la almacenamos en una variable
respuesta_4 = input("\nTu respuesta: ")
# Evaluamos la respuesta ingresada
while respuesta_4  not in ("a", "b", "c", "d", "j"):
  respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_4 == "a":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, Robert Downey Jr. es Iron Man")
elif respuesta_4 == "b":
  puntaje /= 2
  print(f"Respuesta incorrecta {nombre}, él es otro Chris")
elif respuesta_4 == "c":
  puntaje *= 2
  print(f"Respuesta correcta {nombre}, Chris Hemsworth interpreta a Thor ")
elif respuesta_4 == "d":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, Tom Hiddleston interpreta a Loki")
# Agregamos una respuesta secreta
elif respuesta_4 == "j":
  puntaje += 10
  print(f"Vaya! acepta estos 5 puntos extras")

print(f"{nombre} llevas {puntaje} puntos")
# Hacemos una pausa para leer y entender el mensaje de la respuesta  
inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

# Pregunta 5
print("\nNivel 5")
print("¿En que año se estrenó Corazon Valiente?")
print ("a) 1998")
print ("b) 2000")
print ("c) 2005")
print ("d) 1995") # Respuesta correcta
# Solicita la respuesta del usuario y la almacenamos en una variable
respuesta_5 = input("\nTu respuesta: ")
# Evaluamos la respuesta ingresada
while respuesta_5  not in ("a", "b", "c", "d", "l"):
  respuesta_5 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_5 == "a":
  puntaje /= 2
  print(f"Respuesta incorrecta {nombre}, en 1998 se estrenó Armageddon")
elif respuesta_5 == "b":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, en el año 2000 terminó el siglo XX")
elif respuesta_5 == "c":
  puntaje -= 5
  print(f"Respuesta correcta {nombre}, en el 2005 se estrenó Harry Potter y el cáliz de fuego")
elif respuesta_5 == "d":
  puntaje *= 2
  print(f"Respuesta correcta {nombre}, Corazon Valiente con Mel Gibson se estrenó en 1995")
# Agregamos una respuesta secreta
elif respuesta_5 == "l":
  puntaje += 10
  print(f"Buen intento! no vienen mal 10 puntos mas")

print(f"{nombre} llevas {puntaje} puntos")
# Hacemos una pausa para leer y entender el mensaje de la respuesta  
inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

# Pregunta 6
print("\nNivel 6")
print("¿Hasta el 2018 cuantas peliculas tiene la saga 'Piratas del Caribe'?")
print ("a) 5") # Respuesta correcta
print ("b) 6")
print ("c) 4")
print ("d) 7")
# Solicita la respuesta del usuario y la almacenamos en una variable
respuesta_6 = input("\nTu respuesta: ")
# Evaluamos la respuesta ingresada
while respuesta_6  not in ("a", "b", "c", "d", "p"):
  respuesta_6 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_6 == "a":
  puntaje *= 2
  print(f"Correcto {nombre}, Piratas del Caribe tiene 5 películas y un cortometraje")
elif respuesta_6 == "b":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, Piratas del Caribe solo tiene 5 películas y un cortometraje")
elif respuesta_6 == "c":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, Piratas del Caribe no tiene 4 películas")
elif respuesta_6 == "d":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, 7 es demasiado")
# Agregamos una respuesta secreta
elif respuesta_6 == "p":
  print(f"No soy la respuesta correcta pero tampoco perdiste puntos")

print(f"{nombre} llevas {puntaje} puntos")
# Hacemos una pausa para leer y entender el mensaje de la respuesta  
inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

# Categoria Historia
# Pregunta 7
print("\nNivel 7")
print("¿Quien gobernaba en el antiguo Egipto?")
print ("a) El emperador") 
print ("b) El zar") 
print ("c) El faraon") # Respuesta correcta
print ("d) El presidente")
# Solicita la respuesta del usuario y la almacenamos en una variable
respuesta_7 = input("\nTu respuesta: ")
# Evaluamos la respuesta ingresada
while respuesta_7  not in ("a", "b", "c", "d", "m"):
  respuesta_7 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_7 == "a":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, el emperador gobernó Roma")
elif respuesta_7 == "b":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, los zares eran rusos")
elif respuesta_7 == "c":
  puntaje += 10
  print(f"Respuesta correcta {nombre}, los faraones gobernaban en Egipto")
elif respuesta_7 == "d":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, no habian presidentes en el antiguo Egipto")
# Agregamos una respuesta secreta
elif respuesta_7 == "m":
  print(f"Estuviste cerca, no es la respuesta correcta tampoco perderás puntos")

print(f"{nombre} llevas {puntaje} puntos")
# Hacemos una pausa para leer y entender el mensaje de la respuesta  
inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

# Pregunta 8
print("\nNivel 8")
print("Quien fue el ultimo inca del Imperio Incaico?")
print ("a) José de San Martín") 
print ("b) Manco Cápac")
print ("c) Atahualpa") # Respuesta correcta
print ("d) Tupac Amaru II")
# Solicita la respuesta del usuario y la almacenamos en una variable
respuesta_8 = input("\nTu respuesta: ")
# Evaluamos la respuesta ingresada
while respuesta_8  not in ("a", "b", "c", "d", "i"):
  respuesta_8 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_8 == "a":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, José de San Martín proclamó la independencia")
elif respuesta_8 == "b":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, Manco Cápac no fue el último inca")
elif respuesta_8 == "c":
  puntaje += 10
  print(f"Respuesta correcta {nombre}, Atahualpa fue el útlimo inca")
elif respuesta_8 == "d":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, Tupac Amaru II se rebeló contra los españoles")
# Agregamos una respuesta secreta
elif respuesta_8 == "i":
  print(f"Casi aciertas, no perderás puntos en esta ocación")

print(f"{nombre} llevas {puntaje} puntos")
# Hacemos una pausa para leer y entender el mensaje de la respuesta  
inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

# Pregunta 9
print("\nNivel 9")
print("La guerra de los 100 años duró:")
print ("a) 100 años") 
print ("b) 116 años") # Respuesta correcta
print ("c) 10 años")
print ("d) 50 años")
# Solicita la respuesta del usuario y la almacenamos en una variable
respuesta_9 = input("\nTu respuesta: ")
# Evaluamos la respuesta ingresada
while respuesta_9  not in ("a", "b", "c", "d", "y"):
  respuesta_9 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_9 == "a":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, coincidente con 100 pero no")
elif respuesta_9 == "b":
  puntaje += 10
  print(f"Respuesta correcta {nombre}, una guerra de 116 años? quien lo diría")
elif respuesta_9 == "c":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, no duró 10 años")
elif respuesta_9 == "d":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, 50 es casi la mitad de lo que duró")
# Agregamos una respuesta secreta
elif respuesta_9 == "y":
  print(f"Por poco adivinas, no te preocupes no perderás puntos por ahora")

print(f"{nombre} llevas {puntaje} puntos")
# Hacemos una pausa para leer y entender el mensaje de la respuesta  
inicio = input("\nPresiona 'Enter' para avanzar al siguiente nivel")

# Damos las instrucciones sobre la pregunta final
print(f"\n{nombre} has llegado al nivel final, este es mi nivel favorito porque te doy la opción de duplicar"
"\ntu puntaje si respondes correctamente o de lo contrario puedes perder la mitad de tu puntaje. \nEstas listo?")

# Hacemos una pausa para leer y entender las instrucciones
inicio = input("\nPresiona 'Enter' para continuar")

# Categoria Matemáticas
# Pregunta 10
print("\nNivel 10")
print("¿A cuántas unidades equivale 10 decenas de millar?")
print ("a) 100000 unidades") # Respuesta correcta
print ("b) 10000 unidades") 
print ("c) 100 centenas")
print ("d) 100000 decenas")
# Solicita la respuesta del usuario y la almacenamos en una variable
respuesta_10 = input("\nTu respuesta: ")
# Evaluamos la respuesta ingresada
while respuesta_10  not in ("a", "b", "c", "d", "q"):
  respuesta_10 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_10 == "a":
  puntaje *= 2
  print(f"Excelente {nombre}, has duplicado tu puntaje")
elif respuesta_10 == "b":
  puntaje += 5
  print(f"Estuvo cerca {nombre}, te faltó un 0 pero igual te obsequio 5 puntos")
elif respuesta_10 == "c":
  puntaje -= 5
  print(f"Respuesta incorrecta {nombre}, por esta vez te restaré solo 5 puntos")
elif respuesta_10 == "d":
  puntaje /= 2
  print(f"{nombre} 100000 decenas es demasiado, perdiste la mitad de tu puntaje")
# Agregamos una respuesta secreta
elif respuesta_10 == "q":
  print(f"Sorpresa! mantienes tu puntaje {nombre}")

# Mostramos en pantalla el mensaje de despedida 
print(f"\nFelicitaciones {nombre}, has finalizado la trivia con un puntaje de {puntaje} puntos") 
print("Gracias por jugar esta trivia, espero te hayas divertido\n")
