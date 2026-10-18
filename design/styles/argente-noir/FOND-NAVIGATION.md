# Photo en fond du menu ET du sous-formulaire, sans VBA · PLATINUM DRIVE

Schéma : **`schema-fond-navigation.png`**. Aucune ligne de VBA : seulement des propriétés et des **macros incorporées**.

## Le principe

Dans Access, un sous-formulaire **peint toujours son propre fond** (il ne peut pas être transparent). On coupe donc chaque photo en deux :

* **le bandeau** (haut de la photo, 1,905 cm) : dans le formulaire **Menu**, derrière les onglets ;
* **le bas** (18,838 cm) : dans le **formulaire de la page**, affiché par le sous-formulaire.

Le bas change tout seul (chaque page a sa propre image). Pour le haut, le Menu contient **les 7 bandeaux empilés** et la macro de chaque bouton de navigation **affiche le bon et cache les autres**.

## 1. Les images (prêtes dans `assets/photos/`)

| Page | Bandeau → formulaire Menu (41,49 × 1,905 cm) | Bas → formulaire de la page (41,49 × 18,838 cm) |
|---|---|---|
| Tableau de bord (`Frm_Tableau`) | `d-tete-tableau.jpg` | `d-corps-tableau.jpg` |
| Réservations (`Frm_Reservations`) | `d-tete-reservations.jpg` | `d-corps-reservations.jpg` |
| Clients (`Frm_Clients`) | `d-tete-clients.jpg` | `d-corps-clients.jpg` |
| Voitures (`Frm_Voitures`) | `d-tete-voitures.jpg` | `d-corps-voitures.jpg` |
| Marques (`Frm_Marques`) | `d-tete-marques.jpg` | `d-corps-marques.jpg` |
| Carburants (`Frm_Carburants`) | `d-tete-carburants.jpg` | `d-corps-carburants.jpg` |
| Modèles (`Frm_Modeles`) | `d-tete-modeles.jpg` | `d-corps-modeles.jpg` |

## 2. Formulaire Menu

1. Mode Création, sélectionnez tous les contrôles › onglet **Organiser** › **Supprimer la disposition** (sinon Access place lui-même le sous-formulaire et on ne peut pas le régler au millimètre).
2. Formulaire : Largeur **41,49 cm**, hauteur totale des sections **20,74 cm**, `Image` **(aucune)**, `Taille automatique` Oui, `Style bordure` **Fin**, `Boutons Min Max` Réduire seulement, barres de défilement Aucune, sélecteur et boutons de déplacement Non.
3. **Les 7 bandeaux** : onglet **Création** › **Insérer une image** › *Parcourir* › `d-tete-tableau.jpg`, dessinez le contrôle, puis réglez ses propriétés. Recommencez pour les 6 autres :

| Propriété | Valeur |
|---|---|
| Nom | `Img_Fond_tableau`, `Img_Fond_reservations`, `Img_Fond_clients`, `Img_Fond_voitures`, `Img_Fond_marques`, `Img_Fond_carburants`, `Img_Fond_modeles` (image `d-tete-<page>.jpg` correspondante) |
| Gauche / Haut | **0** / **0** (les 7 exactement au même endroit) |
| Largeur / Hauteur | **41,49 cm** / **1,905 cm** |
| Type d'image | Incorporé |
| Mode d'affichage | **Étirer** |
| Style bordure | Transparent |
| Visible | **Oui** pour `Img_Fond_tableau` seulement, **Non** pour les 6 autres |

4. Sélectionnez les 7 images › **Organiser** › **Mettre en arrière-plan** : elles passent derrière le logo et les onglets.
5. Contrôle de navigation (les onglets) : `Style fond` **Transparent**, `Style bordure` Transparent (positions : `COTES.md`, lignes `BoutonNavigation_…`). Nommez les boutons `BoutonNavigation_tableau`, `BoutonNavigation_clients`… (propriété **Nom**).
6. Contrôle **sous-formulaire** (ligne `Sous_Formulaire` de `COTES.md`) :

| Propriété | Valeur |
|---|---|
| Gauche | **0 cm** |
| Haut | **1,905 cm** (tapez les 3 décimales : c'est la ligne de coupe) |
| Largeur / Hauteur | **41,49 cm** / **18,838 cm** |
| Style bordure | **Transparent** |

## 3. Chaque formulaire de page : image fixe

| Formulaire | Propriété `Image` |
|---|---|
| `Frm_Tableau` | `d-corps-tableau.jpg` |
| `Frm_Reservations` | `d-corps-reservations.jpg` |
| `Frm_Clients` | `d-corps-clients.jpg` |
| `Frm_Voitures` | `d-corps-voitures.jpg` |
| `Frm_Marques` | `d-corps-marques.jpg` |
| `Frm_Carburants` | `d-corps-carburants.jpg` |
| `Frm_Modeles` | `d-corps-modeles.jpg` |

Dans chaque page : Largeur **41,49 cm**, Détail **18,838 cm**, en-tête/pied de formulaire supprimés, `Type d'image` Incorporé, `Mode d'affichage de l'image` **Étirer**, `Alignement` Coin supérieur gauche, barres de défilement **Aucune**, sélecteur, boutons de déplacement et diviseurs **Non**. Les cartes restent des Rectangles pleins posés par-dessus la photo (pas de grand Rectangle de fond).

## 4. La macro de chaque bouton de navigation

### Le premier bouton (Clients), pas à pas

1. Formulaire Menu en mode Création, cliquez sur le bouton **Clients**.
2. Feuille de propriétés › onglet **Événement** › ligne **Sur clic** › bouton **`…`** › **Générateur de macro** › OK.
3. Dans la liste **Ajouter une nouvelle action**, choisissez **DéfinirPropriété**, puis remplissez :

| Nom du contrôle | Propriété | Valeur |
|---|---|---|
| `Img_Fond_clients` | Visible | **-1** (= Vrai : on l'affiche) |

4. Ajoutez 6 autres actions **DéfinirPropriété**, une par autre bandeau, avec la Valeur **0** (= Faux : on le cache) : `Img_Fond_tableau`, `Img_Fond_reservations`, `Img_Fond_voitures`, `Img_Fond_marques`, `Img_Fond_carburants`, `Img_Fond_modeles`.
5. **Enregistrer**, puis **Fermer** le générateur. La ligne *Sur clic* affiche `[Macro incorporée]`.

### Les 6 autres boutons : copier-coller

Dans la macro terminée, cliquez dans le générateur, **Ctrl+A** puis **Ctrl+C**. Ouvrez la macro *Sur clic* du bouton suivant (étape 2), **Ctrl+V** : les 7 actions sont collées. Il reste à changer les **Valeurs** selon ce tableau (**-1** = visible, **0** = caché) :

| Bouton cliqué | Img_Fond_tableau | Img_Fond_reservations | Img_Fond_clients | Img_Fond_voitures | Img_Fond_marques | Img_Fond_carburants | Img_Fond_modeles |
|---|---:|---:|---:|---:|---:|---:|---:|
| `BoutonNavigation_tableau` (Tableau de bord) | **-1** | 0 | 0 | 0 | 0 | 0 | 0 |
| `BoutonNavigation_reservations` (Réservations) | 0 | **-1** | 0 | 0 | 0 | 0 | 0 |
| `BoutonNavigation_clients` (Clients) | 0 | 0 | **-1** | 0 | 0 | 0 | 0 |
| `BoutonNavigation_voitures` (Voitures) | 0 | 0 | 0 | **-1** | 0 | 0 | 0 |
| `BoutonNavigation_marques` (Marques) | 0 | 0 | 0 | 0 | **-1** | 0 | 0 |
| `BoutonNavigation_carburants` (Carburants) | 0 | 0 | 0 | 0 | 0 | **-1** | 0 |
| `BoutonNavigation_modeles` (Modèles) | 0 | 0 | 0 | 0 | 0 | 0 | **-1** |

Les boutons gardent leur **Nom du formulaire cible de navigation** (`Frm_Clients`…) : la macro change seulement le bandeau, la navigation (changement de page) reste faite par le formulaire de navigation d'Access.

## 5. Si ça ne marche pas

| Ce que vous voyez | Solution |
|---|---|
| Le haut ne change pas | *Sur clic* du bouton = `[Macro incorporée]` ; les noms `Img_Fond_…` de la macro doivent être exactement ceux des images |
| Le haut est vide au démarrage | `Visible` = **Oui** pour `Img_Fond_tableau` |
| Les onglets ou le logo sont cachés par la photo | Sélectionnez les 7 images › **Organiser** › **Mettre en arrière-plan** |
| Le bas ne change pas | Propriété `Image` de chaque formulaire de page (section 3) |
| Trait fin ou cadre autour de la page | `Style bordure` du contrôle sous-formulaire = **Transparent** |
| Photo décalée de quelques pixels | Sous-formulaire : `Haut` = **1,905**, `Gauche` = **0** ; bandeaux : `Hauteur` = **1,905** |
| Photo déformée | `Mode d'affichage` = **Étirer** partout, formulaire Menu à taille fixe (`Style bordure` Fin) |
