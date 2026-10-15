# TIFFANY CAR · maquettes Access

Design **2. Rail d'icônes** · couleurs **rose et blanc** · application de location de voitures de prestige à Libreville.

Menu étroit à gauche (icône + petit libellé), panneau photo vertical à droite avec un grand chiffre, boutons arrondis, cartes avec une barre colorée à gauche. Fiches : fiche en haut, liste dessous.

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `png/` | Les 8 écrans à reproduire : connexion, tableau de bord, réservations, clients, voitures, marques, carburants, modèles |
| `couleur.md` | **Toutes les couleurs** (codes à saisir dans Access) |
| `COTES.md` | Position et taille de chaque contrôle, en centimètres |
| `assets/photos/` | Photos de voitures de ce projet, déjà recadrées |
| `assets/` | Icônes (PNG) pour les boutons, les cartes et le menu |

## Réaliser ce design dans Access

* Formulaire de navigation **« Onglets verticaux, à gauche »**, réduit à 2,75 cm de large. Boutons de navigation : `Disposition image légende` **Haut** (icône au-dessus du texte), Segoe UI 9 pt, `Forme` **Rectangle arrondi** ; onglet actif : fond blanc, texte couleur *Onglet actif (texte)*.
* Panneau photo : contrôle Image `assets/photos/b-panneau-<page>.jpg` (8,47 × 18,84 cm) collé à droite. Par-dessus, une zone de texte transparente pour le grand chiffre (40 pt blanc), par exemple `=CpteDom("*";"Client")`.
* Cartes : Rectangle blanc, bordure couleur *Bordure des cartes*, et un rectangle couleur *Accent* de 0,11 cm sur le bord gauche.
* Boutons : `Forme` **Rectangle arrondi** (Enregistrer, Supprimer, Se connecter) ou **Ovale** (petits boutons).
* Connexion : formulaire vertical de 12,70 × 16,40 cm, photo `b-connexion.jpg` en haut, logo dans un bouton ovale.

Règles communes : police **Segoe UI**, zones de texte avec bordure fine sur tout le tour, étiquettes sans bordure, `Effet spécial` **Plat** partout.
