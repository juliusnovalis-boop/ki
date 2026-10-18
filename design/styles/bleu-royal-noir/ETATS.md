# États (impressions) · AURION

Chaque bouton **Imprimer** des formulaires ouvre un état. Les aperçus sont dans `etats/png/` (A4, prêts à reproduire).

## Réglages communs

* **Mise en page** : A4, marges de **1 cm** partout (*Mise en page › Marges › Personnalisées*). Portrait sauf mention « paysage ».
* **Bandeau** (en-tête d'état) : Rectangle noir `#000000` sur toute la largeur, 2,28 cm de haut ; logo `assets/marque/aurion-menu.png` (4,79 × 1,16 cm) ; titre en **Bahnschrift SemiBold 16 pt** blanc, majuscules ; date d'édition dorée `#E3C77A` ; trait doré `#C9A24B` dessous.
* **En-tête de page** : Rectangle bleu royal `#002366` de 0,69 cm, étiquettes blanches Bahnschrift SemiBold 8,5 pt en majuscules. Propriété de la section *Répéter la section* : **Oui**.
* **Détail** : zones de texte Segoe UI 9 pt, `Couleur fond` blanc et **`Autre couleur fond` `#F4F6FA`** (lignes alternées automatiques), trait bas `#E1E6EF`. Toutes les zones de texte : `Style bordure` **Transparent**.
* **En-tête de groupe** (quand l'état est regroupé) : Rectangle `#EDF1F9` avec une barre dorée de 0,11 cm à gauche, texte Bahnschrift SemiBold 11 pt `#002366`.
* **Pied de page** : trait doré, « AURION · Location de prestige · Libreville » à gauche, `="Page " & [Page] & " sur " & [Pages]` à droite.
* **Pied d'état** : rectangle bleu royal `#002366` avec le total en **Bahnschrift SemiBold 18 pt doré `#E3C77A`**.

Code des boutons Imprimer (procédure `Sur clic`) :

```vba
DoCmd.OpenReport "Etat_Clients", acViewPreview      ' remplacer par le nom de l'état
```

## Liste des états

| Aperçu | Nom de l'état | Ouvert par | Orientation |
|---|---|---|---|
| `etats/png/01-bon-de-reservation.png` | **Etat_BonReservation** | Réservations › carte 03 Réservation › Imprimer | Portrait |
| `etats/png/02-liste-des-reservations.png` | **Etat_Reservations** | Réservations › carte 04 Liste des réservations › Imprimer | Paysage |
| `etats/png/03-voitures-reservees.png` | **Etat_VoituresReservees** | Tableau de bord › carte 02 Voitures actuellement réservées › Imprimer | Portrait |
| `etats/png/04-liste-des-clients.png` | **Etat_Clients** | Clients › carte 01 Liste des clients › Imprimer | Paysage |
| `etats/png/05-parc-automobile.png` | **Etat_Voitures** | Voitures › carte 01 Liste des voitures › Imprimer | Portrait |
| `etats/png/06-marques.png` | **Etat_Marques** | Marques › carte 01 Liste des marques › Imprimer | Portrait |
| `etats/png/07-carburants.png` | **Etat_Carburants** | Carburants › carte 01 Types de carburant › Imprimer | Portrait |
| `etats/png/08-modeles.png` | **Etat_Modeles** | Modèles › carte 01 Liste des modèles › Imprimer | Portrait |

## Bon de réservation · `Etat_BonReservation`

* Aperçu : `etats/png/01-bon-de-reservation.png` · portrait · 1 page(s) avec les données actuelles
* Bouton : Réservations › carte 03 Réservation › Imprimer
* Source : Requête : Reservation + Client + Voiture + Modele + Marque + Carburant
* Ouverture filtrée : `DoCmd.OpenReport "Etat_BonReservation", acViewPreview, , "IdReservation=" & Me.Txt_Code`

| Section | Hauteur | Remarque |
|---|---:|---|
| En-tête d'état | 10,32 cm | bandeau, client, véhicule et titres des colonnes |
| Détail | 0,90 cm | `Couleur fond` blanc, `Autre couleur fond` #F4F6FA (lignes alternées), trait bas #E1E6EF |
| Pied d'état | 8,73 cm | total, période, conditions et signatures |
| Pied de page | 0,79 cm | en bas de chaque page |

| Contrôle | Type | Section | Gauche | Haut | Largeur | Hauteur | Contenu / format |
|---|---|---|---:|---:|---:|---:|---|
| `Rect_Bandeau` | Rectangle | En-tête d'état | 0,00 | 0,00 | 19,00 | 2,28 | fond noir #000000 |
| `Logo` | Image | En-tête d'état | 0,53 | 0,56 | 4,79 | 1,16 | assets/marque/aurion-menu.png |
| `Lbl_Titre` | Étiquette | En-tête d'état | 6,56 | 0,48 | 11,91 | 0,74 | Bahnschrift SemiBold 16 pt, blanc |
| `Txt_Edition` | Zone de texte | En-tête d'état | 6,56 | 1,32 | 11,91 | 0,53 | ="N° R-" & Format([IdReservation];"0000") & " · Édité le " & Format(Maintenant();"dddd d mmmm yyyy à hh:nn") |
| `Trait_Or` | Trait | En-tête d'état | 0,00 | 2,28 | 19,00 | 0,05 | doré #C9A24B, 1,5 pt |
| `Lbl_Intro` | Étiquette | En-tête d'état | 0,00 | 2,80 | 19,00 | 0,53 | Segoe UI 10 pt |
| `Rect_Client` | Rectangle | En-tête d'état | 0,00 | 3,70 | 9,26 | 5,19 | bordure #D9DFEA |
| `Lbl_Client` | Étiquette | En-tête d'état | 0,42 | 4,02 | 5,29 | 0,48 | Bahnschrift SemiBold 10 pt, #002366 |
| `Lbl_Client_Nom` | Étiquette | En-tête d'état | 0,42 | 4,82 | 2,91 | 0,53 | Segoe UI 9 pt, gris |
| `Txt_Client_Nom` | Zone de texte | En-tête d'état | 3,44 | 4,82 | 5,40 | 0,53 | Segoe UI 10 pt |
| `Rect_Vehicule` | Rectangle | En-tête d'état | 9,74 | 3,70 | 9,26 | 5,19 | bordure #D9DFEA |
| `Lbl_Vehicule` | Étiquette | En-tête d'état | 10,16 | 4,02 | 5,29 | 0,48 | Bahnschrift SemiBold 10 pt, #002366 |
| `Lbl_Vehicule_Modele` | Étiquette | En-tête d'état | 10,16 | 4,82 | 2,91 | 0,53 | Segoe UI 9 pt, gris |
| `Txt_Vehicule_Modele` | Zone de texte | En-tête d'état | 13,18 | 4,82 | 5,40 | 0,53 | Segoe UI 10 pt |
| `Rect_EnteteColonnes` | Rectangle | En-tête d'état | 0,00 | 0,00 | 19,00 | 0,69 | #002366 |
| `Lbl_Designation` | Étiquette | En-tête d'état | 0,00 | 0,00 | 7,12 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Du` | Étiquette | En-tête d'état | 7,12 | 0,00 | 2,14 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Au` | Étiquette | En-tête d'état | 9,26 | 0,00 | 2,14 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Jours` | Étiquette | En-tête d'état | 11,40 | 0,00 | 1,43 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Prixjour` | Étiquette | En-tête d'état | 12,83 | 0,00 | 2,86 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Montant` | Étiquette | En-tête d'état | 15,69 | 0,00 | 3,31 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Txt_Designation` | Zone de texte | Détail | 0,00 | 0,00 | 7,12 | 0,90 | Segoe UI 9 pt |
| `Txt_DateDebut` | Zone de texte | Détail | 7,12 | 0,00 | 2,14 | 0,90 | Segoe UI 9 pt |
| `Txt_DateFin` | Zone de texte | Détail | 9,26 | 0,00 | 2,14 | 0,90 | Segoe UI 9 pt |
| `Txt_Jours` | Zone de texte | Détail | 11,40 | 0,00 | 1,43 | 0,90 | Segoe UI 9 pt |
| `Txt_PrixJour` | Zone de texte | Détail | 12,83 | 0,00 | 2,86 | 0,90 | Segoe UI 9 pt |
| `Txt_Montant` | Zone de texte | Détail | 15,69 | 0,00 | 3,31 | 0,90 | Segoe UI 9 pt |
| `Lbl_Periode` | Étiquette | Pied d'état | 0,00 | 0,00 | 9,00 | 0,42 |  |
| `Txt_Periode` | Zone de texte | Pied d'état | 0,00 | 0,48 | 9,53 | 0,69 | Bahnschrift SemiBold 14 pt |
| `Rect_Total` | Rectangle | Pied d'état | 10,27 | -0,11 | 8,73 | 1,69 | #002366 |
| `Lbl_Total` | Étiquette | Pied d'état | 10,74 | 0,16 | 7,94 | 0,37 |  |
| `Txt_Total` | Zone de texte | Pied d'état | 10,74 | 0,58 | 7,94 | 0,90 | =[Montant] · Bahnschrift SemiBold 21 pt, #E3C77A |
| `Lbl_Conditions` | Étiquette | Pied d'état | 0,00 | 2,54 | 7,94 | 0,42 |  |
| `Txt_Conditions` | Zone de texte | Pied d'état | 0,00 | 3,07 | 19,00 | 1,43 | Segoe UI 9 pt, plusieurs lignes |
| `Rect_SignatureClient` | Rectangle | Pied d'état | 0,00 | 5,19 | 9,26 | 2,91 | bordure #D9DFEA |
| `Lbl_SignatureClient` | Étiquette | Pied d'état | 0,42 | 5,50 | 8,41 | 0,42 |  |
| `Rect_SignatureSociete` | Rectangle | Pied d'état | 9,74 | 5,19 | 9,26 | 2,91 | bordure #D9DFEA |
| `Lbl_SignatureSociete` | Étiquette | Pied d'état | 10,16 | 5,50 | 8,41 | 0,42 |  |
| `Trait_Pied` | Trait | Pied de page | 0,00 | 0,11 | 19,00 | 0,03 | doré |
| `Lbl_Societe` | Étiquette | Pied de page | 0,00 | 0,26 | 11,11 | 0,48 | Bahnschrift 9 pt |
| `Txt_Page` | Zone de texte | Pied de page | 13,71 | 0,26 | 5,29 | 0,48 | ="Page " & [Page] & " sur " & [Pages] |

## Liste des réservations · `Etat_Reservations`

* Aperçu : `etats/png/02-liste-des-reservations.png` · paysage · 2 page(s) avec les données actuelles
* Bouton : Réservations › carte 04 Liste des réservations › Imprimer
* Source : Requête : Reservation + Client + Voiture + Modele + Marque ; Jours = [DateFin]-[DateDebut] ; Montant = [Jours]*[CoutParJour]
* Tri et regroupement (*Regrouper, trier et total*) : IdReservation croissant

| Section | Hauteur | Remarque |
|---|---:|---|
| En-tête d'état | 4,82 cm | bandeau, logo, titre, indicateurs (page 1 seulement) |
| En-tête de page | 0,74 cm | répété en haut de chaque page |
| Détail | 0,53 cm | `Couleur fond` blanc, `Autre couleur fond` #F4F6FA (lignes alternées), trait bas #E1E6EF |
| Pied de page | 0,79 cm | en bas de chaque page |

| Contrôle | Type | Section | Gauche | Haut | Largeur | Hauteur | Contenu / format |
|---|---|---|---:|---:|---:|---:|---|
| `Rect_Bandeau` | Rectangle | En-tête d'état | 0,00 | 0,00 | 27,70 | 2,28 | fond noir #000000 |
| `Logo` | Image | En-tête d'état | 0,53 | 0,56 | 4,79 | 1,16 | assets/marque/aurion-menu.png |
| `Lbl_Titre` | Étiquette | En-tête d'état | 15,27 | 0,48 | 11,91 | 0,74 | Bahnschrift SemiBold 16 pt, blanc |
| `Txt_Edition` | Zone de texte | En-tête d'état | 15,27 | 1,32 | 11,91 | 0,53 | ="Édité le " & Format(Maintenant();"dddd d mmmm yyyy à hh:nn") |
| `Trait_Or` | Trait | En-tête d'état | 0,00 | 2,28 | 27,70 | 0,05 | doré #C9A24B, 1,5 pt |
| `Rect_Indicateur1` | Rectangle | En-tête d'état | 0,00 | 2,80 | 6,69 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur1` | Étiquette | En-tête d'état | 0,37 | 3,04 | 5,95 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur1` | Zone de texte | En-tête d'état | 0,37 | 3,47 | 5,95 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur2` | Rectangle | En-tête d'état | 7,01 | 2,80 | 6,69 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur2` | Étiquette | En-tête d'état | 7,38 | 3,04 | 5,95 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur2` | Zone de texte | En-tête d'état | 7,38 | 3,47 | 5,95 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur3` | Rectangle | En-tête d'état | 14,02 | 2,80 | 6,69 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur3` | Étiquette | En-tête d'état | 14,39 | 3,04 | 5,95 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur3` | Zone de texte | En-tête d'état | 14,39 | 3,47 | 5,95 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur4` | Rectangle | En-tête d'état | 21,01 | 2,80 | 6,69 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur4` | Étiquette | En-tête d'état | 21,38 | 3,04 | 5,95 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur4` | Zone de texte | En-tête d'état | 21,38 | 3,47 | 5,95 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_EnteteColonnes` | Rectangle | En-tête de page | 0,00 | 0,00 | 27,70 | 0,69 | #002366 |
| `Lbl_No` | Étiquette | En-tête de page | 0,00 | 0,00 | 1,35 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Client` | Étiquette | En-tête de page | 1,35 | 0,00 | 4,58 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Matricule` | Étiquette | En-tête de page | 5,93 | 0,00 | 2,70 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Modele` | Étiquette | En-tête de page | 8,63 | 0,00 | 5,64 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Marque` | Étiquette | En-tête de page | 14,26 | 0,00 | 2,96 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Du` | Étiquette | En-tête de page | 17,22 | 0,00 | 2,41 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Au` | Étiquette | En-tête de page | 19,63 | 0,00 | 2,41 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Jours` | Étiquette | En-tête de page | 22,04 | 0,00 | 1,61 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Montant` | Étiquette | En-tête de page | 23,65 | 0,00 | 4,05 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Txt_IdReservation` | Zone de texte | Détail | 0,00 | 0,00 | 1,35 | 0,53 | Segoe UI 9 pt |
| `Txt_Client` | Zone de texte | Détail | 1,35 | 0,00 | 4,58 | 0,53 | Segoe UI 9 pt |
| `Txt_Matricule` | Zone de texte | Détail | 5,93 | 0,00 | 2,70 | 0,53 | Segoe UI 9 pt |
| `Txt_Modele` | Zone de texte | Détail | 8,63 | 0,00 | 5,64 | 0,53 | Segoe UI 9 pt |
| `Txt_Marque` | Zone de texte | Détail | 14,26 | 0,00 | 2,96 | 0,53 | Segoe UI 9 pt |
| `Txt_DateDebut` | Zone de texte | Détail | 17,22 | 0,00 | 2,41 | 0,53 | Segoe UI 9 pt |
| `Txt_DateFin` | Zone de texte | Détail | 19,63 | 0,00 | 2,41 | 0,53 | Segoe UI 9 pt |
| `Txt_Jours` | Zone de texte | Détail | 22,04 | 0,00 | 1,61 | 0,53 | Segoe UI 9 pt |
| `Txt_Montant` | Zone de texte | Détail | 23,65 | 0,00 | 4,05 | 0,53 | Segoe UI 9 pt |
| `Trait_Pied` | Trait | Pied de page | 0,00 | 0,11 | 27,70 | 0,03 | doré |
| `Lbl_Societe` | Étiquette | Pied de page | 0,00 | 0,26 | 11,11 | 0,48 | Bahnschrift 9 pt |
| `Txt_Page` | Zone de texte | Pied de page | 22,41 | 0,26 | 5,29 | 0,48 | ="Page " & [Page] & " sur " & [Pages] |

## Voitures réservées · `Etat_VoituresReservees`

* Aperçu : `etats/png/03-voitures-reservees.png` · portrait · 1 page(s) avec les données actuelles
* Bouton : Tableau de bord › carte 02 Voitures actuellement réservées › Imprimer
* Source : Requête « Voitures réservées » (DateDebut <= Date() Et DateFin >= Date()) ; Retour dans = [DateFin]-Date()
* Tri et regroupement (*Regrouper, trier et total*) : DateFin croissante (prochain retour en premier)

| Section | Hauteur | Remarque |
|---|---:|---|
| En-tête d'état | 4,82 cm | bandeau, logo, titre, indicateurs (page 1 seulement) |
| En-tête de page | 0,74 cm | répété en haut de chaque page |
| Détail | 0,69 cm | `Couleur fond` blanc, `Autre couleur fond` #F4F6FA (lignes alternées), trait bas #E1E6EF |
| Pied d'état | 1,85 cm | à la fin de l'état |
| Pied de page | 0,79 cm | en bas de chaque page |

| Contrôle | Type | Section | Gauche | Haut | Largeur | Hauteur | Contenu / format |
|---|---|---|---:|---:|---:|---:|---|
| `Rect_Bandeau` | Rectangle | En-tête d'état | 0,00 | 0,00 | 19,00 | 2,28 | fond noir #000000 |
| `Logo` | Image | En-tête d'état | 0,53 | 0,56 | 4,79 | 1,16 | assets/marque/aurion-menu.png |
| `Lbl_Titre` | Étiquette | En-tête d'état | 6,56 | 0,48 | 11,91 | 0,74 | Bahnschrift SemiBold 16 pt, blanc |
| `Txt_Edition` | Zone de texte | En-tête d'état | 6,56 | 1,32 | 11,91 | 0,53 | ="Édité le " & Format(Maintenant();"dddd d mmmm yyyy à hh:nn") |
| `Trait_Or` | Trait | En-tête d'état | 0,00 | 2,28 | 19,00 | 0,05 | doré #C9A24B, 1,5 pt |
| `Rect_Indicateur1` | Rectangle | En-tête d'état | 0,00 | 2,80 | 6,11 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur1` | Étiquette | En-tête d'état | 0,37 | 3,04 | 5,37 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur1` | Zone de texte | En-tête d'état | 0,37 | 3,47 | 5,37 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur2` | Rectangle | En-tête d'état | 6,43 | 2,80 | 6,11 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur2` | Étiquette | En-tête d'état | 6,80 | 3,04 | 5,37 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur2` | Zone de texte | En-tête d'état | 6,80 | 3,47 | 5,37 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur3` | Rectangle | En-tête d'état | 12,89 | 2,80 | 6,11 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur3` | Étiquette | En-tête d'état | 13,26 | 3,04 | 5,37 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur3` | Zone de texte | En-tête d'état | 13,26 | 3,47 | 5,37 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_EnteteColonnes` | Rectangle | En-tête de page | 0,00 | 0,00 | 19,00 | 0,69 | #002366 |
| `Lbl_Matricule` | Étiquette | En-tête de page | 0,00 | 0,00 | 2,22 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Modele` | Étiquette | En-tête de page | 2,22 | 0,00 | 5,19 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Client` | Étiquette | En-tête de page | 7,41 | 0,00 | 3,28 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Du` | Étiquette | En-tête de page | 10,69 | 0,00 | 1,91 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Au` | Étiquette | En-tête de page | 12,59 | 0,00 | 1,91 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Retourdans` | Étiquette | En-tête de page | 14,50 | 0,00 | 1,75 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Montant` | Étiquette | En-tête de page | 16,25 | 0,00 | 2,75 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Txt_Matricule` | Zone de texte | Détail | 0,00 | 0,00 | 2,22 | 0,69 | Segoe UI 9 pt |
| `Txt_Modele` | Zone de texte | Détail | 2,22 | 0,00 | 5,19 | 0,69 | Segoe UI 9 pt |
| `Txt_Client` | Zone de texte | Détail | 7,41 | 0,00 | 3,28 | 0,69 | Segoe UI 9 pt |
| `Txt_DateDebut` | Zone de texte | Détail | 10,69 | 0,00 | 1,91 | 0,69 | Segoe UI 9 pt |
| `Txt_DateFin` | Zone de texte | Détail | 12,59 | 0,00 | 1,91 | 0,69 | Segoe UI 9 pt |
| `Txt_RetourDans` | Zone de texte | Détail | 14,50 | 0,00 | 1,75 | 0,69 | Segoe UI 9 pt |
| `Txt_Montant` | Zone de texte | Détail | 16,25 | 0,00 | 2,75 | 0,69 | Segoe UI 9 pt |
| `Txt_Nombre` | Zone de texte | Pied d'état | 0,00 | 0,37 | 10,58 | 1,48 | =Compte(*) & " …" |
| `Rect_Total` | Rectangle | Pied d'état | 10,27 | 0,37 | 8,73 | 1,48 | #002366 |
| `Lbl_Total` | Étiquette | Pied d'état | 10,69 | 0,58 | 7,94 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Total` | Zone de texte | Pied d'état | 10,69 | 0,95 | 7,94 | 0,79 | =Somme([Montant]) · Bahnschrift SemiBold 18 pt, #E3C77A |
| `Trait_Pied` | Trait | Pied de page | 0,00 | 0,11 | 19,00 | 0,03 | doré |
| `Lbl_Societe` | Étiquette | Pied de page | 0,00 | 0,26 | 11,11 | 0,48 | Bahnschrift 9 pt |
| `Txt_Page` | Zone de texte | Pied de page | 13,71 | 0,26 | 5,29 | 0,48 | ="Page " & [Page] & " sur " & [Pages] |

## Liste des clients · `Etat_Clients`

* Aperçu : `etats/png/04-liste-des-clients.png` · paysage · 8 page(s) avec les données actuelles
* Bouton : Clients › carte 01 Liste des clients › Imprimer
* Source : Table Client
* Tri et regroupement (*Regrouper, trier et total*) : Regroupement sur =Gauche([Nom];1), puis tri Nom, Prénom

| Section | Hauteur | Remarque |
|---|---:|---|
| En-tête d'état | 4,82 cm | bandeau, logo, titre, indicateurs (page 1 seulement) |
| En-tête de page | 0,74 cm | répété en haut de chaque page |
| En-tête de groupe | 0,95 cm | un par valeur du regroupement |
| Détail | 0,53 cm | `Couleur fond` blanc, `Autre couleur fond` #F4F6FA (lignes alternées), trait bas #E1E6EF |
| Pied de page | 0,79 cm | en bas de chaque page |

| Contrôle | Type | Section | Gauche | Haut | Largeur | Hauteur | Contenu / format |
|---|---|---|---:|---:|---:|---:|---|
| `Rect_Bandeau` | Rectangle | En-tête d'état | 0,00 | 0,00 | 27,70 | 2,28 | fond noir #000000 |
| `Logo` | Image | En-tête d'état | 0,53 | 0,56 | 4,79 | 1,16 | assets/marque/aurion-menu.png |
| `Lbl_Titre` | Étiquette | En-tête d'état | 15,27 | 0,48 | 11,91 | 0,74 | Bahnschrift SemiBold 16 pt, blanc |
| `Txt_Edition` | Zone de texte | En-tête d'état | 15,27 | 1,32 | 11,91 | 0,53 | ="Édité le " & Format(Maintenant();"dddd d mmmm yyyy à hh:nn") |
| `Trait_Or` | Trait | En-tête d'état | 0,00 | 2,28 | 27,70 | 0,05 | doré #C9A24B, 1,5 pt |
| `Rect_Indicateur1` | Rectangle | En-tête d'état | 0,00 | 2,80 | 6,69 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur1` | Étiquette | En-tête d'état | 0,37 | 3,04 | 5,95 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur1` | Zone de texte | En-tête d'état | 0,37 | 3,47 | 5,95 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur2` | Rectangle | En-tête d'état | 7,01 | 2,80 | 6,69 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur2` | Étiquette | En-tête d'état | 7,38 | 3,04 | 5,95 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur2` | Zone de texte | En-tête d'état | 7,38 | 3,47 | 5,95 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur3` | Rectangle | En-tête d'état | 14,02 | 2,80 | 6,69 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur3` | Étiquette | En-tête d'état | 14,39 | 3,04 | 5,95 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur3` | Zone de texte | En-tête d'état | 14,39 | 3,47 | 5,95 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur4` | Rectangle | En-tête d'état | 21,01 | 2,80 | 6,69 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur4` | Étiquette | En-tête d'état | 21,38 | 3,04 | 5,95 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur4` | Zone de texte | En-tête d'état | 21,38 | 3,47 | 5,95 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_EnteteColonnes` | Rectangle | En-tête de page | 0,00 | 0,00 | 27,70 | 0,69 | #002366 |
| `Lbl_Code` | Étiquette | En-tête de page | 0,00 | 0,00 | 2,25 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Nom` | Étiquette | En-tête de page | 2,25 | 0,00 | 3,55 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Prenom` | Étiquette | En-tête de page | 5,79 | 0,00 | 3,25 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Sexe` | Étiquette | En-tête de page | 9,05 | 0,00 | 1,30 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Adresse` | Étiquette | En-tête de page | 10,35 | 0,00 | 5,90 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Telephone` | Étiquette | En-tête de page | 16,25 | 0,00 | 4,13 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Email` | Étiquette | En-tête de page | 20,37 | 0,00 | 7,33 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Rect_Groupe` | Rectangle | En-tête de groupe | 0,00 | 0,16 | 27,70 | 0,69 | #EDF1F9 |
| `Rect_GroupeOr` | Rectangle | En-tête de groupe | 0,00 | 0,16 | 0,11 | 0,69 | doré |
| `Txt_Groupe` | Zone de texte | En-tête de groupe | 0,42 | 0,16 | 10,58 | 0,69 | Bahnschrift SemiBold 11 pt, #002366 |
| `Txt_GroupeNombre` | Zone de texte | En-tête de groupe | 20,82 | 0,16 | 6,46 | 0,69 | =Compte(*) & " …" |
| `Txt_CIN` | Zone de texte | Détail | 0,00 | 0,00 | 2,25 | 0,53 | Segoe UI 9 pt |
| `Txt_Nom` | Zone de texte | Détail | 2,25 | 0,00 | 3,55 | 0,53 | Segoe UI 9 pt |
| `Txt_Prenom` | Zone de texte | Détail | 5,79 | 0,00 | 3,25 | 0,53 | Segoe UI 9 pt |
| `Txt_Sexe` | Zone de texte | Détail | 9,05 | 0,00 | 1,30 | 0,53 | Segoe UI 9 pt |
| `Txt_Adresse` | Zone de texte | Détail | 10,35 | 0,00 | 5,90 | 0,53 | Segoe UI 9 pt |
| `Txt_Telephone` | Zone de texte | Détail | 16,25 | 0,00 | 4,13 | 0,53 | Segoe UI 9 pt |
| `Txt_Email` | Zone de texte | Détail | 20,37 | 0,00 | 7,33 | 0,53 | Segoe UI 9 pt |
| `Trait_Pied` | Trait | Pied de page | 0,00 | 0,11 | 27,70 | 0,03 | doré |
| `Lbl_Societe` | Étiquette | Pied de page | 0,00 | 0,26 | 11,11 | 0,48 | Bahnschrift 9 pt |
| `Txt_Page` | Zone de texte | Pied de page | 22,41 | 0,26 | 5,29 | 0,48 | ="Page " & [Page] & " sur " & [Pages] |

## Parc automobile · `Etat_Voitures`

* Aperçu : `etats/png/05-parc-automobile.png` · portrait · 2 page(s) avec les données actuelles
* Bouton : Voitures › carte 01 Liste des voitures › Imprimer
* Source : Requête : Voiture + Modele + Marque + Carburant
* Tri et regroupement (*Regrouper, trier et total*) : Regroupement sur Marque, puis CoutParJour décroissant

| Section | Hauteur | Remarque |
|---|---:|---|
| En-tête d'état | 4,82 cm | bandeau, logo, titre, indicateurs (page 1 seulement) |
| En-tête de page | 0,74 cm | répété en haut de chaque page |
| En-tête de groupe | 0,95 cm | un par valeur du regroupement |
| Détail | 0,56 cm | `Couleur fond` blanc, `Autre couleur fond` #F4F6FA (lignes alternées), trait bas #E1E6EF |
| Pied de page | 0,79 cm | en bas de chaque page |

| Contrôle | Type | Section | Gauche | Haut | Largeur | Hauteur | Contenu / format |
|---|---|---|---:|---:|---:|---:|---|
| `Rect_Bandeau` | Rectangle | En-tête d'état | 0,00 | 0,00 | 19,00 | 2,28 | fond noir #000000 |
| `Logo` | Image | En-tête d'état | 0,53 | 0,56 | 4,79 | 1,16 | assets/marque/aurion-menu.png |
| `Lbl_Titre` | Étiquette | En-tête d'état | 6,56 | 0,48 | 11,91 | 0,74 | Bahnschrift SemiBold 16 pt, blanc |
| `Txt_Edition` | Zone de texte | En-tête d'état | 6,56 | 1,32 | 11,91 | 0,53 | ="Édité le " & Format(Maintenant();"dddd d mmmm yyyy à hh:nn") |
| `Trait_Or` | Trait | En-tête d'état | 0,00 | 2,28 | 19,00 | 0,05 | doré #C9A24B, 1,5 pt |
| `Rect_Indicateur1` | Rectangle | En-tête d'état | 0,00 | 2,80 | 4,50 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur1` | Étiquette | En-tête d'état | 0,37 | 3,04 | 3,76 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur1` | Zone de texte | En-tête d'état | 0,37 | 3,47 | 3,76 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur2` | Rectangle | En-tête d'état | 4,82 | 2,80 | 4,50 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur2` | Étiquette | En-tête d'état | 5,19 | 3,04 | 3,76 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur2` | Zone de texte | En-tête d'état | 5,19 | 3,47 | 3,76 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur3` | Rectangle | En-tête d'état | 9,66 | 2,80 | 4,50 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur3` | Étiquette | En-tête d'état | 10,03 | 3,04 | 3,76 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur3` | Zone de texte | En-tête d'état | 10,03 | 3,47 | 3,76 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur4` | Rectangle | En-tête d'état | 14,50 | 2,80 | 4,50 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur4` | Étiquette | En-tête d'état | 14,87 | 3,04 | 3,76 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur4` | Zone de texte | En-tête d'état | 14,87 | 3,47 | 3,76 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_EnteteColonnes` | Rectangle | En-tête de page | 0,00 | 0,00 | 19,00 | 0,69 | #002366 |
| `Lbl_Matricule` | Étiquette | En-tête de page | 0,00 | 0,00 | 2,51 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Modele` | Étiquette | En-tête de page | 2,51 | 0,00 | 5,58 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Annee` | Étiquette | En-tête de page | 8,10 | 0,00 | 1,46 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Couleur` | Étiquette | En-tête de page | 9,55 | 0,00 | 1,96 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Carburant` | Étiquette | En-tête de page | 11,51 | 0,00 | 2,22 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Puissance` | Étiquette | En-tête de page | 13,73 | 0,00 | 2,22 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Prixjour` | Étiquette | En-tête de page | 15,95 | 0,00 | 3,04 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Rect_Groupe` | Rectangle | En-tête de groupe | 0,00 | 0,16 | 19,00 | 0,69 | #EDF1F9 |
| `Rect_GroupeOr` | Rectangle | En-tête de groupe | 0,00 | 0,16 | 0,11 | 0,69 | doré |
| `Txt_Groupe` | Zone de texte | En-tête de groupe | 0,42 | 0,16 | 10,58 | 0,69 | Bahnschrift SemiBold 11 pt, #002366 |
| `Txt_GroupeNombre` | Zone de texte | En-tête de groupe | 12,12 | 0,16 | 6,46 | 0,69 | =Compte(*) & " …" |
| `Txt_Matricule` | Zone de texte | Détail | 0,00 | 0,00 | 2,51 | 0,56 | Segoe UI 9 pt |
| `Txt_Modele` | Zone de texte | Détail | 2,51 | 0,00 | 5,58 | 0,56 | Segoe UI 9 pt |
| `Txt_Annee` | Zone de texte | Détail | 8,10 | 0,00 | 1,46 | 0,56 | Segoe UI 9 pt |
| `Txt_Couleur` | Zone de texte | Détail | 9,55 | 0,00 | 1,96 | 0,56 | Segoe UI 9 pt |
| `Txt_Carburant` | Zone de texte | Détail | 11,51 | 0,00 | 2,22 | 0,56 | Segoe UI 9 pt |
| `Txt_Puissance` | Zone de texte | Détail | 13,73 | 0,00 | 2,22 | 0,56 | Segoe UI 9 pt |
| `Txt_CoutParJour` | Zone de texte | Détail | 15,95 | 0,00 | 3,04 | 0,56 | Segoe UI 9 pt |
| `Trait_Pied` | Trait | Pied de page | 0,00 | 0,11 | 19,00 | 0,03 | doré |
| `Lbl_Societe` | Étiquette | Pied de page | 0,00 | 0,26 | 11,11 | 0,48 | Bahnschrift 9 pt |
| `Txt_Page` | Zone de texte | Pied de page | 13,71 | 0,26 | 5,29 | 0,48 | ="Page " & [Page] & " sur " & [Pages] |

## Marques · `Etat_Marques`

* Aperçu : `etats/png/06-marques.png` · portrait · 1 page(s) avec les données actuelles
* Bouton : Marques › carte 01 Liste des marques › Imprimer
* Source : Requête : Marque + Compte des modèles + Compte et moyenne des voitures
* Tri et regroupement (*Regrouper, trier et total*) : IdMarque croissant

| Section | Hauteur | Remarque |
|---|---:|---|
| En-tête d'état | 4,82 cm | bandeau, logo, titre, indicateurs (page 1 seulement) |
| En-tête de page | 0,74 cm | répété en haut de chaque page |
| Détail | 0,79 cm | `Couleur fond` blanc, `Autre couleur fond` #F4F6FA (lignes alternées), trait bas #E1E6EF |
| Pied d'état | 1,85 cm | à la fin de l'état |
| Pied de page | 0,79 cm | en bas de chaque page |

| Contrôle | Type | Section | Gauche | Haut | Largeur | Hauteur | Contenu / format |
|---|---|---|---:|---:|---:|---:|---|
| `Rect_Bandeau` | Rectangle | En-tête d'état | 0,00 | 0,00 | 19,00 | 2,28 | fond noir #000000 |
| `Logo` | Image | En-tête d'état | 0,53 | 0,56 | 4,79 | 1,16 | assets/marque/aurion-menu.png |
| `Lbl_Titre` | Étiquette | En-tête d'état | 6,56 | 0,48 | 11,91 | 0,74 | Bahnschrift SemiBold 16 pt, blanc |
| `Txt_Edition` | Zone de texte | En-tête d'état | 6,56 | 1,32 | 11,91 | 0,53 | ="Édité le " & Format(Maintenant();"dddd d mmmm yyyy à hh:nn") |
| `Trait_Or` | Trait | En-tête d'état | 0,00 | 2,28 | 19,00 | 0,05 | doré #C9A24B, 1,5 pt |
| `Rect_Indicateur1` | Rectangle | En-tête d'état | 0,00 | 2,80 | 6,11 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur1` | Étiquette | En-tête d'état | 0,37 | 3,04 | 5,37 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur1` | Zone de texte | En-tête d'état | 0,37 | 3,47 | 5,37 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur2` | Rectangle | En-tête d'état | 6,43 | 2,80 | 6,11 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur2` | Étiquette | En-tête d'état | 6,80 | 3,04 | 5,37 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur2` | Zone de texte | En-tête d'état | 6,80 | 3,47 | 5,37 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur3` | Rectangle | En-tête d'état | 12,89 | 2,80 | 6,11 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur3` | Étiquette | En-tête d'état | 13,26 | 3,04 | 5,37 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur3` | Zone de texte | En-tête d'état | 13,26 | 3,47 | 5,37 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_EnteteColonnes` | Rectangle | En-tête de page | 0,00 | 0,00 | 19,00 | 0,69 | #002366 |
| `Lbl_Identifiant` | Étiquette | En-tête de page | 0,00 | 0,00 | 2,12 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Marque` | Étiquette | En-tête de page | 2,12 | 0,00 | 5,79 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Modeles` | Étiquette | En-tête de page | 7,91 | 0,00 | 2,91 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Voitures` | Étiquette | En-tête de page | 10,82 | 0,00 | 2,91 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Tarifmoyenjour` | Étiquette | En-tête de page | 13,73 | 0,00 | 5,27 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Txt_IdMarque` | Zone de texte | Détail | 0,00 | 0,00 | 2,12 | 0,79 | Segoe UI 9 pt |
| `Txt_Marque` | Zone de texte | Détail | 2,12 | 0,00 | 5,79 | 0,79 | Segoe UI 9 pt |
| `Txt_NbModeles` | Zone de texte | Détail | 7,91 | 0,00 | 2,91 | 0,79 | Segoe UI 9 pt |
| `Txt_NbVoitures` | Zone de texte | Détail | 10,82 | 0,00 | 2,91 | 0,79 | Segoe UI 9 pt |
| `Txt_TarifMoyen` | Zone de texte | Détail | 13,73 | 0,00 | 5,27 | 0,79 | Segoe UI 9 pt |
| `Txt_Nombre` | Zone de texte | Pied d'état | 0,00 | 0,37 | 10,58 | 1,48 | =Compte(*) & " …" |
| `Rect_Total` | Rectangle | Pied d'état | 10,27 | 0,37 | 8,73 | 1,48 | #002366 |
| `Lbl_Total` | Étiquette | Pied d'état | 10,69 | 0,58 | 7,94 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Total` | Zone de texte | Pied d'état | 10,69 | 0,95 | 7,94 | 0,79 | =Somme([Montant]) · Bahnschrift SemiBold 18 pt, #E3C77A |
| `Trait_Pied` | Trait | Pied de page | 0,00 | 0,11 | 19,00 | 0,03 | doré |
| `Lbl_Societe` | Étiquette | Pied de page | 0,00 | 0,26 | 11,11 | 0,48 | Bahnschrift 9 pt |
| `Txt_Page` | Zone de texte | Pied de page | 13,71 | 0,26 | 5,29 | 0,48 | ="Page " & [Page] & " sur " & [Pages] |

## Types de carburant · `Etat_Carburants`

* Aperçu : `etats/png/07-carburants.png` · portrait · 1 page(s) avec les données actuelles
* Bouton : Carburants › carte 01 Types de carburant › Imprimer
* Source : Requête : Carburant + Compte des voitures
* Tri et regroupement (*Regrouper, trier et total*) : IdType croissant

| Section | Hauteur | Remarque |
|---|---:|---|
| En-tête d'état | 4,82 cm | bandeau, logo, titre, indicateurs (page 1 seulement) |
| En-tête de page | 0,74 cm | répété en haut de chaque page |
| Détail | 0,90 cm | `Couleur fond` blanc, `Autre couleur fond` #F4F6FA (lignes alternées), trait bas #E1E6EF |
| Pied d'état | 1,85 cm | à la fin de l'état |
| Pied de page | 0,79 cm | en bas de chaque page |

| Contrôle | Type | Section | Gauche | Haut | Largeur | Hauteur | Contenu / format |
|---|---|---|---:|---:|---:|---:|---|
| `Rect_Bandeau` | Rectangle | En-tête d'état | 0,00 | 0,00 | 19,00 | 2,28 | fond noir #000000 |
| `Logo` | Image | En-tête d'état | 0,53 | 0,56 | 4,79 | 1,16 | assets/marque/aurion-menu.png |
| `Lbl_Titre` | Étiquette | En-tête d'état | 6,56 | 0,48 | 11,91 | 0,74 | Bahnschrift SemiBold 16 pt, blanc |
| `Txt_Edition` | Zone de texte | En-tête d'état | 6,56 | 1,32 | 11,91 | 0,53 | ="Édité le " & Format(Maintenant();"dddd d mmmm yyyy à hh:nn") |
| `Trait_Or` | Trait | En-tête d'état | 0,00 | 2,28 | 19,00 | 0,05 | doré #C9A24B, 1,5 pt |
| `Rect_Indicateur1` | Rectangle | En-tête d'état | 0,00 | 2,80 | 4,50 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur1` | Étiquette | En-tête d'état | 0,37 | 3,04 | 3,76 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur1` | Zone de texte | En-tête d'état | 0,37 | 3,47 | 3,76 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur2` | Rectangle | En-tête d'état | 4,82 | 2,80 | 4,50 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur2` | Étiquette | En-tête d'état | 5,19 | 3,04 | 3,76 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur2` | Zone de texte | En-tête d'état | 5,19 | 3,47 | 3,76 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur3` | Rectangle | En-tête d'état | 9,66 | 2,80 | 4,50 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur3` | Étiquette | En-tête d'état | 10,03 | 3,04 | 3,76 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur3` | Zone de texte | En-tête d'état | 10,03 | 3,47 | 3,76 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur4` | Rectangle | En-tête d'état | 14,50 | 2,80 | 4,50 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur4` | Étiquette | En-tête d'état | 14,87 | 3,04 | 3,76 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur4` | Zone de texte | En-tête d'état | 14,87 | 3,47 | 3,76 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_EnteteColonnes` | Rectangle | En-tête de page | 0,00 | 0,00 | 19,00 | 0,69 | #002366 |
| `Lbl_Identifiant` | Étiquette | En-tête de page | 0,00 | 0,00 | 2,17 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Type` | Étiquette | En-tête de page | 2,17 | 0,00 | 4,07 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Voitures` | Étiquette | En-tête de page | 6,24 | 0,00 | 2,43 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Part` | Étiquette | En-tête de page | 8,68 | 0,00 | 2,17 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Repartition` | Étiquette | En-tête de page | 10,85 | 0,00 | 8,15 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Txt_IdType` | Zone de texte | Détail | 0,00 | 0,00 | 2,17 | 0,90 | Segoe UI 9 pt |
| `Txt_Type` | Zone de texte | Détail | 2,17 | 0,00 | 4,07 | 0,90 | Segoe UI 9 pt |
| `Txt_NbVoitures` | Zone de texte | Détail | 6,24 | 0,00 | 2,43 | 0,90 | Segoe UI 9 pt |
| `Txt_Part` | Zone de texte | Détail | 8,68 | 0,00 | 2,17 | 0,90 | Segoe UI 9 pt |
| `Rect_Barre` | Rectangle (barre) | Détail | 11,06 | 0,19 | 4,92 | 0,53 | largeur calculée en VBA (Format) |
| `Txt_Nombre` | Zone de texte | Pied d'état | 0,00 | 0,37 | 10,58 | 1,48 | =Compte(*) & " …" |
| `Rect_Total` | Rectangle | Pied d'état | 10,27 | 0,37 | 8,73 | 1,48 | #002366 |
| `Lbl_Total` | Étiquette | Pied d'état | 10,69 | 0,58 | 7,94 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Total` | Zone de texte | Pied d'état | 10,69 | 0,95 | 7,94 | 0,79 | =Somme([Montant]) · Bahnschrift SemiBold 18 pt, #E3C77A |
| `Trait_Pied` | Trait | Pied de page | 0,00 | 0,11 | 19,00 | 0,03 | doré |
| `Lbl_Societe` | Étiquette | Pied de page | 0,00 | 0,26 | 11,11 | 0,48 | Bahnschrift 9 pt |
| `Txt_Page` | Zone de texte | Pied de page | 13,71 | 0,26 | 5,29 | 0,48 | ="Page " & [Page] & " sur " & [Pages] |

## Modèles · `Etat_Modeles`

* Aperçu : `etats/png/08-modeles.png` · portrait · 2 page(s) avec les données actuelles
* Bouton : Modèles › carte 01 Liste des modèles › Imprimer
* Source : Requête : Modele + Marque + Compte des voitures
* Tri et regroupement (*Regrouper, trier et total*) : Regroupement sur Marque, puis IdModele

| Section | Hauteur | Remarque |
|---|---:|---|
| En-tête d'état | 4,82 cm | bandeau, logo, titre, indicateurs (page 1 seulement) |
| En-tête de page | 0,74 cm | répété en haut de chaque page |
| En-tête de groupe | 0,95 cm | un par valeur du regroupement |
| Détail | 0,56 cm | `Couleur fond` blanc, `Autre couleur fond` #F4F6FA (lignes alternées), trait bas #E1E6EF |
| Pied de page | 0,79 cm | en bas de chaque page |

| Contrôle | Type | Section | Gauche | Haut | Largeur | Hauteur | Contenu / format |
|---|---|---|---:|---:|---:|---:|---|
| `Rect_Bandeau` | Rectangle | En-tête d'état | 0,00 | 0,00 | 19,00 | 2,28 | fond noir #000000 |
| `Logo` | Image | En-tête d'état | 0,53 | 0,56 | 4,79 | 1,16 | assets/marque/aurion-menu.png |
| `Lbl_Titre` | Étiquette | En-tête d'état | 6,56 | 0,48 | 11,91 | 0,74 | Bahnschrift SemiBold 16 pt, blanc |
| `Txt_Edition` | Zone de texte | En-tête d'état | 6,56 | 1,32 | 11,91 | 0,53 | ="Édité le " & Format(Maintenant();"dddd d mmmm yyyy à hh:nn") |
| `Trait_Or` | Trait | En-tête d'état | 0,00 | 2,28 | 19,00 | 0,05 | doré #C9A24B, 1,5 pt |
| `Rect_Indicateur1` | Rectangle | En-tête d'état | 0,00 | 2,80 | 6,11 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur1` | Étiquette | En-tête d'état | 0,37 | 3,04 | 5,37 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur1` | Zone de texte | En-tête d'état | 0,37 | 3,47 | 5,37 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur2` | Rectangle | En-tête d'état | 6,43 | 2,80 | 6,11 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur2` | Étiquette | En-tête d'état | 6,80 | 3,04 | 5,37 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur2` | Zone de texte | En-tête d'état | 6,80 | 3,47 | 5,37 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_Indicateur3` | Rectangle | En-tête d'état | 12,89 | 2,80 | 6,11 | 1,53 | bordure #D9DFEA |
| `Lbl_Indicateur3` | Étiquette | En-tête d'état | 13,26 | 3,04 | 5,37 | 0,37 | Bahnschrift SemiBold 8 pt |
| `Txt_Indicateur3` | Zone de texte | En-tête d'état | 13,26 | 3,47 | 5,37 | 0,69 | Bahnschrift SemiBold 15 pt, #002366 |
| `Rect_EnteteColonnes` | Rectangle | En-tête de page | 0,00 | 0,00 | 19,00 | 0,69 | #002366 |
| `Lbl_Identifiant` | Étiquette | En-tête de page | 0,00 | 0,00 | 2,38 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Modele` | Étiquette | En-tête de page | 2,38 | 0,00 | 8,73 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Voitures` | Étiquette | En-tête de page | 11,11 | 0,00 | 2,91 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Lbl_Prixjour` | Étiquette | En-tête de page | 14,02 | 0,00 | 4,97 | 0,69 | Bahnschrift SemiBold 8,5 pt, blanc |
| `Rect_Groupe` | Rectangle | En-tête de groupe | 0,00 | 0,16 | 19,00 | 0,69 | #EDF1F9 |
| `Rect_GroupeOr` | Rectangle | En-tête de groupe | 0,00 | 0,16 | 0,11 | 0,69 | doré |
| `Txt_Groupe` | Zone de texte | En-tête de groupe | 0,42 | 0,16 | 10,58 | 0,69 | Bahnschrift SemiBold 11 pt, #002366 |
| `Txt_GroupeNombre` | Zone de texte | En-tête de groupe | 12,12 | 0,16 | 6,46 | 0,69 | =Compte(*) & " …" |
| `Txt_IdModele` | Zone de texte | Détail | 0,00 | 0,00 | 2,38 | 0,56 | Segoe UI 9 pt |
| `Txt_Modele` | Zone de texte | Détail | 2,38 | 0,00 | 8,73 | 0,56 | Segoe UI 9 pt |
| `Txt_NbVoitures` | Zone de texte | Détail | 11,11 | 0,00 | 2,91 | 0,56 | Segoe UI 9 pt |
| `Txt_PrixJour` | Zone de texte | Détail | 14,02 | 0,00 | 4,97 | 0,56 | Segoe UI 9 pt |
| `Trait_Pied` | Trait | Pied de page | 0,00 | 0,11 | 19,00 | 0,03 | doré |
| `Lbl_Societe` | Étiquette | Pied de page | 0,00 | 0,26 | 11,11 | 0,48 | Bahnschrift 9 pt |
| `Txt_Page` | Zone de texte | Pied de page | 13,71 | 0,26 | 5,29 | 0,48 | ="Page " & [Page] & " sur " & [Pages] |
