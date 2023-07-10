############################################
# Script - Rapport Nessus  #
############################################

#Importation des modules
import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext
import os
import sys
import time

#Partie 1 - Saisir le nom du rapport de  scan Nessus 

# Créer une fenêtre principale
fenetre = tk.Tk()

# Configurer les dimensions de la fenêtre de dialogue
fenetre.geometry("400x200")

# Afficher la boîte de dialogue pour saisir quelque chose
fenetre.withdraw()
nom_fichier = simpledialog.askstring("Saisir le nom du fichier", "Entrez le nom du fichier :", parent=fenetre) 

# Vérifier si une saisie a été faite
if nom_fichier:
    print("Le nom de fichier saisi est :", nom_fichier)
    if os.path.exists(nom_fichier):
        print("Le fichier existe dans le répertoire courant, passons à l'étape suivante.")
    else:
        print("Le fichier n'existe pas dans le répertoire courant. Fin du programme.")
        sys.exit()
else:
    print("Aucun nom de fichier saisi. Fin du programme.")
    sys.exit()
  

# Fermer la fenêtre principale
fenetre.destroy()

######################
# Fin de la partie 1 #
######################

#Partie 2 - Supprimer les vulnérabilités LOW et INFO du rapport de scan Nessus"
print("############################################")
print("Suppression des vulnérabilités 'INFO' du rapport de scan Nessus en cours...")
time.sleep(2)

def supprimer_contenu_apres_background(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            lignes = fichier.readlines()
            print("Le contenu du ", nom_fichier, " a été lu avec succès. voici le nombre de ligne ", len(lignes))
            

        for i, ligne in enumerate(lignes):
            if "width: 100%; margin: 0 0 10px 0; padding: 5px 10px; background: #67ACE1;" in ligne:
                lignes = lignes[:i]  # Conserver les lignes jusqu' la premire ligne info
                break

        with open(nom_fichier, 'w') as fichier:
            fichier.writelines(lignes)
        print("Vulnérabilités INFO supprimées avec succès.")
    except IOError:
        print("Erreur lors de la lecture ou de l'écriture du fichier.")
        sys.exit()

# Utilisation de la fonction pour supprimer le contenu après la ligne "background: #F8C851"
supprimer_contenu_apres_background(nom_fichier)

######################
# Fin de la partie 2 #
######################

#Partie 3 - Modification header du rapport de scan Nessus"
print("############################################")
print("Modification du header du rapport de scan Nessus en cours...")
time.sleep(2)

#Demande de titre du rapport
#Fonction appelée lorsque le bouton "Ok" de la pop-up est cliqué
def get_input_value():
    global input_value
    input_value = entry.get()
    popup.destroy()

# Ouvrir une pop-up pour saisir le contenu
popup = tk.Tk()
popup.title("Saisie de contenu")

# Définir les dimensions de la pop-up
popup_width = 400
popup_height = 200
screen_width = popup.winfo_screenwidth()
screen_height = popup.winfo_screenheight()
x = (screen_width - popup_width) // 2
y = (screen_height - popup_height) // 2
popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

label = tk.Label(popup, text="Entrez le titre qui sera affiché dans le fichier HTML :")
label.pack()
entry = tk.Entry(popup)
entry.pack()
button = tk.Button(popup, text="Ok", command=get_input_value)
button.pack()
popup.mainloop()


def remplacer_ligne(fichier, ligne_a_remplacer, nouvelle_ligne):
    with open(fichier, 'r') as f:
        lignes = f.readlines()

    #if ligne_a_remplacer < 1 or ligne_a_remplacer > len(lignes):
        #print("La ligne à remplacer n'est pas valide.")
        #return 

    lignes[ligne_a_remplacer - 1] = nouvelle_ligne + '\n'

    with open(fichier, 'w') as f:
        f.writelines(lignes)

    print("Le header a été remplacé avec succès.")

# Chemin vers le fichier à traiter
chemin_fichier = nom_fichier

# Numéro de la ligne à remplacer
ligne_a_remplacer = 258

# Nouvelle ligne
nouvelle_ligne = '''</script></head><body><div id="report" style="width: 1024px; box-sizing: border-box; margin: 0 auto; background: #fff; padding: 0 20px 20px 20px; border-top: #263746 solid 3px; box-shadow: 0 2px 10px rgba(0, 0, 0, .2); margin-bottom: 20px; border-radius: 0 0 3px 3px;"
<div id="report" style="width: 1024px; box-sizing: border-box; margin: 0 auto; background: #fff; padding: 0 20px 20px 20px; border-top: #263746 solid 3px; box-shadow: 0 2px 10px rgba(0, 0, 0, .2); margin-bottom: 20px; border-radius: 0 0 3px 3px;">
    <header style="width: 100%; border-bottom: 1px dotted #ccc; padding: 20px 0; margin: 0 0 20px 0; display: flex; align-items: center;">
        <div style="float: left; margin-left: 250px;">
            <h1>
                <img src="#FILEOFYOURIMAGE" height="225" border="0" alt="LOGO " style="display: block;"></img> </h1> </div>
        <div style="float: right;">
            <h1 style="font-size: 18px;">SSI-Rapport scan Nessus</h1>
            <h2 style="color: #999; text-align: right">Report generated by Nessus| Modified by SSI</h2>
        </div><br> <meta charset="UTF-8">
        <div class="clear"></div>
    </header>
    <div class="clear"></div><h3 style="font-size: 24px; font-weight: 300;">{}</h3><h4 style="color: #999; border-bottom: 1px dotted #ccc; padding: 0 0 0px 0; margin: 0 0 20px 0;"></h4><div class="clear"></div><div style="width: 100%;">
    <div style="width: 100%;">
    </div>
</div>
        <h5 xmlns="" style="font-size: 16px; font-weight: 700; margin-bottom: 20px;">TABLE OF CONTENTS</h5>
        <ul xmlns="" style="list-style-type: none; margin-bottom: 20px;">
<li style="font-size: 14px;">
<a href="#idp998" style="font-weight: 700;">Remediations SSI</a><ul style="list-style-type: disc; margin: 10px 0 0 20px;"><li style="margin: 0 0 10px 0; color: #000000;"><a href="#idp999">Recommandations SSI</a></li></ul>
</li>'''.format(input_value)

# Utilisation de la fonction pour remplacer la ligne
remplacer_ligne(chemin_fichier, ligne_a_remplacer, nouvelle_ligne)

######################
# Fin de la partie 3 #
######################

#Partie 4 - Modification header du rapport de scan Nessus / ajout commentaire SSI"
print("############################################")
print("Ajout des commentaires SSI en cours...")
time.sleep(2)



def valider_texte():
    texte_saisi = texte_widget.get("1.0", tk.END).strip()

    if texte_saisi:
        nom_fichier_html = nom_fichier  # Remplacez par le chemin réel vers votre fichier HTML
        try:
            with open(nom_fichier_html, 'a') as fichier:
                fichier.write(texte_saisi + "\n")
            print("Texte ajouté avec succès dans le fichier HTML.")
        except FileNotFoundError:
            print("Le fichier n'a pas été trouvé.")
            sys.exit()
        except IOError:
            print("Erreur lors de l'écriture du fichier.")
            sys.exit()
    else:
        print("Aucun texte saisi.")
        sys.exit()

    # Fermer la fenêtre principale
    fenetre.destroy()

# Création de la fenêtre principale
fenetre = tk.Tk()

# Création du widget de texte multiligne
texte_widget = scrolledtext.ScrolledText(fenetre, width=150, height=35)
texte_widget.pack()

# Préremplir du texte dans la boîte de dialogue

texte_predefini = '''<!-- NE PAS SUPPRIMER -->\n
<h6 xmlns="" id="idp998" style="padding: 20px 0; border-top: 1px dotted #ccc; border-bottom: 1px dotted #ccc; font-size: 20px; font-weight: 400; line-height: 20px;">Remediations SSI</h6>

<div xmlns="" id="idp999" style="font-size: 22px; font-weight: 700; padding: 10px 0; overflow-wrap: break-word">Recommandations SSI<div class="clear"></div></div> \n<!-- NE PAS SUPPRIMER --> \n\n
<!-- ##################################################################################### -->
<p>Voici les recommandations SSI a appliquer sur le serveur. </p><div class="clear"></div><br>
\n <p> <!-- Commentaire COMPLEMENTAIRE--> </p> \n<br> \n <ul> \n <li></li> \n <li></li> \n <li></li> \n </ul> \n <br> \n<p> 
<!-- ##################################################################################### --> \n
<!-- exemple de balise a utiliser dans le rapport-->
<!-- 
<li class="warning">Ce texte sera en orange et en gras.</li>
<li class="danger">Ce texte sera en rouge et en gras.</li>
<li> Ce texte sera en noir</li>
-->

\n\n\n\n\n\n\n\n\n

<!--NE PAS SUPPRIMER-->

<style>
li.danger {
    color: red; /* Texte en rouge */
    font-weight: bold;
  }
  
  li.warning {
    color: orange; /* Texte en orange */
    font-weight: bold;
  }
</style>
'''

texte_widget.insert(tk.END, texte_predefini)

# Bouton de validation
bouton_valider = tk.Button(fenetre, text="Valider", command=valider_texte)
bouton_valider.pack()

# Démarrer la boucle principale
fenetre.mainloop()


######################
# Fin de la partie 4 #
######################

#Partie 5 - ajout du </body> et </html> en fin de fichier
print("############################################")
print("Finalisation du fichier HTML en cours...")
time.sleep(2)

def ajouter_contenu_html(nom_fichier, contenu_ajoute):
    try:
        with open(nom_fichier, 'a') as fichier:
            fichier.write(contenu_ajoute)
        print("Fin de code ajouté avec succès.")
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
        sys.exit()
    except IOError:
        print("Erreur lors de l'écriture du fichier.")
        sys.exit()

# Ajouter le contenu à la fin du fichier HTML
contenu_ajoute = '<br><div style="width: 1024px; box-sizing: border-box; text-align: center; font-size: 12px; color: #999; padding: 10px 0 20px 0; margin: 0 auto;"> Rapport Scan Nessus - SSI  - CONFIDENTIEL </div></body></html>'
ajouter_contenu_html(nom_fichier, contenu_ajoute)

######################
# Fin de la partie 5 #
######################

#Partie 6 - Ouverture du fichier HTML
filename = nom_fichier
print("Le Rapport est pret sous le nom : " + nom_fichier)
os.system(f'start {filename}')


################################
## Fin du Programme SSI ##
################################