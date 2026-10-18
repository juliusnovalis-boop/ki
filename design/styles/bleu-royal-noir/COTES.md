# Cotes des contrôles

Positions et tailles en **centimètres**, à saisir dans la feuille de propriétés d'Access (onglet *Format* : `Gauche`, `Haut`, `Largeur`, `Hauteur`).

* **Menu** : mesurées depuis le coin haut-gauche du formulaire `Menu` (41,49 × 20,74 cm, sans la barre de titre).
* **Autres écrans** : mesurées depuis le coin haut-gauche du **sous-formulaire** (position et taille : ligne `Sous_Formulaire` du formulaire Menu).
* Les contrôles placés dans une carte sont donnés en position absolue dans le sous-formulaire.
* Fichier généré par `outils/generer.py`.

## Connexion

Maquette : `png/00-connexion.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Login_Fond` | Section Détail | 0,00 | 0,00 | 26,46 | 14,82 |
| `Login_Photo` | Image (e-connexion.jpg) | 0,00 | 0,00 | 14,29 | 14,82 |
| `Lbl_Surtitre` | Étiquette | 1,06 | 11,43 | 7,86 | 0,40 |
| `Lbl_Slogan` | Étiquette | 1,01 | 12,07 | 11,11 | 1,80 |
| `Trait_Or` | Trait | 14,29 | 0,00 | 0,03 | 14,82 |
| `Logo` | Image + étiquette | 15,88 | 1,48 | 5,95 | 0,74 |
| `Lbl_Titre` | Étiquette | 15,88 | 3,33 | 3,65 | 0,98 |
| `Txt_Utilisateur` | Zone de texte | 15,88 | 6,77 | 9,00 | 0,95 |
| `Txt_MotDePasse` | Zone de texte | 15,88 | 8,84 | 9,00 | 0,95 |
| `Btn_Connexion` | Bouton | 15,88 | 10,53 | 9,00 | 1,06 |
| `Login_Copyright` | Étiquette | 15,88 | 13,76 | 4,79 | 0,45 |

## Formulaire « Menu » (commun à tous les écrans)

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Entete` | Section En-tête | 0,00 | 0,00 | 41,49 | 1,80 |
| `Logo` | Image + étiquette | 0,74 | 0,56 | 5,90 | 0,69 |
| `BoutonNavigation_tableau` | Bouton de navigation | 8,84 | 0,42 | 4,50 | 0,95 |
| `BoutonNavigation_reservations` | Bouton de navigation | 13,49 | 0,42 | 3,86 | 0,95 |
| `BoutonNavigation_clients` | Bouton de navigation | 17,52 | 0,42 | 2,83 | 0,95 |
| `BoutonNavigation_voitures` | Bouton de navigation | 20,51 | 0,42 | 3,04 | 0,95 |
| `BoutonNavigation_marques` | Bouton de navigation | 23,71 | 0,42 | 2,83 | 0,95 |
| `BoutonNavigation_carburants` | Bouton de navigation | 26,70 | 0,42 | 3,47 | 0,95 |
| `BoutonNavigation_modeles` | Bouton de navigation | 30,32 | 0,42 | 2,83 | 0,95 |
| `Btn_Avatar` | Bouton (ellipse) | 35,88 | 0,45 | 0,90 | 0,90 |
| `Txt_Utilisateur` | Zone de texte | 37,09 | 0,48 | 3,07 | 0,85 |
| `Btn_Quitter` | Bouton | 40,16 | 0,64 | 0,53 | 0,53 |
| `Trait_Or` | Trait | 0,00 | 1,80 | 41,49 | 0,03 |
| `Bandeau` | Image (e-bandeau-tableau.jpg) | 0,00 | 1,83 | 41,49 | 3,97 |
| `Lbl_Surtitre` | Étiquette | 0,85 | 2,51 | 4,05 | 0,45 |
| `Lbl_Titre_Page` | Étiquette | 0,79 | 3,04 | 6,06 | 1,11 |
| `Lbl_SousTitre` | Étiquette | 0,85 | 4,31 | 10,03 | 0,48 |
| `Date_Heure` | Zone de texte | 34,74 | 2,43 | 5,90 | 0,48 |
| `Sous_Formulaire` | Sous-formulaire | 0,00 | 5,79 | 41,49 | 14,95 |

## Tableau de bord

Maquette : `png/01-tableau-de-bord.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_CA` | Rectangle | 0,64 | 0,53 | 9,74 | 2,75 |
| `Txt_CA` | Zone de texte | 1,22 | 1,53 | 5,66 | 0,98 |
| `Pastille_CA` | Bouton (ellipse) + image | 8,52 | 1,27 | 1,27 | 1,27 |
| `Carte_Location` | Rectangle | 10,80 | 0,53 | 9,74 | 2,75 |
| `Txt_Location` | Zone de texte | 11,40 | 1,56 | 1,27 | 0,98 |
| `Pastille_Location` | Bouton (ellipse) + image | 18,71 | 1,30 | 1,27 | 1,27 |
| `Carte_Clients` | Rectangle | 20,96 | 0,53 | 9,74 | 2,75 |
| `Txt_Clients` | Zone de texte | 21,56 | 1,56 | 1,22 | 0,98 |
| `Pastille_Clients` | Bouton (ellipse) + image | 28,87 | 1,30 | 1,27 | 1,27 |
| `Carte_Meilleur` | Rectangle | 31,12 | 0,53 | 9,74 | 2,75 |
| `Txt_Meilleur` | Zone de texte | 31,72 | 1,56 | 4,47 | 0,77 |
| `Pastille_Meilleur` | Bouton (ellipse) + image | 39,03 | 1,30 | 1,27 | 1,27 |
| `Carte_Reservees` | Rectangle | 0,64 | 3,70 | 28,15 | 10,61 |
| `Btn_Imprimer` | Bouton | 27,65 | 4,00 | 0,79 | 0,79 |
| `Liste_Voitures_Reservees` | Zone de liste | 1,19 | 5,42 | 27,09 | 8,39 |
| `Carte_Top5` | Rectangle | 29,21 | 3,70 | 11,64 | 5,48 |
| `Liste_Top5` | Zone de liste | 29,77 | 5,42 | 10,58 | 3,25 |
| `Carte_Carburants` | Rectangle | 29,21 | 9,60 | 11,64 | 4,71 |
| `Barre_Essence` | Rectangle | 32,15 | 11,54 | 4,15 | 0,26 |
| `Barre_Hybride` | Rectangle | 32,15 | 12,44 | 1,06 | 0,26 |
| `Barre_Electrique` | Rectangle | 32,15 | 13,34 | 0,08 | 0,26 |

## Réservations

Maquette : `png/02-reservations.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Client` | Rectangle | 0,64 | 0,53 | 13,12 | 4,76 |
| `Cbo_Client` | Zone de liste déroulante | 3,84 | 2,25 | 9,42 | 0,74 |
| `Txt_Telephone` | Zone de texte (verrouillée) | 3,84 | 3,20 | 9,42 | 0,74 |
| `Txt_Email` | Zone de texte (verrouillée) | 3,84 | 4,15 | 9,42 | 0,74 |
| `Carte_Voiture` | Rectangle | 14,18 | 0,53 | 13,12 | 4,76 |
| `Cbo_Voiture` | Zone de liste déroulante | 17,38 | 2,25 | 9,42 | 0,74 |
| `Txt_Modele` | Zone de texte (verrouillée) | 17,38 | 3,20 | 9,42 | 0,74 |
| `Txt_Marque` | Zone de texte (verrouillée) | 17,38 | 4,15 | 9,42 | 0,74 |
| `Carte_Montant` | Rectangle | 27,73 | 0,53 | 13,12 | 4,76 |
| `Txt_Montant` | Zone de texte | 28,36 | 1,59 | 5,74 | 1,24 |
| `Txt_Duree` | Zone de texte | 29,66 | 3,39 | 1,64 | 0,48 |
| `Carte_Reservation` | Rectangle | 0,64 | 5,72 | 40,22 | 2,80 |
| `Btn_Ajouter` | Bouton | 37,81 | 6,01 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,76 | 6,01 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,71 | 6,01 | 0,79 | 0,79 |
| `Txt_Code` | Zone de texte | 2,57 | 7,38 | 1,85 | 0,74 |
| `Txt_DateDebut` | Zone de texte | 8,18 | 7,38 | 3,28 | 0,74 |
| `Txt_DateFin` | Zone de texte | 14,95 | 7,38 | 3,28 | 0,74 |
| `Btn_OK` | Bouton | 18,76 | 7,33 | 1,69 | 0,85 |
| `Btn_Premier` | Bouton | 21,56 | 7,38 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 22,46 | 7,38 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 26,27 | 7,38 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 27,17 | 7,38 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 23,36 | 7,38 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,68 | 7,33 | 3,70 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,65 | 7,33 | 3,70 | 0,85 |
| `Carte_Liste` | Rectangle | 0,64 | 8,94 | 40,22 | 6,16 |
| `Btn_Imprimer` | Bouton | 39,71 | 9,23 | 0,79 | 0,79 |
| `Liste_Reservations` | Zone de liste | 1,19 | 10,61 | 39,16 | 4,05 |

## Clients

Maquette : `png/03-clients.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Liste` | Rectangle | 0,64 | 0,53 | 27,09 | 14,58 |
| `Btn_Imprimer` | Bouton | 26,59 | 0,82 | 0,79 | 0,79 |
| `Liste_Clients` | Zone de liste | 1,19 | 2,30 | 26,04 | 12,30 |
| `Txt_Recherche` | Zone de texte (filtre) | 19,24 | 0,82 | 6,88 | 0,79 |
| `Carte_Fiche` | Rectangle | 28,15 | 0,53 | 12,70 | 14,58 |
| `Btn_Ajouter` | Bouton | 38,76 | 0,82 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 39,71 | 0,82 | 0,79 | 0,79 |
| `Txt_CIN` | Zone de texte | 32,15 | 2,41 | 3,70 | 0,74 |
| `Txt_Permis` | Zone de texte | 32,15 | 3,57 | 4,76 | 0,74 |
| `Txt_Prenom` | Zone de texte | 32,15 | 4,74 | 8,20 | 0,74 |
| `Txt_Nom` | Zone de texte | 32,15 | 5,90 | 8,20 | 0,74 |
| `Cbo_Sexe` | Zone de liste déroulante | 32,15 | 7,06 | 2,12 | 0,74 |
| `Txt_Adresse` | Zone de texte | 32,15 | 8,23 | 8,20 | 0,74 |
| `Txt_Telephone` | Zone de texte | 32,15 | 9,39 | 8,20 | 0,74 |
| `Txt_Email` | Zone de texte | 32,15 | 10,56 | 8,20 | 0,74 |
| `Btn_Premier` | Bouton | 31,33 | 12,14 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 32,23 | 12,14 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 36,04 | 12,14 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 36,94 | 12,14 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 33,13 | 12,14 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 28,71 | 13,76 | 5,69 | 0,85 |
| `Btn_Supprimer` | Bouton | 34,66 | 13,76 | 5,69 | 0,85 |

## Voitures

Maquette : `png/04-voitures.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Liste` | Rectangle | 0,64 | 0,53 | 27,09 | 14,58 |
| `Btn_Imprimer` | Bouton | 26,59 | 0,82 | 0,79 | 0,79 |
| `Liste_Voitures` | Zone de liste | 1,19 | 2,30 | 26,04 | 12,30 |
| `Txt_Recherche` | Zone de texte (filtre) | 19,24 | 0,82 | 6,88 | 0,79 |
| `Carte_Fiche` | Rectangle | 28,15 | 0,53 | 12,70 | 14,58 |
| `Btn_Ajouter` | Bouton | 38,76 | 0,82 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 39,71 | 0,82 | 0,79 | 0,79 |
| `Txt_Matricule` | Zone de texte | 32,15 | 2,41 | 3,70 | 0,74 |
| `Txt_Annee` | Zone de texte | 32,15 | 3,57 | 2,12 | 0,74 |
| `Txt_Couleur` | Zone de texte | 32,15 | 4,74 | 8,20 | 0,74 |
| `Txt_Puissance` | Zone de texte | 32,15 | 5,90 | 2,65 | 0,74 |
| `Txt_CoutJour` | Zone de texte | 32,15 | 7,06 | 4,23 | 0,74 |
| `Cbo_Modele` | Zone de liste déroulante | 32,15 | 8,23 | 8,20 | 0,74 |
| `Cbo_Carburant` | Zone de liste déroulante | 32,15 | 9,39 | 8,20 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 32,15 | 10,56 | 8,20 | 0,74 |
| `Btn_Premier` | Bouton | 31,33 | 12,14 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 32,23 | 12,14 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 36,04 | 12,14 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 36,94 | 12,14 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 33,13 | 12,14 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 28,71 | 13,76 | 5,69 | 0,85 |
| `Btn_Supprimer` | Bouton | 34,66 | 13,76 | 5,69 | 0,85 |

## Marques

Maquette : `png/05-marques.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Liste` | Rectangle | 0,64 | 0,53 | 27,09 | 14,58 |
| `Btn_Imprimer` | Bouton | 26,59 | 0,82 | 0,79 | 0,79 |
| `Liste_Marques` | Zone de liste | 1,19 | 2,30 | 26,04 | 12,30 |
| `Txt_Recherche` | Zone de texte (filtre) | 19,24 | 0,82 | 6,88 | 0,79 |
| `Carte_Fiche` | Rectangle | 28,15 | 0,53 | 12,70 | 6,93 |
| `Btn_Ajouter` | Bouton | 38,76 | 0,82 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 39,71 | 0,82 | 0,79 | 0,79 |
| `Txt_IdMarque` | Zone de texte | 32,15 | 2,41 | 2,12 | 0,74 |
| `Txt_Marque` | Zone de texte | 32,15 | 3,57 | 8,20 | 0,74 |
| `Btn_Premier` | Bouton | 31,33 | 5,16 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 32,23 | 5,16 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 36,04 | 5,16 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 36,94 | 5,16 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 33,13 | 5,16 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 28,71 | 6,11 | 5,69 | 0,85 |
| `Btn_Supprimer` | Bouton | 34,66 | 6,11 | 5,69 | 0,85 |
| `Image_Vignette` | Image (e-vignette-marques.jpg) | 28,15 | 7,88 | 12,70 | 7,22 |
| `Lbl_Chiffre` | Étiquette | 28,79 | 12,89 | 0,61 | 1,46 |
| `Lbl_Chiffre_Texte` | Étiquette | 28,84 | 14,21 | 3,65 | 0,48 |

## Carburants

Maquette : `png/06-carburants.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Liste` | Rectangle | 0,64 | 0,53 | 27,09 | 14,58 |
| `Btn_Imprimer` | Bouton | 26,59 | 0,82 | 0,79 | 0,79 |
| `Liste_Carburants` | Zone de liste | 1,19 | 2,30 | 26,04 | 12,30 |
| `Txt_Recherche` | Zone de texte (filtre) | 19,24 | 0,82 | 6,88 | 0,79 |
| `Carte_Fiche` | Rectangle | 28,15 | 0,53 | 12,70 | 6,93 |
| `Btn_Ajouter` | Bouton | 38,76 | 0,82 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 39,71 | 0,82 | 0,79 | 0,79 |
| `Txt_IdType` | Zone de texte | 32,15 | 2,41 | 2,12 | 0,74 |
| `Txt_Type` | Zone de texte | 32,15 | 3,57 | 8,20 | 0,74 |
| `Btn_Premier` | Bouton | 31,33 | 5,16 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 32,23 | 5,16 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 36,04 | 5,16 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 36,94 | 5,16 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 33,13 | 5,16 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 28,71 | 6,11 | 5,69 | 0,85 |
| `Btn_Supprimer` | Bouton | 34,66 | 6,11 | 5,69 | 0,85 |
| `Image_Vignette` | Image (e-vignette-carburants.jpg) | 28,15 | 7,88 | 12,70 | 7,22 |
| `Lbl_Chiffre` | Étiquette | 28,79 | 12,89 | 0,61 | 1,46 |
| `Lbl_Chiffre_Texte` | Étiquette | 28,84 | 14,21 | 3,33 | 0,48 |

## Modèles

Maquette : `png/07-modeles.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Liste` | Rectangle | 0,64 | 0,53 | 27,09 | 14,58 |
| `Btn_Imprimer` | Bouton | 26,59 | 0,82 | 0,79 | 0,79 |
| `Liste_Modeles` | Zone de liste | 1,19 | 2,30 | 26,04 | 12,30 |
| `Txt_Recherche` | Zone de texte (filtre) | 19,24 | 0,82 | 6,88 | 0,79 |
| `Carte_Fiche` | Rectangle | 28,15 | 0,53 | 12,70 | 8,10 |
| `Btn_Ajouter` | Bouton | 38,76 | 0,82 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 39,71 | 0,82 | 0,79 | 0,79 |
| `Txt_IdModele` | Zone de texte | 32,15 | 2,41 | 2,12 | 0,74 |
| `Txt_Modele` | Zone de texte | 32,15 | 3,57 | 8,20 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 32,15 | 4,74 | 8,20 | 0,74 |
| `Btn_Premier` | Bouton | 31,33 | 6,32 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 32,23 | 6,32 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 36,04 | 6,32 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 36,94 | 6,32 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 33,13 | 6,32 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 28,71 | 7,28 | 5,69 | 0,85 |
| `Btn_Supprimer` | Bouton | 34,66 | 7,28 | 5,69 | 0,85 |
| `Image_Vignette` | Image (e-vignette-modeles.jpg) | 28,15 | 9,05 | 12,70 | 6,06 |
| `Lbl_Chiffre` | Étiquette | 28,79 | 12,89 | 1,22 | 1,46 |
| `Lbl_Chiffre_Texte` | Étiquette | 28,84 | 14,21 | 3,86 | 0,48 |
