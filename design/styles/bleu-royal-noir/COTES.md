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
| `Login_Photo` | Image (e-connexion.jpg) | 0,00 | 0,00 | 14,82 | 14,82 |
| `Lbl_Surtitre` | Étiquette | 1,06 | 1,48 | 8,10 | 0,37 |
| `Lbl_Slogan` | Étiquette | 1,01 | 2,12 | 8,89 | 2,01 |
| `Trait_Or` | Trait | 14,82 | 0,00 | 0,03 | 14,82 |
| `Logo` | Image (marque/aurion-connexion.png) | 16,14 | 0,90 | 6,61 | 3,10 |
| `Lbl_Titre` | Étiquette | 16,30 | 4,39 | 4,39 | 1,27 |
| `Txt_Utilisateur` | Zone de texte | 16,30 | 7,78 | 8,68 | 1,01 |
| `Txt_MotDePasse` | Zone de texte | 16,30 | 9,84 | 8,68 | 1,01 |
| `Btn_Connexion` | Bouton | 16,30 | 11,48 | 8,68 | 1,11 |
| `Login_Copyright` | Étiquette | 16,30 | 13,97 | 2,62 | 0,37 |

## Formulaire « Menu » (commun à tous les écrans)

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Entete` | Section En-tête | 0,00 | 0,00 | 41,49 | 1,69 |
| `Logo` | Image (marque/aurion-menu.png) | 0,64 | 0,16 | 5,66 | 1,38 |
| `BoutonNavigation_tableau` | Bouton de navigation | 8,12 | 0,37 | 4,42 | 0,95 |
| `BoutonNavigation_reservations` | Bouton de navigation | 12,70 | 0,37 | 3,81 | 0,95 |
| `BoutonNavigation_clients` | Bouton de navigation | 16,67 | 0,37 | 2,83 | 0,95 |
| `BoutonNavigation_voitures` | Bouton de navigation | 19,66 | 0,37 | 3,04 | 0,95 |
| `BoutonNavigation_marques` | Bouton de navigation | 22,86 | 0,37 | 2,83 | 0,95 |
| `BoutonNavigation_carburants` | Bouton de navigation | 25,85 | 0,37 | 3,44 | 0,95 |
| `BoutonNavigation_modeles` | Bouton de navigation | 29,45 | 0,37 | 2,83 | 0,95 |
| `Btn_Avatar` | Bouton (ellipse) | 33,13 | 0,40 | 0,90 | 0,90 |
| `Txt_Utilisateur` | Zone de texte | 34,29 | 0,42 | 2,65 | 0,85 |
| `Btn_Deconnexion` | Bouton | 37,20 | 0,40 | 3,65 | 0,90 |
| `Trait_Or` | Trait | 0,00 | 1,69 | 41,49 | 0,03 |
| `Sous_Formulaire` | Sous-formulaire | 0,00 | 1,72 | 41,49 | 19,02 |

## Tableau de bord

Maquette : `png/01-tableau-de-bord.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Surtitre` | Étiquette | 0,69 | 0,48 | 6,01 | 0,37 |
| `Lbl_Titre_Page` | Étiquette | 0,64 | 0,90 | 5,87 | 1,16 |
| `Date_Heure` | Zone de texte | 36,96 | 0,58 | 3,89 | 1,43 |
| `Carte_Vedette` | Rectangle | 0,64 | 2,38 | 15,88 | 6,61 |
| `Image_Vedette` | Image (e-vedette.jpg) | 5,95 | 2,41 | 10,53 | 6,56 |
| `Txt_Vedette_Modele` | Étiquette | 1,19 | 3,41 | 5,27 | 1,59 |
| `Txt_Vedette_Matricule` | Étiquette | 1,19 | 5,16 | 2,78 | 0,48 |
| `Txt_Vedette_Puissance` | Étiquette | 3,62 | 6,16 | 1,53 | 0,61 |
| `Txt_Vedette_Tarif` | Étiquette | 3,62 | 7,01 | 1,91 | 0,61 |
| `Txt_Vedette_Année` | Étiquette | 3,62 | 7,86 | 0,93 | 0,61 |
| `Carte_Occupation` | Rectangle | 16,93 | 2,38 | 6,88 | 6,61 |
| `Lbl_Occupation` | Étiquette | 17,49 | 2,78 | 4,79 | 0,48 |
| `Image_Jauge` | Image (jauges/jauge-015.png) | 18,42 | 4,05 | 3,97 | 3,97 |
| `Txt_Taux` | Zone de texte | 16,96 | 5,27 | 6,83 | 1,06 |
| `Carte_CA` | Rectangle | 24,24 | 2,38 | 8,10 | 3,10 |
| `Txt_CA` | Zone de texte | 24,79 | 3,31 | 5,95 | 1,11 |
| `Icone_CA` | Image | 31,04 | 2,70 | 0,79 | 0,79 |
| `Carte_Reservations` | Rectangle | 32,76 | 2,38 | 8,10 | 3,10 |
| `Txt_Reservations` | Zone de texte | 33,31 | 3,31 | 0,85 | 1,11 |
| `Icone_Reservations` | Image | 39,56 | 2,70 | 0,79 | 0,79 |
| `Carte_Clients` | Rectangle | 24,24 | 5,90 | 8,10 | 3,10 |
| `Txt_Clients` | Zone de texte | 24,79 | 6,83 | 1,35 | 1,11 |
| `Icone_Clients` | Image | 31,04 | 6,22 | 0,79 | 0,79 |
| `Carte_Meilleur` | Rectangle | 32,76 | 5,90 | 8,10 | 3,10 |
| `Txt_Meilleur` | Zone de texte | 33,31 | 6,99 | 3,97 | 0,77 |
| `Icone_Meilleur` | Image | 39,56 | 6,22 | 0,79 | 0,79 |
| `Carte_Reservees` | Rectangle | 0,64 | 9,42 | 28,15 | 9,08 |
| `Lbl_Reservees` | Étiquette | 1,19 | 9,82 | 8,52 | 0,48 |
| `Txt_Info_Reservees` | Zone de texte | 25,88 | 9,84 | 1,40 | 0,42 |
| `Btn_Imprimer` | Bouton | 27,65 | 9,66 | 0,79 | 0,79 |
| `Liste_Voitures_Reservees` | Zone de liste | 1,19 | 10,98 | 27,09 | 7,17 |
| `Carte_Top5` | Rectangle | 29,21 | 9,42 | 11,64 | 5,16 |
| `Lbl_Top5` | Étiquette | 29,77 | 9,82 | 5,24 | 0,48 |
| `Liste_Top5` | Zone de liste | 29,77 | 10,98 | 10,58 | 3,25 |
| `Carte_Carburants` | Rectangle | 29,21 | 15,00 | 11,64 | 3,49 |
| `Lbl_Carburants` | Étiquette | 29,77 | 15,40 | 5,77 | 0,48 |
| `Txt_Info_Carburants` | Zone de texte | 38,79 | 15,43 | 1,51 | 0,42 |
| `Barre_Essence` | Rectangle | 32,15 | 16,75 | 4,15 | 0,16 |
| `Barre_Hybride` | Rectangle | 32,15 | 17,38 | 1,06 | 0,16 |
| `Barre_Electrique` | Rectangle | 32,15 | 18,02 | 0,08 | 0,16 |

## Réservations

Maquette : `png/02-reservations.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Client` | Rectangle | 0,64 | 0,53 | 13,12 | 4,76 |
| `Lbl_Client` | Étiquette | 1,19 | 0,93 | 2,14 | 0,48 |
| `Cbo_Client` | Zone de liste déroulante | 3,84 | 2,20 | 9,42 | 0,74 |
| `Txt_Telephone` | Zone de texte (verrouillée) | 3,84 | 3,15 | 9,42 | 0,74 |
| `Txt_Email` | Zone de texte (verrouillée) | 3,84 | 4,10 | 9,42 | 0,74 |
| `Carte_Voiture` | Rectangle | 14,18 | 0,53 | 13,12 | 4,76 |
| `Lbl_Voiture` | Étiquette | 14,74 | 0,93 | 2,49 | 0,48 |
| `Cbo_Voiture` | Zone de liste déroulante | 17,38 | 2,20 | 9,42 | 0,74 |
| `Txt_Modele` | Zone de texte (verrouillée) | 17,38 | 3,15 | 9,42 | 0,74 |
| `Txt_Marque` | Zone de texte (verrouillée) | 17,38 | 4,10 | 9,42 | 0,74 |
| `Carte_Montant` | Rectangle | 27,73 | 0,53 | 13,12 | 4,76 |
| `Txt_Montant` | Zone de texte | 28,28 | 1,51 | 5,85 | 1,38 |
| `Txt_Debut` | Étiquette | 28,28 | 3,31 | 1,59 | 0,42 |
| `Piste_Duree` | Rectangle | 28,28 | 3,94 | 12,07 | 0,11 |
| `Barre_Duree` | Rectangle | 28,28 | 3,94 | 1,96 | 0,11 |
| `Txt_Duree` | Zone de texte | 29,87 | 4,37 | 1,53 | 0,48 |
| `Carte_Reservation` | Rectangle | 0,64 | 5,72 | 40,22 | 2,80 |
| `Lbl_Reservation` | Étiquette | 1,19 | 6,11 | 3,49 | 0,48 |
| `Btn_Ajouter` | Bouton | 37,81 | 5,95 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,76 | 5,95 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,71 | 5,95 | 0,79 | 0,79 |
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
| `Carte_Liste` | Rectangle | 0,64 | 8,94 | 40,22 | 6,27 |
| `Lbl_Liste` | Étiquette | 1,19 | 9,34 | 5,98 | 0,48 |
| `Txt_Info_Liste` | Zone de texte | 37,23 | 9,37 | 2,12 | 0,42 |
| `Btn_Imprimer` | Bouton | 39,71 | 9,18 | 0,79 | 0,79 |
| `Liste_Reservations` | Zone de liste | 1,19 | 10,50 | 39,16 | 4,37 |

## Clients

Maquette : `png/03-clients.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Liste` | Rectangle | 0,64 | 0,53 | 27,09 | 14,68 |
| `Lbl_Liste` | Étiquette | 1,19 | 0,93 | 4,63 | 0,48 |
| `Btn_Imprimer` | Bouton | 26,59 | 0,77 | 0,79 | 0,79 |
| `Liste_Clients` | Zone de liste | 1,19 | 2,09 | 26,04 | 12,78 |
| `Txt_Recherche` | Zone de texte (filtre) | 19,08 | 0,77 | 6,88 | 0,79 |
| `Txt_Info_Liste` | Étiquette | 6,54 | 0,93 | 1,51 | 0,42 |
| `Carte_Fiche` | Rectangle | 28,15 | 0,53 | 12,70 | 14,68 |
| `Lbl_Fiche` | Étiquette | 28,71 | 0,93 | 3,55 | 0,48 |
| `Btn_Ajouter` | Bouton | 38,76 | 0,77 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 39,71 | 0,77 | 0,79 | 0,79 |
| `Txt_CIN` | Zone de texte | 32,15 | 2,30 | 3,70 | 0,74 |
| `Txt_Permis` | Zone de texte | 32,15 | 3,47 | 4,76 | 0,74 |
| `Txt_Prenom` | Zone de texte | 32,15 | 4,63 | 8,20 | 0,74 |
| `Txt_Nom` | Zone de texte | 32,15 | 5,79 | 8,20 | 0,74 |
| `Cbo_Sexe` | Zone de liste déroulante | 32,15 | 6,96 | 2,12 | 0,74 |
| `Txt_Adresse` | Zone de texte | 32,15 | 8,12 | 8,20 | 0,74 |
| `Txt_Telephone` | Zone de texte | 32,15 | 9,29 | 8,20 | 0,74 |
| `Txt_Email` | Zone de texte | 32,15 | 10,45 | 8,20 | 0,74 |
| `Btn_Premier` | Bouton | 31,33 | 12,04 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 32,23 | 12,04 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 36,04 | 12,04 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 36,94 | 12,04 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 33,13 | 12,04 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 28,71 | 13,86 | 5,69 | 0,85 |
| `Btn_Supprimer` | Bouton | 34,66 | 13,86 | 5,69 | 0,85 |

## Voitures

Maquette : `png/04-voitures.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Liste` | Rectangle | 0,64 | 0,53 | 27,09 | 14,68 |
| `Lbl_Liste` | Étiquette | 1,19 | 0,93 | 4,89 | 0,48 |
| `Btn_Imprimer` | Bouton | 26,59 | 0,77 | 0,79 | 0,79 |
| `Liste_Voitures` | Zone de liste | 1,19 | 2,09 | 26,04 | 12,78 |
| `Txt_Recherche` | Zone de texte (filtre) | 19,08 | 0,77 | 6,88 | 0,79 |
| `Txt_Info_Liste` | Étiquette | 6,77 | 0,93 | 1,51 | 0,42 |
| `Carte_Fiche` | Rectangle | 28,15 | 0,53 | 12,70 | 14,68 |
| `Lbl_Fiche` | Étiquette | 28,71 | 0,93 | 3,81 | 0,48 |
| `Btn_Ajouter` | Bouton | 38,76 | 0,77 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 39,71 | 0,77 | 0,79 | 0,79 |
| `Txt_Matricule` | Zone de texte | 32,15 | 2,30 | 3,70 | 0,74 |
| `Txt_Annee` | Zone de texte | 32,15 | 3,47 | 2,12 | 0,74 |
| `Txt_Couleur` | Zone de texte | 32,15 | 4,63 | 8,20 | 0,74 |
| `Txt_Puissance` | Zone de texte | 32,15 | 5,79 | 2,65 | 0,74 |
| `Txt_CoutJour` | Zone de texte | 32,15 | 6,96 | 4,23 | 0,74 |
| `Cbo_Modele` | Zone de liste déroulante | 32,15 | 8,12 | 8,20 | 0,74 |
| `Cbo_Carburant` | Zone de liste déroulante | 32,15 | 9,29 | 8,20 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 32,15 | 10,45 | 8,20 | 0,74 |
| `Btn_Premier` | Bouton | 31,33 | 12,04 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 32,23 | 12,04 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 36,04 | 12,04 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 36,94 | 12,04 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 33,13 | 12,04 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 28,71 | 13,86 | 5,69 | 0,85 |
| `Btn_Supprimer` | Bouton | 34,66 | 13,86 | 5,69 | 0,85 |

## Marques

Maquette : `png/05-marques.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Liste` | Rectangle | 0,64 | 0,53 | 27,09 | 14,68 |
| `Lbl_Liste` | Étiquette | 1,19 | 0,93 | 4,79 | 0,48 |
| `Btn_Imprimer` | Bouton | 26,59 | 0,77 | 0,79 | 0,79 |
| `Liste_Marques` | Zone de liste | 1,19 | 2,09 | 26,04 | 12,78 |
| `Txt_Recherche` | Zone de texte (filtre) | 19,08 | 0,77 | 6,88 | 0,79 |
| `Txt_Info_Liste` | Étiquette | 6,54 | 0,93 | 1,43 | 0,42 |
| `Carte_Fiche` | Rectangle | 28,15 | 0,53 | 12,70 | 6,61 |
| `Lbl_Fiche` | Étiquette | 28,71 | 0,93 | 3,70 | 0,48 |
| `Btn_Ajouter` | Bouton | 38,76 | 0,77 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 39,71 | 0,77 | 0,79 | 0,79 |
| `Txt_IdMarque` | Zone de texte | 32,15 | 2,30 | 2,12 | 0,74 |
| `Txt_Marque` | Zone de texte | 32,15 | 3,47 | 8,20 | 0,74 |
| `Btn_Premier` | Bouton | 31,33 | 5,05 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 32,23 | 5,05 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 36,04 | 5,05 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 36,94 | 5,05 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 33,13 | 5,05 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 28,71 | 5,79 | 5,69 | 0,85 |
| `Btn_Supprimer` | Bouton | 34,66 | 5,79 | 5,69 | 0,85 |
| `Image_Vignette` | Image (e-vignette-marques.jpg) | 28,15 | 7,57 | 12,70 | 7,65 |
| `Lbl_Chiffre` | Étiquette | 28,73 | 12,78 | 0,58 | 1,53 |
| `Lbl_Chiffre_Texte` | Étiquette | 28,79 | 14,31 | 4,15 | 0,37 |

## Carburants

Maquette : `png/06-carburants.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Liste` | Rectangle | 0,64 | 0,53 | 27,09 | 14,68 |
| `Lbl_Liste` | Étiquette | 1,19 | 0,93 | 5,19 | 0,48 |
| `Btn_Imprimer` | Bouton | 26,59 | 0,77 | 0,79 | 0,79 |
| `Liste_Carburants` | Zone de liste | 1,19 | 2,09 | 26,04 | 12,78 |
| `Txt_Recherche` | Zone de texte (filtre) | 19,08 | 0,77 | 6,88 | 0,79 |
| `Txt_Info_Liste` | Étiquette | 6,77 | 0,93 | 0,98 | 0,42 |
| `Carte_Fiche` | Rectangle | 28,15 | 0,53 | 12,70 | 6,61 |
| `Lbl_Fiche` | Étiquette | 28,71 | 0,93 | 4,50 | 0,48 |
| `Btn_Ajouter` | Bouton | 38,76 | 0,77 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 39,71 | 0,77 | 0,79 | 0,79 |
| `Txt_IdType` | Zone de texte | 32,15 | 2,30 | 2,12 | 0,74 |
| `Txt_Type` | Zone de texte | 32,15 | 3,47 | 8,20 | 0,74 |
| `Btn_Premier` | Bouton | 31,33 | 5,05 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 32,23 | 5,05 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 36,04 | 5,05 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 36,94 | 5,05 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 33,13 | 5,05 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 28,71 | 5,79 | 5,69 | 0,85 |
| `Btn_Supprimer` | Bouton | 34,66 | 5,79 | 5,69 | 0,85 |
| `Image_Vignette` | Image (e-vignette-carburants.jpg) | 28,15 | 7,57 | 12,70 | 7,65 |
| `Lbl_Chiffre` | Étiquette | 28,73 | 12,78 | 0,58 | 1,53 |
| `Lbl_Chiffre_Texte` | Étiquette | 28,79 | 14,31 | 4,05 | 0,37 |

## Modèles

Maquette : `png/07-modeles.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Liste` | Rectangle | 0,64 | 0,53 | 27,09 | 14,68 |
| `Lbl_Liste` | Étiquette | 1,19 | 0,93 | 4,76 | 0,48 |
| `Btn_Imprimer` | Bouton | 26,59 | 0,77 | 0,79 | 0,79 |
| `Liste_Modeles` | Zone de liste | 1,19 | 2,09 | 26,04 | 12,78 |
| `Txt_Recherche` | Zone de texte (filtre) | 19,08 | 0,77 | 6,88 | 0,79 |
| `Txt_Info_Liste` | Étiquette | 6,54 | 0,93 | 1,56 | 0,42 |
| `Carte_Fiche` | Rectangle | 28,15 | 0,53 | 12,70 | 7,78 |
| `Lbl_Fiche` | Étiquette | 28,71 | 0,93 | 3,68 | 0,48 |
| `Btn_Ajouter` | Bouton | 38,76 | 0,77 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 39,71 | 0,77 | 0,79 | 0,79 |
| `Txt_IdModele` | Zone de texte | 32,15 | 2,30 | 2,12 | 0,74 |
| `Txt_Modele` | Zone de texte | 32,15 | 3,47 | 8,20 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 32,15 | 4,63 | 8,20 | 0,74 |
| `Btn_Premier` | Bouton | 31,33 | 6,22 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 32,23 | 6,22 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 36,04 | 6,22 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 36,94 | 6,22 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 33,13 | 6,22 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 28,71 | 6,96 | 5,69 | 0,85 |
| `Btn_Supprimer` | Bouton | 34,66 | 6,96 | 5,69 | 0,85 |
| `Image_Vignette` | Image (e-vignette-modeles.jpg) | 28,15 | 8,73 | 12,70 | 6,48 |
| `Lbl_Chiffre` | Étiquette | 28,73 | 12,78 | 1,22 | 1,53 |
| `Lbl_Chiffre_Texte` | Étiquette | 28,79 | 14,31 | 4,47 | 0,37 |
