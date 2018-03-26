# To Do manager Lab 2 with sorted print

def printMenu(): #Funzione per la stampa del menu
    print("------------------------------------------")
    print("1) Insert a new task")
    print("2) Remove a task")
    print("3) Show tasks")
    print("4) Exit")


tasks = list()

while cmd != '4':
    printMenu()
    cmd = input("Inserire il comando: ")
    if cmd == '1':
        task = input("Inserisci un task: ")
        tasks.append(task)
    elif cmd == '2':
        target = input("Inserisci un task da rimuovere: ")
        tasks.remove(target)
    elif cmd == '3':
        print(sorted(tasks))