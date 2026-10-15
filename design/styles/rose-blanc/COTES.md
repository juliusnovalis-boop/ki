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
| `Login_Fond` | Section Détail | 0,00 | 0,00 | 12,70 | 16,40 |
| `Login_Photo` | Image (b-connexion.jpg) | 0,00 | 0,00 | 12,70 | 5,82 |
| `Logo` | Bouton arrondi + image | 5,40 | 4,87 | 1,91 | 1,91 |
| `Lbl_Titre` | Étiquette | 0,00 | 7,30 | 12,70 | 0,66 |
| `Txt_Utilisateur` | Zone de texte | 1,59 | 9,95 | 9,53 | 0,95 |
| `Txt_MotDePasse` | Zone de texte | 1,59 | 11,85 | 9,53 | 0,95 |
| `Btn_Connexion` | Bouton (forme arrondie) | 1,59 | 13,44 | 9,53 | 1,06 |

## Formulaire « Menu » (commun à tous les écrans)

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Menu_Fond` | Rectangle | 0,00 | 0,00 | 2,75 | 20,74 |
| `Logo` | Image | 0,74 | 0,42 | 1,27 | 1,27 |
| `BoutonNavigation_tableau` | Bouton de navigation | 0,21 | 2,54 | 2,33 | 1,69 |
| `BoutonNavigation_reservations` | Bouton de navigation | 0,21 | 4,45 | 2,33 | 1,69 |
| `BoutonNavigation_clients` | Bouton de navigation | 0,21 | 6,35 | 2,33 | 1,69 |
| `BoutonNavigation_voitures` | Bouton de navigation | 0,21 | 8,26 | 2,33 | 1,69 |
| `BoutonNavigation_marques` | Bouton de navigation | 0,21 | 10,16 | 2,33 | 1,69 |
| `BoutonNavigation_carburants` | Bouton de navigation | 0,21 | 12,07 | 2,33 | 1,69 |
| `BoutonNavigation_modeles` | Bouton de navigation | 0,21 | 13,97 | 2,33 | 1,69 |
| `Btn_Quitter` | Bouton | 1,01 | 19,31 | 0,69 | 0,69 |
| `Entete` | Rectangle | 2,75 | 0,00 | 38,74 | 1,91 |
| `Lbl_Titre_Page` | Étiquette | 3,39 | 0,26 | 4,71 | 0,82 |
| `Date_Heure` | Zone de texte | 3,39 | 1,16 | 6,88 | 0,45 |
| `Btn_Avatar` | Bouton (ellipse) | 36,30 | 0,48 | 0,95 | 0,95 |
| `Utilisateur` | Étiquettes | 37,52 | 0,50 | 3,07 | 0,85 |
| `Panneau_Photo` | Image (b-panneau-tableau.jpg) | 33,02 | 1,91 | 8,47 | 18,84 |
| `Panneau_Chiffre` | Zone de texte | 33,76 | 14,08 | 6,32 | 1,48 |
| `Panneau_Texte` | Étiquette | 33,81 | 15,72 | 5,56 | 0,58 |
| `Sous_Formulaire` | Sous-formulaire | 2,75 | 1,91 | 30,27 | 18,84 |

## Tableau de bord

Maquette : `png/01-tableau-de-bord.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_CA` | Rectangle | 0,64 | 0,64 | 9,37 | 2,65 |
| `Pastille_CA` | Bouton (ellipse) + image | 1,27 | 1,35 | 1,27 | 1,27 |
| `Txt_CA` | Zone de texte | 3,07 | 1,61 | 5,08 | 0,87 |
| `Carte_Voitures` | Rectangle | 10,42 | 0,64 | 9,37 | 2,65 |
| `Pastille_Voitures` | Bouton (ellipse) + image | 11,06 | 1,35 | 1,27 | 1,27 |
| `Txt_Voitures` | Zone de texte | 12,86 | 1,61 | 0,71 | 0,87 |
| `Carte_Clients` | Rectangle | 20,21 | 0,64 | 9,37 | 2,65 |
| `Pastille_Clients` | Bouton (ellipse) + image | 20,85 | 1,35 | 1,27 | 1,27 |
| `Txt_Clients` | Zone de texte | 22,65 | 1,61 | 1,08 | 0,87 |
| `Carte_Reservees` | Rectangle | 0,64 | 3,70 | 29,00 | 7,67 |
| `Btn_Imprimer` | Bouton | 28,50 | 4,00 | 0,79 | 0,79 |
| `Liste_Voitures_Reservees` | Zone de liste | 1,27 | 5,42 | 27,94 | 5,45 |
| `Carte_Top5` | Rectangle | 0,64 | 11,80 | 14,29 | 6,40 |
| `Liste_Top5` | Zone de liste | 1,27 | 13,52 | 13,23 | 4,18 |
| `Carte_Carburants` | Rectangle | 15,35 | 11,80 | 14,29 | 6,40 |
| `Liste_Carburants` | Zone de liste | 15,98 | 13,52 | 13,23 | 4,18 |

## Réservations

Maquette : `png/02-reservations.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Reservation` | Rectangle | 0,64 | 0,64 | 29,00 | 4,13 |
| `Btn_Ajouter` | Bouton | 25,64 | 0,93 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 26,59 | 0,93 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 27,54 | 0,93 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 28,50 | 0,93 | 0,79 | 0,79 |
| `Txt_Code` | Zone de texte | 2,86 | 2,35 | 1,85 | 0,74 |
| `Txt_DateDebut` | Zone de texte | 8,26 | 2,35 | 3,18 | 0,74 |
| `Txt_DateFin` | Zone de texte | 14,50 | 2,35 | 3,18 | 0,74 |
| `Btn_OK` | Bouton | 18,10 | 2,30 | 1,59 | 0,85 |
| `Btn_Premier` | Bouton | 2,86 | 3,52 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 3,76 | 3,52 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 7,57 | 3,52 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 8,47 | 3,52 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 4,66 | 3,52 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 22,07 | 3,47 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 25,77 | 3,47 | 3,44 | 0,85 |
| `Carte_Client` | Rectangle | 0,64 | 5,19 | 14,29 | 4,71 |
| `Cbo_Client` | Zone de liste déroulante | 3,92 | 6,91 | 10,58 | 0,74 |
| `Txt_Telephone` | Zone de texte (verrouillée) | 3,92 | 7,86 | 10,58 | 0,74 |
| `Txt_Email` | Zone de texte (verrouillée) | 3,92 | 8,81 | 10,58 | 0,74 |
| `Carte_Voiture` | Rectangle | 15,35 | 5,19 | 14,29 | 4,71 |
| `Cbo_Voiture` | Zone de liste déroulante | 18,63 | 6,91 | 10,58 | 0,74 |
| `Txt_Modele` | Zone de texte (verrouillée) | 18,63 | 7,86 | 10,58 | 0,74 |
| `Txt_Marque` | Zone de texte (verrouillée) | 18,63 | 8,81 | 10,58 | 0,74 |
| `Carte_Liste` | Rectangle | 0,64 | 10,32 | 29,00 | 7,88 |
| `Btn_Imprimer` | Bouton | 28,50 | 10,61 | 0,79 | 0,79 |
| `Liste_Reservations` | Zone de liste | 1,27 | 11,99 | 27,94 | 5,77 |

## Clients

Maquette : `png/03-clients.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Fiche` | Rectangle | 0,64 | 0,64 | 29,00 | 7,62 |
| `Btn_Ajouter` | Bouton | 25,64 | 0,93 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 26,59 | 0,93 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 27,54 | 0,93 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 28,50 | 0,93 | 0,79 | 0,79 |
| `Txt_CIN` | Zone de texte | 4,45 | 2,41 | 3,70 | 0,74 |
| `Txt_Permis` | Zone de texte | 18,73 | 2,41 | 4,76 | 0,74 |
| `Txt_Prenom` | Zone de texte | 4,45 | 3,47 | 10,05 | 0,74 |
| `Txt_Nom` | Zone de texte | 18,73 | 3,47 | 10,05 | 0,74 |
| `Cbo_Sexe` | Zone de liste déroulante | 4,45 | 4,52 | 2,12 | 0,74 |
| `Txt_Adresse` | Zone de texte | 18,73 | 4,52 | 10,05 | 0,74 |
| `Txt_Telephone` | Zone de texte | 4,45 | 5,58 | 10,05 | 0,74 |
| `Txt_Email` | Zone de texte | 18,73 | 5,58 | 10,05 | 0,74 |
| `Btn_Premier` | Bouton | 4,45 | 6,91 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,34 | 6,91 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,15 | 6,91 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,05 | 6,91 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,24 | 6,91 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 22,07 | 6,85 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 25,77 | 6,85 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 0,64 | 8,68 | 29,00 | 9,53 |
| `Btn_Imprimer` | Bouton | 28,50 | 8,97 | 0,79 | 0,79 |
| `Liste_Clients` | Zone de liste | 1,27 | 10,45 | 27,94 | 7,25 |

## Voitures

Maquette : `png/04-voitures.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Fiche` | Rectangle | 0,64 | 0,64 | 29,00 | 7,62 |
| `Btn_Ajouter` | Bouton | 25,64 | 0,93 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 26,59 | 0,93 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 27,54 | 0,93 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 28,50 | 0,93 | 0,79 | 0,79 |
| `Txt_Matricule` | Zone de texte | 4,45 | 2,41 | 3,70 | 0,74 |
| `Txt_Annee` | Zone de texte | 18,73 | 2,41 | 2,12 | 0,74 |
| `Txt_Couleur` | Zone de texte | 4,45 | 3,47 | 10,05 | 0,74 |
| `Txt_Puissance` | Zone de texte | 18,73 | 3,47 | 2,65 | 0,74 |
| `Txt_CoutJour` | Zone de texte | 4,45 | 4,52 | 4,23 | 0,74 |
| `Cbo_Modele` | Zone de liste déroulante | 18,73 | 4,52 | 10,05 | 0,74 |
| `Cbo_Carburant` | Zone de liste déroulante | 4,45 | 5,58 | 10,05 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 18,73 | 5,58 | 10,05 | 0,74 |
| `Btn_Premier` | Bouton | 4,45 | 6,91 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,34 | 6,91 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,15 | 6,91 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,05 | 6,91 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,24 | 6,91 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 22,07 | 6,85 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 25,77 | 6,85 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 0,64 | 8,68 | 29,00 | 9,53 |
| `Btn_Imprimer` | Bouton | 28,50 | 8,97 | 0,79 | 0,79 |
| `Liste_Voitures` | Zone de liste | 1,27 | 10,45 | 27,94 | 7,25 |

## Marques

Maquette : `png/05-marques.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Fiche` | Rectangle | 0,64 | 0,64 | 29,00 | 4,45 |
| `Btn_Ajouter` | Bouton | 25,64 | 0,93 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 26,59 | 0,93 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 27,54 | 0,93 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 28,50 | 0,93 | 0,79 | 0,79 |
| `Txt_IdMarque` | Zone de texte | 4,45 | 2,41 | 2,12 | 0,74 |
| `Txt_Marque` | Zone de texte | 18,73 | 2,41 | 10,05 | 0,74 |
| `Btn_Premier` | Bouton | 4,45 | 3,73 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,34 | 3,73 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,15 | 3,73 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,05 | 3,73 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,24 | 3,73 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 22,07 | 3,68 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 25,77 | 3,68 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 0,64 | 5,50 | 29,00 | 12,70 |
| `Btn_Imprimer` | Bouton | 28,50 | 5,79 | 0,79 | 0,79 |
| `Liste_Marques` | Zone de liste | 1,27 | 7,28 | 27,94 | 10,42 |

## Carburants

Maquette : `png/06-carburants.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Fiche` | Rectangle | 0,64 | 0,64 | 29,00 | 4,45 |
| `Btn_Ajouter` | Bouton | 25,64 | 0,93 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 26,59 | 0,93 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 27,54 | 0,93 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 28,50 | 0,93 | 0,79 | 0,79 |
| `Txt_IdType` | Zone de texte | 4,45 | 2,41 | 2,12 | 0,74 |
| `Txt_Type` | Zone de texte | 18,73 | 2,41 | 10,05 | 0,74 |
| `Btn_Premier` | Bouton | 4,45 | 3,73 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,34 | 3,73 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,15 | 3,73 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,05 | 3,73 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,24 | 3,73 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 22,07 | 3,68 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 25,77 | 3,68 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 0,64 | 5,50 | 29,00 | 12,70 |
| `Btn_Imprimer` | Bouton | 28,50 | 5,79 | 0,79 | 0,79 |
| `Liste_Carburants` | Zone de liste | 1,27 | 7,28 | 27,94 | 10,42 |

## Modèles

Maquette : `png/07-modeles.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_Fiche` | Rectangle | 0,64 | 0,64 | 29,00 | 5,50 |
| `Btn_Ajouter` | Bouton | 25,64 | 0,93 | 0,79 | 0,79 |
| `Btn_Actualiser` | Bouton | 26,59 | 0,93 | 0,79 | 0,79 |
| `Btn_Rechercher` | Bouton | 27,54 | 0,93 | 0,79 | 0,79 |
| `Btn_Imprimer` | Bouton | 28,50 | 0,93 | 0,79 | 0,79 |
| `Txt_IdModele` | Zone de texte | 4,45 | 2,41 | 2,12 | 0,74 |
| `Txt_Modele` | Zone de texte | 18,73 | 2,41 | 10,05 | 0,74 |
| `Cbo_Marque` | Zone de liste déroulante | 4,45 | 3,47 | 10,05 | 0,74 |
| `Btn_Premier` | Bouton | 4,45 | 4,79 | 0,79 | 0,74 |
| `Btn_Precedent` | Bouton | 5,34 | 4,79 | 0,79 | 0,74 |
| `Btn_Suivant` | Bouton | 9,15 | 4,79 | 0,79 | 0,74 |
| `Btn_Dernier` | Bouton | 10,05 | 4,79 | 0,79 | 0,74 |
| `Txt_Compteur` | Zone de texte | 6,24 | 4,79 | 2,80 | 0,74 |
| `Btn_Enregistrer` | Bouton | 22,07 | 4,74 | 3,44 | 0,85 |
| `Btn_Supprimer` | Bouton | 25,77 | 4,74 | 3,44 | 0,85 |
| `Carte_Liste` | Rectangle | 0,64 | 6,56 | 29,00 | 11,64 |
| `Btn_Imprimer` | Bouton | 28,50 | 6,85 | 0,79 | 0,79 |
| `Liste_Modeles` | Zone de liste | 1,27 | 8,33 | 27,94 | 9,37 |
