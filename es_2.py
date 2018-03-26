# To Do manager Lab 2 with sorted print

from sys import argv  # import modulo per parametri da linea di comando


def printMenu():  # Funzione per la stampa del menu
    print("------------------------------------------")
    print("1) Insert a new task")
    print("2) Remove a task")
    print("3) Show tasks")
    print("4) Exit")


def read_from_file(fileRead):
    lista = list()
    txt = open(fileRead, 'r')
    line = txt.readline().rstrip() #rstrip elimina i \n o simili
    while line != "": #la read ritorna una riga vuota in caso di EOF
        lista.append(line)
        line = txt.readline().rstrip()
    return lista


def save_on_file(tasks, file):
    txt = open(file, 'w')
    for task in tasks:
        txt.write(task)
        txt.write("\n") #stamp un a capo dopo ogni task
    txt.close()


def stampa_lista(lista):
    print("\n\n---------------------Lista dei task------------------\n")
    for task in lista:
        print(task)


script_name, file = argv  # leggo il nome dello script e il primo parametro
tasks = read_from_file(file)

while True:
    printMenu()
    cmd = input("Inserire il comando: ")
    if cmd == '1':
        task = input("Inserisci un task: ")
        tasks.append(task)
    elif cmd == '2':
        target = input("Inserisci un task da rimuovere: ")
        tasks.remove(target)
    elif cmd == '3':
        tasks.sort()
        stampa_lista(tasks)
    elif cmd == '4':
        save_on_file(tasks, 'saved.txt')
        exit(1)
