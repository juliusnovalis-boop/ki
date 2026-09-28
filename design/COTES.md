# Cotes des contrôles (en cm, pour la feuille de propriétés d'Access)

Généré automatiquement par `design/outils/generer.py` à partir des maquettes.

* Les positions sont en **centimètres** (96 ppp : 1 cm = 37,8 px), comme dans la feuille de propriétés (onglet *Format* : `Gauche`, `Haut`, `Largeur`, `Hauteur`).
* **Menu** : positions mesurées depuis le coin haut-gauche du formulaire `Menu`.
* **Autres écrans** : positions mesurées depuis le coin haut-gauche du **sous-formulaire** (la zone de contenu, 35,56 × 18,94 cm).
* Les contrôles placés *dans* un panneau sont indiqués avec leur position absolue dans le sous-formulaire (plus pratique dans Access, qui n'a pas de conteneur).

## Connexion (formulaire Login)

Maquette : `maquettes/png/00-connexion.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Fond_Login` | Image (Image du formulaire) | 0,00 | 0,00 | 41,49 | 20,74 |
| `Carte_Login` | Rectangle | 15,19 | 3,18 | 11,11 | 14,39 |
| `Icone_Cadenas` | Image | 19,71 | 4,05 | 2,12 | 2,12 |
| `Txt_Utilisateur` | Zone de texte | 16,27 | 9,66 | 9,00 | 1,11 |
| `Icone_User` | Image | 16,54 | 9,90 | 0,64 | 0,64 |
| `Txt_MotDePasse` | Zone de texte (Masque : Mot de passe) | 16,27 | 11,83 | 9,00 | 1,11 |
| `Icone_Lock` | Image | 16,54 | 12,07 | 0,64 | 0,64 |
| `Btn_Connexion` | Bouton | 16,27 | 13,73 | 9,00 | 1,22 |

## Formulaire « Menu » (commun à tous les écrans)

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Fond_Menu` | Rectangle | 0,00 | 0,00 | 5,93 | 20,74 |
| `Logo` | Image | 0,48 | 0,48 | 4,97 | 1,38 |
| `Barre_Active` | Rectangle | 0,32 | 3,39 | 0,08 | 1,16 |
| `BoutonNavigation_tableau` | Bouton de navigation | 0,32 | 3,39 | 5,29 | 1,16 |
| `BoutonNavigation_reservations` | Bouton de navigation | 0,32 | 4,76 | 5,29 | 1,16 |
| `BoutonNavigation_clients` | Bouton de navigation | 0,32 | 6,14 | 5,29 | 1,16 |
| `BoutonNavigation_voitures` | Bouton de navigation | 0,32 | 7,51 | 5,29 | 1,16 |
| `BoutonNavigation_marques` | Bouton de navigation | 0,32 | 8,89 | 5,29 | 1,16 |
| `BoutonNavigation_carburants` | Bouton de navigation | 0,32 | 10,27 | 5,29 | 1,16 |
| `BoutonNavigation_modeles` | Bouton de navigation | 0,32 | 11,64 | 5,29 | 1,16 |
| `Etat_Systeme` | Rectangle + étiquettes | 0,32 | 18,26 | 5,29 | 2,06 |
| `Entete` | Rectangle | 5,93 | 0,00 | 35,56 | 1,80 |
| `Titre_Page` | Étiquette | 6,77 | 0,29 | 4,42 | 0,77 |
| `Date_Heure` | Zone de texte | 28,73 | 0,45 | 5,19 | 0,90 |
| `Utilisateur` | Image + étiquettes | 34,55 | 0,37 | 3,36 | 1,06 |
| `Btn_Quitter` | Bouton | 39,69 | 0,37 | 1,06 | 1,06 |
| `Ligne_Neon` | Image | 5,93 | 1,77 | 35,56 | 0,05 |

## Tableau de bord (sous-formulaire)

Maquette : `maquettes/png/01-tableau-de-bord.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Carte_CA` | Image (cadre) + étiquettes | 0,85 | 0,74 | 7,99 | 3,28 |
| `Txt_CA` | Zone de texte | 1,48 | 1,91 | 5,74 | 1,22 |
| `Carte_Voitures` | Image (cadre) + étiquettes | 9,47 | 0,74 | 7,99 | 3,28 |
| `Txt_Voitures` | Zone de texte | 10,11 | 1,91 | 1,03 | 1,22 |
| `Carte_Clients` | Image (cadre) + étiquettes | 18,10 | 0,74 | 7,99 | 3,28 |
| `Txt_Clients` | Zone de texte | 18,73 | 1,91 | 1,56 | 1,22 |
| `Carte_Reservations` | Image (cadre) + étiquettes | 26,72 | 0,74 | 7,99 | 3,28 |
| `Txt_Reservations` | Zone de texte | 27,36 | 1,91 | 1,01 | 1,22 |
| `Panneau_Reservees` | Rectangle | 0,85 | 4,76 | 21,70 | 9,21 |
| `Btn_Imprimer` | Bouton (ovale) | 21,25 | 5,03 | 0,90 | 0,90 |
| `Liste_Voitures_Reservees` | Zone de liste | 1,40 | 6,59 | 20,64 | 6,88 |
| `Panneau_Top5` | Rectangle | 23,07 | 4,76 | 11,64 | 9,21 |
| `Liste_Top5` | Zone de liste | 23,63 | 6,59 | 10,58 | 4,66 |
| `Stat_Duree` | Rectangle + zone de texte | 23,63 | 11,72 | 5,08 | 1,85 |
| `Stat_Occupation` | Rectangle + zone de texte | 29,13 | 11,72 | 5,08 | 1,85 |
| `Panneau_Flotte` | Rectangle | 0,85 | 14,50 | 33,87 | 3,70 |

## Réservations (sous-formulaire)

Maquette : `maquettes/png/02-reservations.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Panneau_Client` | Rectangle | 0,64 | 0,53 | 16,93 | 5,50 |
| `Cbo_Client` | Zone de liste déroulante | 4,47 | 2,35 | 11,64 | 0,90 |
| `Txt_Telephone` | Zone de texte (verrouillée) | 4,47 | 3,52 | 11,64 | 0,90 |
| `Txt_Email` | Zone de texte (verrouillée) | 4,47 | 4,68 | 11,64 | 0,90 |
| `Panneau_Voiture` | Rectangle | 17,99 | 0,53 | 16,93 | 5,50 |
| `Cbo_Voiture` | Zone de liste déroulante | 21,83 | 2,35 | 11,64 | 0,90 |
| `Txt_Modele` | Zone de texte (verrouillée) | 21,83 | 3,52 | 11,64 | 0,90 |
| `Txt_Marque` | Zone de texte (verrouillée) | 21,83 | 4,68 | 11,64 | 0,90 |
| `Panneau_Reservation` | Rectangle | 0,64 | 6,46 | 34,29 | 4,87 |
| `Btn_Ajouter` | Bouton (ovale) | 30,14 | 6,72 | 0,90 | 0,90 |
| `Btn_Actualiser` | Bouton (ovale) | 31,30 | 6,72 | 0,90 | 0,90 |
| `Btn_Rechercher` | Bouton (ovale) | 32,46 | 6,72 | 0,90 | 0,90 |
| `Btn_Imprimer` | Bouton (ovale) | 33,63 | 6,72 | 0,90 | 0,90 |
| `Txt_Code` | Zone de texte | 3,15 | 8,39 | 2,38 | 0,90 |
| `Txt_DateDebut` | Zone de texte | 9,23 | 8,39 | 3,70 | 0,90 |
| `Txt_DateFin` | Zone de texte | 16,06 | 8,39 | 3,70 | 0,90 |
| `Btn_OK` | Bouton | 20,13 | 8,31 | 2,43 | 1,06 |
| `Btn_Premier` | Bouton | 1,19 | 9,76 | 1,01 | 0,90 |
| `Btn_Precedent` | Bouton | 2,41 | 9,76 | 1,01 | 0,90 |
| `Compteur` | Zone de texte | 3,62 | 9,76 | 2,43 | 0,90 |
| `Btn_Suivant` | Bouton | 6,06 | 9,76 | 1,01 | 0,90 |
| `Btn_Dernier` | Bouton | 7,28 | 9,76 | 1,01 | 0,90 |
| `Btn_Enregistrer` | Bouton | 9,76 | 9,68 | 3,97 | 1,06 |
| `Btn_Supprimer` | Bouton | 14,10 | 9,68 | 3,97 | 1,06 |
| `Txt_Duree` | Zone de texte (calculée) | 26,48 | 8,23 | 7,67 | 0,90 |
| `Txt_Montant` | Zone de texte (calculée) | 26,48 | 9,60 | 7,67 | 1,11 |
| `Panneau_Liste` | Rectangle | 0,64 | 11,75 | 34,29 | 6,67 |
| `Btn_Imprimer` | Bouton (ovale) | 33,63 | 12,01 | 0,90 | 0,90 |
| `Liste_Reservations` | Zone de liste | 1,19 | 13,47 | 33,23 | 4,45 |

## Clients (sous-formulaire)

Maquette : `maquettes/png/03-clients.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Panneau_Fiche` | Rectangle | 0,64 | 0,64 | 14,29 | 17,78 |
| `Btn_Ajouter` | Bouton (ovale) | 10,13 | 0,90 | 0,90 | 0,90 |
| `Btn_Actualiser` | Bouton (ovale) | 11,30 | 0,90 | 0,90 | 0,90 |
| `Btn_Rechercher` | Bouton (ovale) | 12,46 | 0,90 | 0,90 | 0,90 |
| `Btn_Imprimer` | Bouton (ovale) | 13,63 | 0,90 | 0,90 | 0,90 |
| `Txt_CIN` | Zone de texte | 5,53 | 2,78 | 5,29 | 0,90 |
| `Txt_Permis` | Zone de texte | 5,53 | 4,15 | 5,82 | 0,90 |
| `Txt_Prenom` | Zone de texte | 5,53 | 5,53 | 8,89 | 0,90 |
| `Txt_Nom` | Zone de texte | 5,53 | 6,91 | 8,89 | 0,90 |
| `Cbo_Sexe` | Zone de liste déroulante | 5,53 | 8,28 | 2,65 | 0,90 |
| `Txt_Adresse` | Zone de texte | 5,53 | 9,66 | 8,89 | 0,90 |
| `Txt_Telephone` | Zone de texte | 5,53 | 11,03 | 8,89 | 0,90 |
| `Txt_Email` | Zone de texte | 5,53 | 12,41 | 8,89 | 0,90 |
| `Btn_Premier` | Bouton | 4,15 | 14,00 | 1,01 | 0,90 |
| `Btn_Precedent` | Bouton | 5,37 | 14,00 | 1,01 | 0,90 |
| `Compteur` | Zone de texte | 6,59 | 14,00 | 2,43 | 0,90 |
| `Btn_Suivant` | Bouton | 9,02 | 14,00 | 1,01 | 0,90 |
| `Btn_Dernier` | Bouton | 10,24 | 14,00 | 1,01 | 0,90 |
| `Btn_Enregistrer` | Bouton | 3,62 | 15,95 | 3,97 | 1,06 |
| `Btn_Supprimer` | Bouton | 8,02 | 15,95 | 3,97 | 1,06 |
| `Panneau_Liste` | Rectangle | 15,35 | 0,64 | 19,58 | 17,78 |
| `Btn_Imprimer` | Bouton (ovale) | 33,63 | 0,90 | 0,90 | 0,90 |
| `Liste_Clients` | Zone de liste | 15,90 | 2,46 | 18,47 | 15,45 |

## Voitures (sous-formulaire)

Maquette : `maquettes/png/04-voitures.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Panneau_Fiche` | Rectangle | 0,64 | 0,64 | 14,29 | 17,78 |
| `Btn_Ajouter` | Bouton (ovale) | 10,13 | 0,90 | 0,90 | 0,90 |
| `Btn_Actualiser` | Bouton (ovale) | 11,30 | 0,90 | 0,90 | 0,90 |
| `Btn_Rechercher` | Bouton (ovale) | 12,46 | 0,90 | 0,90 | 0,90 |
| `Btn_Imprimer` | Bouton (ovale) | 13,63 | 0,90 | 0,90 | 0,90 |
| `Txt_Matricule` | Zone de texte | 5,53 | 2,78 | 5,29 | 0,90 |
| `Txt_Annee` | Zone de texte | 5,53 | 4,15 | 3,18 | 0,90 |
| `Txt_Couleur` | Zone de texte | 5,53 | 5,53 | 8,89 | 0,90 |
| `Txt_Puissance` | Zone de texte | 5,53 | 6,91 | 3,18 | 0,90 |
| `Txt_CoutJour` | Zone de texte | 5,53 | 8,28 | 5,29 | 0,90 |
| `Cbo_Modele` | Zone de liste déroulante | 5,53 | 9,66 | 8,89 | 0,90 |
| `Cbo_Carburant` | Zone de liste déroulante | 5,53 | 11,03 | 8,89 | 0,90 |
| `Cbo_Marque` | Zone de liste déroulante | 5,53 | 12,41 | 8,89 | 0,90 |
| `Btn_Premier` | Bouton | 4,15 | 14,00 | 1,01 | 0,90 |
| `Btn_Precedent` | Bouton | 5,37 | 14,00 | 1,01 | 0,90 |
| `Compteur` | Zone de texte | 6,59 | 14,00 | 2,43 | 0,90 |
| `Btn_Suivant` | Bouton | 9,02 | 14,00 | 1,01 | 0,90 |
| `Btn_Dernier` | Bouton | 10,24 | 14,00 | 1,01 | 0,90 |
| `Btn_Enregistrer` | Bouton | 3,62 | 15,95 | 3,97 | 1,06 |
| `Btn_Supprimer` | Bouton | 8,02 | 15,95 | 3,97 | 1,06 |
| `Panneau_Liste` | Rectangle | 15,35 | 0,64 | 19,58 | 17,78 |
| `Btn_Imprimer` | Bouton (ovale) | 33,63 | 0,90 | 0,90 | 0,90 |
| `Liste_Voitures` | Zone de liste | 15,90 | 2,46 | 18,47 | 15,45 |

## Marques (sous-formulaire)

Maquette : `maquettes/png/05-marques.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Panneau_Fiche` | Rectangle | 0,64 | 5,11 | 14,82 | 8,73 |
| `Btn_Ajouter` | Bouton (ovale) | 10,66 | 5,37 | 0,90 | 0,90 |
| `Btn_Actualiser` | Bouton (ovale) | 11,83 | 5,37 | 0,90 | 0,90 |
| `Btn_Rechercher` | Bouton (ovale) | 12,99 | 5,37 | 0,90 | 0,90 |
| `Btn_Imprimer` | Bouton (ovale) | 14,16 | 5,37 | 0,90 | 0,90 |
| `Txt_IdMarque` | Zone de texte | 5,53 | 7,25 | 3,18 | 0,90 |
| `Txt_Marque` | Zone de texte | 5,53 | 8,63 | 9,42 | 0,90 |
| `Btn_Premier` | Bouton | 4,42 | 10,21 | 1,01 | 0,90 |
| `Btn_Precedent` | Bouton | 5,64 | 10,21 | 1,01 | 0,90 |
| `Compteur` | Zone de texte | 6,85 | 10,21 | 2,43 | 0,90 |
| `Btn_Suivant` | Bouton | 9,29 | 10,21 | 1,01 | 0,90 |
| `Btn_Dernier` | Bouton | 10,50 | 10,21 | 1,01 | 0,90 |
| `Btn_Enregistrer` | Bouton | 3,89 | 12,17 | 3,97 | 1,06 |
| `Btn_Supprimer` | Bouton | 8,28 | 12,17 | 3,97 | 1,06 |
| `Panneau_Liste` | Rectangle | 15,88 | 5,11 | 19,05 | 8,73 |
| `Btn_Imprimer` | Bouton (ovale) | 33,63 | 5,37 | 0,90 | 0,90 |
| `Liste_Marques` | Zone de liste | 16,43 | 6,93 | 17,94 | 6,40 |

## Carburants (sous-formulaire)

Maquette : `maquettes/png/06-carburants.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Panneau_Fiche` | Rectangle | 0,64 | 5,11 | 14,82 | 8,73 |
| `Btn_Ajouter` | Bouton (ovale) | 10,66 | 5,37 | 0,90 | 0,90 |
| `Btn_Actualiser` | Bouton (ovale) | 11,83 | 5,37 | 0,90 | 0,90 |
| `Btn_Rechercher` | Bouton (ovale) | 12,99 | 5,37 | 0,90 | 0,90 |
| `Btn_Imprimer` | Bouton (ovale) | 14,16 | 5,37 | 0,90 | 0,90 |
| `Txt_IdType` | Zone de texte | 5,53 | 7,25 | 3,18 | 0,90 |
| `Txt_Type` | Zone de texte | 5,53 | 8,63 | 9,42 | 0,90 |
| `Btn_Premier` | Bouton | 4,42 | 10,21 | 1,01 | 0,90 |
| `Btn_Precedent` | Bouton | 5,64 | 10,21 | 1,01 | 0,90 |
| `Compteur` | Zone de texte | 6,85 | 10,21 | 2,43 | 0,90 |
| `Btn_Suivant` | Bouton | 9,29 | 10,21 | 1,01 | 0,90 |
| `Btn_Dernier` | Bouton | 10,50 | 10,21 | 1,01 | 0,90 |
| `Btn_Enregistrer` | Bouton | 3,89 | 12,17 | 3,97 | 1,06 |
| `Btn_Supprimer` | Bouton | 8,28 | 12,17 | 3,97 | 1,06 |
| `Panneau_Liste` | Rectangle | 15,88 | 5,11 | 19,05 | 8,73 |
| `Btn_Imprimer` | Bouton (ovale) | 33,63 | 5,37 | 0,90 | 0,90 |
| `Liste_Carburants` | Zone de liste | 16,43 | 6,93 | 17,94 | 6,40 |

## Modèles (sous-formulaire)

Maquette : `maquettes/png/07-modeles.png`

| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |
|---|---|---:|---:|---:|---:|
| `Panneau_Fiche` | Rectangle | 0,64 | 4,42 | 14,82 | 10,11 |
| `Btn_Ajouter` | Bouton (ovale) | 10,66 | 4,68 | 0,90 | 0,90 |
| `Btn_Actualiser` | Bouton (ovale) | 11,83 | 4,68 | 0,90 | 0,90 |
| `Btn_Rechercher` | Bouton (ovale) | 12,99 | 4,68 | 0,90 | 0,90 |
| `Btn_Imprimer` | Bouton (ovale) | 14,16 | 4,68 | 0,90 | 0,90 |
| `Txt_IdModele` | Zone de texte | 5,53 | 6,56 | 3,18 | 0,90 |
| `Txt_Modele` | Zone de texte | 5,53 | 7,94 | 9,42 | 0,90 |
| `Cbo_Marque` | Zone de liste déroulante | 5,53 | 9,31 | 9,42 | 0,90 |
| `Btn_Premier` | Bouton | 4,42 | 10,90 | 1,01 | 0,90 |
| `Btn_Precedent` | Bouton | 5,64 | 10,90 | 1,01 | 0,90 |
| `Compteur` | Zone de texte | 6,85 | 10,90 | 2,43 | 0,90 |
| `Btn_Suivant` | Bouton | 9,29 | 10,90 | 1,01 | 0,90 |
| `Btn_Dernier` | Bouton | 10,50 | 10,90 | 1,01 | 0,90 |
| `Btn_Enregistrer` | Bouton | 3,89 | 12,86 | 3,97 | 1,06 |
| `Btn_Supprimer` | Bouton | 8,28 | 12,86 | 3,97 | 1,06 |
| `Panneau_Liste` | Rectangle | 15,88 | 4,42 | 19,05 | 10,11 |
| `Btn_Imprimer` | Bouton (ovale) | 33,63 | 4,68 | 0,90 | 0,90 |
| `Liste_Modeles` | Zone de liste | 16,43 | 6,24 | 17,94 | 7,78 |
