# RENTAL GABON CAR · maquettes Access

Design **5. Prestige** · couleurs **bleu royal et noir** · application de location de voitures de prestige à Libreville.

Maquette spéciale bleu royal et noir, rehaussée d'or, d'argent et de blanc. Barre noire en haut avec onglets en pastilles centrés (comme argenté-noir), filet doré, bandeau photo sur chaque page, 4 indicateurs, graphique de la flotte, recherche dans les listes, fiches en colonne à droite. Connexion en deux panneaux (photo | formulaire).

## Logos (une seule image à insérer)

Le logo complet de l'entreprise (icône **et** nom, bonne police, bonnes couleurs) est déjà prêt en PNG transparent. Dans Access : **Créer › Contrôle Image**, choisir le fichier, `Mode affichage image` **Découpage**, puis saisir la position :

| Fichier | Formulaire | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `assets/logo-connexion.png` | Connexion | 15,88 | 1,48 | 5,98 | 0,74 |
| `assets/logo-menu.png` | Menu | 0,74 | 0,56 | 5,93 | 0,69 |

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

* Formulaire de navigation **« Onglets horizontaux »**. Barre : Rectangle noir `#05070C` de 41,49 × 1,80 cm, puis un **trait doré** `#C9A24B` de 1 pt sur toute la largeur juste dessous.
* Logo à gauche : `assets/logo-menu.png`. À droite : avatar (bouton `Forme` **Ovale** bleu royal, bordure dorée 2 pt), nom de l'utilisateur blanc, rôle argenté, bouton Quitter argenté.
* Boutons de navigation : `Forme` **Rectangle arrondi** (pastille), `Style fond` Transparent, texte et icône argentés `#C4CAD3` ; onglet actif : fond **bleu royal** `#1F4FD8`, texte et icône blancs, gras.
* Bandeau : contrôle Image `assets/photos/e-bandeau-<page>.jpg` collé sous le trait doré, 41,49 × 3,97 cm sur le tableau de bord, 41,49 × 3,18 cm sur les autres pages. Par-dessus : sur-titre doré en majuscules espacées, titre blanc 23 pt, sous-titre argenté, date à droite.
* Cartes : Rectangle `#0F1420`, bordure `#1E2740`, titre blanc en majuscules espacées, petit **trait doré** de 1,06 × 0,05 cm sous le titre ; icônes des cartes et des boutons d'outils dorées.
* Indicateurs : le chiffre d'affaires sur fond **bleu royal plein** ; les 3 autres sur fond carte avec un filet doré de 0,05 cm en haut et une pastille ronde (bouton Ovale `#151B2B`) avec l'icône dorée. Le meilleur client affiche son CA en doré.
* Flotte par carburant : un contrôle **Graphique** (barres horizontales) ou 3 paires de rectangles (piste `#1A2238` + barre de couleur dont la largeur se calcule en VBA : `Me.Barre_Essence.Width = 200 * 15 * n / 60`).
* Fiches : liste à gauche avec une zone de texte **Rechercher…** (filtre) dans la bande de titre ; fiche à droite sur 12,70 cm de large, étiquettes à gauche, champs empilés tous les 1,16 cm. Sur Marques, Carburants et Modèles, la photo `e-vignette-<page>.jpg` remplit le bas de la colonne.
* Réservations : trois cartes en haut (Client, Voiture, et le **montant sur fond bleu royal en doré**), la réservation sur une ligne, la liste dessous.
* Connexion : formulaire de 26,46 × 14,82 cm. À gauche, contrôle Image `assets/photos/e-connexion.jpg` (14,29 × 14,82 cm) avec le slogan blanc ; trait doré vertical ; à droite sur fond `#07090F` : logo `assets/logo-connexion.png`, titre, champs et bouton bleu royal.
* La barre de titre sombre correspond au mode sombre de Windows : elle ne se règle pas dans Access.

Règles communes : police **Segoe UI**, zones de texte avec bordure fine sur tout le tour, étiquettes sans bordure, `Effet spécial` **Plat** partout.
