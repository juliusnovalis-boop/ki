# JADE MOTORS · maquettes Access

Design **3. Menu photo à droite** · couleurs **vert jade et blanc** · application de location de voitures de prestige à Libreville.

Menu à droite posé sur une photo qui change à chaque page, pas d'en-tête, libellés au-dessus des champs, blocs de couleur pleins. Connexion avec les champs sur une seule ligne.

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

* Formulaire de navigation **« Onglets verticaux, à droite »** (6,88 cm). Derrière les boutons, l'image `assets/photos/c-menu-<page>.jpg` (6,88 × 20,74 cm). Boutons de navigation : `Style fond` **Transparent**, texte blanc ; onglet actif : fond blanc, texte couleur *Onglet actif (texte)*.
* Pas d'en-tête : le titre (22 pt, couleur *Titres*) et le sous-titre sont dans chaque sous-formulaire.
* Champs : étiquette **au-dessus** de la zone de texte (étiquette 9,5 pt, puis le champ 0,53 cm plus bas).
* Cartes : Rectangle couleur *Bande / fond des cartes* sans bordure.
* Connexion : photo `c-connexion.jpg` en haut (23,28 × 7,94 cm), champs et bouton alignés sur une ligne dessous, logo `logo-car-front-28px-FFFFFF.png` (blanc) sur la photo.

Règles communes : police **Segoe UI**, zones de texte avec bordure fine sur tout le tour, étiquettes sans bordure, `Effet spécial` **Plat** partout.
