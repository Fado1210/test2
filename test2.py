import csv


def fn_question(question):
    return input(question)


def fn_encode(marque, modele, couleur, cylindre, motorisation, anneeprod):
    file_csv = "test2.csv"
    header = ["marque", "modele", "couleur", "cylindre", "motorisation", "anneeprod"]
    data = [marque, modele, couleur, cylindre, motorisation, anneeprod]
    with open(file_csv, "w", encoding="utf-8", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(header)
        writer.writerow(data)


def fn_est_ancetre(anneeprod):
    if (2021 - anneeprod) >= 25:
        return True
    else:
        return False

q_marque = "Entrez la marque : "
marque = fn_question(q_marque)
q_modele = "Entrez le modele : "
modele = fn_question(q_modele)
q_couleur = "entrez la couleur : "
couleur = fn_question(q_couleur)
q_cylindre = "Entrez le cylindré : "
cylindre = fn_question(q_cylindre)
q_motorisation = "Entrez la motorisation : "
motorisation = fn_question(q_motorisation)
q_anneeprod = "Entrez l'année de production du véhicule : "
anneeprod = int(fn_question(q_anneeprod))

fn_encode(marque, modele, couleur, cylindre, motorisation, anneeprod)

if fn_est_ancetre(anneeprod):
    print(marque, modele, "est ancetre")
else:
    print(marque, modele, "est pas un ancetre")