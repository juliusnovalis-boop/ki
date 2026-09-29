# Icônes et logo — RENTAL GABON CAR

## Logo de l’application

Deux versions horizontales avec fond transparent sont fournies :

- `assets/logo-menu-blanc.svg` / `.png` : version compacte aux proportions du menu. Le PNG mesure 368 × 56 px et doit être affiché à **184 × 28 px** (4,87 × 0,74 cm) sur le fond bleu marine.
- `assets/logo-rental-gabon-car-blanc.svg` / `.png` : logo blanc horizontal plus grand, à placer sur un fond sombre comme le menu bleu marine (`#1E3A8A`).
- `assets/logo-rental-gabon-car-bleu.svg` / `.png` : voiture bleue (`#2563EB`) et nom bleu marine (`#1E3A8A`), à placer sur un fond clair.
- `assets/logo-voiture.png` : pictogramme blanc seul, également utilisé dans les maquettes.

Les logos horizontaux standards ont un SVG de 460 × 72 et un PNG de 920 × 144. Le logo compact du menu a un viewBox de 184 × 28 ; son PNG fait 368 × 56 pour un affichage net à 184 × 28.

## Icônes de l’interface

Les PNG exportés sont les mêmes pictogrammes, traits et couleurs que ceux des maquettes, avec leur taille d’affichage native :

| Fichiers | Usage dans la maquette | Taille PNG | Couleur |
|---|---|---:|---|
| `menu-*.png` | Navigation inactive | 18 × 18 px | `#AFC3F0` |
| `menu-*-actif.png` | Navigation sélectionnée | 18 × 18 px | `#1E3A8A` |
| `carte-*.png` | Titres de cartes | 18 × 18 px | `#2563EB` |
| `bouton-*.png` | Boutons et navigation d’enregistrements | 16 × 16 px | `#2563EB` ; exceptions ci-dessous |
| `date.png` | Date dans l’en-tête | 15 × 15 px | `#6B7280` |
| `indicateur-*.png` | KPI sur fond bleu | 24 × 24 px | `#FFFFFF` |
| `logo-voiture.png` | Marque dans le menu | 24 × 24 px | `#FFFFFF` |

Exceptions des boutons : `bouton-power.png` est marine (`#1E3A8A`), `bouton-enregistrer.png` est blanc (`#FFFFFF`) et `bouton-supprimer.png` est rouge (`#DC2626`). Les variantes n’ont volontairement pas toutes la même couleur ni la même forme : elles correspondent à des contextes distincts (par exemple `car` de profil dans la navigation et `car-front` de face dans l’indicateur et le logo).

Les fichiers de `outils/icones-svg/` sont les sources Lucide à couleur `currentColor` destinées au générateur ; ils ne sont pas des exports PNG colorés prêts à importer. Pour retrouver exactement l’apparence de la maquette dans Access, utilisez les PNG indiqués ci-dessus.

Les photos de l’application ne font pas partie du pack d’icônes. Elles restent dans `outils/photos/` et `assets/photos/`.
