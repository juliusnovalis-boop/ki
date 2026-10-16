# TIFFANY CAR · maquettes Access

Design **2. Rail d'icônes** · couleurs **rose et blanc** · application de location de voitures de prestige à Libreville.

Menu étroit à gauche (icône + petit libellé), panneau photo vertical à droite avec un grand chiffre, boutons arrondis, cartes avec une barre colorée à gauche. Fiches : fiche en haut, liste dessous.

## Logos (une seule image à insérer)

Le logo complet de l'entreprise (icône **et** nom, bonne police, bonnes couleurs) est déjà prêt en PNG transparent. Dans Access : **Créer › Contrôle Image**, choisir le fichier, `Mode affichage image` **Découpage**, puis saisir la position :

| Fichier | Formulaire | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `assets/logo-connexion.png` | Connexion | 4,66 | 4,71 | 3,39 | 3,25 |
| `assets/logo-menu.png` | Menu | 0,74 | 0,42 | 1,27 | 1,27 |

Aperçu des logos et de toutes les icônes : `apercu-icones.png`. Liste détaillée : `ICONES.md`.

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `png/` | Les 8 écrans à reproduire : connexion, tableau de bord, réservations, clients, voitures, marques, carburants, modèles |
| `couleur.md` | **Toutes les couleurs** (codes à saisir dans Access) |
| `COTES.md` | Position et taille de chaque contrôle, en centimètres |
| `ICONES.md` | **Liste de toutes les icônes** : fichier, taille, couleur, contrôle et écran où la mettre |
| `apercu-icones.png` | Aperçu de toutes les icônes (les icônes blanches sont montrées sur fond foncé) |
| `assets/` | Les icônes en PNG transparent, à la taille exacte (logo de la connexion et du menu compris) |
| `assets/photos/` | Les 8 photos de voitures de ce projet, déjà recadrées à la taille exacte |

> Les icônes **blanches** paraissent vides dans l'explorateur Windows (blanc sur blanc) : elles sont bien là, voir `apercu-icones.png`.

## Réaliser ce design dans Access

* Formulaire de navigation **« Onglets verticaux, à gauche »**, réduit à 2,75 cm de large. Boutons de navigation : `Disposition image légende` **Haut** (icône au-dessus du texte), Segoe UI 9 pt, `Forme` **Rectangle arrondi** ; onglet actif : fond blanc, texte couleur *Onglet actif (texte)*.
* Panneau photo : contrôle Image `assets/photos/b-panneau-<page>.jpg` (8,47 × 18,84 cm) collé à droite. Par-dessus, une zone de texte transparente pour le grand chiffre (40 pt blanc), par exemple `=CpteDom("*";"Client")`.
* Cartes : Rectangle blanc, bordure couleur *Bordure des cartes*, et un rectangle couleur *Accent* de 0,11 cm sur le bord gauche.
* Boutons : `Forme` **Rectangle arrondi** (Enregistrer, Supprimer, Se connecter) ou **Ovale** (petits boutons).
* Connexion : formulaire vertical de 12,70 × 16,40 cm, photo `b-connexion.jpg` en haut, logo complet `assets/logo-connexion.png` (carré blanc, icône et nom TIFFANY CAR en une image).

Règles communes : police **Segoe UI**, zones de texte avec bordure fine sur tout le tour, étiquettes sans bordure, `Effet spécial` **Plat** partout.
