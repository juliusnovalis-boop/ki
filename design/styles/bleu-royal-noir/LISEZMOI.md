# AURION · maquettes Access

Design **5. Prestige futuriste** · couleurs **bleu royal et noir** · application de location de voitures de prestige à Libreville.

Maquette spéciale **bleu royal `#002366` et noir**, rehaussée d'or, d'argent et de blanc, inspirée des écrans de bord des voitures de luxe : police **Bahnschrift**, grands chiffres fins, cartes numérotées (01, 02…), jauge d'occupation, voiture phare en photo sur le tableau de bord, barre de progression de la location, onglets en pastilles centrés (comme argenté-noir). Connexion en deux panneaux (photo | formulaire).

## Logos (une seule image à insérer)

Le logo complet de l'entreprise (icône **et** nom, bonne police, bonnes couleurs) est déjà prêt en PNG transparent. Dans Access : **Créer › Contrôle Image**, choisir le fichier, `Mode affichage image` **Découpage**, puis saisir la position :

| Fichier | Formulaire | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `assets/logo-connexion.png` | Connexion | 16,14 | 0,90 | 6,61 | 3,10 |
| `assets/logo-menu.png` | Menu | 0,64 | 0,16 | 5,66 | 1,38 |

Aperçu des logos et de toutes les icônes : `apercu-icones.png`. Liste détaillée : `ICONES.md`.

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `png/` | Les 8 écrans à reproduire : connexion, tableau de bord, réservations, clients, voitures, marques, carburants, modèles |
| `couleur.md` | **Toutes les couleurs** (codes à saisir dans Access) |
| `COTES.md` | Position et taille de chaque contrôle, en centimètres |
| `ICONES.md` | **Liste de toutes les icônes** : fichier, taille, couleur, contrôle et écran où la mettre |
| `apercu-icones.png` | Aperçu de toutes les icônes (les icônes blanches sont montrées sur fond foncé) |
| `assets/` | Les icônes en PNG transparent, à la taille exacte (logo de la connexion et du menu compris), et `jauges/` : les 21 images de la jauge |
| `assets/photos/` | Les 8 photos de voitures de ce projet, déjà recadrées à la taille exacte |

> Les icônes **blanches** paraissent vides dans l'explorateur Windows (blanc sur blanc) : elles sont bien là, voir `apercu-icones.png`.

## Réaliser ce design dans Access

* Formulaire de navigation **« Onglets horizontaux »**. Barre : Rectangle noir `#000000` de 41,49 × 1,69 cm, puis un **trait doré** `#C9A24B` de 1 pt sur toute la largeur juste dessous. Logo à gauche : `assets/logo-menu.png`.
* Boutons de navigation : `Forme` **Rectangle arrondi** (pastille), police **Bahnschrift 11 pt**, `Style fond` Transparent, texte et icône argentés `#C4CAD3` ; onglet actif : fond **bleu royal `#002366`**, bordure `#2A55B8`, texte et icône blancs, gras.
* À droite de la barre : avatar (bouton `Forme` **Ovale** `#002366`, bordure dorée 2 pt), nom et rôle de l'utilisateur, puis le bouton **Se déconnecter** : `Forme` **Rectangle arrondi** de 3,65 × 0,90 cm, fond `#0A1838`, bordure `#2A55B8`, texte blanc Bahnschrift 10,5 pt, image `log-out` dorée à gauche du texte (`Disposition image légende` **Gauche**). Dans `Sur clic` : fermer le formulaire Menu et rouvrir le formulaire de connexion (`DoCmd.Close acForm, Me.Name` puis `DoCmd.OpenForm "Connexion"`).
* Cartes : Rectangle `#06112A`, bordure `#13284F`. Titre en **Bahnschrift SemiBold 11 pt majuscules**, précédé du **numéro doré** (01, 02…, Bahnschrift Light). Sous le titre : un trait `#13284F` sur toute la largeur et un petit trait doré de 1,06 cm × 2 pt à gauche.
* Tableau de bord : pas de bandeau, mais un en-tête *Bonjour, admin* (Bahnschrift SemiBold 28 pt) et l'heure en grand à droite (Bahnschrift Light 26 pt, `=Format(Maintenant();"hh:nn")`).
* Voiture phare : contrôle Image `assets/photos/e-vedette.jpg` (10,53 × 6,56 cm) dans la carte, à droite ; les caractéristiques à gauche viennent de la table Voiture (Puissance, CoutParJour, Annee).
* Jauge d'occupation : contrôle Image `assets/jauges/jauge-015.png` (3,97 × 3,97 cm) et une zone de texte transparente au centre pour le taux. Les 21 images `jauge-000.png` à `jauge-100.png` (pas de 5 %) permettent d'animer la jauge en VBA dans `Form_Load` : `Me.Image_Jauge.Picture = CurrentProject.Path & "\assets\jauges\jauge-" & Format(Round(taux / 5) * 5, "000") & ".png"`.
* Indicateurs : le chiffre d'affaires sur fond **bleu royal `#002366`** (bordure `#2A55B8`) ; les autres sur fond carte avec un petit trait doré en haut. Chiffres en Bahnschrift Light 26 pt blancs, icône dorée en haut à droite.
* Flotte par carburant et durée de la location : rectangles fins (piste + barre). Largeur de la barre en VBA, par exemple `Me.Barre_Essence.Width = Me.Piste_Essence.Width * n / 60`.
* Pages : bandeau `assets/photos/e-bandeau-<page>.jpg` (41,49 × 3,28 cm) sous le trait doré, sur-titre doré espacé, titre Bahnschrift SemiBold 28 pt, date dans un petit cadre noir à droite.
* Fiches : liste à gauche avec la zone **Rechercher…** (filtre) dans la bande de titre ; fiche à droite (12,70 cm), champs tous les 1,16 cm. Sur Marques, Carburants et Modèles, la photo `e-vignette-<page>.jpg` complète la colonne avec un grand chiffre.
* Réservations : cartes 01 Client et 02 Voiture, carte du **montant en doré sur bleu royal** avec la barre de progression de la location, puis 03 Réservation sur une ligne et 04 Liste.
* Connexion : formulaire de 26,46 × 14,82 cm. À gauche, `assets/photos/e-connexion.jpg` (14,82 × 14,82 cm) avec le slogan en haut ; trait doré vertical ; à droite sur fond `#01040B` : `assets/logo-connexion.png`, titre Bahnschrift, libellés en majuscules, bouton bleu royal **SE CONNECTER**.
* **Logo AURION** (dossier `assets/marque/`) : `aurion-menu.png` (barre du menu, 5,66 × 1,38 cm), `aurion-connexion.png` (connexion, 6,61 × 3,10 cm), `aurion-logo-hd.png` et `aurion-embleme-hd.png` en grand format (états imprimés, page de garde), et **`aurion.ico`** pour l'icône de l'application : *Fichier › Options › Base de données active › Icône de l'application*, cocher *Utiliser comme icône de formulaire et d'état*. Tous les PNG sont transparents, prévus pour un fond foncé.
* La barre de titre sombre correspond au mode sombre de Windows : elle ne se règle pas dans Access.

Règles communes : police **Segoe UI**, zones de texte avec bordure fine sur tout le tour, étiquettes sans bordure, `Effet spécial` **Plat** partout.
