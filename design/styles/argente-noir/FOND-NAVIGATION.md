# Photo en fond du menu ET du sous-formulaire · PLATINUM DRIVE

Schéma : **`schema-fond-navigation.png`**.

## Pourquoi ça ne marche pas avec une seule image

Dans Access, le contrôle sous-formulaire (le `NavigationSubform` du formulaire de navigation) **peint toujours son propre fond** : un formulaire ne peut pas être transparent. L'image du formulaire Menu est donc cachée partout où se trouve le sous-formulaire.

**La solution** : couper la photo en deux morceaux **exactement alignés**. Le formulaire Menu garde la photo complète (on n'en voit que la bande des onglets) et chaque page affichée dans le sous-formulaire reçoit **le bas de la même photo**. À l'écran on voit une seule photo continue.

## 1. Les images (déjà prêtes dans `assets/photos/`)

| Page | Formulaire Menu (photo complète, 41,49 × 20,74 cm) | Formulaire de la page (bas de la photo, 41,49 × 18,84 cm) |
|---|---|---|
| Tableau de bord (`Frm_Tableau`) | `d-fond-tableau.jpg` | `d-corps-tableau.jpg` |
| Réservations (`Frm_Reservations`) | `d-fond-reservations.jpg` | `d-corps-reservations.jpg` |
| Clients (`Frm_Clients`) | `d-fond-clients.jpg` | `d-corps-clients.jpg` |
| Voitures (`Frm_Voitures`) | `d-fond-voitures.jpg` | `d-corps-voitures.jpg` |
| Marques (`Frm_Marques`) | `d-fond-marques.jpg` | `d-corps-marques.jpg` |
| Carburants (`Frm_Carburants`) | `d-fond-carburants.jpg` | `d-corps-carburants.jpg` |
| Modèles (`Frm_Modeles`) | `d-fond-modeles.jpg` | `d-corps-modeles.jpg` |

`d-corps-<page>.jpg` = `d-fond-<page>.jpg` coupée à **1,905 cm** du haut (72 pixels) : c'est la hauteur de la barre des onglets.

## 2. Formulaire Menu (formulaire de navigation)

1. Mode Création, sélectionner tous les contrôles › onglet **Organiser** › **Supprimer la disposition**. Sans ça, Access place lui-même le sous-formulaire et on ne peut pas le régler au millimètre.
2. Feuille de propriétés du **formulaire** :

| Propriété | Valeur |
|---|---|
| Largeur | **41,49 cm** (hauteur totale des sections : **20,74 cm**) |
| Image | `assets\photos\d-fond-tableau.jpg` (remplacée ensuite par le code) |
| Type d'image | **Lié** |
| Mode d'affichage de l'image | **Étirer** |
| Alignement de l'image | Coin supérieur gauche |
| Mosaïque | Non |
| Taille automatique | Oui |
| Style bordure | **Fin** (la fenêtre garde sa taille, donc le raccord reste parfait) |
| Boutons Min Max | Réduire seulement |
| Barres de défilement / Sélecteur / Boutons de déplacement | Aucune / Non / Non |

3. Contrôle de navigation (les onglets) : `Style fond` **Transparent**, `Style bordure` **Transparent**, positions dans `COTES.md` (lignes `BoutonNavigation_…`).
4. Contrôle **sous-formulaire** (`NavigationSubform`, ligne `Sous_Formulaire` de `COTES.md`) :

| Propriété | Valeur |
|---|---|
| Gauche | **0 cm** |
| Haut | **1,905 cm** (tapez bien les 3 décimales : c'est la ligne de coupe des images) |
| Largeur | **41,49 cm** |
| Hauteur | **18,838 cm** |
| Style bordure | **Transparent** |
| Apparence (effet spécial) | Normal |

## 3. Chaque formulaire de page : image FIXE, aucun code

C'est ce qui règle le changement de page : **chaque page emporte son propre bas de photo**. Quand vous cliquez sur *Clients*, Access affiche `Frm_Clients` dans le sous-formulaire, et `Frm_Clients` arrive avec `d-corps-clients.jpg`. Rien à programmer.

| Formulaire de page | Propriété `Image` (feuille de propriétés, onglet Format) |
|---|---|
| `Frm_Tableau` | `d-corps-tableau.jpg` |
| `Frm_Reservations` | `d-corps-reservations.jpg` |
| `Frm_Clients` | `d-corps-clients.jpg` |
| `Frm_Voitures` | `d-corps-voitures.jpg` |
| `Frm_Marques` | `d-corps-marques.jpg` |
| `Frm_Carburants` | `d-corps-carburants.jpg` |
| `Frm_Modeles` | `d-corps-modeles.jpg` |

| Propriété (dans chaque page) | Valeur |
|---|---|
| Largeur | **41,49 cm** · hauteur du Détail **18,838 cm** |
| En-tête / pied de formulaire | Supprimés (clic droit › décocher *En-tête/pied de formulaire*) |
| Type d'image | **Incorporé** (l'image est enregistrée dans la base : elle marche même si le dossier bouge) |
| Mode d'affichage de l'image | **Étirer** |
| Alignement de l'image | Coin supérieur gauche |
| Barres de défilement | **Aucune** |
| Sélecteur d'enregistrement / Boutons de déplacement / Diviseurs | Non / Non / Non |

Les cartes restent des Rectangles pleins posés **par-dessus** la photo. Ne mettez pas de grand Rectangle de fond : il cacherait la photo.

## 4. Le formulaire Menu : l'image change à chaque clic

Le haut de la photo est dans le formulaire Menu, qui reste ouvert : c'est **le seul endroit où il faut du code**. Chaque bouton de navigation remplace l'image du Menu par la photo de sa page.

1. Nommez les boutons de navigation comme dans `COTES.md` : sélectionnez un bouton › propriété **Nom** (`BoutonNavigation_tableau`, `BoutonNavigation_clients`…).
2. Formulaire Menu en mode Création › onglet **Création** › **Afficher le code**, puis collez tout ce code :

```vba
Option Compare Database
Option Explicit

' Change la photo du formulaire Menu (le haut, derrière les onglets)
Private Sub FondMenu(page As String)
    Me.Picture = CurrentProject.Path & "\assets\photos\d-fond-" & page & ".jpg"
End Sub

Private Sub Form_Load()
    FondMenu "tableau"            ' page affichée à l'ouverture
End Sub

Private Sub BoutonNavigation_tableau_Click()
    FondMenu "tableau"
End Sub

Private Sub BoutonNavigation_reservations_Click()
    FondMenu "reservations"
End Sub

Private Sub BoutonNavigation_clients_Click()
    FondMenu "clients"
End Sub

Private Sub BoutonNavigation_voitures_Click()
    FondMenu "voitures"
End Sub

Private Sub BoutonNavigation_marques_Click()
    FondMenu "marques"
End Sub

Private Sub BoutonNavigation_carburants_Click()
    FondMenu "carburants"
End Sub

Private Sub BoutonNavigation_modeles_Click()
    FondMenu "modeles"
End Sub
```

3. Vérifiez que chaque bouton est bien relié : propriété **Sur clic** du bouton = `[Procédure événementielle]`. Si ce n'est pas le cas, cliquez sur `…` à côté de *Sur clic* › **Générateur de code** : Access relie la procédure.
4. Les boutons gardent leur propriété **Nom du formulaire cible de navigation** (`Frm_Clients`…) : le code ne fait que changer la photo, la navigation reste celle d'Access.

Ça marche aussi sans formulaire de navigation (formulaire Menu + contrôle sous-formulaire + boutons ordinaires) : ajoutez simplement `Me.Sous_Formulaire.SourceObject = "Frm_Clients"` dans le clic, à côté de `FondMenu "clients"`.

## 5. Si la photo ne change pas quand on clique

| Ce que vous voyez | Cause | Solution |
|---|---|---|
| Bandeau jaune *« Avertissement de sécurité : le contenu actif a été désactivé »* | Access bloque **tout** le VBA | Cliquez **Activer le contenu**, ou mieux : *Fichier › Options › Centre de gestion de la confidentialité › Paramètres › Emplacements approuvés* › ajoutez le dossier de la base |
| Le bas change mais pas le haut | Le clic n'est pas relié au code | `Sur clic` = `[Procédure événementielle]` (étape 4.3) ; le **Nom** du bouton doit être exactement celui de la procédure |
| Le haut change mais pas le bas | La page n'a pas sa propre image | Propriété `Image` du formulaire de page (section 3) |
| Message « Impossible de trouver le fichier » | Mauvais dossier | Le dossier `assets` doit être à côté du fichier `.accdb` |
| Trait fin ou cadre autour de la page | Bordure du sous-formulaire | `Style bordure` du contrôle sous-formulaire = **Transparent** |
| Photo décalée de quelques pixels | Mauvaise position | `Haut` du contrôle sous-formulaire = **1,905**, `Gauche` = **0** |
| Photo déformée | Mauvais mode | `Mode d'affichage de l'image` = **Étirer** partout, formulaire Menu à taille fixe |
