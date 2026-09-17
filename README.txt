WINTER ARC — mini SaaS local
=============================

Contenu de ce dossier :
  - index.html          -> l'application
  - server.py            -> petit serveur local (lit/écrit les .json)
  - transactions.json    -> tes mouvements de wallet
  - goals.json           -> tes objectifs
  - journal.json         -> tes entrées de journaling

Ces trois fichiers .json sont lus et réécrits directement par
l'application à chaque ajout, modification ou suppression. Tu peux
les ouvrir avec un éditeur de texte pour voir tes données brutes, ou
les copier ailleurs pour faire une sauvegarde.

COMMENT LANCER L'APPLICATION
-----------------------------
Il faut Python 3, déjà installé par défaut sur Mac et la plupart des
distributions Linux. Sous Windows, installe-le une fois depuis
https://python.org (coche "Add Python to PATH" pendant l'installation).

1. Ouvre un terminal (ou une invite de commandes) dans ce dossier.
   - Windows : clic droit dans le dossier -> "Ouvrir dans le terminal"
   - Mac : clic droit dans le Finder -> Services -> "Nouveau terminal
     au dossier" (ou glisse le dossier dans l'app Terminal)
2. Lance :
     python3 server.py
   (sous Windows, si ça ne marche pas, essaie : python server.py)
3. Ton navigateur s'ouvre automatiquement sur http://localhost:8420
   Sinon, ouvre cette adresse toi-même.
4. Laisse la fenêtre du terminal ouverte tant que tu utilises
   l'application. Pour l'arrêter : Ctrl+C dans le terminal.

IMPORTANT
---------
N'ouvre pas index.html directement (double-clic) : sans le serveur,
la page ne peut ni lire ni écrire les fichiers .json. Passe toujours
par http://localhost:8420 après avoir lancé server.py.

Astuce : crée un raccourci vers server.py, ou un script de lancement,
pour démarrer Winter Arc plus vite au quotidien.
