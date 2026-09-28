# Rental Car : refonte des formulaires (thème clair)

Maquettes des 8 écrans de `Database20.accdb`, dessinées comme de vraies captures d'Access :
fenêtre Windows, police Segoe UI, zones de texte, listes déroulantes et zones de liste telles qu'Access les affiche.
Pas d'effets spéciaux : **tout se règle dans la feuille de propriétés**, sans code.

| Écran | Maquette | Formulaire |
|---|---|---|
| Connexion | [`00-connexion.png`](maquettes/png/00-connexion.png) | `Login` |
| Tableau de bord | [`01-tableau-de-bord.png`](maquettes/png/01-tableau-de-bord.png) | `Menu` + `Tableau Bord` |
| Réservations | [`02-reservations.png`](maquettes/png/02-reservations.png) | `Réservation` |
| Clients | [`03-clients.png`](maquettes/png/03-clients.png) | `Client` |
| Voitures | [`04-voitures.png`](maquettes/png/04-voitures.png) | `Voiture` |
| Marques | [`05-marques.png`](maquettes/png/05-marques.png) | `Marque` |
| Carburants | [`06-carburants.png`](maquettes/png/06-carburants.png) | `Carburant` |
| Modèles | [`07-modeles.png`](maquettes/png/07-modeles.png) | `Modèle` |

* `COTES.md` : position et taille de chaque contrôle, en cm.
* `assets/` : les icônes en PNG transparent (menu, boutons, indicateurs), à importer dans Access.
* `maquettes/*.html` : les mêmes maquettes, à ouvrir dans un navigateur (sous Windows, elles s'affichent en Segoe UI).

---

## 1. Couleurs

Une seule couleur d'accent (bleu), du gris pour le reste. Dans Access, tapez le code directement dans la propriété (ex. `#2563EB`).

| Rôle | Code |
|---|---|
| Fond de la zone de contenu | `#F3F5F8` |
| Menu, bandeau, cartes, champs | `#FFFFFF` |
| Bordure des cartes et du menu | `#E1E5EB` |
| Trait sous le titre des cartes | `#EDF0F4` |
| Bordure des champs et des listes | `#C9D0DA` |
| Champ en lecture seule : fond / bordure | `#F4F5F7` / `#DDE1E7` |
| Texte principal | `#111827` |
| Texte des étiquettes | `#4B5563` |
| Texte secondaire (date, « 25 réservations ») | `#6B7280` |
| **Bleu** (bouton Enregistrer, onglet actif) | `#2563EB` (texte de l'onglet actif : `#1D4ED8`) |
| Fond de l'onglet actif | `#EAF1FD` |
| Rouge (Supprimer) : texte / bordure | `#DC2626` / `#E8A5A5` |
| Pastilles des indicateurs | bleu `#EAF1FD`, vert `#E9F7EE`, violet `#F1ECFD` |

**Police : Segoe UI partout.** Tailles : titre de page 16 pt semi-gras, titre de carte 12 pt semi-gras,
étiquettes et champs 11 pt, zones de liste 10 pt, chiffres des indicateurs 20 pt semi-gras.

---

## 2. Réglages généraux (une seule fois)

1. **Fichier › Options › Base de données active** : cochez *Utiliser les contrôles à thème Windows sur les formulaires*
   (nécessaire pour les couleurs des boutons et les coins arrondis).
2. Sur chaque formulaire : `Sélecteur d'enregistrement` Non, `Boutons de déplacement` Non,
   `Diviseurs d'enregistrements` Non, `Barre de défilement` Aucune.
3. Sous-formulaires (Tableau Bord, Réservation, Client…) : section *Détail*, `Couleur fond` = `#F3F5F8`,
   taille **35,67 × 19,26 cm**, `Style bordure` Aucun.
4. Icônes : en mode Création, *Création › Insérer une image › Parcourir* et sélectionnez les PNG de `assets/`.
   Elles deviennent des images partagées réutilisables dans la propriété `Image` des boutons.

---

## 3. Réglages par contrôle

**Carte** (un Rectangle + une Étiquette + un Trait)
* Rectangle : `Couleur fond` `#FFFFFF`, `Style bordure` Continu, `Couleur bordure` `#E1E5EB`, `Épaisseur` Filet, `Effet spécial` Plat.
  Placez-le en premier puis *Organiser › Mettre en arrière-plan*.
* Titre : Segoe UI Semibold 12 pt, `#111827`, à 0,53 cm du bord gauche et 0,37 cm du haut.
* Trait horizontal à 1,32 cm du haut de la carte : `Couleur bordure` `#EDF0F4`.

**Étiquettes** : Segoe UI 11 pt, `#4B5563`, fond transparent, alignées à gauche.

**Zones de texte et listes déroulantes** : `Couleur fond` `#FFFFFF`, `Couleur bordure` `#C9D0DA`, `Style bordure` Continu,
`Effet spécial` Plat, Segoe UI 11 pt `#111827`, hauteur 0,74 cm, `Marge gauche` 0,15 cm.
* Lecture seule (Téléphone, Email, Modèle, Marque, Durée, Montant) : `Verrouillé` Oui, `Couleur fond` `#F4F5F7`, `Couleur bordure` `#DDE1E7`.
* Montant : même chose en semi-gras 12 pt, aligné à droite. Format : `# ##0" FCFA"`.

**Boutons** (`Utiliser le thème` Oui, *Format › Modifier la forme › Rectangle à coins arrondis*)

| Bouton | Fond | Survol | Bordure | Texte |
|---|---|---|---|---|
| Enregistrer | `#2563EB` | `#1D4ED8` | `#2563EB` | `#FFFFFF`, semi-gras 11 pt |
| Supprimer | `#FFFFFF` | `#FEF2F2` | `#E8A5A5` | `#DC2626`, semi-gras 11 pt |
| OK | `#FFFFFF` | `#F3F4F6` | `#C9D0DA` | `#374151`, 11 pt |
| Petits boutons (＋ ⟳ 🔍 🖨, ⏮ ◀ ▶ ⏭, Quitter) | `#FFFFFF` | `#F3F4F6` | `#D5DAE1` | image `bouton-….png`, pas de légende |

Taille : Enregistrer et Supprimer 3,18 × 0,85 cm ; petits boutons 0,79 × 0,79 cm.
Le compteur « 1 sur 25 » est une zone de texte sans bordure : `=[CurrentRecord] & " sur " & Compte(*)`.

**Zones de liste** : `En-têtes colonnes` Oui, `Couleur fond` `#FFFFFF`, `Couleur bordure` `#C9D0DA`, Segoe UI 10 pt `#1F2937`.
Les largeurs de colonnes de la maquette sont dans `COTES.md`. Les dates et montants se formatent dans la requête :
`Format([DateDebut];"jj/mm/aaaa")`, `Format([CA];"# ##0")`.

**Indicateurs du tableau de bord** : un Rectangle blanc (bordure `#E1E5EB`) de 11,17 × 2,54 cm, une étiquette grise
(« Chiffre d'affaires »), une zone de texte en Segoe UI Semibold 20 pt, et à droite un petit Rectangle coloré
de 1,27 × 1,27 cm avec l'icône `indicateur-….png` centrée dessus.

**Formulaire Menu** (formulaire de navigation)
* Menu à gauche : 5,82 cm de large, `#FFFFFF`, trait vertical `#E1E5EB` à droite. Logo : image `logo-voiture.png` + étiquette
  « Rental Car » Segoe UI Semibold 14 pt.
* Boutons de navigation : forme Rectangle à coins arrondis, `Couleur fond` `#FFFFFF`, `Couleur de pointage` `#F3F4F6`,
  `Couleur si appuyé` `#EAF1FD`, `Couleur texte` `#4B5563`, `Couleur texte si appuyé` `#1D4ED8`, `Couleur bordure` `#FFFFFF`,
  Segoe UI 11 pt, `Image` `menu-….png`, `Disposition image légende` Gauche, hauteur 1,01 cm.
* Bandeau : 1,48 cm de haut, `#FFFFFF`, trait `#E1E5EB` en bas. Titre de page Segoe UI Semibold 16 pt.
  Date : zone de texte `=Maintenant()`, format `jj/mm/aaaa hh:nn`, 10 pt `#6B7280`, sans bordure.

**Formulaire Login** : `Fenêtre indépendante` Oui, `Fenêtre modale` Oui, `Boutons Min Max` Aucun, fond `#FFFFFF`,
11,64 × 10,16 cm. Champ mot de passe : `Masque de saisie` = Mot de passe.

---

## 4. Ce que j'ai changé par rapport à vos formulaires actuels

* Même structure (menu à gauche, bandeau, fiche à gauche et liste à droite) : rien à réorganiser.
* Fond clair uniforme, cartes blanches alignées sur une même grille (marges de 0,63 cm).
* Libellés en minuscules plutôt qu'en majuscules, plus lisibles.
* Tableau de bord : la liste « Voitures actuellement réservées » n'affiche plus le numéro du modèle, et la liste des
  réservations (requête existante « Liste des réservations ») occupe le bas de l'écran.

## 5. Problèmes repérés dans la base

1. **Réservation n° 11** : la date de fin (06/12/2026) est avant la date de début (13/02/2027). La durée est négative,
   ce qui fausse le chiffre d'affaires. Ajoutez sur la table `Reservation` : `Valide si` = `[DateFin]>=[DateDebut]`.
2. **Requête « Voitures réservées »** : seul critère `DateFin >= Date()`, elle affiche donc aussi les réservations
   à venir. Ajoutez `DateDebut <= Date()` (8 réservations en cours au 28/09/2026 ; c'est ce que montre la maquette).
3. **Requête « Liste des réservations »** : la jointure Marque ↔ Modèle y figure deux fois.
4. La table `Users` stocke les mots de passe en clair.

---

## Régénérer les maquettes (facultatif)

```bash
cd design/outils
npm install          # Chromium sans interface pour le rendu
python3 generer.py   # recrée maquettes/, assets/ et COTES.md
```
Icônes : [Lucide](https://lucide.dev), licence ISC.
