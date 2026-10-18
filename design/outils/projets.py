"""Prépare les 4 projets « camarades » : couleur.md, LISEZMOI.md et un zip téléchargeable par projet.

Usage (après generer.py) : python3 outils/projets.py
Sorties : design/styles/<style>/couleur.md, design/styles/<style>/LISEZMOI.md, design/styles/README.md
          et projets/<NOM>-<style>.zip à la racine du dépôt.
"""
import glob
import json
import os
import zipfile
from pathlib import Path

from themes import THEMES

ICI = Path(__file__).resolve().parent
DESIGN = ICI.parent
RACINE = DESIGN.parent

DESIGNS = {
    "a": {
        "nom": "Éditorial",
        "resume": "Menu en barre noire en haut, grand bandeau photo noir et blanc, gros chiffres à empattements "
                  "(style magazine), boutons carrés en majuscules. Fiches : liste à gauche, fiche à droite.",
        "polices": "Segoe UI pour les contrôles ; **Georgia** pour les grands titres, les chiffres des indicateurs et le montant.",
        "guide": [
            "Formulaire de navigation, disposition **« Onglets horizontaux »**. Barre : Rectangle couleur *Menu* de 1,69 cm de haut.",
            "Boutons de navigation : fond couleur *Menu*, texte couleur *Texte du menu* en Segoe UI 9 pt **majuscules**, sans bordure ; "
            "onglet actif : texte blanc gras et un trait blanc de 3 pt dessous (petit rectangle blanc).",
            "Bandeau : contrôle Image `assets/photos/a-bandeau-<page>.jpg` (41,49 × 3,97 cm) en haut du sous-formulaire. "
            "Titre en **Georgia** 28 pt blanc, sous-titre en majuscules 9 pt.",
            "Cartes : Rectangle blanc, bordure couleur *Bordure des cartes*, et un rectangle noir de 0,08 cm collé en haut (le filet). "
            "Titres en majuscules 9 pt, gras.",
            "Les grands chiffres (indicateurs, montant) sont en Georgia 28 pt.",
            "Connexion : photo `a-connexion.jpg` sur tout le formulaire, carte blanche à droite, logo complet `assets/logo-connexion.png` (voir « Logos » plus haut).",
        ],
    },
    "b": {
        "nom": "Rail d'icônes",
        "resume": "Menu étroit à gauche (icône + petit libellé), panneau photo vertical à droite avec un grand chiffre, "
                  "boutons arrondis, cartes avec une barre colorée à gauche. Fiches : fiche en haut, liste dessous.",
        "polices": "Segoe UI partout (titres de page 16 pt semi-gras, grand chiffre du panneau 40 pt).",
        "guide": [
            "Formulaire de navigation **« Onglets verticaux, à gauche »**, réduit à 2,75 cm de large. Boutons de navigation : "
            "`Disposition image légende` **Haut** (icône au-dessus du texte), Segoe UI 9 pt, `Forme` **Rectangle arrondi** ; "
            "onglet actif : fond blanc, texte couleur *Onglet actif (texte)*.",
            "Panneau photo : contrôle Image `assets/photos/b-panneau-<page>.jpg` (8,47 × 18,84 cm) collé à droite. Par-dessus, une zone "
            "de texte transparente pour le grand chiffre (40 pt blanc), par exemple `=CpteDom(\"*\";\"Client\")`.",
            "Cartes : Rectangle blanc, bordure couleur *Bordure des cartes*, et un rectangle couleur *Accent* de 0,11 cm sur le bord gauche.",
            "Boutons : `Forme` **Rectangle arrondi** (Enregistrer, Supprimer, Se connecter) ou **Ovale** (petits boutons).",
            "Connexion : formulaire vertical de 12,70 × 16,40 cm, photo `b-connexion.jpg` en haut, logo complet `assets/logo-connexion.png` (carré blanc, icône et nom TIFFANY CAR en une image).",
        ],
    },
    "c": {
        "nom": "Menu photo à droite",
        "resume": "Menu à droite posé sur une photo qui change à chaque page, pas d'en-tête, libellés au-dessus des champs, "
                  "blocs de couleur pleins. Connexion avec les champs sur une seule ligne.",
        "polices": "Segoe UI partout (titre de page 22 pt, étiquettes 9,5 pt au-dessus des champs).",
        "guide": [
            "Formulaire de navigation **« Onglets verticaux, à droite »** (6,88 cm). Derrière les boutons, l'image "
            "`assets/photos/c-menu-<page>.jpg` (6,88 × 20,74 cm). Boutons de navigation : `Style fond` **Transparent**, texte blanc ; "
            "onglet actif : fond blanc, texte couleur *Onglet actif (texte)*.",
            "Pas d'en-tête : le titre (22 pt, couleur *Titres*) et le sous-titre sont dans chaque sous-formulaire.",
            "Champs : étiquette **au-dessus** de la zone de texte (étiquette 9,5 pt, puis le champ 0,53 cm plus bas).",
            "Cartes : Rectangle couleur *Bande / fond des cartes* sans bordure.",
            "Connexion : photo `c-connexion.jpg` en haut (23,28 × 7,94 cm), champs et bouton alignés sur une ligne dessous, logo complet `assets/logo-connexion.png` (blanc) sur la photo.",
        ],
    },
    "d": {
        "nom": "Cockpit",
        "resume": "Photo de voiture en fond de toute l'application, onglets en pastilles centrés en haut, cartes anthracite, "
                  "indicateurs argentés empilés. Connexion : carte centrée sur une photo sombre.",
        "polices": "Segoe UI partout ; titres de cartes en majuscules 9,5 pt espacées.",
        "guide": [
            "Formulaire de navigation **« Onglets horizontaux »**. Propriété **`Image`** du formulaire Menu : "
            "`assets/photos/d-fond-<page>.jpg` (41,49 × 20,74 cm), `Mode affichage image` **Découpage**. Dans chaque sous-formulaire, "
            "`Style fond` des sections : **Transparent**, ou la même image en fond.",
            "Boutons de navigation : `Forme` **Rectangle arrondi** (pastille), `Style fond` Transparent, texte couleur *Texte du menu* ; "
            "onglet actif : fond couleur *Onglet actif (fond)*, texte noir.",
            "Cartes : Rectangle couleur *Cartes (fond)*, bordure couleur *Bordure des cartes*, titres en majuscules 9,5 pt, "
            "petit trait couleur *Accent* de 1,06 cm sous le titre.",
            "Indicateurs et montant : Rectangles argentés (couleurs *Indicateurs*), texte et icônes noirs.",
            "Connexion : propriété **`Image`** du formulaire de connexion = `assets/photos/d-connexion.jpg`, carte centrée "
            "(Rectangle couleur *Cartes (fond)*), logo complet `assets/logo-connexion.png` (icône et nom en une image).",
            "La barre de titre sombre correspond au mode sombre de Windows : elle ne se règle pas dans Access.",
        ],
    },
    "e": {
        "nom": "Prestige futuriste",
        "resume": "Maquette spéciale **bleu royal `#002366` et noir**, rehaussée d'or, d'argent et de blanc, inspirée des écrans de bord "
                  "des voitures de luxe : police **Bahnschrift**, grands chiffres fins, cartes numérotées (01, 02…), jauge d'occupation, "
                  "voiture phare en photo sur le tableau de bord, barre de progression de la location, onglets en pastilles centrés "
                  "(comme argenté-noir). Connexion en deux panneaux (photo | formulaire).",
        "polices": "**Bahnschrift** (installée avec Windows 10 et 11) pour les titres, le menu, les chiffres et les petits libellés en "
                   "majuscules : *Bahnschrift SemiBold* (titres), *Bahnschrift Light* (grands chiffres), *Bahnschrift* (menu). "
                   "**Segoe UI** pour les champs, listes et textes courants. Les petits libellés dorés ou argentés sont en majuscules 9 pt.",
        "guide": [
            "Formulaire de navigation **« Onglets horizontaux »**. Barre : Rectangle noir `#000000` de 41,49 × 1,69 cm, puis un **trait doré** "
            "`#C9A24B` de 1 pt sur toute la largeur juste dessous. Logo à gauche : `assets/logo-menu.png`.",
            "Boutons de navigation : `Forme` **Rectangle arrondi** (pastille), police **Bahnschrift 11 pt**, `Style fond` Transparent, texte et icône argentés `#C4CAD3` ; "
            "onglet actif : fond **bleu royal `#002366`**, bordure `#2A55B8`, texte et icône blancs, gras.",
            "À droite de la barre : avatar (bouton `Forme` **Ovale** `#002366`, bordure dorée 2 pt), nom et rôle de l'utilisateur, puis le bouton "
            "**Se déconnecter** : `Forme` **Rectangle arrondi** de 3,65 × 0,90 cm, fond `#0A1838`, bordure `#2A55B8`, texte blanc Bahnschrift 10,5 pt, "
            "image `log-out` dorée à gauche du texte (`Disposition image légende` **Gauche**). Dans `Sur clic` : fermer le formulaire Menu et rouvrir le formulaire de connexion "
            "(`DoCmd.Close acForm, Me.Name` puis `DoCmd.OpenForm \"Connexion\"`).",
            "Cartes : Rectangle `#06112A`, bordure `#13284F`. Titre en **Bahnschrift SemiBold 11 pt majuscules**, précédé du **numéro doré** "
            "(01, 02…, Bahnschrift Light). Sous le titre : un trait `#13284F` sur toute la largeur et un petit trait doré de 1,06 cm × 2 pt à gauche.",
            "Tableau de bord : pas de bandeau, mais un en-tête *Bonjour, admin* (Bahnschrift SemiBold 28 pt) et l'heure en grand à droite "
            "(Bahnschrift Light 26 pt, `=Format(Maintenant();\"hh:nn\")`).",
            "Voiture phare : contrôle Image `assets/photos/e-vedette.jpg` (10,53 × 6,56 cm) dans la carte, à droite ; les caractéristiques à gauche "
            "viennent de la table Voiture (Puissance, CoutParJour, Annee).",
            "Jauge d'occupation : contrôle Image `assets/jauges/jauge-015.png` (3,97 × 3,97 cm) et une zone de texte transparente au centre pour le taux. "
            "Les 21 images `jauge-000.png` à `jauge-100.png` (pas de 5 %) permettent d'animer la jauge en VBA dans `Form_Load` : "
            "`Me.Image_Jauge.Picture = CurrentProject.Path & \"\\assets\\jauges\\jauge-\" & Format(Round(taux / 5) * 5, \"000\") & \".png\"`.",
            "Indicateurs : le chiffre d'affaires sur fond **bleu royal `#002366`** (bordure `#2A55B8`) ; les autres sur fond carte avec un petit trait doré en haut. "
            "Chiffres en Bahnschrift Light 26 pt blancs, icône dorée en haut à droite.",
            "Flotte par carburant et durée de la location : rectangles fins (piste + barre). Largeur de la barre en VBA, par exemple "
            "`Me.Barre_Essence.Width = Me.Piste_Essence.Width * n / 60`.",
            "Pages : bandeau `assets/photos/e-bandeau-<page>.jpg` (41,49 × 3,28 cm) sous le trait doré, sur-titre doré espacé, titre Bahnschrift SemiBold 28 pt, "
            "date dans un petit cadre noir à droite.",
            "Fiches : liste à gauche avec la zone **Rechercher…** (filtre) dans la bande de titre ; fiche à droite (12,70 cm), champs tous les 1,16 cm. "
            "Sur Marques, Carburants et Modèles, la photo `e-vignette-<page>.jpg` complète la colonne avec un grand chiffre.",
            "Réservations : cartes 01 Client et 02 Voiture, carte du **montant en doré sur bleu royal** avec la barre de progression de la location, "
            "puis 03 Réservation sur une ligne et 04 Liste.",
            "Connexion : formulaire de 26,46 × 14,82 cm. À gauche, `assets/photos/e-connexion.jpg` (14,82 × 14,82 cm) avec le slogan en haut ; trait doré vertical ; "
            "à droite sur fond `#01040B` : `assets/logo-connexion.png`, titre Bahnschrift, libellés en majuscules, bouton bleu royal **SE CONNECTER**.",
            "**Logo AURION** (dossier `assets/marque/`) : `aurion-menu.png` (barre du menu, 5,66 × 1,38 cm), `aurion-connexion.png` "
            "(connexion, 6,61 × 3,10 cm), `aurion-logo-hd.png` et `aurion-embleme-hd.png` en grand format (états imprimés, page de garde), "
            "et **`aurion.ico`** pour l'icône de l'application : *Fichier › Options › Base de données active › Icône de l'application*, "
            "cocher *Utiliser comme icône de formulaire et d'état*. Tous les PNG sont transparents, prévus pour un fond foncé.",
            "**Icônes exclusives AURION, modèle Médaillon** : chaque icône est un mini-emblème assorti au logo (disque bleu royal, liseré doré, "
            "halo bleu, dessin or et argent à angles coupés). Tableau de bord = compteur de vitesse, Marques = écusson, Voitures = supercar de profil. "
            "Menu : images de 0,58 cm (22 px) ; indicateurs du tableau de bord : 0,79 cm (30 px). PNG transparents dans `assets/` "
            "(voir `apercu-icones.png`), utilisés par aucun autre projet.",
            "La barre de titre sombre correspond au mode sombre de Windows : elle ne se règle pas dans Access.",
        ],
    },
}

ROLES = [  # (clé css, élément, où le saisir dans Access)
    ("menu", "Menu / barre de navigation", "Rectangle du menu : *Couleur fond*"),
    ("nav-txt", "Texte du menu", "Boutons de navigation : *Couleur texte*"),
    ("nav-actif-fond", "Onglet actif (fond)", "Bouton de navigation : *Couleur appuyé* (et *Couleur pointage*)"),
    ("nav-actif-txt", "Onglet actif (texte)", "Bouton de navigation : *Couleur texte appuyé*"),
    ("fond", "Fond des formulaires", "Section Détail : *Couleur fond*"),
    ("surface", "Cartes (fond)", "Rectangle de la carte : *Couleur fond*"),
    ("carte-bordure", "Bordure des cartes", "Rectangle de la carte : *Couleur bordure*"),
    ("bande", "Bande / fond des cartes", "Bande de titre des cartes (ou fond des cartes du design 3)"),
    ("titre", "Titres", "Étiquettes de titre : *Couleur texte*"),
    ("accent", "Accent (bouton principal, avatar, filets)", "Bouton Enregistrer / Se connecter : *Couleur fond*"),
    ("accent-txt", "Texte du bouton principal", "Bouton principal : *Couleur texte*"),
    ("btn-bordure", "Bordure des petits boutons", "Boutons d'outils : *Couleur bordure*"),
    ("etiq", "Étiquettes", "Étiquettes des champs : *Couleur texte*"),
    ("champ", "Zones de texte (fond)", "Zones de texte / listes déroulantes : *Couleur fond*"),
    ("champ-bordure", "Zones de texte (bordure)", "Zones de texte : *Couleur bordure*"),
    ("texte", "Texte saisi", "Zones de texte : *Couleur texte*"),
    ("lecture", "Champ en lecture seule (fond)", "Téléphone, Email, Modèle, Durée… : *Couleur fond*"),
    ("lecture-txt", "Champ en lecture seule (texte)", "Mêmes champs : *Couleur texte*"),
    ("montant", "Montant (fond)", "Zone de texte Montant : *Couleur fond*"),
    ("montant-txt", "Montant (texte)", "Zone de texte Montant : *Couleur texte*"),
    ("liste-bordure", "Zones de liste (bordure)", "Zones de liste : *Couleur bordure*"),
    ("gris", "Textes secondaires", "Sous-titres, compteurs (« 25 réservations ») : *Couleur texte*"),
    ("danger", "Bouton Supprimer (texte)", "Bouton Supprimer : *Couleur texte*"),
    ("danger-bordure", "Bouton Supprimer (bordure)", "Bouton Supprimer : *Couleur bordure*"),
]


def cm(px):
    return f"{px / 37.795:.2f}".replace(".", ",")


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def couleur_md(t):
    d = DESIGNS[t["design"]]
    c = t["css"]
    L = [f"# Couleurs · {t['societe']}", "",
         f"Projet **{t['societe']}** · design **{d['nom']}** · couleurs **{t['nom'].lower()}**.", "",
         "## Comment saisir une couleur dans Access", "",
         "1. Sélectionner le contrôle, ouvrir la **Feuille de propriétés** (F4), onglet **Format**.",
         "2. Dans *Couleur fond*, *Couleur texte* ou *Couleur bordure*, taper directement le code **`#RRVVBB`** "
         "(exemple : `" + c["accent"] + "`) puis Entrée.",
         "3. Ou cliquer sur **…** › **Autres couleurs** › onglet *Personnalisées* et saisir Rouge, Vert, Bleu (colonne RVB).", "",
         "## Palette principale", "",
         "| Rôle | Code | RVB |", "|---|---|---|"]
    vus = []
    for k, lib in [("menu", "Couleur de la marque (menu)"), ("accent", "Accent"), ("titre", "Titres"), ("fond", "Fond"),
                   ("surface", "Cartes"), ("texte", "Texte"), ("or", "Or (filets, icônes, sur-titres, montant)"),
                   ("or-clair", "Or clair (chiffres en doré)"), ("argent", "Argent (menu, textes secondaires)"),
                   ("royal-bordure", "Bordure des éléments bleu royal"), ("royal-clair", "Bleu royal clair (barre Électrique)")]:
        if k not in c:
            continue
        L.append(f"| {lib} | `{c[k]}` | {', '.join(map(str, rgb(c[k])))} |")
        vus.append(c[k])
    L += ["", "## Couleur de chaque élément", "", "| Élément | Code | RVB | Où le saisir |", "|---|---|---|---|"]
    for k, lib, ou in ROLES:
        v = c[k]
        r = ", ".join(map(str, rgb(v))) if v.startswith("#") else "–"
        L.append(f"| {lib} | `{v}` | {r} | {ou} |")
    L += ["", "## Indicateurs du tableau de bord", "", "| Indicateur | Fond | Pastille de l'icône | Texte |", "|---|---|---|---|"]
    txt = "#0B0C0E (noir)" if t["design"] == "d" else "#FFFFFF (blanc)"
    for (fond, past), lib in zip(t["kpi"], ["Chiffre d'affaires", "Voitures", "Clients", "Meilleur client"]):
        L.append(f"| {lib} | `{fond}` ({', '.join(map(str, rgb(fond)))}) | `{past}` | `{txt}` |")
    v = t["voile"]
    L += ["", "## Photos", "",
          f"Les photos de `assets/photos/` sont déjà recadrées et teintées (voile `#{v[0]:02X}{v[1]:02X}{v[2]:02X}`"
          + (", noir et blanc" if "grayscale" in t.get("photo_filtre", "") else "")
          + ") : il suffit de les insérer avec un contrôle **Image**, ou en propriété **Image** du formulaire.",
          "", "## Polices", "", d["polices"], ""]
    return "\n".join(L)


def lisezmoi(t, num):
    d = DESIGNS[t["design"]]
    L = [f"# {t['societe']} · maquettes Access", "",
         f"Design **{num}. {d['nom']}** · couleurs **{t['nom'].lower()}** · application de location de voitures de prestige à Libreville.", "",
         d["resume"], "",
         "## Logos (une seule image à insérer)", "",
         "Le logo complet de l'entreprise (icône **et** nom, bonne police, bonnes couleurs) est déjà prêt en PNG transparent. "
         "Dans Access : **Créer › Contrôle Image**, choisir le fichier, `Mode affichage image` **Découpage**, puis saisir la position :", "",
         "| Fichier | Formulaire | Gauche | Haut | Largeur | Hauteur |", "|---|---|---:|---:|---:|---:|"]
    import json
    lg = json.loads((DESIGN / t["dossier"] / "logos.json").read_text())
    for ou, lib in [("connexion", "Connexion"), ("menu", "Menu")]:
        p = lg[ou]
        L.append(f"| `assets/logo-{ou}.png` | {lib} | {cm(p['x'])} | {cm(p['y'])} | {cm(p['w'])} | {cm(p['h'])} |")
    fe = DESIGN / t["dossier"] / "etats.json"
    if fe.exists():
        L += ["", "## États (impressions)", "",
              "Chaque bouton **Imprimer** ouvre un état A4 : aperçus dans `etats/png/`, sections et contrôles en cm dans **`ETATS.md`**.", "",
              "| Aperçu | État | Bouton Imprimer |", "|---|---|---|"]
        for x in json.loads(fe.read_text()):
            L.append(f"| `{x['png']}` | **{x['nom']}** ({x['titre']}) | {x['bouton']} |")
    L += ["", "Aperçu des logos et de toutes les icônes : `apercu-icones.png`. Liste détaillée : `ICONES.md`.", "",
         "## Contenu du dossier", "",
         "| Fichier | Rôle |", "|---|---|",
         "| `png/` | Les 8 écrans à reproduire : connexion, tableau de bord, réservations, clients, voitures, marques, carburants, modèles |",
         "| `couleur.md` | **Toutes les couleurs** (codes à saisir dans Access) |",
         ] + (["| `etats/png/` et `ETATS.md` | Les **états** (impressions) ouverts par les boutons Imprimer, avec leurs cotes |"] if fe.exists() else []) + [
         "| `COTES.md` | Position et taille de chaque contrôle, en centimètres |",
         "| `ICONES.md` | **Liste de toutes les icônes** : fichier, taille, couleur, contrôle et écran où la mettre |",
         "| `apercu-icones.png` | Aperçu de toutes les icônes (les icônes blanches sont montrées sur fond foncé) |",
         "| `assets/` | Les icônes en PNG transparent, à la taille exacte (logo de la connexion et du menu compris)"
         + (", et `jauges/` : les 21 images de la jauge" if t["design"] == "e" else "") + " |",
         "| `assets/photos/` | Les 8 photos de voitures de ce projet, déjà recadrées à la taille exacte |", "",
         "> Les icônes **blanches** paraissent vides dans l'explorateur Windows (blanc sur blanc) : elles sont bien là, "
         "voir `apercu-icones.png`.", "",
         "## Réaliser ce design dans Access", ""]
    L += [f"* {x}" for x in d["guide"]]
    L += ["", "Règles communes : police **Segoe UI**, zones de texte avec bordure fine sur tout le tour, "
          "étiquettes sans bordure, `Effet spécial` **Plat** partout.", ""]
    return "\n".join(L)


def verifier(zp, nom, dos):
    """Contrôle du zip : écrans, photos et icônes utilisés par chaque écran, fichiers d'aide."""
    import re
    z = zipfile.ZipFile(zp)
    assert z.testzip() is None, "zip corrompu"
    dedans = {n[len(nom) + 1:] for n in z.namelist()}
    attendu = {"LISEZMOI.md", "couleur.md", "COTES.md", "ICONES.md", "apercu-icones.png", "assets/logo-connexion.png", "assets/logo-menu.png"}
    for h in sorted((dos / "etats").glob("*.html")) if (dos / "etats").exists() else []:
        attendu |= {f"etats/png/{h.stem}.png", "ETATS.md"}
        attendu |= {f"assets/{r}" for r in re.findall(r'src="\.\./assets/([^"]+)"', h.read_text())}
    for h in sorted(dos.glob("0*.html")):
        attendu.add(f"png/{h.stem}.png")
        attendu |= {f"assets/{r}" for r in re.findall(r'(?:src="|url\(["\']?)assets/([^"\')]+)', h.read_text())}
    attendu |= {f"assets/{f}" for f in re.findall(r"^\| `([^`]+\.png)`", (dos / "ICONES.md").read_text(), re.M)}
    manque = sorted(attendu - dedans)
    if manque:
        raise SystemExit(f"{zp.name} : il manque {manque}")
    n_ico = sum(1 for f in dedans if f.startswith("assets/") and f.endswith(".png"))
    n_ph = sum(1 for f in dedans if f.startswith("assets/photos/"))
    n_ecr = sum(1 for f in dedans if f.startswith("png/"))
    n_et = sum(1 for f in dedans if f.startswith("etats/png/"))
    return f"contrôle OK : {n_ecr} écrans, {n_et} états, {n_ph} photos, {n_ico} icônes, rien ne manque"


def main():
    styles = [t for t in THEMES if t["design"] != "bleu"]
    (RACINE / "projets").mkdir(exist_ok=True)
    for num, t in enumerate(styles, 1):
        dos = DESIGN / t["dossier"]
        (dos / "couleur.md").write_text(couleur_md(t))
        (dos / "LISEZMOI.md").write_text(lisezmoi(t, num))
        nom = f"{t['societe'].replace(' ', '-')}-{t['cle']}"
        out = RACINE / "projets" / f"{nom}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            extra = (["ETATS.md"] + sorted(os.path.relpath(f, dos) for f in glob.glob(str(dos / "etats" / "png" / "*.png")))
                     if (dos / "ETATS.md").exists() else [])
            fic = ["LISEZMOI.md", "couleur.md", "COTES.md", "ICONES.md", "apercu-icones.png"] + extra + sorted(
                os.path.relpath(f, dos) for f in glob.glob(str(dos / "png" / "*.png")) + glob.glob(str(dos / "assets" / "**" / "*.*"), recursive=True))
            for f in fic:
                z.write(dos / f, f"{nom}/{f}")
        print(out.name, len(fic), "fichiers", out.stat().st_size // 1024, "Ko", "·", verifier(out, nom, dos))


if __name__ == "__main__":
    main()
