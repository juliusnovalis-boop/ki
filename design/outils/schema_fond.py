"""Platinum Drive : photo de fond derrière le menu ET le sous-formulaire, SANS VBA (macros DéfinirPropriété).

Sorties : styles/argente-noir/FOND-NAVIGATION.md et schema-fond-navigation.png
Usage (après generer.py argente-noir) : LD_LIBRARY_PATH=/tmp/al/lib python3 outils/schema_fond.py
"""
import json
import subprocess
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
DOS = ICI.parent / "styles" / "argente-noir"
FONTS = (ICI.parent / "maquettes" / "fonts").as_uri()
W, H, TETE, BARRE = 1568, 784, 72, 24          # formulaire Menu, hauteur du bandeau des onglets, barre de titre Windows
CM = 37.795
PAGES = [("tableau", "Frm_Tableau", "Tableau de bord"), ("reservations", "Frm_Reservations", "Réservations"),
         ("clients", "Frm_Clients", "Clients"), ("voitures", "Frm_Voitures", "Voitures"), ("marques", "Frm_Marques", "Marques"),
         ("carburants", "Frm_Carburants", "Carburants"), ("modeles", "Frm_Modeles", "Modèles")]


def cm(px, n=2):
    return f"{px / CM:.{n}f}".replace(".", ",")


def photo(nom):
    return (DOS / "assets" / "photos" / nom).as_uri()


def macro_html(actif):
    """Macro incorporée telle qu'elle apparaît dans le Générateur de macro d'Access."""
    blocs = ""
    for k, _f, _t in PAGES:
        on = k == actif
        bord = "#2B579A" if on else "#C8C8C8"
        blocs += (f'<div class="act" style="border-color:{bord}{";background:#EAF1FB" if on else ""}">'
                  f'<div class="an">DéfinirPropriété</div>'
                  f'<div class="ar"><span>Nom du contrôle</span><i>Img_Fond_{k}</i></div>'
                  f'<div class="ar"><span>Propriété</span><i>Visible</i></div>'
                  f'<div class="ar"><span>Valeur</span><i style="{"font-weight:600;color:#2B579A" if on else ""}">{"-1" if on else "0"}</i></div></div>')
    return (f'<div class="mac"><div class="mt">Menu : BoutonNavigation_{actif} : Sur clic</div>{blocs}'
            f'<div class="add">+ Ajouter une nouvelle action</div></div>')


def schema():
    ecran = (DOS / "png" / "01-tableau-de-bord.png").as_uri()
    ecran2 = (DOS / "png" / "03-clients.png").as_uri()
    k = 1000 / W
    y1, y2 = BARRE * k, (BARRE + TETE) * k
    hs = (H + BARRE) * k
    pile = "".join(
        f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:6px">'
        f'<img src="{photo(f"d-tete-{p}.jpg")}" style="width:140px;height:26px;object-fit:cover;object-position:50% 100%;'
        f'filter:brightness(2.2);border:1px solid {"#E3C77A" if i == 0 else "#3A3D42"}">'
        f'<span style="font-size:13px;width:165px;white-space:nowrap">Img_Fond_{p}</span>'
        f'<span style="font-size:13px;white-space:nowrap;color:{"#E3C77A" if i == 0 else "#7D838C"}">Visible : {"Oui" if i == 0 else "Non"}</span></div>'
        for i, (p, _f, _t) in enumerate(PAGES))
    h = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: UI; font-weight: 400; src: local("Segoe UI"), url({FONTS}/open-sans-latin-400-normal.woff2); }}
@font-face {{ font-family: UI; font-weight: 600; src: local("Segoe UI Semibold"), url({FONTS}/open-sans-latin-600-normal.woff2); }}
html, body {{ margin: 0; }}
#a {{ width: 1520px; padding: 28px 32px 30px; background: #0E0F11; color: #E8EAED; font-family: UI, sans-serif; box-sizing: border-box; }}
h1 {{ margin: 0; font-size: 26px; font-weight: 600; letter-spacing: 1px; }}
h2 {{ font-size: 18px; margin: 0 0 12px; color: #FFFFFF; font-weight: 600; }}
.s {{ color: #9AA0A8; font-size: 15px; margin: 6px 0 22px; }}
.rang {{ display: flex; gap: 32px; }}
.cap {{ position: relative; width: 1000px; }}
.cap > img {{ width: 1000px; display: block; }}
.z {{ position: absolute; left: -3px; width: 1000px; box-sizing: border-box; }}
.n {{ display: inline-flex; width: 26px; height: 26px; border-radius: 13px; align-items: center; justify-content: center; font-weight: 600; font-size: 15px; margin-right: 8px; color: #0E0F11; }}
.pa {{ position: absolute; box-shadow: 0 0 0 3px #0E0F11; }}
.leg {{ margin-top: 16px; font-size: 15px; line-height: 34px; }}
.col {{ width: 420px; font-size: 14px; color: #C9CDD2; line-height: 1.6; }}
.lbl {{ font-size: 13px; color: #9AA0A8; margin: 6px 0 14px; }}
.or {{ color: #E3C77A; }} .bl {{ color: #7FC4FF; }}
.mac {{ width: 470px; background: #FFFFFF; color: #222; font: 12px "Segoe UI", UI, sans-serif; padding: 10px 12px 12px; box-sizing: border-box; }}
.mt {{ background: #F3F3F3; border-bottom: 1px solid #D4D4D4; margin: -10px -12px 10px; padding: 7px 12px; font-weight: 600; color: #444; }}
.act {{ border: 1px solid #C8C8C8; margin-bottom: 5px; padding: 4px 8px 5px; }}
.an {{ font-weight: 600; color: #2B579A; margin-bottom: 2px; }}
.ar {{ display: flex; gap: 8px; line-height: 17px; }}
.ar span {{ width: 110px; text-align: right; color: #555; }}
.ar i {{ font-style: normal; border: 1px solid #ABABAB; padding: 0 5px; min-width: 140px; }}
.add {{ color: #777; border: 1px dashed #BBB; padding: 3px 8px; margin-top: 4px; }}
</style></head><body><div id="a">
<h1>PLATINUM DRIVE · une seule photo derrière le menu <span class="or">et</span> le sous-formulaire · <span class="or">sans VBA</span></h1>
<div class="s">Access ne sait pas rendre un sous-formulaire transparent : la photo est coupée en deux morceaux alignés, et des macros affichent le bon bandeau.</div>
<div class="rang">
 <div class="cap"><img src="{ecran}">
  <div class="z" style="top:{y1:.1f}px;height:{y2 - y1:.1f}px;border:3px solid #E3C77A"></div>
  <div class="z" style="top:{y2:.1f}px;height:{hs - y2:.1f}px;border:3px dashed #7FC4FF"></div>
  <div class="n pa" style="left:890px;top:{(y1 + y2) / 2 - 13:.0f}px;background:#E3C77A">1</div>
  <div class="n pa" style="left:-15px;top:{y2 + 14:.0f}px;background:#7FC4FF">2</div>
  <div class="n pa" style="left:470px;top:{(y2 + hs) / 2 - 13:.0f}px;background:#7FC4FF;width:34px;height:34px;border-radius:17px;font-size:18px">3</div>
  <div class="leg">
   <div><span class="n" style="background:#E3C77A">1</span>Formulaire <b>Menu</b> : <b>7 contrôles Image</b> empilés derrière les onglets (<b class="or">d-tete-&lt;page&gt;.jpg</b>, 41,49 × 1,905 cm) · un seul visible</div>
   <div><span class="n" style="background:#7FC4FF">2</span>Contrôle <b>sous-formulaire</b> : Gauche 0 · Haut <b>1,905 cm</b> · 41,49 × 18,84 cm · Style bordure Transparent</div>
   <div><span class="n" style="background:#7FC4FF">3</span>Formulaire de la page · propriété Image <b>fixe</b> = <b class="bl">d-corps-&lt;page&gt;.jpg</b> (bas de la même photo) · aucune macro</div>
  </div>
 </div>
 <div class="col">
  <h2>Les 7 bandeaux du Menu</h2>
  <div>{pile}</div>
  <div class="lbl">Les 7 au même endroit (Gauche 0, Haut 0), derrière les onglets (aperçus éclaircis).</div>
  <h2>Ce qui change la photo</h2>
  • <b>En bas</b> : chaque page a son image <b class="bl">d-corps</b> → elle arrive toute seule avec la page.<br>
  • <b>En haut</b> : la macro du bouton cliqué rend son bandeau visible (<b>-1</b>) et cache les 6 autres (<b>0</b>).<br>
  • DéfinirPropriété est une action « sûre » : elle marche même si le contenu actif est désactivé.
 </div>
</div>
<h2 style="margin-top:26px">Quand on clique sur l'onglet « Clients »</h2>
<div style="display:flex;align-items:flex-start;gap:22px">
 {macro_html("clients")}
 <div style="flex:1">
  <div style="display:flex;gap:16px;align-items:center">
   <div><img src="{ecran}" style="width:440px;display:block"><div class="lbl">Avant : Tableau de bord</div></div>
   <div style="font-size:36px;color:#E3C77A">→</div>
   <div><img src="{ecran2}" style="width:440px;display:block"><div class="lbl">Après : Clients</div></div>
  </div>
  <div style="font-size:14px;line-height:1.7;color:#C9CDD2;margin-top:4px">
   <b class="or">① La macro</b> (à gauche) affiche <b>Img_Fond_clients</b> et cache les autres bandeaux du Menu.<br>
   <b class="bl">② Access charge Frm_Clients</b> dans le sous-formulaire : il arrive avec <b>d-corps-clients.jpg</b>.<br>
   Haut et bas viennent de la même photo : le raccord est invisible.</div>
 </div>
</div>
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
    tete, bas = cm(TETE, 3), cm(H - TETE, 3)
    L = ["# Photo en fond du menu ET du sous-formulaire, sans VBA · PLATINUM DRIVE", "",
         "Schéma : **`schema-fond-navigation.png`**. Aucune ligne de VBA : seulement des propriétés et des **macros incorporées**.", "",
         "## Le principe", "",
         "Dans Access, un sous-formulaire **peint toujours son propre fond** (il ne peut pas être transparent). On coupe donc chaque photo en deux :", "",
         f"* **le bandeau** (haut de la photo, {tete} cm) : dans le formulaire **Menu**, derrière les onglets ;",
         f"* **le bas** ({bas} cm) : dans le **formulaire de la page**, affiché par le sous-formulaire.", "",
         "Le bas change tout seul (chaque page a sa propre image). Pour le haut, le Menu contient **les 7 bandeaux empilés** "
         "et la macro de chaque bouton de navigation **affiche le bon et cache les autres**.", "",
         "## 1. Les images (prêtes dans `assets/photos/`)", "",
         f"| Page | Bandeau → formulaire Menu (41,49 × {tete} cm) | Bas → formulaire de la page (41,49 × {bas} cm) |", "|---|---|---|"]
    for k, f, t in PAGES:
        L.append(f"| {t} (`{f}`) | `d-tete-{k}.jpg` | `d-corps-{k}.jpg` |")
    L += ["", "## 2. Formulaire Menu", "",
          "1. Mode Création, sélectionnez tous les contrôles › onglet **Organiser** › **Supprimer la disposition** "
          "(sinon Access place lui-même le sous-formulaire et on ne peut pas le régler au millimètre).",
          f"2. Formulaire : Largeur **{cm(W)} cm**, hauteur totale des sections **{cm(H)} cm**, `Image` **(aucune)**, `Taille automatique` Oui, "
          "`Style bordure` **Fin**, `Boutons Min Max` Réduire seulement, barres de défilement Aucune, sélecteur et boutons de déplacement Non.",
          "3. **Les 7 bandeaux** : onglet **Création** › **Insérer une image** › *Parcourir* › `d-tete-tableau.jpg`, dessinez le contrôle, puis "
          "réglez ses propriétés. Recommencez pour les 6 autres :", "",
          "| Propriété | Valeur |", "|---|---|",
          "| Nom | `Img_Fond_tableau`, `Img_Fond_reservations`, `Img_Fond_clients`, `Img_Fond_voitures`, `Img_Fond_marques`, "
          "`Img_Fond_carburants`, `Img_Fond_modeles` (image `d-tete-<page>.jpg` correspondante) |",
          "| Gauche / Haut | **0** / **0** (les 7 exactement au même endroit) |",
          f"| Largeur / Hauteur | **{cm(W)} cm** / **{tete} cm** |",
          "| Type d'image | Incorporé |",
          "| Mode d'affichage | **Étirer** |",
          "| Style bordure | Transparent |",
          "| Visible | **Oui** pour `Img_Fond_tableau` seulement, **Non** pour les 6 autres |", "",
          "4. Sélectionnez les 7 images › **Organiser** › **Mettre en arrière-plan** : elles passent derrière le logo et les onglets.",
          "5. Contrôle de navigation (les onglets) : `Style fond` **Transparent**, `Style bordure` Transparent (positions : `COTES.md`, "
          "lignes `BoutonNavigation_…`). Nommez les boutons `BoutonNavigation_tableau`, `BoutonNavigation_clients`… (propriété **Nom**).",
          "6. Contrôle **sous-formulaire** (ligne `Sous_Formulaire` de `COTES.md`) :", "",
          "| Propriété | Valeur |", "|---|---|",
          "| Gauche | **0 cm** |",
          f"| Haut | **{tete} cm** (tapez les 3 décimales : c'est la ligne de coupe) |",
          f"| Largeur / Hauteur | **{cm(W)} cm** / **{bas} cm** |",
          "| Style bordure | **Transparent** |", "",
          "## 3. Chaque formulaire de page : image fixe", "",
          "| Formulaire | Propriété `Image` |", "|---|---|"]
    for k, f, t in PAGES:
        L.append(f"| `{f}` | `d-corps-{k}.jpg` |")
    L += ["", f"Dans chaque page : Largeur **{cm(W)} cm**, Détail **{bas} cm**, en-tête/pied de formulaire supprimés, `Type d'image` Incorporé, "
          "`Mode d'affichage de l'image` **Étirer**, `Alignement` Coin supérieur gauche, barres de défilement **Aucune**, sélecteur, boutons de "
          "déplacement et diviseurs **Non**. Les cartes restent des Rectangles pleins posés par-dessus la photo (pas de grand Rectangle de fond).", "",
          "## 4. La macro de chaque bouton de navigation", "",
          "### Le premier bouton (Clients), pas à pas", "",
          "1. Formulaire Menu en mode Création, cliquez sur le bouton **Clients**.",
          "2. Feuille de propriétés › onglet **Événement** › ligne **Sur clic** › bouton **`…`** › **Générateur de macro** › OK.",
          "3. Dans la liste **Ajouter une nouvelle action**, choisissez **DéfinirPropriété**, puis remplissez :", "",
          "| Nom du contrôle | Propriété | Valeur |", "|---|---|---|",
          "| `Img_Fond_clients` | Visible | **-1** (= Vrai : on l'affiche) |", "",
          "4. Ajoutez 6 autres actions **DéfinirPropriété**, une par autre bandeau, avec la Valeur **0** (= Faux : on le cache) : "
          "`Img_Fond_tableau`, `Img_Fond_reservations`, `Img_Fond_voitures`, `Img_Fond_marques`, `Img_Fond_carburants`, `Img_Fond_modeles`.",
          "5. **Enregistrer**, puis **Fermer** le générateur. La ligne *Sur clic* affiche `[Macro incorporée]`.", "",
          "### Les 6 autres boutons : copier-coller", "",
          "Dans la macro terminée, cliquez dans le générateur, **Ctrl+A** puis **Ctrl+C**. Ouvrez la macro *Sur clic* du bouton suivant "
          "(étape 2), **Ctrl+V** : les 7 actions sont collées. Il reste à changer les **Valeurs** selon ce tableau "
          "(**-1** = visible, **0** = caché) :", "",
          "| Bouton cliqué | " + " | ".join(f"Img_Fond_{k}" for k, _f, _t in PAGES) + " |",
          "|---|" + "---:|" * len(PAGES)]
    for k, _f, t in PAGES:
        L.append(f"| `BoutonNavigation_{k}` ({t}) | " + " | ".join("**-1**" if j == k else "0" for j, _g, _u in PAGES) + " |")
    L += ["", "Les boutons gardent leur **Nom du formulaire cible de navigation** (`Frm_Clients`…) : la macro change seulement le bandeau, "
          "la navigation (changement de page) reste faite par le formulaire de navigation d'Access.", "",
          "## 5. Si ça ne marche pas", "",
          "| Ce que vous voyez | Solution |", "|---|---|",
          "| Le haut ne change pas | *Sur clic* du bouton = `[Macro incorporée]` ; les noms `Img_Fond_…` de la macro doivent être exactement ceux des images |",
          "| Le haut est vide au démarrage | `Visible` = **Oui** pour `Img_Fond_tableau` |",
          "| Les onglets ou le logo sont cachés par la photo | Sélectionnez les 7 images › **Organiser** › **Mettre en arrière-plan** |",
          "| Le bas ne change pas | Propriété `Image` de chaque formulaire de page (section 3) |",
          "| Trait fin ou cadre autour de la page | `Style bordure` du contrôle sous-formulaire = **Transparent** |",
          f"| Photo décalée de quelques pixels | Sous-formulaire : `Haut` = **{tete}**, `Gauche` = **0** ; bandeaux : `Hauteur` = **{tete}** |",
          "| Photo déformée | `Mode d'affichage` = **Étirer** partout, formulaire Menu à taille fixe (`Style bordure` Fin) |", ""]
    (DOS / "FOND-NAVIGATION.md").write_text("\n".join(L))


if __name__ == "__main__":
    guide()
    schema()
    print("FOND-NAVIGATION.md et schema-fond-navigation.png écrits")
