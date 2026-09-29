# RENTAL GABON CAR : refonte des formulaires (thème bleu, avec photos)

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
* [`COULEURS.md`](COULEURS.md) : palette hexadécimale pour reprendre les couleurs dans Access.
* [`ICONES_LOGO.md`](ICONES_LOGO.md) : formats et usages des icônes et logos exportables.
* `outils/photos/` : les 8 photos originales fournies pour le projet : `carburants-pompe.jpg`, `clients-accueil.jpg`,
  `login-route.jpg`, `menu-route.jpg`, `modeles-interieur.jpg`, `reservations-cles.jpg`, `tableau-flotte.jpg` et
  `voitures-showroom.jpg`. Aucune autre photo source n'est utilisée.
* `assets/` : les icônes en PNG transparent (menu, boutons, cartes, indicateurs), à importer dans Access.
* `assets/photos/` : les recadrages teintés en bleu, générés à partir de ces 8 originaux pour les bandeaux, le menu et la connexion.
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

**Police : Segoe UI partout.** Tailles : titre du bandeau photo 20 pt semi-gras blanc, titre de carte 12 pt semi-gras,
étiquettes et champs 11 pt, zones de liste 10 pt, chiffres des indicateurs 20 pt semi-gras.
Les titres de carte sont précédés d'une icône bleue de 0,48 cm (`carte-….png`) et commencent à 1,27 cm du bord de la carte.

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

**Indicateurs du tableau de bord** : un Rectangle plein de 11,17 × 2,65 cm (fond et bordure `#1E40AF`, `#2563EB` ou `#3B82F6`),
une étiquette « Chiffre d'affaires » en 11 pt `#DCE7FF`, une zone de texte en Segoe UI Semibold 20 pt blanc (fond et
bordure transparents), et à droite un Rectangle de 1,27 × 1,27 cm (`#3F5BBE`, `#4B7FEF` ou `#5C97F8`) avec l'icône blanche
`indicateur-….png` centrée dessus. Sous le chiffre, une ligne d'info en 10 pt `#DCE7FF`
(« sur 25 réservations », « 8 en location aujourd'hui », « Meilleur client : Cynthia Kombila »).

**Formulaire Menu** (formulaire de navigation)
* Menu à gauche : contrôle Image `photos/menu-fond.jpg` de 5,82 × 20,74 cm, sur toute la hauteur (bleu uni en haut,
  photo de route de nuit qui apparaît en bas). Placez-le en arrière-plan (*Organiser › Mettre en arrière-plan*).
  Au-dessus : petite étiquette « MENU PRINCIPAL » 9 pt `#8FA6DA`, et en bas « Location de véhicules à Libreville » 10 pt `#DCE6FB`.
  Logo : image `logo-voiture.png` (blanche) + étiquette « RENTAL GABON CAR » Segoe UI Semibold 11 pt blanc.
  Pour le menu, utilisez le logo compact `assets/logo-menu-blanc.png` à **4,87 × 0,74 cm** (184 × 28 px), placé à 0,48 cm du bord gauche et 0,42 cm du haut. Le PNG fait 368 × 56 px pour rester net à cette taille.
  Pour les autres fonds, utilisez `assets/logo-rental-gabon-car-blanc.png` sur fond sombre ou sa version `-bleu.png` sur fond clair.
* Boutons de navigation : forme Rectangle à coins arrondis, `Couleur fond` `#1E3A8A`, `Couleur de pointage` `#264796`,
  `Couleur si appuyé` `#FFFFFF`, `Couleur texte` `#DCE6FB`, `Couleur texte de pointage` `#FFFFFF`,
  `Couleur texte si appuyé` `#1E3A8A`, `Couleur bordure` `#1E3A8A`, Segoe UI 11 pt, `Image` `menu-….png`,
  `Disposition image légende` Gauche, hauteur 1,01 cm. L'icône bleue `menu-…-actif.png` sert pour l'onglet sélectionné.
* En-tête : 1,48 cm de haut, `#FFFFFF`, avec en bas un trait bleu `#2563EB` de 2 pt. Il n'y a plus de titre de page
  ici (il passe dans le bandeau photo).
  * À gauche, la date : zone de texte `=Maintenant()`, `Format` `jjjj j mmmm aaaa - hh:nn`, 10 pt `#6B7280`, sans bordure.
  * À droite, l'utilisateur : bouton `Forme` Ovale de 0,85 × 0,85 cm, fond `#2563EB`, texte « AD » blanc 9 pt semi-gras,
    puis deux étiquettes « admin » (10 pt semi-gras `#111827`) et « Administrateur » (9 pt `#6B7280`), puis le bouton Quitter.
    Pour afficher le vrai nom : `=[Forms]![Login]![Txt_Utilisateur]` ou une variable remplie à la connexion.

**Formulaire Login** : `Fenêtre indépendante` Oui, `Fenêtre modale` Oui, `Boutons Min Max` Aucun, fond `#FFFFFF`,
23,28 × 13,23 cm. La moitié gauche est l'image `photos/login-photo.jpg` (11,11 × 13,23 cm, Ferrari bleue sur une route
côtière), avec par-dessus le logo et « RENTAL GABON CAR » 14 pt blanc, « Location de véhicules à Libreville » 16 pt
blanc et « © 2026 RENTAL GABON CAR » 9 pt `#C9D6F5`. À droite, le formulaire : titre « Connexion » 20 pt `#1E3A8A`,
champs de 9,53 cm, bouton « Se connecter » bleu sur toute la largeur. Champ mot de passe : `Masque de saisie` = Mot de passe.

**Bandeaux photo (tous les écrans du menu)** : en haut de la zone de contenu, à 0,63 cm des bords, un contrôle Image
`photos/bandeau-<écran>.jpg` de 34,40 cm de large, 3,39 cm de haut sur le tableau de bord et 2,43 cm sur les autres écrans.
Le dégradé bleu est déjà dans l'image : le texte reste lisible à gauche. Posez dessus deux étiquettes :
le titre (Segoe UI Semibold 20 pt blanc) et une ligne d'info (11 pt `#DCE6FB`), par exemple « 200 clients enregistrés ».
Pour que les chiffres restent à jour, utilisez des zones de texte : `=CpteDom("*";"Client") & " clients enregistrés"`.

**Réglages des images et du texte posé dessus**
* Contrôle Image : `Mode affichage` **Découpage** (les images ont déjà la bonne taille ; mettez Zoom si vous les redimensionnez),
  `Type image` **Partagé** (l'image n'est stockée qu'une fois dans la base, même si elle sert sur plusieurs formulaires),
  `Style bordure` Transparent.
* Étiquettes sur une photo : `Style fond` **Transparent**, `Style bordure` Transparent, puis *Mettre au premier plan*.
* Les huit photos originales sont conservées dans `outils/photos/` ; les fichiers de `assets/photos/` sont leurs
  recadrages teintés en bleu. `tableau-flotte.jpg` sert au tableau de bord et à l'écran Voitures ; `voitures-showroom.jpg`
  sert à l'écran Marques. Le menu et la connexion utilisent `menu-route.jpg` et `login-route.jpg`.
  Vérifiez les droits d'utilisation avant toute diffusion commerciale. Formats générés : bandeaux 1300 × 128 et 1300 × 92,
  menu 220 × 784, connexion 420 × 500.

---

## 4. Ce que j'ai changé par rapport à vos formulaires actuels

* Même structure (menu à gauche, bandeau, fiche à gauche et liste à droite) : rien à réorganiser.
* Menu bleu marine, indicateurs en bleu, fond bleu très clair, cartes blanches alignées sur une même grille (marges de 0,63 cm).
* Libellés en minuscules plutôt qu'en majuscules, plus lisibles.
* Huit photos de référence fournies pour le projet : flotte premium, remise des clés, clientèle, showroom, pompe,
  habitacle, route côtière et menu de nuit. Elles restent sous un voile bleu discret, pour garder un rendu sobre et homogène.
* Catalogue de démonstration : Ferrari, Lamborghini, Bentley, Bugatti et Rolls-Royce ; l'écran Voitures affiche désormais
  aussi les colonnes Modèle et Marque, afin que le niveau de gamme soit visible dans la liste.
* Tableau de bord : un message d'accueil, la liste « Voitures actuellement réservées » (sans le numéro du modèle),
  les 5 meilleurs clients et une nouvelle petite liste « Flotte par carburant » (Essence 31, Diesel 23, Hybride 6), avec
  une requête de regroupement sur `Voiture` + `Carburant` : `Type` (Regroupement), `Voitures : Compte(*)`,
  `Part : [Voitures]/CpteDom("*";"Voiture")` avec la propriété `Format` = Pourcentage, 1 décimale.
* Boutons Enregistrer / Supprimer avec icône (`bouton-enregistrer.png`, `bouton-supprimer.png`, `Disposition image légende` Gauche).

## 5. Problèmes repérés dans la base

1. **Réservation n° 11** : la date de fin (06/12/2026) est avant la date de début (13/02/2027). La durée est négative,
   ce qui fausse le chiffre d'affaires. Ajoutez sur la table `Reservation` : `Valide si` = `[DateFin]>=[DateDebut]`.
2. **Requête « Voitures réservées »** : seul critère `DateFin >= Date()`, elle affiche donc aussi les réservations
   à venir. Ajoutez `DateDebut <= Date()` (8 réservations en cours au 28/09/2026 ; c'est ce que montre la maquette).
3. **Requête « Liste des réservations »** : la jointure Marque ↔ Modèle y figure deux fois.
4. La table `Users` stocke les mots de passe en clair.

---

## 6. Catalogue automobile premium

La maquette et `design/outils/donnees.json` utilisent un catalogue de démonstration de 5 marques et 60 modèles :
**Ferrari, Lamborghini, Bentley, Bugatti et Rolls-Royce**. L'écran Voitures affiche aussi Modèle et Marque dans la liste.
Les identifiants existants sont conservés pour ne pas casser les relations Voiture → Modèle ni les réservations.

Pour appliquer ce catalogue à `Database20.accdb` sur Windows :

1. Faites une copie de la base et **fermez Access**.
2. Depuis le dossier du projet, ouvrez l'invite de commandes et lancez :

   ```bat
   cscript //nologo design\outils\appliquer-parc-premium.vbs
   ```

   Vous pouvez aussi passer le chemin complet de la base en argument. Le script exige Access ou l'Access Database Engine ;
   il crée une sauvegarde horodatée à côté du fichier, effectue les changements dans une transaction et annule tout si un
   identifiant attendu manque.
3. Rouvrez la base et vérifiez les tables `Marque` et `Modele`.

**Important :** le fichier `Database20.accdb` du dépôt n'est pas modifié par cette session, car Access n'est pas disponible
sous Linux. Le script `.vbs` est fourni pour effectuer la mise à jour dans Access ; il n'a pas été exécuté ici.
Il met à jour les noms des marques/modèles et leur liaison, mais laisse volontairement inchangés les prix journaliers,
les clients, les réservations et les carburants. Les tarifs du formulaire restent donc ceux de votre base ; il vaut mieux
les valider séparément avant de les augmenter pour une flotte premium.

## Régénérer les maquettes (facultatif)

```bash
cd design/outils
npm install          # Chromium sans interface pour le rendu
python3 generer.py   # recrée maquettes/, assets/ et COTES.md
```
Icônes : [Lucide](https://lucide.dev), licence ISC.
