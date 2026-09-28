# Cotes des contrôles

Positions et tailles en **centimètres**, à saisir dans la feuille de propriétés d'Access (onglet *Format* : `Gauche`, `Haut`, `Largeur`, `Hauteur`).

* **Menu** : mesurées depuis le coin haut-gauche du formulaire `Menu` (41,49 × 20,74 cm).
* **Autres écrans** : mesurées depuis le coin haut-gauche du **sous-formulaire** (35,67 × 19,26 cm).
* Les contrôles placés dans une carte sont donnés en position absolue dans le sous-formulaire.
* Fichier généré par `outils/generer.py`.

## Connexion

Maquette : `maquettes/png/00-connexion.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Login_Fond` | Section Détail | 0,00 | 0,00 | 23,28 | 13,23 |
| `Login_Photo` | Image (login-photo.jpg) | 0,00 | 0,00 | 11,11 | 13,23 |
| `Logo` | Image + étiquette | 0,95 | 0,95 | 6,06 | 0,74 |
| `Login_Slogan` | Étiquette | 0,95 | 10,27 | 9,26 | 1,48 |
| `Login_Copyright` | Étiquette | 0,95 | 12,01 | 4,18 | 0,45 |
| `Lbl_Titre` | Étiquette | 12,44 | 2,22 | 3,65 | 0,98 |
| `Txt_Utilisateur` | Zone de texte | 12,44 | 5,29 | 9,53 | 0,90 |
| `Txt_MotDePasse` | Zone de texte | 12,44 | 7,20 | 9,53 | 0,90 |
| `Btn_Connexion` | Bouton | 12,44 | 8,84 | 9,53 | 1,01 |

## Formulaire « Menu » (commun à tous les écrans)

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Menu_Fond` | Image (menu-fond.jpg) | 0,00 | 0,00 | 5,82 | 20,74 |
| `Logo` | Image + étiquette | 0,48 | 0,42 | 4,87 | 0,64 |
| `BoutonNavigation_tableau` | Bouton de navigation | 0,32 | 2,91 | 5,19 | 1,01 |
| `BoutonNavigation_reservations` | Bouton de navigation | 0,32 | 4,07 | 5,19 | 1,01 |
| `BoutonNavigation_clients` | Bouton de navigation | 0,32 | 5,24 | 5,19 | 1,01 |
| `BoutonNavigation_voitures` | Bouton de navigation | 0,32 | 6,40 | 5,19 | 1,01 |
| `BoutonNavigation_marques` | Bouton de navigation | 0,32 | 7,57 | 5,19 | 1,01 |
| `BoutonNavigation_carburants` | Bouton de navigation | 0,32 | 8,73 | 5,19 | 1,01 |
| `BoutonNavigation_modeles` | Bouton de navigation | 0,32 | 9,90 | 5,19 | 1,01 |
| `Slogan` | Étiquette | 0,64 | 19,05 | 3,52 | 0,95 |
| `Entete` | Rectangle | 5,82 | 0,00 | 35,67 | 1,48 |
| `Date_Heure` | Zone de texte | 6,46 | 0,48 | 5,82 | 0,48 |
| `Btn_Avatar` | Bouton (ellipse) | 35,45 | 0,32 | 0,85 | 0,85 |
| `Utilisateur` | Étiquettes | 36,51 | 0,29 | 3,07 | 0,85 |
| `Btn_Quitter` | Bouton | 40,01 | 0,32 | 0,85 | 0,85 |

## Tableau de bord

Maquette : `maquettes/png/01-tableau-de-bord.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (bandeau-tableau.jpg) | 0,64 | 0,64 | 34,40 | 3,39 |
| `Bandeau_Titre` | Étiquette | 1,48 | 1,56 | 5,27 | 0,98 |
| `Bandeau_SousTitre` | Étiquette | 1,48 | 2,46 | 11,03 | 0,53 |
| `Carte_CA` | Rectangle | 0,64 | 4,45 | 11,17 | 2,65 |
| `Txt_CA` | Zone de texte | 1,19 | 5,32 | 5,08 | 0,98 |
| `Pastille_CA` | Rectangle + image | 9,97 | 5,16 | 1,27 | 1,27 |
| `Carte_Voitures` | Rectangle | 12,22 | 4,45 | 11,17 | 2,65 |
| `Txt_Voitures` | Zone de texte | 12,78 | 5,32 | 0,79 | 0,98 |
| `Pastille_Voitures` | Rectangle + image | 21,56 | 5,16 | 1,27 | 1,27 |
| `Carte_Clients` | Rectangle | 23,81 | 4,45 | 11,17 | 2,65 |
| `Txt_Clients` | Zone de texte | 24,37 | 5,32 | 1,22 | 0,98 |
| `Pastille_Clients` | Rectangle + image | 33,15 | 5,16 | 1,27 | 1,27 |
| `Carte_Reservees` | Rectangle | 0,64 | 7,51 | 22,12 | 11,11 |
| `Btn_Imprimer` | Bouton | 21,62 | 7,81 | 0,79 | 0,79 |
| `Liste_Voitures_Reservees` | Zone de liste | 1,19 | 9,29 | 21,01 | 8,84 |
| `Carte_Top5` | Rectangle | 23,18 | 7,51 | 11,85 | 5,34 |
| `Liste_Top5` | Zone de liste | 23,73 | 9,23 | 10,80 | 3,28 |
| `Carte_Carburants` | Rectangle | 23,18 | 13,28 | 11,85 | 5,34 |
| `Liste_Carburants` | Zone de liste | 23,73 | 15,00 | 10,80 | 3,28 |

## Réservations

Maquette : `maquettes/png/02-reservations.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (bandeau-reservations.jpg) | 0,64 | 0,64 | 34,40 | 2,43 |
| `Bandeau_Titre` | Étiquette | 1,48 | 1,08 | 4,39 | 0,98 |
| `Bandeau_SousTitre` | Étiquette | 1,48 | 1,98 | 7,14 | 0,53 |
| `Carte_Client` | Rectangle | 0,64 | 3,49 | 16,99 | 4,76 |
| `Cbo_Client` | Zone de liste déroulante | 3,94 | 5,21 | 12,44 | 0,74 |
| `Txt_Telephone` | Zone de texte (verrouillée) | 3,94 | 6,16 | 12,44 | 0,74 |
| `Txt_Email` | Zone de texte (verrouillée) | 3,94 | 7,12 | 12,44 | 0,74 |
| `Carte_Voiture` | Rectangle | 18,04 | 3,49 | 16,99 | 4,76 |
| `Cbo_Voiture` | Zone de liste déroulante | 21,35 | 5,21 | 12,44 | 0,74 |
| `Txt_Modele` | Zone de texte (verrouillée) | 21,35 | 6,16 | 12,44 | 0,74 |
| `Txt_Marque` | Zone de texte (verrouillée) | 21,35 | 7,12 | 12,44 | 0,74 |
| `Carte_Reservation` | Rectangle | 0,64 | 8,68 | 34,40 | 4,76 |
| `Btn_Ajouter` | Bouton | 31,04 | 8,97 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 31,99 | 8,97 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 32,94 | 8,97 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 33,89 | 8,97 | 0,79 | 0,79 |
| `Txt_Code` | Zone de texte | 3,94 | 10,40 | 2,12 | 0,74 |
| `Txt_DateDebut` | Zone de texte | 3,94 | 11,35 | 3,18 | 0,74 |
| `Txt_DateFin` | Zone de texte | 10,24 | 11,35 | 3,18 | 0,74 |
| `Btn_OK` | Bouton | 13,73 | 11,30 | 1,59 | 0,85 |
| `Btn_Premier` | Bouton | 3,94 | 12,36 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 4,84 | 12,36 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 8,65 | 12,36 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 9,55 | 12,36 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 5,74 | 12,36 | 2,80 | 0,74 |
| `Txt_Duree` | Zone de texte (verrouillée) | 20,61 | 10,40 | 5,29 | 0,74 |
| `Txt_Montant` | Zone de texte (verrouillée) | 20,61 | 11,35 | 5,29 | 0,74 |
| `Btn_Enregistrer` | Bouton | 27,38 | 12,30 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 31,09 | 12,30 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 0,64 | 13,86 | 34,40 | 4,76 |
| `Btn_Imprimer` | Bouton | 33,89 | 14,16 | 0,79 | 0,79 |
| `Liste_Reservations` | Zone de liste | 1,19 | 15,53 | 33,34 | 2,75 |

## Clients

Maquette : `maquettes/png/03-clients.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (bandeau-clients.jpg) | 0,64 | 0,64 | 34,40 | 2,43 |
| `Bandeau_Titre` | Étiquette | 1,48 | 1,08 | 2,33 | 0,98 |
| `Bandeau_SousTitre` | Étiquette | 1,48 | 1,98 | 4,05 | 0,53 |
| `Carte_Fiche` | Rectangle | 0,64 | 3,49 | 13,76 | 13,49 |
| `Btn_Ajouter` | Bouton | 10,40 | 3,78 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 11,35 | 3,78 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 12,30 | 3,78 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 13,26 | 3,78 | 0,79 | 0,79 |
| `Txt_CIN` | Zone de texte | 4,63 | 5,37 | 3,70 | 0,74 |
| `Txt_Permis` | Zone de texte | 4,63 | 6,43 | 4,76 | 0,74 |
| `Txt_Prenom` | Zone de texte | 4,63 | 7,49 | 9,26 | 0,74 |
| `Txt_Nom` | Zone de texte | 4,63 | 8,55 | 9,26 | 0,74 |
| `Cbo_Sexe` | Zone de liste déroulante | 4,63 | 9,60 | 2,12 | 0,74 |
| `Txt_Adresse` | Zone de texte | 4,63 | 10,66 | 9,26 | 0,74 |
| `Txt_Telephone` | Zone de texte | 4,63 | 11,72 | 9,26 | 0,74 |
| `Txt_Email` | Zone de texte | 4,63 | 12,78 | 9,26 | 0,74 |
| `Btn_Premier` | Bouton | 4,63 | 14,05 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,53 | 14,05 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,34 | 14,05 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,24 | 14,05 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,43 | 14,05 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 6,75 | 15,69 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 10,45 | 15,69 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 14,82 | 3,49 | 20,21 | 15,13 |
| `Btn_Imprimer` | Bouton | 33,89 | 3,78 | 0,79 | 0,79 |
| `Liste_Clients` | Zone de liste | 15,37 | 5,27 | 19,16 | 12,86 |

## Voitures

Maquette : `maquettes/png/04-voitures.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (bandeau-voitures.jpg) | 0,64 | 0,64 | 34,40 | 2,43 |
| `Bandeau_Titre` | Étiquette | 1,48 | 1,08 | 2,86 | 0,98 |
| `Bandeau_SousTitre` | Étiquette | 1,48 | 1,98 | 8,49 | 0,53 |
| `Carte_Fiche` | Rectangle | 0,64 | 3,49 | 13,76 | 13,49 |
| `Btn_Ajouter` | Bouton | 10,40 | 3,78 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 11,35 | 3,78 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 12,30 | 3,78 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 13,26 | 3,78 | 0,79 | 0,79 |
| `Txt_Matricule` | Zone de texte | 4,63 | 5,37 | 3,70 | 0,74 |
| `Txt_Annee` | Zone de texte | 4,63 | 6,43 | 2,12 | 0,74 |
| `Txt_Couleur` | Zone de texte | 4,63 | 7,49 | 9,26 | 0,74 |
| `Txt_Puissance` | Zone de texte | 4,63 | 8,55 | 2,12 | 0,74 |
| `Txt_CoutJour` | Zone de texte | 4,63 | 9,60 | 3,70 | 0,74 |
| `Cbo_Modele` | Zone de liste déroulante | 4,63 | 10,66 | 9,26 | 0,74 |
| `Cbo_Carburant` | Zone de liste déroulante | 4,63 | 11,72 | 9,26 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 4,63 | 12,78 | 9,26 | 0,74 |
| `Btn_Premier` | Bouton | 4,63 | 14,05 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,53 | 14,05 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,34 | 14,05 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,24 | 14,05 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,43 | 14,05 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 6,75 | 15,69 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 10,45 | 15,69 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 14,82 | 3,49 | 20,21 | 15,13 |
| `Btn_Imprimer` | Bouton | 33,89 | 3,78 | 0,79 | 0,79 |
| `Liste_Voitures` | Zone de liste | 15,37 | 5,27 | 19,16 | 12,86 |

## Marques

Maquette : `maquettes/png/05-marques.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (bandeau-marques.jpg) | 0,64 | 0,64 | 34,40 | 2,43 |
| `Bandeau_Titre` | Étiquette | 1,48 | 1,08 | 2,99 | 0,98 |
| `Bandeau_SousTitre` | Étiquette | 1,48 | 1,98 | 4,34 | 0,53 |
| `Carte_Fiche` | Rectangle | 0,64 | 3,49 | 13,76 | 7,14 |
| `Btn_Ajouter` | Bouton | 10,40 | 3,78 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 11,35 | 3,78 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 12,30 | 3,78 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 13,26 | 3,78 | 0,79 | 0,79 |
| `Txt_IdMarque` | Zone de texte | 4,63 | 5,37 | 2,12 | 0,74 |
| `Txt_Marque` | Zone de texte | 4,63 | 6,43 | 9,26 | 0,74 |
| `Btn_Premier` | Bouton | 4,63 | 7,70 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,53 | 7,70 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,34 | 7,70 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,24 | 7,70 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,43 | 7,70 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 6,75 | 9,34 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 10,45 | 9,34 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 14,82 | 3,49 | 20,21 | 7,94 |
| `Btn_Imprimer` | Bouton | 33,89 | 3,78 | 0,79 | 0,79 |
| `Liste_Marques` | Zone de liste | 15,37 | 5,27 | 19,16 | 5,66 |

## Carburants

Maquette : `maquettes/png/06-carburants.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (bandeau-carburants.jpg) | 0,64 | 0,64 | 34,40 | 2,43 |
| `Bandeau_Titre` | Étiquette | 1,48 | 1,08 | 3,84 | 0,98 |
| `Bandeau_SousTitre` | Étiquette | 1,48 | 1,98 | 3,73 | 0,53 |
| `Carte_Fiche` | Rectangle | 0,64 | 3,49 | 13,76 | 7,14 |
| `Btn_Ajouter` | Bouton | 10,40 | 3,78 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 11,35 | 3,78 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 12,30 | 3,78 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 13,26 | 3,78 | 0,79 | 0,79 |
| `Txt_IdType` | Zone de texte | 4,63 | 5,37 | 2,12 | 0,74 |
| `Txt_Type` | Zone de texte | 4,63 | 6,43 | 9,26 | 0,74 |
| `Btn_Premier` | Bouton | 4,63 | 7,70 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,53 | 7,70 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,34 | 7,70 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,24 | 7,70 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,43 | 7,70 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 6,75 | 9,34 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 10,45 | 9,34 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 14,82 | 3,49 | 20,21 | 7,94 |
| `Btn_Imprimer` | Bouton | 33,89 | 3,78 | 0,79 | 0,79 |
| `Liste_Carburants` | Zone de liste | 15,37 | 5,27 | 19,16 | 5,66 |

## Modèles

Maquette : `maquettes/png/07-modeles.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (bandeau-modeles.jpg) | 0,64 | 0,64 | 34,40 | 2,43 |
| `Bandeau_Titre` | Étiquette | 1,48 | 1,08 | 2,88 | 0,98 |
| `Bandeau_SousTitre` | Étiquette | 1,48 | 1,98 | 6,32 | 0,53 |
| `Carte_Fiche` | Rectangle | 0,64 | 3,49 | 13,76 | 8,20 |
| `Btn_Ajouter` | Bouton | 10,40 | 3,78 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 11,35 | 3,78 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 12,30 | 3,78 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 13,26 | 3,78 | 0,79 | 0,79 |
| `Txt_IdModele` | Zone de texte | 4,63 | 5,37 | 2,12 | 0,74 |
| `Txt_Modele` | Zone de texte | 4,63 | 6,43 | 9,26 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 4,63 | 7,49 | 9,26 | 0,74 |
| `Btn_Premier` | Bouton | 4,63 | 8,76 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,53 | 8,76 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,34 | 8,76 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,24 | 8,76 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,43 | 8,76 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 6,75 | 10,40 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 10,45 | 10,40 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 14,82 | 3,49 | 20,21 | 15,13 |
| `Btn_Imprimer` | Bouton | 33,89 | 3,78 | 0,79 | 0,79 |
| `Liste_Modeles` | Zone de liste | 15,37 | 5,27 | 19,16 | 12,86 |
