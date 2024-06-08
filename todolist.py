import os

class Tache:
    
    def __init__(self, nom, description, est_faite=False) -> None:
        self.nom  = nom
        self.description = description
        self.est_faite = est_faite


def afficher_taches(taches):
    if len(taches) == 0:
        print("\nAucune tache à afficher pour l'instant! \n")
    print("Voici la liste des taches:\n")
    for index, tache in enumerate(taches):
        etat = 'Terminé' if tache.est_faite == True else "En cours"
        print(f"{index + 1}. {tache.nom} -- {etat}")
        print(f"    - {tache.description}")

def ajouter_tache(taches):
    nom = input("Entrez le nom de la tache: ")
    description = input("Entrez une description pour la tache: ")
    tache = Tache(nom=nom, description=description)
    taches.append(tache)
    

def marquer_terminer(taches):
    index = int(input("Entrez l'index de la tache: "))
    taches[index -1].est_faite = True
    
    
def supprimer_tache(taches):
    index = int(input("Entrez l'index de la tache: "))
    del taches[index -1]
    

def charger_taches(path):
    taches = list()
    if os.path.isfile(path=path):
        with open(path, "r") as f:
            for line in f:
                tache = line.strip().split(",")
                if len(tache) > 1:
                    taches.append(
                        Tache(tache[0], tache[1], bool(tache[2]))
                    )
    return taches


def sauvegarder_taches(fichier, taches):
    with open(fichier, "w") as f:
        for tache in taches:
            f.write(f"{tache.nom},{tache.description},{tache.est_faite}\n")

def main():
    
    options = """
    
    
    
        ### TODO LIST ###
        1. Lister les taches
        2. Ajouter une tache
        3. Marquer une tache terminé
        4. Supprimer une tache
        5. Sauvegarder les modifications
        6. Quitter
        
        Choisissez une option:
        
    """
    
    taches = charger_taches("taches.txt")
    while True:
        
        option = int(input(options))
        if option == 1:
            afficher_taches(taches)
        
        elif option == 2:
            ajouter_tache(taches)
            
        elif option == 3:
            marquer_terminer(taches)
            
        elif option == 4:
            supprimer_tache(taches)
            
        elif option == 5:
            sauvegarder_taches("taches.txt", taches)
        elif option == 6:
            sauvegarder_taches("taches.txt", taches)
            print("Merci d'avoir utilisé notre service!")
            break
        else:
            print("l'option invalide!\nVeuillez reesayer")
            
if __name__ == '__main__':
    main()
        
    

