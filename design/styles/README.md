# Les 4 styles de couleurs

Même disposition, mêmes cotes (`../COTES.md`) et même mode d'emploi que le style bleu (`../README.md`) :
seules les couleurs et les images changent.

![Aperçu des 4 styles](apercu-4-styles.png)

| Style | Dossier | Esprit |
|---|---|---|
| 1. Noir et blanc | [`noir-blanc/`](noir-blanc/png/) | Sobre et intemporel, photos en noir et blanc |
| 2. Rose et blanc | [`rose-blanc/`](rose-blanc/png/) | Framboise profond et rose vif, photos teintées |
| 3. Vert jade et blanc | [`vert-jade-blanc/`](vert-jade-blanc/png/) | Vert jade et vert forêt, élégant et frais |
| 4. Argenté et noir | [`argente-noir/`](argente-noir/png/) | Thème sombre, boutons et indicateurs argentés, très « prestige » |

Chaque dossier contient :
* `png/` : les 8 écrans (connexion, tableau de bord, réservations, clients, voitures, marques, carburants, modèles) ;
* `assets/` : les icônes PNG **dans les couleurs du style** et `assets/photos/` : les photos déjà teintées et recadrées ;
* les maquettes HTML et leur `style.css`.

Pour changer de style dans Access : importez les images du dossier choisi (mêmes noms de fichiers que le style bleu),
puis remplacez les couleurs dans la feuille de propriétés avec le tableau ci-dessous.

## Couleurs à saisir dans Access

| Élément | Noir et blanc | Rose et blanc | Vert jade et blanc | Argenté et noir |
|---|---|---|---|---|
| Menu (fond, en haut de l'image du menu) | `#0D0D0D` | `#9D174D` | `#064E3B` | `#000000` |
| Fond de la zone de contenu | `#F2F2F2` | `#FCF1F6` | `#EDF7F3` | `#0B0C0E` |
| Cartes (fond) | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` | `#16181B` |
| Bande de titre des cartes | `#F8F8F8` | `#FEF6FA` | `#F3FAF7` | `#1B1D21` |
| Bordure des cartes | `#DADADA` | `#F2D2E1` | `#CDE7DC` | `#2A2D32` |
| Titres des cartes, « Connexion » | `#0D0D0D` | `#9D174D` | `#065F46` | `#E8EAED` |
| Bouton principal, avatar, trait sous l'en-tête | `#111111` | `#DB2777` | `#00A86B` | `#C9CDD2` |
| Texte du bouton principal | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` | `#0B0C0E` |
| En-tête (fond) | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` | `#121417` |
| Trait sous l'en-tête | `#0D0D0D` | `#DB2777` | `#00A86B` | `#AEB3B9` |
| Texte du menu | `#D4D4D4` | `#FCE1EE` | `#D1F2E4` | `#B8BCC2` |
| Onglet actif (fond) | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` | `#D4D7DB` |
| Onglet actif (texte) | `#0D0D0D` | `#9D174D` | `#064E3B` | `#000000` |
| Zones de texte (fond) | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` | `#1F2226` |
| Zones de texte (bordure) | `#C8C8C8` | `#C9D0DA` | `#C9D0DA` | `#3A3E44` |
| Texte des champs | `#111111` | `#111827` | `#111827` | `#F1F2F4` |
| Étiquettes | `#4A4A4A` | `#4B5563` | `#4B5563` | `#A3A8AF` |
| Champ en lecture seule (fond) | `#F5F5F5` | `#FAF5F7` | `#F4F8F6` | `#1A1C20` |
| Montant (fond) | `#F1F1F1` | `#FDE8F2` | `#E2F5EC` | `#24272C` |
| Montant (texte) | `#0D0D0D` | `#9D174D` | `#047857` | `#F1F2F4` |
| Zones de liste (bordure) | `#BDBDBD` | `#EBB8CF` | `#A8D6C2` | `#3A3E44` |
| Petits boutons (bordure) | `#CFCFCF` | `#F0C6DA` | `#BCE0D0` | `#3A3E44` |
| Supprimer (texte) | `#DC2626` | `#B91C1C` | `#DC2626` | `#F87171` |
| Indicateurs (fond 1 / 2 / 3) | `#0D0D0D` / `#262626` / `#404040` | `#9D174D` / `#DB2777` / `#EC4899` | `#065F46` / `#00A86B` / `#10B981` | `#D9DCE0` / `#C2C6CC` / `#A9AEB5` |
| Pastilles des indicateurs | `#2A2A2A` / `#404040` / `#5A5A5A` | `#B53D6F` / `#E35491` / `#F06DAC` | `#2A7A63` / `#2DBA87` / `#3CC99A` | `#BFC3C9` / `#A9AEB5` / `#91969E` |
| Texte des indicateurs | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` | `#0B0C0E` |

## Conseils par style

* **Noir et blanc** : les photos sont en noir et blanc ; gardez les icônes noires (`#111111`) et un seul trait noir sous l'en-tête.
* **Rose et blanc** : le rouge de « Supprimer » est plus foncé (`#B91C1C`) pour ne pas se confondre avec le rose.
* **Vert jade et blanc** : le vert jade `#00A86B` sert aux boutons et icônes, le vert forêt `#064E3B` au menu.
* **Argenté et noir** : c'est un thème sombre. Dans Access, mettez le fond de **chaque section** (Détail, En-tête) en
  `#0B0C0E`, les cartes en `#16181B`, et pour les zones de texte `Couleur fond` `#1F2226` et `Couleur texte` `#F1F2F4`.
  Le bouton principal est argenté avec un texte noir. Les indicateurs sont argentés, avec un texte et des icônes noirs.
  La barre de titre sombre de la maquette correspond au mode sombre de Windows (*Paramètres › Couleurs*) : elle ne se règle pas dans Access.

Pour régénérer un seul style : `python3 outils/generer.py rose-blanc` (voir `../README.md`).
