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
| `Login_Fond` | Section Détail | 0,00 | 0,00 | 23,28 | 13,76 |
| `Login_Photo` | Image (c-connexion.jpg) | 0,00 | 0,00 | 23,28 | 7,94 |
| `Logo` | Image + étiquette | 1,06 | 0,90 | 4,34 | 0,74 |
| `Lbl_Titre` | Étiquette | 1,06 | 5,19 | 4,31 | 1,14 |
| `Txt_Utilisateur` | Zone de texte | 1,06 | 9,47 | 6,88 | 0,95 |
| `Txt_MotDePasse` | Zone de texte | 8,47 | 9,47 | 6,88 | 0,95 |
| `Btn_Connexion` | Bouton | 15,88 | 9,47 | 6,35 | 0,95 |

## Formulaire « Menu » (commun à tous les écrans)

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Menu_Fond` | Image (c-menu-tableau.jpg) | 34,61 | 0,00 | 6,88 | 20,74 |
| `Logo` | Image + étiquette | 35,24 | 0,74 | 3,78 | 0,69 |
| `BoutonNavigation_tableau` | Bouton de navigation | 35,03 | 3,18 | 6,03 | 1,01 |
| `BoutonNavigation_reservations` | Bouton de navigation | 35,03 | 4,39 | 6,03 | 1,01 |
| `BoutonNavigation_clients` | Bouton de navigation | 35,03 | 5,61 | 6,03 | 1,01 |
| `BoutonNavigation_voitures` | Bouton de navigation | 35,03 | 6,83 | 6,03 | 1,01 |
| `BoutonNavigation_marques` | Bouton de navigation | 35,03 | 8,04 | 6,03 | 1,01 |
| `BoutonNavigation_carburants` | Bouton de navigation | 35,03 | 9,26 | 6,03 | 1,01 |
| `BoutonNavigation_modeles` | Bouton de navigation | 35,03 | 10,48 | 6,03 | 1,01 |
| `Carte_Utilisateur` | Rectangle | 35,03 | 18,63 | 6,03 | 1,59 |
| `Btn_Avatar` | Bouton (ellipse) | 35,35 | 19,00 | 0,85 | 0,85 |
| `Utilisateur` | Étiquettes | 36,51 | 18,97 | 3,07 | 0,85 |
| `Btn_Quitter` | Bouton | 40,11 | 19,16 | 0,53 | 0,53 |
| `Sous_Formulaire` | Sous-formulaire | 0,00 | 0,00 | 34,61 | 20,74 |

## Tableau de bord

Maquette : `png/01-tableau-de-bord.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,64 | 5,79 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,80 | 9,90 | 0,53 |
| `Date_Heure` | Zone de texte | 27,91 | 0,90 | 5,85 | 0,48 |
| `Carte_CA` | Rectangle | 0,85 | 3,18 | 10,53 | 2,91 |
| `Txt_CA` | Zone de texte | 1,43 | 4,18 | 6,24 | 1,08 |
| `Carte_Voitures` | Rectangle | 12,01 | 3,18 | 10,53 | 2,91 |
| `Txt_Voitures` | Zone de texte | 12,59 | 4,18 | 0,90 | 1,08 |
| `Carte_Clients` | Rectangle | 23,18 | 3,18 | 10,53 | 2,91 |
| `Txt_Clients` | Zone de texte | 23,76 | 4,18 | 1,35 | 1,08 |
| `Carte_Reservees` | Rectangle | 0,85 | 6,61 | 20,11 | 13,49 |
| `Btn_Imprimer` | Bouton | 19,84 | 6,88 | 0,79 | 0,79 |
| `Liste_Voitures_Reservees` | Zone de liste | 1,38 | 8,31 | 19,05 | 11,27 |
| `Carte_Top5` | Rectangle | 21,59 | 6,61 | 12,17 | 6,35 |
| `Liste_Top5` | Zone de liste | 22,12 | 8,31 | 11,11 | 4,13 |
| `Carte_Carburants` | Rectangle | 21,59 | 13,39 | 12,17 | 6,72 |
| `Liste_Carburants` | Zone de liste | 22,12 | 15,08 | 11,11 | 4,50 |

## Réservations

Maquette : `png/02-reservations.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,64 | 4,84 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,80 | 7,14 | 0,53 |
| `Date_Heure` | Zone de texte | 27,91 | 0,90 | 5,85 | 0,48 |
| `Carte_Client` | Rectangle | 0,85 | 3,18 | 10,69 | 6,61 |
| `Cbo_Client` | Zone de liste déroulante | 1,38 | 5,40 | 9,63 | 0,74 |
| `Txt_Telephone` | Zone de texte (verrouillée) | 1,38 | 6,93 | 9,63 | 0,74 |
| `Txt_Email` | Zone de texte (verrouillée) | 1,38 | 8,47 | 9,63 | 0,74 |
| `Carte_Voiture` | Rectangle | 11,96 | 3,18 | 10,69 | 6,61 |
| `Cbo_Voiture` | Zone de liste déroulante | 12,49 | 5,40 | 9,63 | 0,74 |
| `Txt_Modele` | Zone de texte (verrouillée) | 12,49 | 6,93 | 9,63 | 0,74 |
| `Txt_Marque` | Zone de texte (verrouillée) | 12,49 | 8,47 | 9,63 | 0,74 |
| `Carte_Reservation` | Rectangle | 23,07 | 3,18 | 10,69 | 6,61 |
| `Btn_Ajouter` | Bouton | 31,70 | 3,44 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 32,65 | 3,44 | 0,79 | 0,79 |
| `Txt_Code` | Zone de texte | 23,60 | 5,40 | 1,85 | 0,74 |
| `Txt_DateDebut` | Zone de texte | 25,88 | 5,40 | 2,67 | 0,74 |
| `Txt_DateFin` | Zone de texte | 28,87 | 5,40 | 2,67 | 0,74 |
| `Btn_OK` | Bouton | 31,64 | 5,40 | 1,59 | 0,79 |
| `Txt_Duree` | Zone de texte (verrouillée) | 23,60 | 6,93 | 4,60 | 0,74 |
| `Txt_Montant` | Zone de texte (verrouillée) | 28,63 | 6,93 | 4,60 | 0,74 |
| `Btn_Premier` | Bouton | 23,60 | 8,20 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 24,50 | 8,20 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 28,31 | 8,20 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 29,21 | 8,20 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 25,40 | 8,20 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 26,62 | 10,16 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 30,32 | 10,16 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 0,85 | 11,43 | 32,91 | 8,68 |
| `Btn_Imprimer` | Bouton | 32,65 | 11,69 | 0,79 | 0,79 |
| `Liste_Reservations` | Zone de liste | 1,38 | 13,07 | 31,86 | 6,56 |

## Clients

Maquette : `png/03-clients.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,64 | 2,54 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,80 | 4,05 | 0,53 |
| `Date_Heure` | Zone de texte | 27,91 | 0,90 | 5,85 | 0,48 |
| `Carte_Fiche` | Rectangle | 0,85 | 3,18 | 11,64 | 16,67 |
| `Btn_Ajouter` | Bouton | 8,52 | 3,44 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 9,47 | 3,44 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 10,42 | 3,44 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 11,38 | 3,44 | 0,79 | 0,79 |
| `Txt_CIN` | Zone de texte | 1,38 | 5,40 | 5,29 | 0,74 |
| `Txt_Permis` | Zone de texte | 1,38 | 6,93 | 6,35 | 0,74 |
| `Txt_Prenom` | Zone de texte | 1,38 | 8,47 | 10,58 | 0,74 |
| `Txt_Nom` | Zone de texte | 1,38 | 10,00 | 10,58 | 0,74 |
| `Cbo_Sexe` | Zone de liste déroulante | 1,38 | 11,54 | 3,70 | 0,74 |
| `Txt_Adresse` | Zone de texte | 1,38 | 13,07 | 10,58 | 0,74 |
| `Txt_Telephone` | Zone de texte | 1,38 | 14,61 | 10,58 | 0,74 |
| `Txt_Email` | Zone de texte | 1,38 | 16,14 | 10,58 | 0,74 |
| `Btn_Premier` | Bouton | 1,38 | 17,30 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 2,28 | 17,30 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 6,09 | 17,30 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 6,99 | 17,30 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 3,18 | 17,30 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 1,38 | 18,47 | 5,16 | 0,85 |
| `Btn_Supprimer` | Bouton | 6,80 | 18,47 | 5,16 | 0,85 |
| `Carte_Liste` | Rectangle | 13,12 | 3,18 | 20,64 | 16,93 |
| `Btn_Imprimer` | Bouton | 32,65 | 3,44 | 0,79 | 0,79 |
| `Liste_Clients` | Zone de liste | 13,65 | 4,92 | 19,58 | 14,66 |

## Voitures

Maquette : `png/04-voitures.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,64 | 3,12 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,80 | 10,61 | 0,53 |
| `Date_Heure` | Zone de texte | 27,91 | 0,90 | 5,85 | 0,48 |
| `Carte_Fiche` | Rectangle | 0,85 | 3,18 | 11,64 | 16,67 |
| `Btn_Ajouter` | Bouton | 8,52 | 3,44 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 9,47 | 3,44 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 10,42 | 3,44 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 11,38 | 3,44 | 0,79 | 0,79 |
| `Txt_Matricule` | Zone de texte | 1,38 | 5,40 | 5,29 | 0,74 |
| `Txt_Annee` | Zone de texte | 1,38 | 6,93 | 3,70 | 0,74 |
| `Txt_Couleur` | Zone de texte | 1,38 | 8,47 | 10,58 | 0,74 |
| `Txt_Puissance` | Zone de texte | 1,38 | 10,00 | 4,23 | 0,74 |
| `Txt_CoutJour` | Zone de texte | 1,38 | 11,54 | 5,82 | 0,74 |
| `Cbo_Modele` | Zone de liste déroulante | 1,38 | 13,07 | 10,58 | 0,74 |
| `Cbo_Carburant` | Zone de liste déroulante | 1,38 | 14,61 | 10,58 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 1,38 | 16,14 | 10,58 | 0,74 |
| `Btn_Premier` | Bouton | 1,38 | 17,30 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 2,28 | 17,30 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 6,09 | 17,30 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 6,99 | 17,30 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 3,18 | 17,30 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 1,38 | 18,47 | 5,16 | 0,85 |
| `Btn_Supprimer` | Bouton | 6,80 | 18,47 | 5,16 | 0,85 |
| `Carte_Liste` | Rectangle | 13,12 | 3,18 | 20,64 | 16,93 |
| `Btn_Imprimer` | Bouton | 32,65 | 3,44 | 0,79 | 0,79 |
| `Liste_Voitures` | Zone de liste | 13,65 | 4,92 | 19,58 | 14,66 |

## Marques

Maquette : `png/05-marques.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,64 | 3,31 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,80 | 6,46 | 0,53 |
| `Date_Heure` | Zone de texte | 27,91 | 0,90 | 5,85 | 0,48 |
| `Carte_Fiche` | Rectangle | 0,85 | 3,18 | 11,64 | 7,46 |
| `Btn_Ajouter` | Bouton | 8,52 | 3,44 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 9,47 | 3,44 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 10,42 | 3,44 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 11,38 | 3,44 | 0,79 | 0,79 |
| `Txt_IdMarque` | Zone de texte | 1,38 | 5,40 | 3,70 | 0,74 |
| `Txt_Marque` | Zone de texte | 1,38 | 6,93 | 10,58 | 0,74 |
| `Btn_Premier` | Bouton | 1,38 | 8,10 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 2,28 | 8,10 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 6,09 | 8,10 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 6,99 | 8,10 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 3,18 | 8,10 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 1,38 | 9,26 | 5,16 | 0,85 |
| `Btn_Supprimer` | Bouton | 6,80 | 9,26 | 5,16 | 0,85 |
| `Carte_Liste` | Rectangle | 13,12 | 3,18 | 20,64 | 9,53 |
| `Btn_Imprimer` | Bouton | 32,65 | 3,44 | 0,79 | 0,79 |
| `Liste_Marques` | Zone de liste | 13,65 | 4,92 | 19,58 | 7,25 |

## Carburants

Maquette : `png/06-carburants.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,64 | 4,21 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,80 | 3,73 | 0,53 |
| `Date_Heure` | Zone de texte | 27,91 | 0,90 | 5,85 | 0,48 |
| `Carte_Fiche` | Rectangle | 0,85 | 3,18 | 11,64 | 7,46 |
| `Btn_Ajouter` | Bouton | 8,52 | 3,44 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 9,47 | 3,44 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 10,42 | 3,44 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 11,38 | 3,44 | 0,79 | 0,79 |
| `Txt_IdType` | Zone de texte | 1,38 | 5,40 | 3,70 | 0,74 |
| `Txt_Type` | Zone de texte | 1,38 | 6,93 | 10,58 | 0,74 |
| `Btn_Premier` | Bouton | 1,38 | 8,10 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 2,28 | 8,10 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 6,09 | 8,10 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 6,99 | 8,10 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 3,18 | 8,10 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 1,38 | 9,26 | 5,16 | 0,85 |
| `Btn_Supprimer` | Bouton | 6,80 | 9,26 | 5,16 | 0,85 |
| `Carte_Liste` | Rectangle | 13,12 | 3,18 | 20,64 | 9,53 |
| `Btn_Imprimer` | Bouton | 32,65 | 3,44 | 0,79 | 0,79 |
| `Liste_Carburants` | Zone de liste | 13,65 | 4,92 | 19,58 | 7,25 |

## Modèles

Maquette : `png/07-modeles.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,64 | 3,15 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,80 | 6,32 | 0,53 |
| `Date_Heure` | Zone de texte | 27,91 | 0,90 | 5,85 | 0,48 |
| `Carte_Fiche` | Rectangle | 0,85 | 3,18 | 11,64 | 9,00 |
| `Btn_Ajouter` | Bouton | 8,52 | 3,44 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 9,47 | 3,44 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 10,42 | 3,44 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 11,38 | 3,44 | 0,79 | 0,79 |
| `Txt_IdModele` | Zone de texte | 1,38 | 5,40 | 3,70 | 0,74 |
| `Txt_Modele` | Zone de texte | 1,38 | 6,93 | 10,58 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 1,38 | 8,47 | 10,58 | 0,74 |
| `Btn_Premier` | Bouton | 1,38 | 9,63 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 2,28 | 9,63 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 6,09 | 9,63 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 6,99 | 9,63 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 3,18 | 9,63 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 1,38 | 10,80 | 5,16 | 0,85 |
| `Btn_Supprimer` | Bouton | 6,80 | 10,80 | 5,16 | 0,85 |
| `Carte_Liste` | Rectangle | 13,12 | 3,18 | 20,64 | 16,93 |
| `Btn_Imprimer` | Bouton | 32,65 | 3,44 | 0,79 | 0,79 |
| `Liste_Modeles` | Zone de liste | 13,65 | 4,92 | 19,58 | 14,66 |
