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

## 3. Chaque formulaire de page (Frm_Tableau, Frm_Clients…)

| Propriété | Valeur |
|---|---|
| Largeur | **41,49 cm** · hauteur du Détail **18,838 cm** |
| En-tête / pied de formulaire | Supprimés (clic droit › décocher *En-tête/pied de formulaire*) |
| Image | `assets\photos\d-corps-<page>.jpg` (remplacée par le code) |
| Type d'image | **Lié** |
| Mode d'affichage de l'image | **Étirer** |
| Alignement de l'image | Coin supérieur gauche |
| Barres de défilement | **Aucune** |
| Sélecteur d'enregistrement / Boutons de déplacement / Diviseurs | Non / Non / Non |

Les cartes restent des Rectangles pleins (couleur *Cartes (fond)*), posés **par-dessus** la photo. Ne mettez pas de grand Rectangle de fond : il cacherait la photo. (Dans `COTES.md`, la ligne `Image_Fond_SousFormulaire` donne la place de cette photo ; on la met dans la propriété **Image** du formulaire plutôt que dans un contrôle Image, pour qu'elle ne gêne pas les clics.)

## 4. Le code (change les deux photos à chaque page)

Créer un **module standard** nommé `Mod_Fond` :

```vba
' Module standard : Mod_Fond
Public Sub AppliquerFond(frm As Form, page As String)
    Dim dossier As String
    dossier = CurrentProject.Path & "\assets\photos\"
    ' bas de la photo : fond du formulaire affiché dans le sous-formulaire
    frm.Picture = dossier & "d-corps-" & page & ".jpg"
    ' photo complète : fond du formulaire Menu (on n'en voit que le haut, derrière les onglets)
    On Error Resume Next          ' formulaire ouvert seul, sans le Menu
    frm.Parent.Picture = dossier & "d-fond-" & page & ".jpg"
End Sub
```

Puis, dans le module de **chaque formulaire de page** (événement *Sur chargement*) :

```vba
' Dans chaque formulaire de page (ici Frm_Clients)
Private Sub Form_Load()
    AppliquerFond Me, "clients"
End Sub
```

| Formulaire | Code dans `Form_Load` |
|---|---|
| `Frm_Tableau` | `AppliquerFond Me, "tableau"` |
| `Frm_Reservations` | `AppliquerFond Me, "reservations"` |
| `Frm_Clients` | `AppliquerFond Me, "clients"` |
| `Frm_Voitures` | `AppliquerFond Me, "voitures"` |
| `Frm_Marques` | `AppliquerFond Me, "marques"` |
| `Frm_Carburants` | `AppliquerFond Me, "carburants"` |
| `Frm_Modeles` | `AppliquerFond Me, "modeles"` |

Quand on clique sur un onglet, la page se charge dans le sous-formulaire, met **son** bas de photo et change la photo du Menu : le haut et le bas viennent toujours de la même image.

Ça marche aussi sans formulaire de navigation (formulaire Menu + contrôle sous-formulaire + boutons qui font `Me.Sous_Formulaire.SourceObject = "Frm_Clients"`) : `Me.Parent` désigne alors le formulaire Menu.

## 5. Si le raccord n'est pas parfait

| Problème | Solution |
|---|---|
| Trait fin ou cadre autour de la page | `Style bordure` du contrôle sous-formulaire = **Transparent** |
| Photo décalée de quelques pixels | `Haut` du contrôle sous-formulaire = **1,905**, `Gauche` = **0** |
| Photo déformée ou trop grande | `Mode d'affichage de l'image` = **Étirer** dans les deux formulaires, et formulaire Menu à taille fixe |
| Bande grise à droite ou en bas de la page | Barres de défilement **Aucune**, largeur et hauteur exactes du formulaire de page |
| « Fichier introuvable » | Le dossier `assets` doit être à côté du fichier `.accdb` (`CurrentProject.Path`) |
