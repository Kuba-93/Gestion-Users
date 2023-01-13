import csv

student_fields = ['nom', 'prenom', 'age', 'ville']
student_database = 'data.csv'


def display_menu():
    print("Gestion des Users")
    print("1. Ajouter une personne")
    print("2. Afficher une personne")
    print("3. Modifier une personne")
    print("4. Supprimer une personne")
    print("5. Quitter")


def add_student():
    print("Ajouter les informations de la personne")
    global student_fields
    global student_database


    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("")
    input("Appuyez sur n'importe quelle touche pour continuer")
    return


def view_students():
    global student_fields
    global student_database

    print("--- Dossiers des étudiants ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n--------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Appuyez sur n'importe quelle touche pour continuer")


def update_student():
    global student_fields
    global student_database

    print("--- Mettre à jour l'élève ---")
    roll = input("Entrez l'ID a mettre à jour: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Étudiant trouvé : ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Introuvable")

    input("Appuyez sur n'importe quelle touche pour continuer")


def delete_student():
    global student_fields
    global student_database

    print("--- Étudiant supprimer ---")
    roll = input("Entrez l'ID pour supprimer: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("", roll, "Supprimé avec succès")
    else:
        print("Introuvable")

    input("Appuyez sur n'importe quelle touche pour continuer")

while True:
    display_menu()

    choice = input("Choisissez une option: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    else:
        break

print("Merci !")


