# ONYX CAR · maquettes Access

Design **1. Éditorial** · couleurs **noir et blanc** · application de location de voitures de prestige à Libreville.

Menu en barre noire en haut, grand bandeau photo noir et blanc, gros chiffres à empattements (style magazine), boutons carrés en majuscules. Fiches : liste à gauche, fiche à droite.

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

* Formulaire de navigation, disposition **« Onglets horizontaux »**. Barre : Rectangle couleur *Menu* de 1,69 cm de haut.
* Boutons de navigation : fond couleur *Menu*, texte couleur *Texte du menu* en Segoe UI 9 pt **majuscules**, sans bordure ; onglet actif : texte blanc gras et un trait blanc de 3 pt dessous (petit rectangle blanc).
* Bandeau : contrôle Image `assets/photos/a-bandeau-<page>.jpg` (41,49 × 3,97 cm) en haut du sous-formulaire. Titre en **Georgia** 28 pt blanc, sous-titre en majuscules 9 pt.
* Cartes : Rectangle blanc, bordure couleur *Bordure des cartes*, et un rectangle noir de 0,08 cm collé en haut (le filet). Titres en majuscules 9 pt, gras.
* Les grands chiffres (indicateurs, montant) sont en Georgia 28 pt.
* Connexion : photo `a-connexion.jpg` sur tout le formulaire, carte blanche à droite, logo `logo-car-front-26px-FFFFFF.png` (blanc).

Règles communes : police **Segoe UI**, zones de texte avec bordure fine sur tout le tour, étiquettes sans bordure, `Effet spécial` **Plat** partout.
