"""Prépare les 4 projets « camarades » : couleur.md, LISEZMOI.md et un zip téléchargeable par projet.

Usage (après generer.py) : python3 outils/projets.py
Sorties : design/styles/<style>/couleur.md, design/styles/<style>/LISEZMOI.md, design/styles/README.md
          et projets/<NOM>-<style>.zip à la racine du dépôt.
"""
import glob
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
            "Connexion : photo `a-connexion.jpg` sur tout le formulaire, carte blanche à droite.",
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
            "Connexion : formulaire vertical de 12,70 × 16,40 cm, photo `b-connexion.jpg` en haut, logo dans un bouton ovale.",
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
            "Connexion : photo `c-connexion.jpg` en haut (23,28 × 7,94 cm), champs et bouton alignés sur une ligne dessous.",
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
                   ("surface", "Cartes"), ("texte", "Texte")]:
        L.append(f"| {lib} | `{c[k]}` | {', '.join(map(str, rgb(c[k])))} |")
        vus.append(c[k])
    L += ["", "## Couleur de chaque élément", "", "| Élément | Code | RVB | Où le saisir |", "|---|---|---|---|"]
    for k, lib, ou in ROLES:
        v = c[k]
        r = ", ".join(map(str, rgb(v))) if v.startswith("#") else "–"
        L.append(f"| {lib} | `{v}` | {r} | {ou} |")
    L += ["", "## Indicateurs du tableau de bord", "", "| Indicateur | Fond | Pastille de l'icône | Texte |", "|---|---|---|---|"]
    txt = "#0B0C0E (noir)" if t["design"] == "d" else "#FFFFFF (blanc)"
    for (fond, past), lib in zip(t["kpi"], ["Chiffre d'affaires", "Voitures", "Clients"]):
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
         "## Contenu du dossier", "",
         "| Fichier | Rôle |", "|---|---|",
         "| `png/` | Les 8 écrans à reproduire : connexion, tableau de bord, réservations, clients, voitures, marques, carburants, modèles |",
         "| `couleur.md` | **Toutes les couleurs** (codes à saisir dans Access) |",
         "| `COTES.md` | Position et taille de chaque contrôle, en centimètres |",
         "| `assets/photos/` | Photos de voitures de ce projet, déjà recadrées |",
         "| `assets/` | Icônes (PNG) pour les boutons, les cartes et le menu |", "",
         "## Réaliser ce design dans Access", ""]
    L += [f"* {x}" for x in d["guide"]]
    L += ["", "Règles communes : police **Segoe UI**, zones de texte avec bordure fine sur tout le tour, "
          "étiquettes sans bordure, `Effet spécial` **Plat** partout.", ""]
    return "\n".join(L)


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
            fic = ["LISEZMOI.md", "couleur.md", "COTES.md"] + sorted(
                os.path.relpath(f, dos) for f in glob.glob(str(dos / "png" / "*.png")) + glob.glob(str(dos / "assets" / "**" / "*.*"), recursive=True))
            for f in fic:
                z.write(dos / f, f"{nom}/{f}")
        print(out.name, len(fic), "fichiers", out.stat().st_size // 1024, "Ko")


if __name__ == "__main__":
    main()
