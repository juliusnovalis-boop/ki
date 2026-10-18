# PLATINUM DRIVE · maquettes Access

Design **4. Cockpit** · couleurs **argenté et noir** · application de location de voitures de prestige à Libreville.

Photo de voiture en fond de toute l'application, onglets en pastilles centrés en haut, cartes anthracite, indicateurs argentés empilés. Connexion : carte centrée sur une photo sombre.

## Logos (une seule image à insérer)

Le logo complet de l'entreprise (icône **et** nom, bonne police, bonnes couleurs) est déjà prêt en PNG transparent. Dans Access : **Créer › Contrôle Image**, choisir le fichier, `Mode affichage image` **Découpage**, puis saisir la position :

| Fichier | Formulaire | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `assets/logo-connexion.png` | Connexion | 9,05 | 2,01 | 5,19 | 2,14 |
| `assets/logo-menu.png` | Menu | 0,85 | 0,58 | 4,97 | 0,69 |

Aperçu des logos et de toutes les icônes : `apercu-icones.png`. Liste détaillée : `ICONES.md`.

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `png/` | Les 8 écrans à reproduire : connexion, tableau de bord, réservations, clients, voitures, marques, carburants, modèles |
| `couleur.md` | **Toutes les couleurs** (codes à saisir dans Access) |
| `FOND-NAVIGATION.md` et `schema-fond-navigation.png` | **Photo de fond derrière le menu et le sous-formulaire** : pas à pas et code VBA |
| `COTES.md` | Position et taille de chaque contrôle, en centimètres |
| `ICONES.md` | **Liste de toutes les icônes** : fichier, taille, couleur, contrôle et écran où la mettre |
| `apercu-icones.png` | Aperçu de toutes les icônes (les icônes blanches sont montrées sur fond foncé) |
| `assets/` | Les icônes en PNG transparent, à la taille exacte (logo de la connexion et du menu compris) |
| `assets/photos/` | Les 8 photos de voitures de ce projet, déjà recadrées à la taille exacte |

> Les icônes **blanches** paraissent vides dans l'explorateur Windows (blanc sur blanc) : elles sont bien là, voir `apercu-icones.png`.

## Réaliser ce design dans Access

* Formulaire de navigation **« Onglets horizontaux »**. **Photo de fond sur le menu ET le sous-formulaire** : Access ne rend pas un sous-formulaire transparent, la photo est donc coupée en deux morceaux alignés. Formulaire Menu : `Image` = `assets/photos/d-fond-<page>.jpg` (photo complète, 41,49 × 20,74 cm), **changée par le clic de chaque bouton de navigation** ; chaque page : `Image` **fixe** = `assets/photos/d-corps-<page>.jpg` (bas de la photo, 41,49 × 18,84 cm, aucun code : elle change toute seule avec la page) ; les deux en **Étirer**, sous-formulaire au **Haut 1,905 cm**, sans bordure. Pas à pas, code VBA et schéma : **`FOND-NAVIGATION.md`** et `schema-fond-navigation.png`.
* Boutons de navigation : `Forme` **Rectangle arrondi** (pastille), `Style fond` Transparent, texte couleur *Texte du menu* ; onglet actif : fond couleur *Onglet actif (fond)*, texte noir.
* Cartes : Rectangle couleur *Cartes (fond)*, bordure couleur *Bordure des cartes*, titres en majuscules 9,5 pt, petit trait couleur *Accent* de 1,06 cm sous le titre.
* Indicateurs et montant : Rectangles argentés (couleurs *Indicateurs*), texte et icônes noirs.
* Connexion : propriété **`Image`** du formulaire de connexion = `assets/photos/d-connexion.jpg`, carte centrée (Rectangle couleur *Cartes (fond)*), logo complet `assets/logo-connexion.png` (icône et nom en une image).
* La barre de titre sombre correspond au mode sombre de Windows : elle ne se règle pas dans Access.

Règles communes : police **Segoe UI**, zones de texte avec bordure fine sur tout le tour, étiquettes sans bordure, `Effet spécial` **Plat** partout.
