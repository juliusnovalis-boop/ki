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
| `Login_Photo` | Image (a-connexion.jpg) | 0,00 | 0,00 | 23,28 | 13,23 |
| `Logo` | Image + étiquette | 1,06 | 0,95 | 3,70 | 0,69 |
| `Login_Slogan` | Étiquette | 1,06 | 9,53 | 10,58 | 2,01 |
| `Login_Copyright` | Étiquette | 1,06 | 11,91 | 3,07 | 0,45 |
| `Login_Carte` | Rectangle | 13,23 | 1,16 | 9,00 | 10,90 |
| `Lbl_Titre` | Étiquette | 14,08 | 2,22 | 4,05 | 1,08 |
| `Txt_Utilisateur` | Zone de texte | 14,08 | 5,40 | 7,30 | 0,90 |
| `Txt_MotDePasse` | Zone de texte | 14,08 | 7,30 | 7,30 | 0,90 |
| `Btn_Connexion` | Bouton | 14,08 | 8,94 | 7,30 | 1,06 |

## Formulaire « Menu » (commun à tous les écrans)

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Entete` | Rectangle | 0,00 | 0,00 | 41,49 | 1,69 |
| `Logo` | Image + étiquette | 0,74 | 0,56 | 3,41 | 0,58 |
| `BoutonNavigation_tableau` | Bouton de navigation | 7,94 | 0,00 | 4,45 | 1,69 |
| `BoutonNavigation_reservations` | Bouton de navigation | 12,38 | 0,00 | 3,70 | 1,69 |
| `BoutonNavigation_clients` | Bouton de navigation | 16,09 | 0,00 | 2,49 | 1,69 |
| `BoutonNavigation_voitures` | Bouton de navigation | 18,57 | 0,00 | 2,73 | 1,69 |
| `BoutonNavigation_marques` | Bouton de navigation | 21,30 | 0,00 | 2,49 | 1,69 |
| `BoutonNavigation_carburants` | Bouton de navigation | 23,79 | 0,00 | 3,23 | 1,69 |
| `BoutonNavigation_modeles` | Bouton de navigation | 27,01 | 0,00 | 2,49 | 1,69 |
| `Date_Heure` | Zone de texte | 33,55 | 0,64 | 4,76 | 0,45 |
| `Btn_Avatar` | Bouton (ellipse) | 38,95 | 0,42 | 0,85 | 0,85 |
| `Btn_Quitter` | Bouton | 40,32 | 0,58 | 0,53 | 0,53 |
| `Sous_Formulaire` | Sous-formulaire | 0,00 | 1,69 | 41,49 | 19,05 |

## Tableau de bord

Maquette : `png/01-tableau-de-bord.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (a-bandeau-tableau.jpg) | 0,00 | 0,00 | 41,49 | 3,97 |
| `Bandeau_Titre` | Étiquette | 1,27 | 0,93 | 6,88 | 1,27 |
| `Bandeau_SousTitre` | Étiquette | 1,32 | 2,35 | 10,85 | 0,45 |
| `Bande_Indicateurs` | Rectangle | 0,85 | 4,60 | 39,79 | 3,07 |
| `Txt_CA` | Zone de texte | 1,72 | 5,74 | 7,62 | 1,30 |
| `Txt_Voitures` | Zone de texte | 14,98 | 5,74 | 1,16 | 1,16 |
| `Txt_Clients` | Zone de texte | 28,23 | 5,74 | 1,77 | 1,16 |
| `Carte_Reservees` | Rectangle | 0,85 | 8,10 | 24,34 | 10,48 |
| `Btn_Imprimer` | Bouton | 24,05 | 8,44 | 0,79 | 0,79 |
| `Liste_Voitures_Reservees` | Zone de liste | 1,40 | 9,87 | 23,28 | 8,26 |
| `Carte_Top5` | Rectangle | 25,61 | 8,10 | 15,03 | 5,61 |
| `Liste_Top5` | Zone de liste | 26,17 | 9,87 | 13,97 | 3,39 |
| `Carte_Carburants` | Rectangle | 25,61 | 14,13 | 15,03 | 4,45 |
| `Liste_Carburants` | Zone de liste | 26,17 | 15,90 | 13,97 | 2,22 |

## Réservations

Maquette : `png/02-reservations.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (a-bandeau-reservations.jpg) | 0,00 | 0,00 | 41,49 | 3,97 |
| `Bandeau_Titre` | Étiquette | 1,27 | 0,93 | 5,64 | 1,27 |
| `Bandeau_SousTitre` | Étiquette | 1,32 | 2,35 | 8,97 | 0,45 |
| `Carte_Client` | Rectangle | 0,85 | 4,60 | 12,91 | 4,66 |
| `Cbo_Client` | Zone de liste déroulante | 4,05 | 6,38 | 9,21 | 0,74 |
| `Txt_Telephone` | Zone de texte (verrouillée) | 4,05 | 7,33 | 9,21 | 0,74 |
| `Txt_Email` | Zone de texte (verrouillée) | 4,05 | 8,28 | 9,21 | 0,74 |
| `Carte_Voiture` | Rectangle | 14,18 | 4,60 | 12,91 | 4,66 |
| `Cbo_Voiture` | Zone de liste déroulante | 17,38 | 6,38 | 9,21 | 0,74 |
| `Txt_Modele` | Zone de texte (verrouillée) | 17,38 | 7,33 | 9,21 | 0,74 |
| `Txt_Marque` | Zone de texte (verrouillée) | 17,38 | 8,28 | 9,21 | 0,74 |
| `Carte_Montant` | Rectangle | 27,52 | 4,60 | 13,12 | 4,66 |
| `Txt_Montant` | Zone de texte | 28,26 | 5,87 | 6,24 | 1,30 |
| `Txt_Duree` | Zone de texte | 28,26 | 7,46 | 1,69 | 0,53 |
| `Carte_Reservation` | Rectangle | 0,85 | 9,68 | 39,79 | 2,96 |
| `Btn_Ajouter` | Bouton | 36,65 | 10,03 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 37,60 | 10,03 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,55 | 10,03 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,50 | 10,03 | 0,79 | 0,79 |
| `Txt_Code` | Zone de texte | 2,73 | 11,46 | 1,59 | 0,74 |
| `Txt_DateDebut` | Zone de texte | 7,59 | 11,46 | 3,18 | 0,74 |
| `Txt_DateFin` | Zone de texte | 13,78 | 11,46 | 3,18 | 0,74 |
| `Btn_OK` | Bouton | 17,28 | 11,40 | 1,59 | 0,85 |
| `Btn_Premier` | Bouton | 19,71 | 11,46 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 20,61 | 11,46 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 24,42 | 11,46 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 25,32 | 11,46 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 21,51 | 11,46 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,99 | 11,40 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,70 | 11,40 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 0,85 | 13,07 | 39,79 | 5,34 |
| `Btn_Imprimer` | Bouton | 39,50 | 13,41 | 0,79 | 0,79 |
| `Liste_Reservations` | Zone de liste | 1,40 | 14,79 | 38,74 | 3,23 |

## Clients

Maquette : `png/03-clients.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (a-bandeau-clients.jpg) | 0,00 | 0,00 | 41,49 | 3,97 |
| `Bandeau_Titre` | Étiquette | 1,27 | 0,93 | 3,04 | 1,27 |
| `Bandeau_SousTitre` | Étiquette | 1,32 | 2,35 | 5,16 | 0,45 |
| `Carte_Liste` | Rectangle | 0,85 | 4,60 | 24,34 | 13,81 |
| `Btn_Imprimer` | Bouton | 24,05 | 4,95 | 0,79 | 0,79 |
| `Liste_Clients` | Zone de liste | 1,40 | 6,43 | 23,28 | 11,54 |
| `Carte_Fiche` | Rectangle | 25,61 | 4,60 | 15,03 | 13,49 |
| `Btn_Ajouter` | Bouton | 36,65 | 4,95 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 37,60 | 4,95 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,55 | 4,95 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,50 | 4,95 | 0,79 | 0,79 |
| `Txt_CIN` | Zone de texte | 29,61 | 6,54 | 3,70 | 0,74 |
| `Txt_Permis` | Zone de texte | 29,61 | 7,59 | 4,76 | 0,74 |
| `Txt_Prenom` | Zone de texte | 29,61 | 8,65 | 10,53 | 0,74 |
| `Txt_Nom` | Zone de texte | 29,61 | 9,71 | 10,53 | 0,74 |
| `Cbo_Sexe` | Zone de liste déroulante | 29,61 | 10,77 | 2,12 | 0,74 |
| `Txt_Adresse` | Zone de texte | 29,61 | 11,83 | 10,53 | 0,74 |
| `Txt_Telephone` | Zone de texte | 29,61 | 12,89 | 10,53 | 0,74 |
| `Txt_Email` | Zone de texte | 29,61 | 13,94 | 10,53 | 0,74 |
| `Btn_Premier` | Bouton | 29,61 | 15,21 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 30,51 | 15,21 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 34,32 | 15,21 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 35,22 | 15,21 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 31,41 | 15,21 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,99 | 16,85 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,70 | 16,85 | 3,44 | 0,85 |

## Voitures

Maquette : `png/04-voitures.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (a-bandeau-voitures.jpg) | 0,00 | 0,00 | 41,49 | 3,97 |
| `Bandeau_Titre` | Étiquette | 1,27 | 0,93 | 3,70 | 1,27 |
| `Bandeau_SousTitre` | Étiquette | 1,32 | 2,35 | 13,02 | 0,45 |
| `Carte_Liste` | Rectangle | 0,85 | 4,60 | 24,34 | 13,81 |
| `Btn_Imprimer` | Bouton | 24,05 | 4,95 | 0,79 | 0,79 |
| `Liste_Voitures` | Zone de liste | 1,40 | 6,43 | 23,28 | 11,54 |
| `Carte_Fiche` | Rectangle | 25,61 | 4,60 | 15,03 | 13,49 |
| `Btn_Ajouter` | Bouton | 36,65 | 4,95 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 37,60 | 4,95 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,55 | 4,95 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,50 | 4,95 | 0,79 | 0,79 |
| `Txt_Matricule` | Zone de texte | 29,61 | 6,54 | 3,70 | 0,74 |
| `Txt_Annee` | Zone de texte | 29,61 | 7,59 | 2,12 | 0,74 |
| `Txt_Couleur` | Zone de texte | 29,61 | 8,65 | 10,53 | 0,74 |
| `Txt_Puissance` | Zone de texte | 29,61 | 9,71 | 2,65 | 0,74 |
| `Txt_CoutJour` | Zone de texte | 29,61 | 10,77 | 4,23 | 0,74 |
| `Cbo_Modele` | Zone de liste déroulante | 29,61 | 11,83 | 10,53 | 0,74 |
| `Cbo_Carburant` | Zone de liste déroulante | 29,61 | 12,89 | 10,53 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 29,61 | 13,94 | 10,53 | 0,74 |
| `Btn_Premier` | Bouton | 29,61 | 15,21 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 30,51 | 15,21 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 34,32 | 15,21 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 35,22 | 15,21 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 31,41 | 15,21 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,99 | 16,85 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,70 | 16,85 | 3,44 | 0,85 |

## Marques

Maquette : `png/05-marques.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (a-bandeau-marques.jpg) | 0,00 | 0,00 | 41,49 | 3,97 |
| `Bandeau_Titre` | Étiquette | 1,27 | 0,93 | 3,84 | 1,27 |
| `Bandeau_SousTitre` | Étiquette | 1,32 | 2,35 | 7,70 | 0,45 |
| `Carte_Liste` | Rectangle | 0,85 | 4,60 | 24,34 | 7,94 |
| `Btn_Imprimer` | Bouton | 24,05 | 4,95 | 0,79 | 0,79 |
| `Liste_Marques` | Zone de liste | 1,40 | 6,43 | 23,28 | 5,66 |
| `Carte_Fiche` | Rectangle | 25,61 | 4,60 | 15,03 | 7,14 |
| `Btn_Ajouter` | Bouton | 36,65 | 4,95 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 37,60 | 4,95 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,55 | 4,95 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,50 | 4,95 | 0,79 | 0,79 |
| `Txt_IdMarque` | Zone de texte | 29,61 | 6,54 | 2,12 | 0,74 |
| `Txt_Marque` | Zone de texte | 29,61 | 7,59 | 10,53 | 0,74 |
| `Btn_Premier` | Bouton | 29,61 | 8,86 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 30,51 | 8,86 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 34,32 | 8,86 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 35,22 | 8,86 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 31,41 | 8,86 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,99 | 10,50 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,70 | 10,50 | 3,44 | 0,85 |

## Carburants

Maquette : `png/06-carburants.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (a-bandeau-carburants.jpg) | 0,00 | 0,00 | 41,49 | 3,97 |
| `Bandeau_Titre` | Étiquette | 1,27 | 0,93 | 4,92 | 1,27 |
| `Bandeau_SousTitre` | Étiquette | 1,32 | 2,35 | 4,63 | 0,45 |
| `Carte_Liste` | Rectangle | 0,85 | 4,60 | 24,34 | 7,94 |
| `Btn_Imprimer` | Bouton | 24,05 | 4,95 | 0,79 | 0,79 |
| `Liste_Carburants` | Zone de liste | 1,40 | 6,43 | 23,28 | 5,66 |
| `Carte_Fiche` | Rectangle | 25,61 | 4,60 | 15,03 | 7,14 |
| `Btn_Ajouter` | Bouton | 36,65 | 4,95 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 37,60 | 4,95 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,55 | 4,95 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,50 | 4,95 | 0,79 | 0,79 |
| `Txt_IdType` | Zone de texte | 29,61 | 6,54 | 2,12 | 0,74 |
| `Txt_Type` | Zone de texte | 29,61 | 7,59 | 10,53 | 0,74 |
| `Btn_Premier` | Bouton | 29,61 | 8,86 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 30,51 | 8,86 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 34,32 | 8,86 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 35,22 | 8,86 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 31,41 | 8,86 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,99 | 10,50 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,70 | 10,50 | 3,44 | 0,85 |

## Modèles

Maquette : `png/07-modeles.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Bandeau` | Image (a-bandeau-modeles.jpg) | 0,00 | 0,00 | 41,49 | 3,97 |
| `Bandeau_Titre` | Étiquette | 1,27 | 0,93 | 3,68 | 1,27 |
| `Bandeau_SousTitre` | Étiquette | 1,32 | 2,35 | 7,67 | 0,45 |
| `Carte_Liste` | Rectangle | 0,85 | 4,60 | 24,34 | 13,81 |
| `Btn_Imprimer` | Bouton | 24,05 | 4,95 | 0,79 | 0,79 |
| `Liste_Modeles` | Zone de liste | 1,40 | 6,43 | 23,28 | 11,54 |
| `Carte_Fiche` | Rectangle | 25,61 | 4,60 | 15,03 | 8,20 |
| `Btn_Ajouter` | Bouton | 36,65 | 4,95 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 37,60 | 4,95 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 38,55 | 4,95 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 39,50 | 4,95 | 0,79 | 0,79 |
| `Txt_IdModele` | Zone de texte | 29,61 | 6,54 | 2,12 | 0,74 |
| `Txt_Modele` | Zone de texte | 29,61 | 7,59 | 10,53 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 29,61 | 8,65 | 10,53 | 0,74 |
| `Btn_Premier` | Bouton | 29,61 | 9,92 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 30,51 | 9,92 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 34,32 | 9,92 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 35,22 | 9,92 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 31,41 | 9,92 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 32,99 | 11,56 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 36,70 | 11,56 | 3,44 | 0,85 |
