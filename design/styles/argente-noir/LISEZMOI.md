# PLATINUM DRIVE · maquettes Access

Design **4. Cockpit** · couleurs **argenté et noir** · application de location de voitures de prestige à Libreville.

Photo de voiture en fond de toute l'application, onglets en pastilles centrés en haut, cartes anthracite, indicateurs argentés empilés. Connexion : carte centrée sur une photo sombre.

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

* Formulaire de navigation **« Onglets horizontaux »**. Propriété **`Image`** du formulaire Menu : `assets/photos/d-fond-<page>.jpg` (41,49 × 20,74 cm), `Mode affichage image` **Découpage**. Dans chaque sous-formulaire, `Style fond` des sections : **Transparent**, ou la même image en fond.
* Boutons de navigation : `Forme` **Rectangle arrondi** (pastille), `Style fond` Transparent, texte couleur *Texte du menu* ; onglet actif : fond couleur *Onglet actif (fond)*, texte noir.
* Cartes : Rectangle couleur *Cartes (fond)*, bordure couleur *Bordure des cartes*, titres en majuscules 9,5 pt, petit trait couleur *Accent* de 1,06 cm sous le titre.
* Indicateurs et montant : Rectangles argentés (couleurs *Indicateurs*), texte et icônes noirs.
* Connexion : propriété **`Image`** du formulaire de connexion = `assets/photos/d-connexion.jpg`, carte centrée (Rectangle couleur *Cartes (fond)*), logo `logo-car-front-48px-C9CDD2.png`.
* La barre de titre sombre correspond au mode sombre de Windows : elle ne se règle pas dans Access.

Règles communes : police **Segoe UI**, zones de texte avec bordure fine sur tout le tour, étiquettes sans bordure, `Effet spécial` **Plat** partout.
