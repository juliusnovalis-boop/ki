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
| `Login_Fond` | Section Détail | 0,00 | 0,00 | 11,64 | 10,16 |
| `Logo` | Image + étiquette | 1,06 | 0,95 | 3,47 | 0,74 |
| `Lbl_Titre` | Étiquette | 1,06 | 2,43 | 2,91 | 0,77 |
| `Txt_Utilisateur` | Zone de texte | 1,06 | 4,97 | 9,53 | 0,85 |
| `Txt_MotDePasse` | Zone de texte | 1,06 | 6,77 | 9,53 | 0,85 |
| `Btn_Connexion` | Bouton | 1,06 | 8,36 | 9,53 | 0,95 |

## Formulaire « Menu » (commun à tous les écrans)

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Menu_Fond` | Rectangle | 0,00 | 0,00 | 5,82 | 20,74 |
| `Logo` | Image + étiquette | 0,53 | 0,40 | 3,41 | 0,69 |
| `BoutonNavigation_tableau` | Bouton de navigation | 0,32 | 2,01 | 5,19 | 1,01 |
| `BoutonNavigation_reservations` | Bouton de navigation | 0,32 | 3,18 | 5,19 | 1,01 |
| `BoutonNavigation_clients` | Bouton de navigation | 0,32 | 4,34 | 5,19 | 1,01 |
| `BoutonNavigation_voitures` | Bouton de navigation | 0,32 | 5,50 | 5,19 | 1,01 |
| `BoutonNavigation_marques` | Bouton de navigation | 0,32 | 6,67 | 5,19 | 1,01 |
| `BoutonNavigation_carburants` | Bouton de navigation | 0,32 | 7,83 | 5,19 | 1,01 |
| `BoutonNavigation_modeles` | Bouton de navigation | 0,32 | 9,00 | 5,19 | 1,01 |
| `Entete` | Rectangle | 5,82 | 0,00 | 35,67 | 1,48 |
| `Titre_Page` | Étiquette | 6,46 | 0,34 | 4,42 | 0,77 |
| `Date_Heure` | Zone de texte | 36,17 | 0,48 | 3,41 | 0,48 |
| `Btn_Quitter` | Bouton | 40,01 | 0,32 | 0,85 | 0,85 |

## Tableau de bord

Maquette : `maquettes/png/01-tableau-de-bord.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_CA` | Rectangle | 0,64 | 0,64 | 11,17 | 2,54 |
| `Txt_CA` | Zone de texte | 1,19 | 1,77 | 5,08 | 0,98 |
| `Pastille_CA` | Rectangle + image | 9,97 | 1,30 | 1,27 | 1,27 |
| `Carte_Voitures` | Rectangle | 12,22 | 0,64 | 11,17 | 2,54 |
| `Txt_Voitures` | Zone de texte | 12,78 | 1,77 | 0,79 | 0,98 |
| `Pastille_Voitures` | Rectangle + image | 21,56 | 1,30 | 1,27 | 1,27 |
| `Carte_Clients` | Rectangle | 23,81 | 0,64 | 11,17 | 2,54 |
| `Txt_Clients` | Zone de texte | 24,37 | 1,77 | 1,22 | 0,98 |
| `Pastille_Clients` | Rectangle + image | 33,15 | 1,30 | 1,27 | 1,27 |
| `Carte_Reservees` | Rectangle | 0,64 | 3,60 | 22,12 | 7,20 |
| `Btn_Imprimer` | Bouton | 21,62 | 3,89 | 0,79 | 0,79 |
| `Liste_Voitures_Reservees` | Zone de liste | 1,19 | 5,37 | 21,01 | 4,92 |
| `Carte_Top5` | Rectangle | 23,18 | 3,60 | 11,85 | 7,20 |
| `Liste_Top5` | Zone de liste | 23,73 | 5,37 | 10,80 | 4,92 |
| `Carte_Dernieres` | Rectangle | 0,64 | 11,22 | 34,40 | 7,20 |
| `Btn_Imprimer` | Bouton | 33,89 | 11,51 | 0,79 | 0,79 |
| `Liste_Dernieres` | Zone de liste | 1,19 | 12,99 | 33,34 | 4,92 |

## Réservations

Maquette : `maquettes/png/02-reservations.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Client` | Rectangle | 0,64 | 0,64 | 16,99 | 5,08 |
| `Cbo_Client` | Zone de liste déroulante | 3,94 | 2,46 | 12,70 | 0,74 |
| `Txt_Telephone` | Zone de texte (verrouillée) | 3,94 | 3,47 | 12,70 | 0,74 |
| `Txt_Email` | Zone de texte (verrouillée) | 3,94 | 4,47 | 12,70 | 0,74 |
| `Carte_Voiture` | Rectangle | 18,04 | 0,64 | 16,99 | 5,08 |
| `Cbo_Voiture` | Zone de liste déroulante | 21,35 | 2,46 | 12,70 | 0,74 |
| `Txt_Modele` | Zone de texte (verrouillée) | 21,35 | 3,47 | 12,70 | 0,74 |
| `Txt_Marque` | Zone de texte (verrouillée) | 21,35 | 4,47 | 12,70 | 0,74 |
| `Carte_Reservation` | Rectangle | 0,64 | 6,14 | 34,40 | 5,19 |
| `Btn_Ajouter` | Bouton | 31,04 | 6,43 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 31,99 | 6,43 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 32,94 | 6,43 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 33,89 | 6,43 | 0,79 | 0,79 |
| `Txt_Code` | Zone de texte | 3,94 | 7,96 | 2,12 | 0,74 |
| `Txt_DateDebut` | Zone de texte | 3,94 | 8,97 | 3,18 | 0,74 |
| `Txt_DateFin` | Zone de texte | 10,24 | 8,97 | 3,18 | 0,74 |
| `Btn_OK` | Bouton | 13,73 | 8,92 | 1,59 | 0,85 |
| `Btn_Premier` | Bouton | 3,94 | 10,13 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 4,84 | 10,13 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 8,65 | 10,13 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 9,55 | 10,13 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 5,74 | 10,13 | 2,80 | 0,74 |
| `Txt_Duree` | Zone de texte (verrouillée) | 20,61 | 7,96 | 5,29 | 0,74 |
| `Txt_Montant` | Zone de texte (verrouillée) | 20,61 | 8,97 | 5,29 | 0,74 |
| `Btn_Enregistrer` | Bouton | 27,91 | 10,08 | 3,18 | 0,85 |
| `Btn_Supprimer` | Bouton | 31,35 | 10,08 | 3,18 | 0,85 |
| `Carte_Liste` | Rectangle | 0,64 | 11,75 | 34,40 | 7,20 |
| `Btn_Imprimer` | Bouton | 33,89 | 12,04 | 0,79 | 0,79 |
| `Liste_Reservations` | Zone de liste | 1,19 | 13,52 | 33,34 | 4,92 |

## Clients

Maquette : `maquettes/png/03-clients.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Fiche` | Rectangle | 0,64 | 0,64 | 13,76 | 13,49 |
| `Btn_Ajouter` | Bouton | 10,40 | 0,93 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 11,35 | 0,93 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 12,30 | 0,93 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 13,26 | 0,93 | 0,79 | 0,79 |
| `Txt_CIN` | Zone de texte | 4,63 | 2,51 | 3,70 | 0,74 |
| `Txt_Permis` | Zone de texte | 4,63 | 3,57 | 4,76 | 0,74 |
| `Txt_Prenom` | Zone de texte | 4,63 | 4,63 | 9,26 | 0,74 |
| `Txt_Nom` | Zone de texte | 4,63 | 5,69 | 9,26 | 0,74 |
| `Cbo_Sexe` | Zone de liste déroulante | 4,63 | 6,75 | 2,12 | 0,74 |
| `Txt_Adresse` | Zone de texte | 4,63 | 7,81 | 9,26 | 0,74 |
| `Txt_Telephone` | Zone de texte | 4,63 | 8,86 | 9,26 | 0,74 |
| `Txt_Email` | Zone de texte | 4,63 | 9,92 | 9,26 | 0,74 |
| `Btn_Premier` | Bouton | 4,63 | 11,19 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,53 | 11,19 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,34 | 11,19 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,24 | 11,19 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,43 | 11,19 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 7,28 | 12,83 | 3,18 | 0,85 |
| `Btn_Supprimer` | Bouton | 10,72 | 12,83 | 3,18 | 0,85 |
| `Carte_Liste` | Rectangle | 14,82 | 0,64 | 20,21 | 17,99 |
| `Btn_Imprimer` | Bouton | 33,89 | 0,93 | 0,79 | 0,79 |
| `Liste_Clients` | Zone de liste | 15,37 | 2,41 | 19,16 | 15,72 |

## Voitures

Maquette : `maquettes/png/04-voitures.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Fiche` | Rectangle | 0,64 | 0,64 | 13,76 | 13,49 |
| `Btn_Ajouter` | Bouton | 10,40 | 0,93 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 11,35 | 0,93 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 12,30 | 0,93 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 13,26 | 0,93 | 0,79 | 0,79 |
| `Txt_Matricule` | Zone de texte | 4,63 | 2,51 | 3,70 | 0,74 |
| `Txt_Annee` | Zone de texte | 4,63 | 3,57 | 2,12 | 0,74 |
| `Txt_Couleur` | Zone de texte | 4,63 | 4,63 | 9,26 | 0,74 |
| `Txt_Puissance` | Zone de texte | 4,63 | 5,69 | 2,12 | 0,74 |
| `Txt_CoutJour` | Zone de texte | 4,63 | 6,75 | 3,70 | 0,74 |
| `Cbo_Modele` | Zone de liste déroulante | 4,63 | 7,81 | 9,26 | 0,74 |
| `Cbo_Carburant` | Zone de liste déroulante | 4,63 | 8,86 | 9,26 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 4,63 | 9,92 | 9,26 | 0,74 |
| `Btn_Premier` | Bouton | 4,63 | 11,19 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,53 | 11,19 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,34 | 11,19 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,24 | 11,19 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,43 | 11,19 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 7,28 | 12,83 | 3,18 | 0,85 |
| `Btn_Supprimer` | Bouton | 10,72 | 12,83 | 3,18 | 0,85 |
| `Carte_Liste` | Rectangle | 14,82 | 0,64 | 20,21 | 17,99 |
| `Btn_Imprimer` | Bouton | 33,89 | 0,93 | 0,79 | 0,79 |
| `Liste_Voitures` | Zone de liste | 15,37 | 2,41 | 19,16 | 15,72 |

## Marques

Maquette : `maquettes/png/05-marques.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Fiche` | Rectangle | 0,64 | 0,64 | 13,76 | 7,14 |
| `Btn_Ajouter` | Bouton | 10,40 | 0,93 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 11,35 | 0,93 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 12,30 | 0,93 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 13,26 | 0,93 | 0,79 | 0,79 |
| `Txt_IdMarque` | Zone de texte | 4,63 | 2,51 | 2,12 | 0,74 |
| `Txt_Marque` | Zone de texte | 4,63 | 3,57 | 9,26 | 0,74 |
| `Btn_Premier` | Bouton | 4,63 | 4,84 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,53 | 4,84 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,34 | 4,84 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,24 | 4,84 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,43 | 4,84 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 7,28 | 6,48 | 3,18 | 0,85 |
| `Btn_Supprimer` | Bouton | 10,72 | 6,48 | 3,18 | 0,85 |
| `Carte_Liste` | Rectangle | 14,82 | 0,64 | 20,21 | 7,94 |
| `Btn_Imprimer` | Bouton | 33,89 | 0,93 | 0,79 | 0,79 |
| `Liste_Marques` | Zone de liste | 15,37 | 2,41 | 19,16 | 5,66 |

## Carburants

Maquette : `maquettes/png/06-carburants.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Fiche` | Rectangle | 0,64 | 0,64 | 13,76 | 7,14 |
| `Btn_Ajouter` | Bouton | 10,40 | 0,93 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 11,35 | 0,93 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 12,30 | 0,93 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 13,26 | 0,93 | 0,79 | 0,79 |
| `Txt_IdType` | Zone de texte | 4,63 | 2,51 | 2,12 | 0,74 |
| `Txt_Type` | Zone de texte | 4,63 | 3,57 | 9,26 | 0,74 |
| `Btn_Premier` | Bouton | 4,63 | 4,84 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,53 | 4,84 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,34 | 4,84 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,24 | 4,84 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,43 | 4,84 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 7,28 | 6,48 | 3,18 | 0,85 |
| `Btn_Supprimer` | Bouton | 10,72 | 6,48 | 3,18 | 0,85 |
| `Carte_Liste` | Rectangle | 14,82 | 0,64 | 20,21 | 7,94 |
| `Btn_Imprimer` | Bouton | 33,89 | 0,93 | 0,79 | 0,79 |
| `Liste_Carburants` | Zone de liste | 15,37 | 2,41 | 19,16 | 5,66 |

## Modèles

Maquette : `maquettes/png/07-modeles.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Fiche` | Rectangle | 0,64 | 0,64 | 13,76 | 8,20 |
| `Btn_Ajouter` | Bouton | 10,40 | 0,93 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 11,35 | 0,93 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 12,30 | 0,93 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 13,26 | 0,93 | 0,79 | 0,79 |
| `Txt_IdModele` | Zone de texte | 4,63 | 2,51 | 2,12 | 0,74 |
| `Txt_Modele` | Zone de texte | 4,63 | 3,57 | 9,26 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 4,63 | 4,63 | 9,26 | 0,74 |
| `Btn_Premier` | Bouton | 4,63 | 5,90 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,53 | 5,90 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,34 | 5,90 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,24 | 5,90 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,43 | 5,90 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 7,28 | 7,54 | 3,18 | 0,85 |
| `Btn_Supprimer` | Bouton | 10,72 | 7,54 | 3,18 | 0,85 |
| `Carte_Liste` | Rectangle | 14,82 | 0,64 | 20,21 | 17,99 |
| `Btn_Imprimer` | Bouton | 33,89 | 0,93 | 0,79 | 0,79 |
| `Liste_Modeles` | Zone de liste | 15,37 | 2,41 | 19,16 | 15,72 |
