# ❄️ Winter Arc

Un mini-SaaS personnel, ultraminimaliste, pour suivre ton *Winter Arc* : finances, objectifs quotidiens, journaling et compte à rebours jusqu'au 25 décembre — le tout auto-hébergé, sans compte, sans cloud, sans dépendance.

Aucune base de données, aucun framework : une page HTML/CSS/JS auto-contenue et un serveur Python de ~150 lignes (bibliothèque standard uniquement) qui lit et écrit directement dans des fichiers `.json` à la racine du projet.

---

## ✨ Fonctionnalités

| Page | Ce qu'elle fait |
|---|---|
| **Dashboard** | Compte à rebours jusqu'au 25 décembre (jour X / Y, barre de progression, date de départ modifiable), résumé du wallet global et du jour, avancement des objectifs, statut du journal du jour |
| **Wallet** | Mini comptabilité : boutons **+** / **−** pour ajouter un mouvement (montant + raison), solde total, historique complet |
| **Calendar** | Grille mensuelle avec le solde du jour en couleur (vert positif, rouge négatif, gris à zéro) — clique une date pour ouvrir directement le journaling de ce jour |
| **Goals** | Objectifs **quotidiens** à cocher chaque jour, streak 🔥 en cours par objectif, grille de suivi façon *GitHub contributions* |
| **Journaling** | Minuteur **Pomodoro** de 10 min pour la session d'écriture, texte du jour + note sur 5, historique consultable, courbe d'évolution de la note dans le temps |

Design ultraminimaliste, crème & terracotta, typo Fraunces/Inter — dans l'esprit de claude.ai. Mode sombre automatique selon les préférences système. Interface adaptée mobile (navigation en barre basse).

---

## 🗂 Structure du projet

```
winter-arc/
├── index.html          # l'application (une seule page, aucune dépendance externe)
├── server.py            # serveur local (Python 3, bibliothèque standard uniquement)
├── transactions.json    # mouvements du wallet
├── goals.json            # objectifs et historique de streaks
├── journal.json          # entrées de journaling
├── settings.json         # réglages (date de départ du Winter Arc)
└── README.md
```

Chaque fichier `.json` est lu et réécrit en clair à chaque action — ouvre-les avec n'importe quel éditeur de texte pour inspecter ou sauvegarder tes données brutes.

---

## 🚀 Démarrage

**Prérequis :** Python 3 (déjà installé sur macOS/Linux ; sur Windows, installe-le depuis [python.org](https://python.org) en cochant *Add Python to PATH*).

```bash
git clone https://github.com/<ton-compte>/winter-arc.git
cd winter-arc
python3 server.py
```

Le navigateur s'ouvre automatiquement sur **http://localhost:8420**. Si ce n'est pas le cas, ouvre l'adresse toi-même.

> ⚠️ N'ouvre jamais `index.html` directement (double-clic) : par sécurité, un fichier HTML seul ne peut pas lire/écrire de fichiers sur le disque. Il faut toujours passer par `server.py`.

### Accès depuis tout le réseau local

Le serveur écoute sur `0.0.0.0` : au démarrage, le terminal affiche l'adresse à utiliser depuis un autre appareil du même réseau Wi-Fi (téléphone, tablette...) :

```
- Sur cet appareil : http://localhost:8420
- Depuis un autre appareil du réseau : http://192.168.x.x:8420
```

### Utilisation sur Android (Termux)

```bash
pkg install python
termux-setup-storage
cd ~/storage/downloads/winter-arc
python server.py
```
Ouvre ensuite `http://localhost:8420` dans le navigateur du téléphone.

---

## 🛠 Stack technique

- **Frontend** : HTML/CSS/JS vanilla, aucune dépendance de build, aucune librairie externe (hormis les polices Google Fonts)
- **Backend** : `http.server` de la bibliothèque standard Python — pas de Flask, pas de Django, pas de `pip install`
- **Stockage** : fichiers `.json` en clair, à la racine du projet — lisibles, versionnables, sauvegardables en un copier-coller

---

## 💾 Sauvegarde de tes données

Tes données vivent uniquement dans les fichiers `.json` de ce dossier. Pour les sauvegarder ou les transférer sur un autre appareil, copie simplement ces quatre fichiers :

```
transactions.json  goals.json  journal.json  settings.json
```

---

## 📌 Idées d'évolution

- [ ] Export / import en un clic (zip des `.json`)
- [ ] Catégories de dépenses dans le Wallet
- [ ] Bilan hebdomadaire / mensuel agrégé
- [ ] Prompts guidés pour le journaling
- [ ] Code PIN léger pour l'accès réseau

Contributions et suggestions bienvenues via les *issues*.

---

## 📄 Licence

MIT — fais-en ce que tu veux.
