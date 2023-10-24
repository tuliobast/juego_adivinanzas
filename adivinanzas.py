"""
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
"""
import random

def create_house()-> (list, list):
    house= [list(["⬜️"]*4) for _ in range(4)]
    if random.choice([True, False]):
        door= [random.randint(0, 3), random.choice([0, 3])]
    else:
         door= [random.randint(0, 3), random.choice([0, 3])]

    house[door[0]][door[1]]= "🚪"

    def generate_candy(door: list) -> list:
        candy=[random.randint(0, 3), random.randint(0, 3)]
        if candy == door[0] and candy == door[1]:
            return generate_candy(door)
        return candy
    
    candy= generate_candy(door)
    house[candy[0]][candy[1]]= "🍭"

    for row in house:
        print("".join(map(str, row)))

    return house, door


def move(position: list) -> list:
    row, col= position[0],position[1]
    movements= "N S E O "

    if row == 0: movements = movements.replace("N ", "")
    if row == 3: movements = movements.replace("S ", "")
    if col == 0: movements = movements.replace("O ", "")
    if col == 3: movements = movements.replace("E ", "")

    movement= input(f"Hacia donde te quiere desplazar [{movements}]?: ").upper()

    if movement in movements: 
        if movement == "N": position =[row-1,col]
        elif movement == "S": position =[row+1,col]
        elif movement == "E": position =[row,col+1]
        elif movement == "O": position =[row,col-1]

        return position
    else:
        print("Desplazamiento incorrecto. Selecciona una de las opciones validas.")
        return move(position)
    

def riddle():
    while True:

        riddles = [
        ("¿Qué lenguaje de programación fue creado por Guido van Rossum?", "Python"),
        ("¿Cuál es el sistema operativo de código abierto más popular?", "Linux"),
        ("¿Qué compañía desarrolló el sistema operativo Windows?", "Microsoft"),
        ("¿Qué lenguaje de programación se utiliza principalmente para el desarrollo web del lado del cliente?", "JavaScript"),
        ("¿Cuál es el protocolo estándar para enviar correos electrónicos?", "SMTP"),
        ("¿Qué significa HTML?", "HyperText Markup Language"),
        ("¿Cuál es la base de datos relacional de código abierto más popular?", "MySQL"),
        ("¿Qué significa URL?", "Uniform Resource Locator"),
        ("¿Qué compañía desarrolló el lenguaje de programación Java?", "Sun"),
        ("¿Qué estructura de datos es LIFO?", "Pila"),
        ("¿Qué lenguaje de programación fue diseñado por Bjarne Stroustrup?", "C++"),
        ("¿Qué significa HTTP?", "HyperText Transfer Protocol"),
        ("¿Qué significa SQL?", "Structured Query Language"),
        ("¿Cuál es el lenguaje de hojas de estilo utilizado en la web?", "CSS"),
        ("¿Qué significa API?", "Application Programming Interface"),
        ("¿Qué estructura de datos es FIFO?", "Cola"),
        ("¿Cuál es el lenguaje de programación más antiguo aún en uso?", "Fortran"),
        ("¿Qué significa IDE?", "Integrated Development Environment"),
        ("¿Qué compañía es la creadora del sistema operativo macOS?", "Apple"),
        ("¿Qué lenguaje se utiliza comúnmente para el desarrollo de aplicaciones Android?", "Kotlin")
    ]

        current_riddle= riddles[random.randint(0, len(riddles)-1)]

        answer= input(f"{current_riddle[0]}: ")
        if answer.lower() == current_riddle[1].lower():
            print("Respuesta correcta!\n")
        else:
            print("Respuesta incorrecta!\n")

house, door= create_house()

position= door
print(f"Posicion Inicial: {position}\n")

print("""
👻 BOOooooOOOooooOO!
Si quieres encontrar el dulces de la casa encantada
tendras que buscarlos a traves de sus habitaciones.
Pero recuerda, no podras moverte si antes no respondes 
correctamente a su enigma""")

while True:
   
    position = move(position)
    print(f"Posicion: {position}")

    house_room = house[position[0]][position[1]]

    if house_room=="⬜️":
        print("Responde correctamente la pregunta.")
        riddle()
        ghost= random.randint(1,10)==1
        if ghost:
            print("""
          👻 BOOooooOOOooooOO!
           Para salir de esta habitacion deberas responder otra pregunta""")
            riddle()
    elif house_room =="🍭":
        print("""
          👻 BOOooooOOOooooOO!
          Has encontrado los dulces 🍭 y espacadp de la casa encantada 🏰
          """)
        
        break