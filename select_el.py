import sys
import tkinter
import tkinter.filedialog as tkFileDialog


def exp_doss():
    dossier = tkFileDialog.askdirectory(title="Choisir le répertoire cible")
    if dossier:
        return dossier
    else: 
        print("Aucun chemin renvoyé")
        sys.exit(1)

def select_file():
    chemin = tkFileDialog.askopenfilename(title="Choisissez votre fichier Blender", filetypes=[("Blender files", "*.blend")])
    if chemin:
        return chemin
    else:
        print("Aucun chemin renvoyé")
        sys.exit(1)
