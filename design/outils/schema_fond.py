"""Platinum Drive : schéma « une photo pour le menu et le sous-formulaire » + guide FOND-NAVIGATION.md.

Usage (après generer.py argente-noir) : LD_LIBRARY_PATH=/tmp/al/lib python3 outils/schema_fond.py
"""
import json
import subprocess
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
DOS = ICI.parent / "styles" / "argente-noir"
FONTS = (ICI.parent / "maquettes" / "fonts").as_uri()
W, H, TETE, BARRE = 1568, 784, 72, 24          # formulaire Menu, hauteur de la barre de navigation, barre de titre Windows
CM = 37.795
PAGES = [("tableau", "Frm_Tableau", "Tableau de bord"), ("reservations", "Frm_Reservations", "Réservations"),
         ("clients", "Frm_Clients", "Clients"), ("voitures", "Frm_Voitures", "Voitures"), ("marques", "Frm_Marques", "Marques"),
         ("carburants", "Frm_Carburants", "Carburants"), ("modeles", "Frm_Modeles", "Modèles")]


def cm(px, n=2):
    return f"{px / CM:.{n}f}".replace(".", ",")


VBA_MODULE = """' Module du formulaire Menu (Création > Afficher le code)
Private Sub FondMenu(page As String)
    Me.Picture = CurrentProject.Path & "\\assets\\photos\\d-fond-" & page & ".jpg"
End Sub

Private Sub Form_Load()
    FondMenu "tableau"            ' page affichée à l'ouverture
End Sub

Private Sub BoutonNavigation_tableau_Click()
    FondMenu "tableau"
End Sub

Private Sub BoutonNavigation_clients_Click()
    FondMenu "clients"
End Sub"""

VBA_FORM = """' Pages : AUCUN code. Image fixe dans la feuille de propriétés :
'   Frm_Clients  > Image = d-corps-clients.jpg  (Type d'image : Incorporé)
'   Frm_Voitures > Image = d-corps-voitures.jpg ..."""


def schema():
    ecran = (DOS / "png" / "01-tableau-de-bord.png").as_uri()
    fond = (DOS / "assets" / "photos" / "d-fond-tableau.jpg").as_uri()
    corps = (DOS / "assets" / "photos" / "d-corps-tableau.jpg").as_uri()
    ecran2 = (DOS / "png" / "03-clients.png").as_uri()
    k = 1000 / W                                   # échelle de la capture
    y1, y2 = BARRE * k, (BARRE + TETE) * k
    hs = (H + BARRE) * k
    kt = 420 / W                                   # échelle des vignettes
    code = (VBA_MODULE + "\n\n" + VBA_FORM).replace("&", "&amp;").replace("<", "&lt;")
    h = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: UI; font-weight: 400; src: url({FONTS}/open-sans-latin-400-normal.woff2); }}
@font-face {{ font-family: UI; font-weight: 600; src: url({FONTS}/open-sans-latin-600-normal.woff2); }}
html, body {{ margin: 0; }}
#a {{ width: 1520px; padding: 28px 32px 30px; background: #0E0F11; color: #E8EAED; font-family: UI, sans-serif; box-sizing: border-box; }}
h1 {{ margin: 0; font-size: 26px; font-weight: 600; letter-spacing: 1px; }}
.s {{ color: #9AA0A8; font-size: 15px; margin: 6px 0 22px; }}
.rang {{ display: flex; gap: 32px; }}
.cap {{ position: relative; width: 1000px; }}
.pa {{ position: absolute; box-shadow: 0 0 0 3px #0E0F11; }}
.leg {{ margin-top: 16px; font-size: 15px; line-height: 34px; }}
.cap img {{ width: 1000px; display: block; }}
.z {{ position: absolute; left: -3px; width: 1000px; box-sizing: border-box; }}
.n {{ display: inline-flex; width: 26px; height: 26px; border-radius: 13px; align-items: center; justify-content: center; font-weight: 600; font-size: 15px; margin-right: 8px; color: #0E0F11; }}
.et {{ position: absolute; font-size: 14px; padding: 6px 10px; background: rgba(14,15,17,.92); white-space: nowrap; }}
.col {{ width: 420px; font-size: 14px; color: #C9CDD2; }}
.col h2 {{ font-size: 16px; margin: 0 0 10px; color: #FFFFFF; font-weight: 600; }}
.vig {{ position: relative; width: 420px; }}
.vig img {{ display: block; width: 420px; }}
.lbl {{ font-size: 13px; color: #9AA0A8; margin: 6px 0 14px; }}
pre {{ margin: 22px 0 0; padding: 16px 20px; background: #16181B; border: 1px solid #2A2D31; font: 13px/1.5 Consolas, "DejaVu Sans Mono", monospace; color: #DADDE1; white-space: pre; }}
.or {{ color: #E3C77A; }} .bl {{ color: #7FC4FF; }}
</style></head><body><div id="a">
<h1>PLATINUM DRIVE · une seule photo derrière le menu <span class="or">et</span> le sous-formulaire</h1>
<div class="s">Access ne sait pas rendre un sous-formulaire transparent : on coupe donc la photo en deux morceaux exactement alignés.</div>
<div class="rang">
 <div class="cap"><img src="{ecran}">
  <div class="z" style="top:{y1:.1f}px;height:{y2 - y1:.1f}px;border:3px solid #E3C77A"></div>
  <div class="z" style="top:{y2:.1f}px;height:{hs - y2:.1f}px;border:3px dashed #7FC4FF"></div>
  <div class="n pa" style="left:890px;top:{(y1 + y2) / 2 - 13:.0f}px;background:#E3C77A">1</div>
  <div class="n pa" style="left:-15px;top:{y2 + 14:.0f}px;background:#7FC4FF">2</div>
  <div class="n pa" style="left:470px;top:{(y2 + hs) / 2 - 13:.0f}px;background:#7FC4FF;width:34px;height:34px;border-radius:17px;font-size:18px">3</div>
  <div class="leg">
   <div><span class="n" style="background:#E3C77A">1</span>Formulaire <b>Menu</b> · Image = <b class="or">d-fond-&lt;page&gt;.jpg</b> (photo complète, 41,49 × 20,74 cm) · on n'en voit que la bande des onglets</div>
   <div><span class="n" style="background:#7FC4FF">2</span>Contrôle <b>sous-formulaire</b> : Gauche 0 · Haut <b>1,905 cm</b> · 41,49 × 18,84 cm · Style bordure Transparent</div>
   <div><span class="n" style="background:#7FC4FF">3</span>Formulaire de la page (Frm_Tableau, Frm_Clients…) · Image = <b class="bl">d-corps-&lt;page&gt;.jpg</b> (bas de la même photo, 41,49 × 18,84 cm)</div>
  </div>
 </div>
 <div class="col">
  <h2>Comment la photo est coupée</h2>
  <div class="vig"><img src="{fond}"><div style="position:absolute;left:0;top:{TETE * kt:.1f}px;width:420px;border-top:2px dashed #E3C77A"></div>
   <div style="position:absolute;right:6px;top:{TETE * kt + 4:.0f}px;font-size:12px;color:#E3C77A">coupe à 1,905 cm</div></div>
  <div class="lbl"><b class="or">d-fond-tableau.jpg</b> · photo complète → formulaire Menu</div>
  <div class="vig" style="margin-left:0"><img src="{corps}"></div>
  <div class="lbl"><b class="bl">d-corps-tableau.jpg</b> · tout ce qui est sous la ligne → sous-formulaire</div>
  <h2 style="margin-top:6px">Les réglages qui comptent</h2>
  <div>• <b>Pages</b> : image <b class="bl">d-corps</b> FIXE (Incorporé) → elle change toute seule avec la page.<br>
  • <b>Menu</b> : image <b class="or">d-fond</b> changée par le clic de chaque bouton de navigation.<br>
  • Les deux en <b>Étirer</b> ; sous-formulaire au <b>Haut 1,905 cm</b>, sans bordure.<br>
  • VBA activé : bandeau jaune → <b>Activer le contenu</b>.</div>
 </div>
</div>
<h2 style="font-size:18px;margin:26px 0 12px;color:#FFFFFF">Quand on clique sur l'onglet « Clients »</h2>
<div style="display:flex;align-items:center;gap:22px">
 <div><img src="{ecran}" style="width:600px;display:block"><div class="lbl">Avant : page Tableau de bord</div></div>
 <div style="font-size:14px;line-height:1.7;width:240px;color:#C9CDD2"><b class="or">① le clic</b> exécute <code>FondMenu "clients"</code> :
  le Menu prend <b class="or">d-fond-clients.jpg</b><br><br><b class="bl">② Access charge Frm_Clients</b>, qui arrive avec
  <b class="bl">d-corps-clients.jpg</b> (aucun code)<div style="font-size:40px;color:#E3C77A;text-align:center">→</div></div>
 <div><img src="{ecran2}" style="width:600px;display:block"><div class="lbl">Après : page Clients, haut et bas de la même nouvelle photo</div></div>
</div>
<pre>{code}</pre>
</div></body></html>"""
    tmp = Path(tempfile.mkdtemp(prefix="schema-"))
    (tmp / "s.html").write_text(h)
    jf = tmp / "j.json"
    jf.write_text(json.dumps({"assets": [{"html": (tmp / "s.html").as_uri(), "out": str(DOS / "schema-fond-navigation.png"),
                                          "w": 1520, "h": 1900, "transparent": False, "sel": "#a"}], "ecrans": [], "cotes": str(tmp / "c.json")}))
    r = subprocess.run(["node", str(ICI / "rendre.mjs"), str(jf)], cwd=ICI)
    if r.returncode:
        raise SystemExit(r.returncode)


def guide():
    L = ["# Photo en fond du menu ET du sous-formulaire · PLATINUM DRIVE", "",
         "Schéma : **`schema-fond-navigation.png`**.", "",
         "## Pourquoi ça ne marche pas avec une seule image", "",
         "Dans Access, le contrôle sous-formulaire (le `NavigationSubform` du formulaire de navigation) **peint toujours son propre fond** : "
         "un formulaire ne peut pas être transparent. L'image du formulaire Menu est donc cachée partout où se trouve le sous-formulaire.", "",
         "**La solution** : couper la photo en deux morceaux **exactement alignés**. Le formulaire Menu garde la photo complète (on n'en voit que "
         "la bande des onglets) et chaque page affichée dans le sous-formulaire reçoit **le bas de la même photo**. À l'écran on voit une seule photo continue.", "",
         "## 1. Les images (déjà prêtes dans `assets/photos/`)", "",
         "| Page | Formulaire Menu (photo complète, 41,49 × 20,74 cm) | Formulaire de la page (bas de la photo, 41,49 × 18,84 cm) |",
         "|---|---|---|"]
    for k, f, t in PAGES:
        L.append(f"| {t} (`{f}`) | `d-fond-{k}.jpg` | `d-corps-{k}.jpg` |")
    L += ["", f"`d-corps-<page>.jpg` = `d-fond-<page>.jpg` coupée à **{cm(TETE, 3)} cm** du haut ({TETE} pixels) : c'est la hauteur de la barre des onglets.", "",
          "## 2. Formulaire Menu (formulaire de navigation)", "",
          "1. Mode Création, sélectionner tous les contrôles › onglet **Organiser** › **Supprimer la disposition**. "
          "Sans ça, Access place lui-même le sous-formulaire et on ne peut pas le régler au millimètre.",
          "2. Feuille de propriétés du **formulaire** :", "",
          "| Propriété | Valeur |", "|---|---|",
          f"| Largeur | **{cm(W)} cm** (hauteur totale des sections : **{cm(H)} cm**) |",
          "| Image | `assets\\photos\\d-fond-tableau.jpg` (remplacée ensuite par le code) |",
          "| Type d'image | **Lié** |",
          "| Mode d'affichage de l'image | **Étirer** |",
          "| Alignement de l'image | Coin supérieur gauche |",
          "| Mosaïque | Non |",
          "| Taille automatique | Oui |",
          "| Style bordure | **Fin** (la fenêtre garde sa taille, donc le raccord reste parfait) |",
          "| Boutons Min Max | Réduire seulement |",
          "| Barres de défilement / Sélecteur / Boutons de déplacement | Aucune / Non / Non |", "",
          "3. Contrôle de navigation (les onglets) : `Style fond` **Transparent**, `Style bordure` **Transparent**, positions dans `COTES.md` "
          "(lignes `BoutonNavigation_…`).",
          "4. Contrôle **sous-formulaire** (`NavigationSubform`, ligne `Sous_Formulaire` de `COTES.md`) :", "",
          "| Propriété | Valeur |", "|---|---|",
          "| Gauche | **0 cm** |",
          f"| Haut | **{cm(TETE, 3)} cm** (tapez bien les 3 décimales : c'est la ligne de coupe des images) |",
          f"| Largeur | **{cm(W)} cm** |",
          f"| Hauteur | **{cm(H - TETE, 3)} cm** |",
          "| Style bordure | **Transparent** |",
          "| Apparence (effet spécial) | Normal |", "",
          "## 3. Chaque formulaire de page : image FIXE, aucun code", "",
          "C'est ce qui règle le changement de page : **chaque page emporte son propre bas de photo**. Quand vous cliquez sur *Clients*, "
          "Access affiche `Frm_Clients` dans le sous-formulaire, et `Frm_Clients` arrive avec `d-corps-clients.jpg`. Rien à programmer.", "",
          "| Formulaire de page | Propriété `Image` (feuille de propriétés, onglet Format) |", "|---|---|"]
    for k, f, t in PAGES:
        L.append(f"| `{f}` | `d-corps-{k}.jpg` |")
    L += ["", "| Propriété (dans chaque page) | Valeur |", "|---|---|",
          f"| Largeur | **{cm(W)} cm** · hauteur du Détail **{cm(H - TETE, 3)} cm** |",
          "| En-tête / pied de formulaire | Supprimés (clic droit › décocher *En-tête/pied de formulaire*) |",
          "| Type d'image | **Incorporé** (l'image est enregistrée dans la base : elle marche même si le dossier bouge) |",
          "| Mode d'affichage de l'image | **Étirer** |",
          "| Alignement de l'image | Coin supérieur gauche |",
          "| Barres de défilement | **Aucune** |",
          "| Sélecteur d'enregistrement / Boutons de déplacement / Diviseurs | Non / Non / Non |", "",
          "Les cartes restent des Rectangles pleins posés **par-dessus** la photo. Ne mettez pas de grand Rectangle de fond : il cacherait la photo.", "",
          "## 4. Le formulaire Menu : l'image change à chaque clic", "",
          "Le haut de la photo est dans le formulaire Menu, qui reste ouvert : c'est **le seul endroit où il faut du code**. "
          "Chaque bouton de navigation remplace l'image du Menu par la photo de sa page.", "",
          "1. Nommez les boutons de navigation comme dans `COTES.md` : sélectionnez un bouton › propriété **Nom** "
          "(`BoutonNavigation_tableau`, `BoutonNavigation_clients`…).",
          "2. Formulaire Menu en mode Création › onglet **Création** › **Afficher le code**, puis collez tout ce code :", "", "```vba",
          "Option Compare Database", "Option Explicit", "",
          "' Change la photo du formulaire Menu (le haut, derrière les onglets)",
          "Private Sub FondMenu(page As String)",
          '    Me.Picture = CurrentProject.Path & "\\assets\\photos\\d-fond-" & page & ".jpg"',
          "End Sub", "",
          "Private Sub Form_Load()",
          '    FondMenu "tableau"            \' page affichée à l\'ouverture',
          "End Sub"]
    for k, f, t in PAGES:
        L += ["", f"Private Sub BoutonNavigation_{k}_Click()", f'    FondMenu "{k}"', "End Sub"]
    L += ["```", "",
          "3. Vérifiez que chaque bouton est bien relié : propriété **Sur clic** du bouton = `[Procédure événementielle]`. "
          "Si ce n'est pas le cas, cliquez sur `…` à côté de *Sur clic* › **Générateur de code** : Access relie la procédure.",
          "4. Les boutons gardent leur propriété **Nom du formulaire cible de navigation** (`Frm_Clients`…) : "
          "le code ne fait que changer la photo, la navigation reste celle d'Access.", "",
          "Ça marche aussi sans formulaire de navigation (formulaire Menu + contrôle sous-formulaire + boutons ordinaires) : "
          'ajoutez simplement `Me.Sous_Formulaire.SourceObject = "Frm_Clients"` dans le clic, à côté de `FondMenu "clients"`.', "",
          "## 5. Si la photo ne change pas quand on clique", "",
          "| Ce que vous voyez | Cause | Solution |", "|---|---|---|",
          "| Bandeau jaune *« Avertissement de sécurité : le contenu actif a été désactivé »* | Access bloque **tout** le VBA | "
          "Cliquez **Activer le contenu**, ou mieux : *Fichier › Options › Centre de gestion de la confidentialité › Paramètres › "
          "Emplacements approuvés* › ajoutez le dossier de la base |",
          "| Le bas change mais pas le haut | Le clic n'est pas relié au code | `Sur clic` = `[Procédure événementielle]` (étape 4.3) ; "
          "le **Nom** du bouton doit être exactement celui de la procédure |",
          "| Le haut change mais pas le bas | La page n'a pas sa propre image | Propriété `Image` du formulaire de page (section 3) |",
          "| Message « Impossible de trouver le fichier » | Mauvais dossier | Le dossier `assets` doit être à côté du fichier `.accdb` |",
          "| Trait fin ou cadre autour de la page | Bordure du sous-formulaire | `Style bordure` du contrôle sous-formulaire = **Transparent** |",
          f"| Photo décalée de quelques pixels | Mauvaise position | `Haut` du contrôle sous-formulaire = **{cm(TETE, 3)}**, `Gauche` = **0** |",
          "| Photo déformée | Mauvais mode | `Mode d'affichage de l'image` = **Étirer** partout, formulaire Menu à taille fixe |", ""]
    (DOS / "FOND-NAVIGATION.md").write_text("\n".join(L))


if __name__ == "__main__":
    guide()
    schema()
    print("FOND-NAVIGATION.md et schema-fond-navigation.png écrits")
