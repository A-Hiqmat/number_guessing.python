import random

#On definit la fonction 
def jeux():
    #Pour eviter la reinitialisation à chaque partie du score, on la sort de la boucle des parties individuelle pour qu'elle compte leur ensemble
    score=0

    while True:
        #Par contre, on réinitialise les tentatives et le chiffre à deviner sinon ce n'est pas marrant
        tentative=0
        chiffre_inconnu= random.randint(1,100)
        print("J'ai choisi un nombre entre 1 et 100. Essayez de le deviner (si vous souhaitez quitter la partie A TOUT MOMENT écrivez : 0 )")
        print(f"Score: {score}")
    
        #On recréer une boucle qui va nout permettre de jouer indefiniment de nouvelle partie indépendante(car nous somme déjà à l'intérieur d'une boucle) 
        #Uniquement SI le nombre est deviné 
        while True:
            
            #On vérifie que la proposition soit bien un chiffre entier entre 1 et 100
            try:
                proposition = int(input("Votre proposition : "))
            except ValueError:
                print("Veuillez entrer un nombre valide !")
                continue
            #Ordre important car 0<1 donc == proposition < 1 
            if proposition == 0:
                print(f"Votre score total est de : {score} \nMerci d'avoir participé et à bientôt ")
                return
            if proposition > 100 or proposition < 1 :
                print("pour rappel, le chiffre inconnu est entre 1 et 100. Veuillez réessayer avec un chiffre valide")
                continue
            
            #Après verification ,on est sur que le chiffre entrée est une tentative valable peut importe sa valeur
            tentative += 1

            #Analyse de  la propositon
            if proposition == chiffre_inconnu:
                print(f"épatant, vous avez trouvé le chiffre inconnu qui était {chiffre_inconnu} en {tentative} essais !")
                score += 1      
                break   
            elif proposition < chiffre_inconnu:
                print("Trop bas, essayez plus grand !")
            else :#ou elif proposition > chiffre_inconnu
                print("Trop haut, essayez plus petit !")

#On appelle la fonction pour la démarrer
jeux()  