import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_mistakes = 5
mistakes = 0
difficulty = 0
# Lista para almacenar las letras adivinadas
guessed_letters = [""]
letters = []
word_displayed ="_"*len(secret_word)
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
while difficulty>3 or difficulty<1 :
    difficulty=int(input("Selecciona una dificultad:\n[1] Facil: se muestran todas las vocales\n[2] Intermedio: se muestran la primera y última letra\n[3] Difícil: no se muestra ninguna letra\n"))
    if difficulty==3:   
        break
    elif difficulty ==2:
        guessed_letters.extend([secret_word[0], secret_word[-1]])
    elif difficulty ==1:
        guessed_letters.extend(["a","e","i","o","u","á","é","í","ó","ú"])
    else: 
        difficulty=int(input("Ingrese un número entre 1 y 3.\n[1] Facil: se muestran todas las vocales\n[2] Intermedio: se muestran la primera y última letra\n[3] Difícil: no se muestra ninguna letra\n"))
# Mostrarla palabra parcialmente adivinada
for letter in secret_word:
    if letter in guessed_letters:
        letters.append(letter)
    else:
        letters.append("_")
word_displayed = "".join(letters)
print(f"Palabra: {word_displayed}")
while (mistakes< max_mistakes):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    if letter == "":
        print ("Error! Ingresa una letra válida.")
        continue
    # Verificar si la letra ya ha sido adivinada
    else:
        if letter in guessed_letters:
            print("Ya has intentado con esa letra. Intenta con otra.")
            continue
        # Agregar la letra a la lista de letras adivinadasNota: Por cada funcionalidad agregada se debe realizar al menos un commit que identifique el cambio.
        guessed_letters.append(letter)
        # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            mistakes+=1
            print(f"Lo siento, la letra no está en la palabra. Acumulas {mistakes} error(es)")
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
        # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has alcanzado los {max_mistakes} errores.")
    print(f"La palabra secreta era: {secret_word}")
