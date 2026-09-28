# RENTAL GABON CAR : refonte des formulaires (thème bleu)

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

Le bleu est la couleur principale : menu bleu marine, bandeau souligné de bleu, indicateurs en trois bleus,
titres des cartes et icônes en bleu. Dans Access, tapez le code directement dans la propriété (ex. `#2563EB`).

| Rôle | Code |
|---|---|
| **Menu latéral** (fond) | `#1E3A8A` |
| Menu : texte / icônes | `#DCE6FB` / `#AFC3F0` |
| Menu : onglet actif (fond / texte) | `#FFFFFF` / `#1E3A8A` |
| Menu : survol | `#264796` |
| Bleu principal (bouton Enregistrer, trait sous le bandeau, icônes des boutons) | `#2563EB` |
| Titres (page et cartes) | `#1E3A8A` |
| Indicateurs : Chiffre d'affaires / Voitures / Clients | `#1E40AF` / `#2563EB` / `#3B82F6` |
| Pastille de l'icône sur chaque indicateur | `#3F5BBE` / `#4B7FEF` / `#5C97F8` |
| Fond de la zone de contenu | `#EEF2F9` |
| Bande de titre des cartes | `#F2F6FD` |
| Bordure des cartes et trait sous le titre | `#D3DDEE` |
| Bordure des petits boutons | `#C6D4EE` |
| Bordure des zones de liste | `#B9C9E6` |
| Champs : fond / bordure | `#FFFFFF` / `#C9D0DA` |
| Champ en lecture seule : fond / bordure | `#F4F5F7` / `#DDE1E7` |
| Montant : fond / bordure / texte | `#EAF1FD` / `#C6D4EE` / `#1E40AF` |
| Texte principal / étiquettes / texte secondaire | `#111827` / `#4B5563` / `#6B7280` |
| Rouge (Supprimer) : texte / bordure | `#DC2626` / `#E8A5A5` |

**Police : Segoe UI partout.** Tailles : titre de page 16 pt semi-gras, titre de carte 12 pt semi-gras,
étiquettes et champs 11 pt, zones de liste 10 pt, chiffres des indicateurs 20 pt semi-gras.

**Nom de l'application : RENTAL GABON CAR.** Mettez-le aussi dans la propriété `Légende` des formulaires `Menu`
et `Login` : c'est le texte qui s'affiche dans la barre de titre de la fenêtre (« RENTAL GABON CAR » et
« RENTAL GABON CAR - Connexion »). Vous pouvez aussi le définir dans *Fichier › Options › Base de données active ›
Titre de l'application*.

---

## 2. Réglages généraux (une seule fois)

1. **Fichier › Options › Base de données active** : cochez *Utiliser les contrôles à thème Windows sur les formulaires*
   (nécessaire pour les couleurs des boutons et les coins arrondis).
2. Sur chaque formulaire : `Sélecteur d'enregistrement` Non, `Boutons de déplacement` Non,
   `Diviseurs d'enregistrements` Non, `Barre de défilement` Aucune.
3. Sous-formulaires (Tableau Bord, Réservation, Client…) : section *Détail*, `Couleur fond` = `#EEF2F9`,
   taille **35,67 × 19,26 cm**, `Style bordure` Aucun.
4. Icônes : en mode Création, *Création › Insérer une image › Parcourir* et sélectionnez les PNG de `assets/`.
   Elles deviennent des images partagées réutilisables dans la propriété `Image` des boutons.

---

## 3. Réglages par contrôle

**Carte** (un Rectangle + une Étiquette + un Trait)
* Rectangle : `Couleur fond` `#FFFFFF`, `Style bordure` Continu, `Couleur bordure` `#D3DDEE`, `Épaisseur` Filet, `Effet spécial` Plat.
  Placez-le en premier puis *Organiser › Mettre en arrière-plan*.
* Bande de titre : Rectangle de 1,32 cm de haut sur toute la largeur de la carte, `Couleur fond` `#F2F6FD`, sans bordure.
* Titre : Segoe UI Semibold 12 pt, `#1E3A8A`, à 0,53 cm du bord gauche et 0,37 cm du haut.
* Trait horizontal à 1,32 cm du haut de la carte : `Couleur bordure` `#D3DDEE`.

**Étiquettes** : Segoe UI 11 pt, `#4B5563`, fond transparent, alignées à gauche.

**Zones de texte et listes déroulantes** : `Couleur fond` `#FFFFFF`, `Couleur bordure` `#C9D0DA`, `Style bordure` Continu,
`Effet spécial` Plat, Segoe UI 11 pt `#111827`, hauteur 0,74 cm, `Marge gauche` 0,15 cm.
* Lecture seule (Téléphone, Email, Modèle, Marque, Durée, Montant) : `Verrouillé` Oui, `Couleur fond` `#F4F5F7`, `Couleur bordure` `#DDE1E7`.
* Montant : semi-gras 12 pt, aligné à droite, fond `#EAF1FD`, bordure `#C6D4EE`, texte `#1E40AF`. Format : `# ##0" FCFA"`.

**Boutons** (`Utiliser le thème` Oui, *Format › Modifier la forme › Rectangle à coins arrondis*)

| Bouton | Fond | Survol | Bordure | Texte |
|---|---|---|---|---|
| Enregistrer | `#2563EB` | `#1D4ED8` | `#2563EB` | `#FFFFFF`, semi-gras 11 pt |
| Supprimer | `#FFFFFF` | `#FEF2F2` | `#E8A5A5` | `#DC2626`, semi-gras 11 pt |
| OK | `#FFFFFF` | `#F3F4F6` | `#C9D0DA` | `#374151`, 11 pt |
| Petits boutons (＋ ⟳ 🔍 🖨, ⏮ ◀ ▶ ⏭, Quitter) | `#FFFFFF` | `#EAF1FD` | `#C6D4EE` | image `bouton-….png` (icône bleue), pas de légende |

Taille : Enregistrer et Supprimer 3,18 × 0,85 cm ; petits boutons 0,79 × 0,79 cm.
Le compteur « 1 sur 25 » est une zone de texte sans bordure : `=[CurrentRecord] & " sur " & Compte(*)`.

**Zones de liste** : `En-têtes colonnes` Oui, `Couleur fond` `#FFFFFF`, `Couleur bordure` `#B9C9E6`, Segoe UI 10 pt `#1F2937`.
Les largeurs de colonnes de la maquette sont dans `COTES.md`. Les dates et montants se formatent dans la requête :
`Format([DateDebut];"jj/mm/aaaa")`, `Format([CA];"# ##0")`.

**Indicateurs du tableau de bord** : un Rectangle plein de 11,17 × 2,54 cm (fond et bordure `#1E40AF`, `#2563EB` ou `#3B82F6`),
une étiquette « Chiffre d'affaires » en 11 pt `#DCE7FF`, une zone de texte en Segoe UI Semibold 20 pt blanc (fond et
bordure transparents), et à droite un Rectangle de 1,27 × 1,27 cm (`#3F5BBE`, `#4B7FEF` ou `#5C97F8`) avec l'icône blanche
`indicateur-….png` centrée dessus.

**Formulaire Menu** (formulaire de navigation)
* Menu à gauche : Rectangle de 5,82 cm de large sur toute la hauteur, `Couleur fond` `#1E3A8A`, sans bordure.
  Logo : image `logo-voiture.png` (blanche) + étiquette « RENTAL GABON CAR » Segoe UI Semibold 11 pt blanc.
* Boutons de navigation : forme Rectangle à coins arrondis, `Couleur fond` `#1E3A8A`, `Couleur de pointage` `#264796`,
  `Couleur si appuyé` `#FFFFFF`, `Couleur texte` `#DCE6FB`, `Couleur texte de pointage` `#FFFFFF`,
  `Couleur texte si appuyé` `#1E3A8A`, `Couleur bordure` `#1E3A8A`, Segoe UI 11 pt, `Image` `menu-….png`,
  `Disposition image légende` Gauche, hauteur 1,01 cm. L'icône bleue `menu-…-actif.png` sert pour l'onglet sélectionné.
* Bandeau : 1,48 cm de haut, `#FFFFFF`, avec en bas un trait bleu `#2563EB` de 2 pt. Titre de page Segoe UI Semibold 16 pt `#1E3A8A`.
  Date : zone de texte `=Maintenant()`, format `jj/mm/aaaa hh:nn`, 10 pt `#6B7280`, sans bordure.

**Formulaire Login** : `Fenêtre indépendante` Oui, `Fenêtre modale` Oui, `Boutons Min Max` Aucun, fond `#FFFFFF`,
11,64 × 11,11 cm. En haut, un Rectangle bleu `#1E3A8A` de 2,54 cm de haut avec le logo blanc et « RENTAL GABON CAR »
en Segoe UI Semibold 14 pt blanc. Titre « Connexion » 16 pt `#1E3A8A`. Champ mot de passe : `Masque de saisie` = Mot de passe.

---

## 4. Ce que j'ai changé par rapport à vos formulaires actuels

* Même structure (menu à gauche, bandeau, fiche à gauche et liste à droite) : rien à réorganiser.
* Menu bleu marine, indicateurs en bleu, fond bleu très clair, cartes blanches alignées sur une même grille (marges de 0,63 cm).
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
