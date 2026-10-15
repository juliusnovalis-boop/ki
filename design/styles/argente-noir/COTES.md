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
| `Login_Photo` | Image (d-connexion.jpg) | 0,00 | 0,00 | 23,28 | 13,76 |
| `Login_Carte` | Rectangle | 6,35 | 1,27 | 10,58 | 11,22 |
| `Logo` | Image | 11,01 | 2,01 | 1,27 | 1,27 |
| `Lbl_Titre` | Étiquette | 6,35 | 3,49 | 10,58 | 0,66 |
| `Txt_Utilisateur` | Zone de texte | 7,41 | 6,03 | 8,47 | 0,90 |
| `Txt_MotDePasse` | Zone de texte | 7,41 | 7,94 | 8,47 | 0,90 |
| `Btn_Connexion` | Bouton | 7,41 | 9,58 | 8,47 | 1,01 |

## Formulaire « Menu » (commun à tous les écrans)

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Image_Fond` | Image (d-fond-tableau.jpg) | 0,00 | 0,00 | 41,49 | 20,74 |
| `Logo` | Image + étiquette | 0,85 | 0,58 | 5,69 | 0,69 |
| `BoutonNavigation_tableau` | Bouton de navigation | 9,10 | 0,48 | 4,50 | 0,95 |
| `BoutonNavigation_reservations` | Bouton de navigation | 13,76 | 0,48 | 3,86 | 0,95 |
| `BoutonNavigation_clients` | Bouton de navigation | 17,78 | 0,48 | 2,83 | 0,95 |
| `BoutonNavigation_voitures` | Bouton de navigation | 20,77 | 0,48 | 3,04 | 0,95 |
| `BoutonNavigation_marques` | Bouton de navigation | 23,97 | 0,48 | 2,83 | 0,95 |
| `BoutonNavigation_carburants` | Bouton de navigation | 26,96 | 0,48 | 3,47 | 0,95 |
| `BoutonNavigation_modeles` | Bouton de navigation | 30,59 | 0,48 | 2,83 | 0,95 |
| `Btn_Avatar` | Bouton (ellipse) | 38,74 | 0,53 | 0,85 | 0,85 |
| `Btn_Quitter` | Bouton | 40,01 | 0,69 | 0,53 | 0,53 |
| `Sous_Formulaire` | Sous-formulaire | 0,00 | 1,91 | 41,49 | 18,84 |

## Tableau de bord

Maquette : `png/01-tableau-de-bord.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,48 | 5,79 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,59 | 10,80 | 0,48 |
| `Date_Heure` | Zone de texte | 35,38 | 0,85 | 5,27 | 0,48 |
| `Carte_CA` | Rectangle | 0,85 | 2,75 | 9,53 | 3,18 |
| `Txt_CA` | Zone de texte | 1,43 | 3,76 | 5,66 | 0,98 |
| `Pastille_CA` | Bouton (ellipse) + image | 8,57 | 3,28 | 1,27 | 1,27 |
| `Carte_Voitures` | Rectangle | 0,85 | 6,35 | 9,53 | 3,18 |
| `Txt_Voitures` | Zone de texte | 1,43 | 7,36 | 0,79 | 0,98 |
| `Pastille_Voitures` | Bouton (ellipse) + image | 8,57 | 6,88 | 1,27 | 1,27 |
| `Carte_Clients` | Rectangle | 0,85 | 9,95 | 9,53 | 3,18 |
| `Txt_Clients` | Zone de texte | 1,43 | 10,95 | 1,22 | 0,98 |
| `Pastille_Clients` | Bouton (ellipse) + image | 8,57 | 10,48 | 1,27 | 1,27 |
| `Carte_Reservees` | Rectangle | 10,80 | 2,75 | 29,85 | 8,73 |
| `Btn_Imprimer` | Bouton | 39,50 | 3,04 | 0,79 | 0,79 |
| `Liste_Voitures_Reservees` | Zone de liste | 11,35 | 4,47 | 28,79 | 6,51 |
| `Carte_Top5` | Rectangle | 10,80 | 11,91 | 29,85 | 6,30 |
| `Liste_Top5` | Zone de liste | 11,35 | 13,63 | 28,79 | 4,07 |
| `Carte_Carburants` | Rectangle | 0,85 | 13,55 | 9,53 | 4,66 |
| `Liste_Carburants` | Zone de liste | 1,40 | 15,27 | 8,47 | 2,43 |

## Réservations

Maquette : `png/02-reservations.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,48 | 4,84 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,59 | 7,01 | 0,48 |
| `Date_Heure` | Zone de texte | 35,38 | 0,85 | 5,27 | 0,48 |
| `Carte_Reservation` | Rectangle | 0,85 | 2,75 | 11,11 | 7,83 |
| `Btn_Ajouter` | Bouton | 7,96 | 3,04 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 8,92 | 3,04 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 9,87 | 3,04 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 10,82 | 3,04 | 0,79 | 0,79 |
| `Txt_Code` | Zone de texte | 4,58 | 4,47 | 2,12 | 0,74 |
| `Txt_DateDebut` | Zone de texte | 4,58 | 5,48 | 3,70 | 0,74 |
| `Txt_DateFin` | Zone de texte | 4,58 | 6,48 | 3,70 | 0,74 |
| `Btn_OK` | Bouton | 8,81 | 6,43 | 2,12 | 0,85 |
| `Btn_Premier` | Bouton | 4,58 | 7,65 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,48 | 7,65 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,29 | 7,65 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,19 | 7,65 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,38 | 7,65 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 1,40 | 9,23 | 4,89 | 0,85 |
| `Btn_Supprimer` | Bouton | 6,56 | 9,23 | 4,89 | 0,85 |
| `Carte_Montant` | Rectangle | 0,85 | 11,01 | 11,11 | 7,20 |
| `Txt_Montant` | Zone de texte | 1,43 | 12,17 | 5,66 | 1,22 |
| `Txt_Duree` | Zone de texte | 2,73 | 13,65 | 1,64 | 0,48 |
| `Carte_Client` | Rectangle | 12,38 | 2,75 | 13,92 | 4,71 |
| `Cbo_Client` | Zone de liste déroulante | 15,58 | 4,47 | 10,21 | 0,74 |
| `Txt_Telephone` | Zone de texte (verrouillée) | 15,58 | 5,42 | 10,21 | 0,74 |
| `Txt_Email` | Zone de texte (verrouillée) | 15,58 | 6,38 | 10,21 | 0,74 |
| `Carte_Voiture` | Rectangle | 26,72 | 2,75 | 13,92 | 4,71 |
| `Cbo_Voiture` | Zone de liste déroulante | 29,92 | 4,47 | 10,21 | 0,74 |
| `Txt_Modele` | Zone de texte (verrouillée) | 29,92 | 5,42 | 10,21 | 0,74 |
| `Txt_Marque` | Zone de texte (verrouillée) | 29,92 | 6,38 | 10,21 | 0,74 |
| `Carte_Liste` | Rectangle | 12,38 | 7,88 | 28,26 | 10,32 |
| `Btn_Imprimer` | Bouton | 39,50 | 8,18 | 0,79 | 0,79 |
| `Liste_Reservations` | Zone de liste | 12,94 | 9,55 | 27,20 | 8,20 |

## Clients

Maquette : `png/03-clients.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,48 | 2,54 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,59 | 4,00 | 0,48 |
| `Date_Heure` | Zone de texte | 35,38 | 0,85 | 5,27 | 0,48 |
| `Carte_Liste` | Rectangle | 0,85 | 2,75 | 39,79 | 7,94 |
| `Btn_Imprimer` | Bouton | 39,50 | 3,04 | 0,79 | 0,79 |
| `Liste_Clients` | Zone de liste | 1,40 | 4,52 | 38,74 | 5,66 |
| `Carte_Fiche` | Rectangle | 0,85 | 11,11 | 39,79 | 6,83 |
| `Btn_Ajouter` | Bouton | 36,65 | 11,40 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 37,60 | 11,40 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,55 | 11,40 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,50 | 11,40 | 0,79 | 0,79 |
| `Txt_CIN` | Zone de texte | 4,58 | 12,89 | 3,70 | 0,74 |
| `Txt_Permis` | Zone de texte | 17,81 | 12,89 | 4,76 | 0,74 |
| `Txt_Prenom` | Zone de texte | 31,04 | 12,89 | 9,00 | 0,74 |
| `Txt_Nom` | Zone de texte | 4,58 | 13,94 | 9,00 | 0,74 |
| `Cbo_Sexe` | Zone de liste déroulante | 17,81 | 13,94 | 2,12 | 0,74 |
| `Txt_Adresse` | Zone de texte | 31,04 | 13,94 | 9,00 | 0,74 |
| `Txt_Telephone` | Zone de texte | 4,58 | 15,00 | 9,00 | 0,74 |
| `Txt_Email` | Zone de texte | 17,81 | 15,00 | 9,00 | 0,74 |
| `Btn_Premier` | Bouton | 4,58 | 16,59 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,48 | 16,59 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,29 | 16,59 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,19 | 16,59 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,38 | 16,59 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,99 | 16,54 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,70 | 16,54 | 3,44 | 0,85 |

## Voitures

Maquette : `png/04-voitures.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,48 | 3,12 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,59 | 10,42 | 0,48 |
| `Date_Heure` | Zone de texte | 35,38 | 0,85 | 5,27 | 0,48 |
| `Carte_Liste` | Rectangle | 0,85 | 2,75 | 39,79 | 7,94 |
| `Btn_Imprimer` | Bouton | 39,50 | 3,04 | 0,79 | 0,79 |
| `Liste_Voitures` | Zone de liste | 1,40 | 4,52 | 38,74 | 5,66 |
| `Carte_Fiche` | Rectangle | 0,85 | 11,11 | 39,79 | 6,83 |
| `Btn_Ajouter` | Bouton | 36,65 | 11,40 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 37,60 | 11,40 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,55 | 11,40 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,50 | 11,40 | 0,79 | 0,79 |
| `Txt_Matricule` | Zone de texte | 4,58 | 12,89 | 3,70 | 0,74 |
| `Txt_Annee` | Zone de texte | 17,81 | 12,89 | 2,12 | 0,74 |
| `Txt_Couleur` | Zone de texte | 31,04 | 12,89 | 9,00 | 0,74 |
| `Txt_Puissance` | Zone de texte | 4,58 | 13,94 | 2,65 | 0,74 |
| `Txt_CoutJour` | Zone de texte | 17,81 | 13,94 | 4,23 | 0,74 |
| `Cbo_Modele` | Zone de liste déroulante | 31,04 | 13,94 | 9,00 | 0,74 |
| `Cbo_Carburant` | Zone de liste déroulante | 4,58 | 15,00 | 9,00 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 17,81 | 15,00 | 9,00 | 0,74 |
| `Btn_Premier` | Bouton | 4,58 | 16,59 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,48 | 16,59 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,29 | 16,59 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,19 | 16,59 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,38 | 16,59 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,99 | 16,54 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,70 | 16,54 | 3,44 | 0,85 |

## Marques

Maquette : `png/05-marques.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,48 | 3,31 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,59 | 6,32 | 0,48 |
| `Date_Heure` | Zone de texte | 35,38 | 0,85 | 5,27 | 0,48 |
| `Carte_Liste` | Rectangle | 0,85 | 2,75 | 39,79 | 7,94 |
| `Btn_Imprimer` | Bouton | 39,50 | 3,04 | 0,79 | 0,79 |
| `Liste_Marques` | Zone de liste | 1,40 | 4,52 | 38,74 | 5,66 |
| `Carte_Fiche` | Rectangle | 0,85 | 11,11 | 39,79 | 4,71 |
| `Btn_Ajouter` | Bouton | 36,65 | 11,40 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 37,60 | 11,40 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,55 | 11,40 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,50 | 11,40 | 0,79 | 0,79 |
| `Txt_IdMarque` | Zone de texte | 4,58 | 12,89 | 2,12 | 0,74 |
| `Txt_Marque` | Zone de texte | 17,81 | 12,89 | 9,00 | 0,74 |
| `Btn_Premier` | Bouton | 4,58 | 14,47 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,48 | 14,47 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,29 | 14,47 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,19 | 14,47 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,38 | 14,47 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,99 | 14,42 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,70 | 14,42 | 3,44 | 0,85 |

## Carburants

Maquette : `png/06-carburants.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,48 | 4,21 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,59 | 3,65 | 0,48 |
| `Date_Heure` | Zone de texte | 35,38 | 0,85 | 5,27 | 0,48 |
| `Carte_Liste` | Rectangle | 0,85 | 2,75 | 39,79 | 7,94 |
| `Btn_Imprimer` | Bouton | 39,50 | 3,04 | 0,79 | 0,79 |
| `Liste_Carburants` | Zone de liste | 1,40 | 4,52 | 38,74 | 5,66 |
| `Carte_Fiche` | Rectangle | 0,85 | 11,11 | 39,79 | 4,71 |
| `Btn_Ajouter` | Bouton | 36,65 | 11,40 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 37,60 | 11,40 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,55 | 11,40 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,50 | 11,40 | 0,79 | 0,79 |
| `Txt_IdType` | Zone de texte | 4,58 | 12,89 | 2,12 | 0,74 |
| `Txt_Type` | Zone de texte | 17,81 | 12,89 | 9,00 | 0,74 |
| `Btn_Premier` | Bouton | 4,58 | 14,47 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,48 | 14,47 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,29 | 14,47 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,19 | 14,47 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,38 | 14,47 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,99 | 14,42 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,70 | 14,42 | 3,44 | 0,85 |

## Modèles

Maquette : `png/07-modeles.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Lbl_Titre_Page` | Étiquette | 0,85 | 0,48 | 3,15 | 1,06 |
| `Lbl_SousTitre` | Étiquette | 0,90 | 1,59 | 6,19 | 0,48 |
| `Date_Heure` | Zone de texte | 35,38 | 0,85 | 5,27 | 0,48 |
| `Carte_Liste` | Rectangle | 0,85 | 2,75 | 39,79 | 7,94 |
| `Btn_Imprimer` | Bouton | 39,50 | 3,04 | 0,79 | 0,79 |
| `Liste_Modeles` | Zone de liste | 1,40 | 4,52 | 38,74 | 5,66 |
| `Carte_Fiche` | Rectangle | 0,85 | 11,11 | 39,79 | 4,71 |
| `Btn_Ajouter` | Bouton | 36,65 | 11,40 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 37,60 | 11,40 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,55 | 11,40 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,50 | 11,40 | 0,79 | 0,79 |
| `Txt_IdModele` | Zone de texte | 4,58 | 12,89 | 2,12 | 0,74 |
| `Txt_Modele` | Zone de texte | 17,81 | 12,89 | 9,00 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 31,04 | 12,89 | 9,00 | 0,74 |
| `Btn_Premier` | Bouton | 4,58 | 14,47 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,48 | 14,47 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,29 | 14,47 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,19 | 14,47 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,38 | 14,47 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,99 | 14,42 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,70 | 14,42 | 3,44 | 0,85 |
