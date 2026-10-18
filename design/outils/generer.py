#!/usr/bin/env python3
"""
Générateur des maquettes RENTAL CAR (thème clair, rendu « Access »).

  cd design/outils && npm install && python3 generer.py

Produit :
  design/maquettes/*.html        maquettes (ouvrables dans un navigateur)
  design/maquettes/png/*.png     captures des maquettes
  design/assets/*.png            icônes à importer dans Access
  design/COTES.md                positions et tailles des contrôles, en cm
"""
import html
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
DESIGN = ICI.parent
MAQ = DESIGN / "maquettes"
ASSETS = DESIGN / "assets"
SVG_DIR = ICI / "icones-svg"

from themes import THEMES
import designs as D

T = THEMES[0]                # thème courant (changé par appliquer_theme)
ASSET_URL = "../assets"      # chemin des images vu depuis les fichiers HTML
NOM_APPLI = "RENTAL GABON CAR"
W, H = 1568, 784            # zone du formulaire (sans la barre de titre)
CW, CH = W - 220, H - 56    # zone de contenu (sous-formulaire) : 1348 x 728
DONNEES = json.loads((ICI / "donnees.json").read_text())
CLIENTS = {c["CIN"]: c for c in DONNEES["Client"]}
MARQUES = {m["IdMarque"]: m["Marque"] for m in DONNEES["Marque"]}
CARBURANTS = {c["IdType"]: c["Type"] for c in DONNEES["Carburant"]}
MODELES = {m["IdModele"]: m for m in DONNEES["Modele"]}
VOITURES = {v["Matricule"]: v for v in DONNEES["Voiture"]}


def modele_de(mat):
    m = MODELES[VOITURES[mat]["Modele"]]
    return m["Modele"], MARQUES[m["Marque"]]


def duree(r):
    import datetime as dt
    return (dt.date.fromisoformat(r["DateFin"][:10]) - dt.date.fromisoformat(r["DateDebut"][:10])).days


def montant(r):
    return duree(r) * VOITURES[r["Voiture"]]["CoutParJour"]


# --------------------------------------------------------------------------
def e(s):
    return html.escape(str(s))


def acc(nom, typ):
    return f'data-acc="{e(nom)}" data-type="{e(typ)}"'


def svg(name, color, size=18, stroke=1.75):
    raw = (SVG_DIR / f"{name}.svg").read_text()
    inner = re.search(r"<svg[^>]*>(.*)</svg>", raw, re.S).group(1)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round" style="display:block" data-ico="{name}">{inner}</svg>')


def fdate(iso):
    y, m, d = iso[:10].split("-")
    return f"{d}/{m}/{y}"


def fcfa(n):
    return f"{n:,}".replace(",", " ")


# --------------------------------------------------------------------------
# Fenêtre Windows
# --------------------------------------------------------------------------
ICONE_FORM = ('<svg class="ico" viewBox="0 0 14 14"><rect x=".5" y="1.5" width="13" height="11" fill="#fff" stroke="#6B6B6B"/>'
              '<rect x=".5" y="1.5" width="13" height="3" fill="#A4373A"/><rect x="2.5" y="6.5" width="4" height="1.5" fill="#6B6B6B"/>'
              '<rect x="7.5" y="6.5" width="4" height="1.5" fill="#6B6B6B"/><rect x="2.5" y="9.5" width="4" height="1.5" fill="#6B6B6B"/>'
              '<rect x="7.5" y="9.5" width="4" height="1.5" fill="#6B6B6B"/></svg>')


def fenetre(titre_fen, largeur, hauteur, corps, boutons=("min", "max", "fermer")):
    ctrl = ""
    glyphes = {
        "min": '<svg width="10" height="10"><path d="M0 5.5h10" stroke="currentColor" stroke-width="1"/></svg>',
        "max": '<svg width="10" height="10"><rect x="2.5" y=".5" width="7" height="7" fill="none" stroke="currentColor"/><path d="M.5 2.5v7h7" fill="none" stroke="currentColor"/></svg>',
        "fermer": '<svg width="10" height="10"><path d="M0 0l10 10M10 0L0 10" stroke="currentColor" stroke-width="1"/></svg>',
    }
    for i, b in enumerate(reversed(boutons)):
        ctrl += f'<div class="ctrl" style="right:{i * 46}px">{glyphes[b]}</div>'
    return f"""<div class="fenetre d-{T.get('design', 'bleu')}" id="fenetre" style="width:{largeur}px">
<div class="barre-titre">{ICONE_FORM}<span class="txt">{e(titre_fen)}</span>{ctrl}</div>
<div class="ecran" id="ecran" style="width:{largeur}px;height:{hauteur}px">
{corps}
</div></div>"""


def page(titre, corps):
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>{e(titre)} · {NOM_APPLI}</title>
<link rel="stylesheet" href="style.css"><meta name="theme" content="{T['cle']}"></head>
<body>{corps}</body></html>"""


# --------------------------------------------------------------------------
# Formulaire Menu
# --------------------------------------------------------------------------
MENU = [
    ("tableau", "Tableau de bord", "layout-dashboard"),
    ("reservations", "Réservations", "calendar-range"),
    ("clients", "Clients", "users"),
    ("voitures", "Voitures", "car"),
    ("marques", "Marques", "tag"),
    ("carburants", "Carburants", "fuel"),
    ("modeles", "Modèles", "layers"),
]


def coquille(actif, titre, contenu):
    nav = ""
    for i, (cle, lib, ico) in enumerate(MENU):
        y = 110 + i * 44
        on = cle == actif
        nav += (f'<div class="nav{" actif" if on else ""}" style="top:{y}px" {acc("BoutonNavigation_" + cle, "Bouton de navigation")}>'
                f'{svg(ico, T["nav_ico_actif"] if on else T["nav_ico"], 18)}{e(lib)}</div>')
    corps = f"""
<div class="menu" {acc("Menu_Fond", "Image (menu-fond.jpg)")}>
  <img class="abs" src="{ASSET_URL}/photos/menu-fond.jpg" style="left:0;top:0;width:220px;height:{H}px">
  <div class="logo" {acc("Logo", "Image + étiquette")}>{svg("car-front", T["logo"], 24, 1.8)}{NOM_APPLI}</div>
  <div class="rubrique" style="top:84px">Menu principal</div>
  {nav}
  <div class="slogan" {acc("Slogan", "Étiquette")}>Location de véhicules<br>à Libreville</div>
</div>
<div class="entete" {acc("Entete", "Rectangle")}>
  <div class="date" style="left:24px" {acc("Date_Heure", "Zone de texte")}>{svg("calendar-range", T["gris"], 15)}lundi 28 septembre 2026 · 20:06</div>
  <div class="avatar" style="right:196px;top:12px" {acc("Btn_Avatar", "Bouton (ellipse)")}>AD</div>
  <div class="utilisateur" style="right:72px;top:11px" {acc("Utilisateur", "Étiquettes")}><b>admin</b><span>Administrateur</span></div>
  <div class="btn-ico abs" style="right:24px;top:12px;width:32px;height:32px" {acc("Btn_Quitter", "Bouton")}>{svg("power", T["icone_titre"], 16)}</div>
</div>
<div class="contenu" id="contenu">
{contenu}
</div>"""
    return fenetre(NOM_APPLI, W, H, corps)


BANDEAUX = {  # clé : (photo source, position de l'image, hauteur)
    "tableau": ("tableau-flotte.jpg", "center 70%", 128),
    "reservations": ("reservations-cles.jpg", "center 52%", 92),
    "clients": ("clients-accueil.jpg", "center 30%", 92),
    "voitures": ("voitures-showroom.jpg", "center 66%", 92),
    "marques": ("marques-calandres.jpg", "center 46%", 92),
    "carburants": ("carburants-pompe.jpg", "center 48%", 92),
    "modeles": ("modeles-interieur.jpg", "center 55%", 92),
}
BW = CW - 48  # largeur des bandeaux : 1300 px


def bandeau(cle, titre, sous_titre):
    h = BANDEAUX[cle][2]
    ty = (h - 58) // 2
    return (f'<div class="bandeau" style="left:24px;top:24px;width:{BW}px;height:{h}px;'
            f'background-image:url({ASSET_URL}/photos/bandeau-{cle}.jpg)" {acc("Bandeau", "Image (bandeau-" + cle + ".jpg)")}>'
            f'<div class="b-titre" style="top:{ty}px" {acc("Bandeau_Titre", "Étiquette")}>{e(titre)}</div>'
            f'<div class="b-sous" style="top:{ty + 34}px" {acc("Bandeau_SousTitre", "Étiquette")}>{e(sous_titre)}</div></div>')


# --------------------------------------------------------------------------
# Briques
# --------------------------------------------------------------------------
ACTIONS = {"Ajouter": "plus", "Actualiser": "refresh-cw", "Rechercher": "search", "Imprimer": "printer"}


def carte(nom, titre, x, y, w, h, interieur="", actions=(), info=None, icone=None):
    act = ""
    if actions:
        act = '<div class="actions">' + "".join(
            f'<div class="btn-ico" title="{a}" {acc("Btn_" + a, "Bouton")}>{svg(ACTIONS[a], T["icone"], 16)}</div>' for a in actions) + "</div>"
    tx = 48 if icone else 20
    ico = f'<div class="abs" style="left:20px;top:16px">{svg(icone, T["icone"], 18)}</div>' if icone else ""
    k = {"a": 10.9, "d": 10.4, "e": 9.4}.get(T.get("design"), 8.6)  # largeur moyenne d'une lettre du titre
    inf = f'<div class="info" style="left:{tx + 14 + int(len(titre) * k)}px">{e(info)}</div>' if info else ""
    return (f'<div class="carte" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px" {acc(nom, "Rectangle")}>'
            f'<div class="bande"></div>{ico}<div class="titre-c" style="left:{tx}px">{e(titre)}</div>{inf}{act}'
            f'<div class="trait"></div>{interieur}</div>')


def fleche_bas():
    return (f'<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="{T["etiq"]}" stroke-width="2.5" '
            'stroke-linecap="round" stroke-linejoin="round" style="display:block"><path d="m6 9 6 6 6-6"/></svg>')


def champ(nom, lib, val, x, y, lw, w, kind="texte", droite=False, total=False):
    cls = "champ" + (" lecture" if kind == "lecture" else "") + (" droite" if droite else "") + (" total" if total else "")
    extra = ""
    if kind == "liste":
        cls += " liste-der"
        extra = f'<span class="fleche">{fleche_bas()}</span>'
    typ = {"texte": "Zone de texte", "lecture": "Zone de texte (verrouillée)", "liste": "Zone de liste déroulante"}[kind]
    out = f'<div class="etiq" style="left:{x}px;top:{y}px">{e(lib)}</div>' if lib else ""
    return out + f'<div class="{cls}" style="left:{x + lw}px;top:{y}px;width:{w}px" {acc(nom, typ)}>{e(val)}{extra}</div>'


def nav_enreg(x, y, texte):
    ico = [("Premier", "chevron-first"), ("Precedent", "chevron-left"), ("Suivant", "chevron-right"), ("Dernier", "chevron-last")]
    out = ""
    pos = [x, x + 34, x + 178, x + 212]
    for (n, i), px in zip(ico, pos):
        out += f'<div class="btn-nav" style="left:{px}px;top:{y}px" {acc("Btn_" + n, "Bouton")}>{svg(i, T["icone"], 16)}</div>'
    out += f'<div class="compteur" style="left:{x + 68}px;top:{y}px;width:106px" {acc("Txt_Compteur", "Zone de texte")}>{e(texte)}</div>'
    return out


def boutons_crud(x, y, w=130):
    return (f'<div class="btn primaire" style="left:{x}px;top:{y}px;width:{w}px" {acc("Btn_Enregistrer", "Bouton")}>{svg("save", T["accent_txt"], 16)}Enregistrer</div>'
            f'<div class="btn danger" style="left:{x + w + 10}px;top:{y}px;width:{w}px" {acc("Btn_Supprimer", "Bouton")}>{svg("trash-2", T["danger"], 16)}Supprimer</div>')


def liste(nom, cols, lignes, x, y, w, h, total=None):
    """Zone de liste façon Access. cols = [(titre, largeur, 'num'?)]"""
    vis = (h - 2 - 21) // 20
    n = total or len(lignes)
    dispo = w - 2 - (17 if n > vis else 0)
    tw = sum(c[1] for c in cols)
    if tw < dispo:  # on répartit la place restante sur toutes les colonnes
        k = dispo / tw
        cols = [(c[0], int(c[1] * k)) + tuple(c[2:]) for c in cols]
        cols[-1] = (cols[-1][0], cols[-1][1] + dispo - sum(c[1] for c in cols)) + tuple(cols[-1][2:])
        tw = dispo
    colg = "".join(f'<col style="width:{c[1]}px">' for c in cols)
    th = "".join(f'<th class="{c[2] if len(c) > 2 else ""}">{e(c[0])}</th>' for c in cols)
    trs = "".join("<tr>" + "".join(f'<td class="{cols[i][2] if len(cols[i]) > 2 else ""}">{e(v)}</td>'
                                   for i, v in enumerate(l)) + "</tr>" for l in lignes)
    defil = ""
    if n > vis:
        piste = h - 2 - 34
        ph = max(20, int(piste * vis / n))
        tri_h = '<svg width="7" height="4"><path d="M0 4L3.5 0L7 4z" fill="#606060"/></svg>'
        tri_b = '<svg width="7" height="4"><path d="M0 0L3.5 4L7 0z" fill="#606060"/></svg>'
        defil = (f'<div class="defil"><div class="fl" style="top:0">{tri_h}</div>'
                 f'<div class="pouce" style="top:19px;height:{ph}px"></div>'
                 f'<div class="fl" style="bottom:0">{tri_b}</div></div>')
    return (f'<div class="liste" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px" {acc(nom, "Zone de liste")}>'
            f'<table style="width:{tw}px"><colgroup>{colg}</colgroup><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>{defil}</div>')


# --------------------------------------------------------------------------
# Données communes
# --------------------------------------------------------------------------

def lignes_reservations():
    out = []
    for r in DONNEES["Reservation"][:7]:
        c = CLIENTS[r["Client"]]
        mo, ma = modele_de(r["Voiture"])
        out.append([r["IdReservation"], fdate(r["DateDebut"]), fdate(r["DateFin"]), c["Prénom"], c["Nom"], r["Voiture"], mo, ma])
    return out


# --------------------------------------------------------------------------
# Écrans
# --------------------------------------------------------------------------
def stats():
    """Chiffres calculés comme les requêtes de la base : CA = Somme((DateFin-DateDebut)*CoutParJour)."""
    from collections import defaultdict
    ca = sum(montant(r) for r in DONNEES["Reservation"])
    par_client = defaultdict(int)
    for r in DONNEES["Reservation"]:
        par_client[r["Client"]] += montant(r)
    top = sorted(par_client.items(), key=lambda kv: -kv[1])[:5]
    top = [(CLIENTS[c]["Prénom"], CLIENTS[c]["Nom"], v) for c, v in top]
    return ca, top


def ecran_tableau():
    if T["design"] != "bleu":
        return D.fn("tableau")()
    ca, top = stats()
    (k1, p1), (k2, p2), (k3, p3) = T["kpi"]
    kpis = [("CA", "Chiffre d'affaires", fcfa(ca), "FCFA", "sur 25 réservations", "wallet", k1, p1),
            ("Voitures", "Voitures", "60", "", "8 en location aujourd'hui", "car-front", k2, p2),
            ("Clients", "Clients", "200", "", f"Meilleur client : {top[0][0]} {top[0][1]}", "users", k3, p3)]
    kw = (CW - 48 - 32) // 3
    out = bandeau("tableau", "Bonjour, admin", "Voici l'activité de RENTAL GABON CAR au 28 septembre 2026.")
    for i, (n, lib, val, unit, sub, ico, fond, pastille) in enumerate(kpis):
        x = 24 + i * (kw + 16)
        u = f"<small>{unit}</small>" if unit else ""
        out += (f'<div class="kpi" style="left:{x}px;top:168px;width:{kw}px;height:100px;background:{fond};border-color:{fond}" {acc("Carte_" + n, "Rectangle")}>'
                f'<div class="lib">{e(lib)}</div><div class="val" {acc("Txt_" + n, "Zone de texte")}>{val}{u}</div>'
                f'<div class="sub">{e(sub)}</div>'
                f'<div class="pastille" style="background:{pastille}" {acc("Pastille_" + n, "Rectangle + image")}>{svg(ico, T["kpi_ico"], 24)}</div></div>')

    import datetime as dt
    auj = dt.date(2026, 9, 28)
    res = []
    for r in DONNEES["Reservation"]:
        d0, d1 = dt.date.fromisoformat(r["DateDebut"][:10]), dt.date.fromisoformat(r["DateFin"][:10])
        if d0 <= auj <= d1:
            c = CLIENTS[r["Client"]]
            res.append([r["Voiture"], modele_de(r["Voiture"])[0], fdate(r["DateDebut"]), fdate(r["DateFin"]), c["Prénom"], c["Nom"]])
    lw1 = 836
    l1 = liste("Liste_Voitures_Reservees",
               [("Matricule", 110), ("Modèle", 220), ("Date de début", 110), ("Date de fin", 110), ("Prénom", 110), ("Nom", 110)],
               res, 20, 66, lw1 - 42, 334)
    p1 = carte("Carte_Reservees", "Voitures actuellement réservées", 24, 284, lw1, 420, l1, actions=["Imprimer"],
               info="8 en cours", icone="clipboard-list")

    lw2 = CW - 48 - 16 - lw1
    l2 = liste("Liste_Top5", [("Prénom", 120), ("Nom", 120), ("CA (FCFA)", 150, "num")],
               [[a, b, fcfa(c)] for a, b, c in top], 20, 64, lw2 - 40, 124)
    p2 = carte("Carte_Top5", "5 meilleurs clients", 24 + lw1 + 16, 284, lw2, 202, l2, icone="trophy")
    l3 = liste("Liste_Carburants", [("Type", 150), ("Voitures", 110, "num"), ("Part", 130, "num")],
               flotte_carburant(), 20, 64, lw2 - 40, 124)
    p3 = carte("Carte_Carburants", "Flotte par carburant", 24 + lw1 + 16, 502, lw2, 202, l3, icone="fuel")
    return coquille("tableau", "Tableau de bord", out + p1 + p2 + p3)


def flotte_carburant():
    from collections import Counter
    n = Counter(v["Carburant"] for v in DONNEES["Voiture"])
    return [[CARBURANTS[k], c, f"{c * 100 / 60:.1f} %".replace(".", ",")] for k, c in n.most_common()]


def ecran_reservations():
    if T["design"] != "bleu":
        return D.fn("reservations")()
    lw, iw = 104, 470
    cw = (CW - 48 - 16) // 2
    r1 = DONNEES["Reservation"][0]
    R1_MOD, R1_MAR = modele_de(r1["Voiture"])
    b = bandeau("reservations", "Réservations", "25 réservations · 8 en cours aujourd'hui")
    cli = (champ("Cbo_Client", "Client", "Jean Mboumba", 20, 64, lw, iw, "liste")
           + champ("Txt_Telephone", "Téléphone", "(+241) 62 54 85 85", 20, 100, lw, iw, "lecture")
           + champ("Txt_Email", "Email", "jean.mboumba1@example.com", 20, 136, lw, iw, "lecture"))
    p1 = carte("Carte_Client", "Client", 24, 132, cw, 180, cli, icone="user")
    voi = (champ("Cbo_Voiture", "Voiture", "AB-3988-AA", 20, 64, lw, iw, "liste")
           + champ("Txt_Modele", "Modèle", R1_MOD, 20, 100, lw, iw, "lecture")
           + champ("Txt_Marque", "Marque", R1_MAR, 20, 136, lw, iw, "lecture"))
    p2 = carte("Carte_Voiture", "Voiture", 24 + cw + 16, 132, cw, 180, voi, icone="car")

    res = (champ("Txt_Code", "Code", "1", 20, 64, 104, 80, droite=True)
           + champ("Txt_DateDebut", "Date de début", "23/09/2026", 20, 100, 104, 120, droite=True)
           + champ("Txt_DateFin", "Date de fin", "24/10/2026", 272, 100, 90, 120, droite=True)
           + f'<div class="btn secondaire" style="left:494px;top:98px;width:60px" {acc("Btn_OK", "Bouton")}>OK</div>'
           + nav_enreg(124, 138, "1 sur 25")
           + '<div class="sep-v" style="left:640px;top:51px;height:127px"></div>'
           + champ("Txt_Duree", "Durée", f"{duree(r1)} jour(s)", 664, 64, 90, 200, "lecture", droite=True)
           + champ("Txt_Montant", "Montant", f"{fcfa(montant(r1))} FCFA", 664, 100, 90, 200, "lecture", droite=True, total=True)
           + boutons_crud(CW - 48 - 20 - 270, 136))
    p3 = carte("Carte_Reservation", "Réservation", 24, 328, CW - 48, 180, res,
               actions=["Ajouter", "Actualiser", "Rechercher", "Imprimer"], icone="calendar-range")

    l = liste("Liste_Reservations", [("Code", 60, "num"), ("Date de début", 130), ("Date de fin", 130), ("Prénom", 150), ("Nom", 160),
                                     ("Matricule", 140), ("Modèle", 150), ("Marque", 120)],
              lignes_reservations(), 20, 62, CW - 48 - 40, 104, total=25)
    p4 = carte("Carte_Liste", "Liste des réservations", 24, 524, CW - 48, 180, l, actions=["Imprimer"],
               info="25 réservations", icone="list")
    return coquille("reservations", "Réservations", b + p1 + p2 + p3 + p4)


def ecran_fiche(cle, titre, sous_titre, titre_fiche, icone, champs, titre_liste, cols, lignes, total, compteur, info,
                fiche_w=520, grande_liste=True):
    if T["design"] != "bleu":
        return D.fn("fiche")(cle, titre_fiche, icone, champs, titre_liste, cols, lignes, total, compteur, info, grande_liste)
    y0 = 132
    lw = 130
    iw = fiche_w - 40 - lw
    inner = ""
    y = 70
    for (n, lib, val, kind, *opt) in champs:
        inner += champ(n, lib, val, 20, y, lw, opt[0] if opt else iw, kind)
        y += 40
    y += 8
    inner += nav_enreg(20 + lw, y, compteur)
    y += 46
    inner += f'<div class="sep-h" style="left:0;top:{y}px;width:{fiche_w - 2}px"></div>'
    y += 16
    inner += boutons_crud(fiche_w - 20 - 270, y)
    h = y + 32 + 18
    p1 = carte("Carte_Fiche", titre_fiche, 24, y0, fiche_w, h, inner,
               actions=["Ajouter", "Actualiser", "Rechercher", "Imprimer"], icone=icone)
    lx = 24 + fiche_w + 16
    lw_ = CW - 24 - lx
    lh = (704 - y0) if grande_liste else max(h, 300)
    l = liste("Liste_" + cle.capitalize(), cols, lignes, 20, 66, lw_ - 40, lh - 86, total=total)
    p2 = carte("Carte_Liste", titre_liste, lx, y0, lw_, lh, l, actions=["Imprimer"], info=info, icone="list")
    return coquille(cle, titre, bandeau(cle, titre, sous_titre) + p1 + p2)


def ecran_clients():
    c = CLIENTS["CL-0001"]
    champs = [("Txt_CIN", "Code client", c["CIN"], "texte", 140), ("Txt_Permis", "N° de permis", c["NumPermis"], "texte", 180),
              ("Txt_Prenom", "Prénom", c["Prénom"], "texte"), ("Txt_Nom", "Nom", c["Nom"], "texte"),
              ("Cbo_Sexe", "Sexe", c["Sexe"], "liste", 80), ("Txt_Adresse", "Adresse", c["Adresse"], "texte"),
              ("Txt_Telephone", "Téléphone", c["Téléphone"], "texte"), ("Txt_Email", "Email", c["Email"], "texte")]
    lignes = [[x["CIN"], x["NumPermis"], x["Prénom"], x["Nom"], x["Sexe"], x["Adresse"], x["Téléphone"]] for x in DONNEES["Client"][:30]]
    cols = [("Code client", 76), ("N° de permis", 112), ("Prénom", 86), ("Nom", 96), ("Sexe", 36), ("Adresse", 160), ("Téléphone", 139)]
    return ecran_fiche("clients", "Clients", "200 clients enregistrés", "Fiche client", "user", champs, "Liste des clients",
                       cols, lignes, 200, "1 sur 200", "200 clients")


def ecran_voitures():
    vs = DONNEES["Voiture"]
    v0 = vs[0]
    mo, ma = modele_de(v0["Matricule"])
    champs = [("Txt_Matricule", "Matricule", v0["Matricule"], "texte", 140), ("Txt_Annee", "Année", v0["Annee"], "texte", 80),
              ("Txt_Couleur", "Couleur", v0["Couleur"], "texte"), ("Txt_Puissance", "Puissance", f"{fcfa(v0['Puissance'])} ch", "texte", 100),
              ("Txt_CoutJour", "Coût par jour", f"{fcfa(v0['CoutParJour'])} FCFA", "texte", 160), ("Cbo_Modele", "Modèle", mo, "liste"),
              ("Cbo_Carburant", "Carburant", CARBURANTS[v0["Carburant"]], "liste"), ("Cbo_Marque", "Marque", ma, "liste")]
    lignes = [[v["Matricule"], modele_de(v["Matricule"])[0], v["Annee"], v["Couleur"], f"{fcfa(v['Puissance'])} ch",
               fcfa(v["CoutParJour"])] for v in vs[:30]]
    cols = [("Matricule", 100), ("Modèle", 210), ("Année", 56), ("Couleur", 70), ("Puissance", 80), ("Coût par jour", 110, "num")]
    return ecran_fiche("voitures", "Voitures", "60 véhicules de prestige · 5 marques · 3 types de carburant", "Fiche voiture", "car",
                       champs, "Liste des voitures", cols, lignes, 60, "1 sur 60", "60 voitures")


def ecran_marques():
    champs = [("Txt_IdMarque", "Identifiant", "1", "texte", 80), ("Txt_Marque", "Marque", MARQUES[1], "texte")]
    lignes = [[m["IdMarque"], m["Marque"]] for m in DONNEES["Marque"]]
    return ecran_fiche("marques", "Marques", "5 marques · 60 modèles", "Fiche marque", "tag", champs, "Liste des marques",
                       [("Identifiant", 90), ("Marque", 200)], lignes, None, "1 sur 5", "5 marques", grande_liste=False)


def ecran_carburants():
    champs = [("Txt_IdType", "Identifiant", "1", "texte", 80), ("Txt_Type", "Type", CARBURANTS[1], "texte")]
    lignes = [[c["IdType"], c["Type"]] for c in DONNEES["Carburant"]]
    return ecran_fiche("carburants", "Carburants", "3 types de carburant", "Fiche carburant", "fuel", champs,
                       "Types de carburant", [("Identifiant", 90), ("Type", 200)], lignes, None, "1 sur 3", "3 types",
                       grande_liste=False)


def ecran_modeles():
    marques = {m["IdMarque"]: m["Marque"] for m in DONNEES["Marque"]}
    champs = [("Txt_IdModele", "Identifiant", "1", "texte", 80), ("Txt_Modele", "Modèle", MODELES[1]["Modele"], "texte"),
              ("Cbo_Marque", "Marque", MARQUES[1], "liste")]
    lignes = [[m["IdModele"], m["Modele"], marques[m["Marque"]]] for m in DONNEES["Modele"][:30]]
    return ecran_fiche("modeles", "Modèles", "60 modèles répartis sur 5 marques", "Fiche modèle", "layers", champs,
                       "Liste des modèles", [("Identifiant", 90), ("Modèle", 260), ("Marque", 140)], lignes, 60,
                       "1 sur 60", "60 modèles")


def ecran_login():
    if T["design"] != "bleu":
        return D.fn("login")()
    lw, lh = 880, 500
    fx = 470
    corps = f"""
<div class="abs" style="left:0;top:0;width:{lw}px;height:{lh}px;background:var(--surface)" {acc("Login_Fond", "Section Détail")}></div>
<img class="abs" src="{ASSET_URL}/photos/login-photo.jpg" style="left:0;top:0;width:420px;height:{lh}px" {acc("Login_Photo", "Image (login-photo.jpg)")}>
<div class="abs" style="left:36px;top:36px;display:flex;align-items:center;gap:10px;font-size:18.67px;font-weight:600;color:#FFFFFF;letter-spacing:.5px" {acc("Logo", "Image + étiquette")}>{svg("car-front", "#FFFFFF", 28, 1.8)}{NOM_APPLI}</div>
<div class="abs" style="left:36px;top:388px;width:350px;font-size:21.33px;font-weight:600;color:#FFFFFF;line-height:28px" {acc("Login_Slogan", "Étiquette")}>Location de véhicules<br>à Libreville</div>
<div class="abs" style="left:36px;top:454px;font-size:12px;color:rgba(255,255,255,.75)" {acc("Login_Copyright", "Étiquette")}>© 2026 RENTAL GABON CAR</div>
<div class="abs" style="left:{fx}px;top:84px;font-size:26.67px;font-weight:600;color:var(--titre)" {acc("Lbl_Titre", "Étiquette")}>Connexion</div>
<div class="abs" style="left:{fx}px;top:126px;font-size:14.67px;color:var(--gris)">Entrez vos identifiants pour accéder à l'application.</div>
<div class="etiq" style="left:{fx}px;top:172px">Nom d'utilisateur</div>
<div class="champ" style="left:{fx}px;top:200px;width:360px;height:34px;line-height:32px" {acc("Txt_Utilisateur", "Zone de texte")}>admin</div>
<div class="etiq" style="left:{fx}px;top:244px">Mot de passe</div>
<div class="champ" style="left:{fx}px;top:272px;width:360px;height:34px;line-height:32px;letter-spacing:2px" {acc("Txt_MotDePasse", "Zone de texte")}>********</div>
<div class="btn primaire" style="left:{fx}px;top:334px;width:360px;height:38px" {acc("Btn_Connexion", "Bouton")}>Se connecter</div>
<div class="abs" style="left:{fx}px;top:392px;width:360px;font-size:12px;color:var(--gris);text-align:center">Mot de passe oublié ? Contactez l'administrateur.</div>
"""
    return fenetre(NOM_APPLI + " - Connexion", lw, lh, corps, boutons=("fermer",))


ECRANS = [
    ("00-connexion", "Connexion", ecran_login),
    ("01-tableau-de-bord", "Tableau de bord", ecran_tableau),
    ("02-reservations", "Réservations", ecran_reservations),
    ("03-clients", "Clients", ecran_clients),
    ("04-voitures", "Voitures", ecran_voitures),
    ("05-marques", "Marques", ecran_marques),
    ("06-carburants", "Carburants", ecran_carburants),
    ("07-modeles", "Modèles", ecran_modeles),
]


# --------------------------------------------------------------------------
# Icônes PNG à importer dans Access
# --------------------------------------------------------------------------
def assets_jobs(tmp, icones=None):
    jobs = []

    def add(out, taille, name, color, size, stroke=1.75):
        off = (taille - size) / 2
        corps = f'<div style="position:absolute;left:{off}px;top:{off}px">{svg(name, color, size, stroke)}</div>'
        p = tmp / (out.replace("/", "_") + ".html")
        p.write_text(f'<!doctype html><html><head><style>html,body{{margin:0;background:transparent}}'
                     f'#a{{position:relative;width:{taille}px;height:{taille}px}}</style></head><body><div id="a">{corps}</div></body></html>')
        jobs.append({"html": p.as_uri(), "out": str(ASSETS / out), "w": taille, "h": taille, "transparent": True, "sel": "#a"})

    if icones is not None:                    # designs : exactement les icônes dessinées sur les écrans
        for (name, color, size, stroke), info in icones.items():
            add(info["fichier"], size, name, color, size, stroke)
    for _, _, ico in (MENU if icones is None else []):
        add(f"menu-{ico}.png", 20, ico, T["nav_ico"], 18)
        add(f"menu-{ico}-actif.png", 20, ico, T["nav_ico_actif"], 18)
    for ico in (list(ACTIONS.values()) + ["chevron-first", "chevron-left", "chevron-right", "chevron-last", "power"] if icones is None else []):
        add(f"bouton-{ico}.png", 16, ico, T["icone_titre"] if ico == "power" else T["icone"], 16)
    if icones is None:
        add("date.png", 16, "calendar-range", T["gris"], 15)
        add("logo-voiture.png", 28, "car-front", T["logo"], 24, 1.8)
        for ico, col in [("wallet", T["kpi_ico"]), ("car-front", T["kpi_ico"]), ("users", T["kpi_ico"])]:
            add(f"indicateur-{ico}.png", 24, ico, col, 24)
        add("bouton-enregistrer.png", 16, "save", T["accent_txt"], 16)
        add("bouton-supprimer.png", 16, "trash-2", T["danger"], 16)
        for ico in ["user", "car", "calendar-range", "list", "trophy", "clipboard-list", "tag", "fuel", "layers"]:
            add(f"carte-{ico}.png", 18, ico, T["icone"], 18)

    # Photos : recadrées à la taille exacte et assombries en bleu, prêtes pour Access
    def photo(out, w, h, src, pos, voile, filtre="none"):
        p = tmp / (out.replace("/", "_") + ".html")
        p.write_text(f'<!doctype html><html><head><style>html,body{{margin:0}}#a{{position:relative;width:{w}px;height:{h}px;'
                     f'overflow:hidden;background:{T["menu"]}}}#a img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;'
                     f'object-position:{pos};filter:{filtre}}}#a .v{{position:absolute;inset:0;background:{voile}}}</style></head>'
                     f'<body><div id="a"><img src="{(ICI / "photos" / src).as_uri()}"><div class="v"></div></div></body></html>')
        jobs.append({"html": p.as_uri(), "out": str(ASSETS / out), "w": w, "h": h, "transparent": False, "sel": "#a"})

    v = T["voile"]  # couleur du voile posé sur les photos (r, g, b)
    sat = T.get("photo_filtre", "none")

    def rgba(al):
        return f"rgba({v[0]},{v[1]},{v[2]},{al})"

    if T["design"] != "bleu":
        D.photos_jobs(photo, H, W)
        if T["design"] == "e":
            jobs += D.e_jauges_jobs(tmp)
        return jobs
    voile_b = f"linear-gradient(90deg, {rgba(.97)} 0%, {rgba(.92)} 30%, {rgba(.55)} 58%, {rgba(.18)} 100%)"
    for cle, (src, pos, h) in BANDEAUX.items():
        photo(f"photos/bandeau-{cle}.jpg", BW, h, src, pos, voile_b, sat)
    photo("photos/menu-fond.jpg", 220, H, "menu-route-nuit.jpg", "center 70%",
          f"linear-gradient(180deg, {T['menu']} 0%, {T['menu']} 55%, {rgba(.55)} 70%, {rgba(.25)} 86%, {rgba(.60)} 100%)", sat)
    photo("photos/login-photo.jpg", 420, 500, "login-route-cotiere.jpg", "80% center",
          f"linear-gradient(180deg, {rgba(.88)} 0%, {rgba(.35)} 38%, {rgba(.25)} 62%, {rgba(.92)} 100%)", sat)
    return jobs


# --------------------------------------------------------------------------
# Relevé des icônes réellement dessinées sur les écrans d'un design
# --------------------------------------------------------------------------
from html.parser import HTMLParser

VIDES = {"img", "input", "br", "hr", "meta", "link", "source", "col", "wbr"}
PREFIXES = [("BoutonNavigation", "menu"), ("Btn_Quitter", "bouton"), ("Btn_", "bouton"), ("Logo", "logo"),
            ("Pastille", "indicateur"), ("KPI", "indicateur"), ("Carte_CA", "indicateur"), ("Carte_Voitures", "indicateur"),
            ("Carte_Clients", "indicateur"), ("Bande_Indicateurs", "indicateur"), ("Date", "date"), ("Lbl_", "carte"), ("Carte", "carte")]


class Releve(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pile, self.trouve, self.dans_svg = [], [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "svg" and "data-ico" in a:
            ctx = next((x for x in reversed(self.pile) if x), None)
            self.trouve.append(((a["data-ico"], a["stroke"], int(float(a["width"])), float(a["stroke-width"])), ctx))
        if self.dans_svg or tag == "svg":
            self.dans_svg += 1 if tag == "svg" else 0
            return
        if tag not in VIDES:
            self.pile.append(a.get("data-acc"))

    def handle_startendtag(self, tag, attrs):
        if tag == "svg":
            self.handle_starttag(tag, attrs)
            self.dans_svg -= 1

    def handle_endtag(self, tag):
        if tag == "svg":
            self.dans_svg -= 1
            return
        if self.dans_svg:
            return
        if tag not in VIDES and self.pile:
            self.pile.pop()


# Logo complet (une seule image) : sélecteurs des éléments repris, marge (anneau du design B), fond de l'aperçu
LOGOS = {
    "a": {"connexion": (['[data-acc="Logo"]'], 0, "#2B2D31"), "menu": (['[data-acc="Logo"]'], 0, "#0D0D0D")},
    "b": {"connexion": (['[data-acc="Logo"]', '[data-acc="Lbl_Titre"]'], 6, "#F6E3EC"), "menu": (['[data-acc="Logo"]'], 0, "#9D174D")},
    "c": {"connexion": (['[data-acc="Logo"]'], 0, "#064E3B"), "menu": (['[data-acc="Logo"]'], 0, "#064E3B")},
    "d": {"connexion": (['[data-acc="Logo"]', '[data-acc="Lbl_Titre"]'], 0, "#16181B"), "menu": (['[data-acc="Logo"]'], 0, "#0B0C0E")},
    "e": {"connexion": (['[data-acc="Logo"]'], 0, "#07090F"), "menu": (['[data-acc="Logo"]'], 0, "#05070C")},
}


def logos_jobs(t):
    out = []
    for ou, fic in [("connexion", "00-connexion"), ("menu", "01-tableau-de-bord")]:
        sels, marge, _ = LOGOS[t["design"]][ou]
        out.append({"html": (MAQ / f"{fic}.html").as_uri(), "sels": sels, "marge": marge, "out": str(ASSETS / f"logo-{ou}.png")})
    return out


def releve_icones(pages):
    """pages : [(fichier écran, titre, html)] -> {(nom, couleur, taille, trait): infos}"""
    icones = {}
    for fic, titre, h in pages:
        r = Releve()
        r.feed(h)
        for cle, ctx in r.trouve:
            i = icones.setdefault(cle, {"ecrans": [], "ctx": []})
            if titre not in i["ecrans"]:
                i["ecrans"].append(titre)
            if ctx and ctx not in i["ctx"]:
                i["ctx"].append(ctx)
    noms = set()
    for (name, color, size, stroke), i in sorted(icones.items(), key=lambda kv: (kv[0][0], kv[0][2])):
        pre = next((p for c in i["ctx"] for k, p in PREFIXES if c.startswith(k)), "icone")
        actif = "-actif" if pre == "menu" and color.upper() == T["nav_ico_actif"].upper() else ""
        f = f"{pre}-{name}{actif}-{size}px-{color.lstrip('#').upper()}.png"
        while f in noms:
            f = f.replace(".png", "-b.png")
        noms.add(f)
        i["fichier"] = f
    return icones


def lum(hexa):
    h = hexa.lstrip("#")
    r, g_, b = (int(h[k:k + 2], 16) for k in (0, 2, 4))
    return (0.299 * r + 0.587 * g_ + 0.114 * b) / 255


def planche_icones(icones, tmp):
    """Page HTML montrant toutes les icônes du design (fond sombre pour les icônes claires)."""
    cases = []
    for ou in ("connexion", "menu"):
        fond = LOGOS[T["design"]][ou][2]
        cases.append(f'<div class="c logo"><div class="i" style="background:{fond};width:auto;height:auto;padding:12px">'
                     f'<img src="{(ASSETS / f"logo-{ou}.png").as_uri()}" style="display:block"></div>'
                     f'<div class="n"><b>logo-{ou}.png</b><br>Logo complet ({"page de connexion" if ou == "connexion" else "menu"})</div></div>')
    for (name, color, size, stroke), i in sorted(icones.items(), key=lambda kv: kv[1]["fichier"]):
        fond = "#2B2D31" if lum(color) > .62 else "#FFFFFF"
        cases.append(f'<div class="c"><div class="i" style="background:{fond}">{svg(name, color, size, stroke)}</div>'
                     f'<div class="n">{e(i["fichier"])}</div></div>')
    p = tmp / "planche-icones.html"
    p.write_text('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;font:12px "Open Sans",sans-serif}'
                 '#a{display:grid;grid-template-columns:repeat(5,250px);gap:10px;padding:16px;background:#ECEDEF;width:1290px}'
                 '.c{background:#fff;border:1px solid #D6D8DC;padding:8px;display:flex;align-items:center;gap:10px}'
                 '.i{width:56px;height:56px;display:flex;align-items:center;justify-content:center;border:1px solid #E1E3E6;flex:none}'
                 '.n{word-break:break-all;color:#333}.logo{grid-column:span 5;gap:16px}.logo .n{word-break:normal}</style></head><body><div id="a">' + "".join(cases) + '</div></body></html>')
    return {"html": p.as_uri(), "out": str(MAQ / "apercu-icones.png"), "w": 1322, "h": 200, "transparent": False, "sel": "#a"}


def ecrire_icones_md(icones):
    L = [f"# Icônes · {NOM_APPLI}", "",
         "Toutes les icônes dessinées sur les 8 écrans, déjà exportées en PNG transparent dans `assets/` "
         "(aperçu : `apercu-icones.png`).", "",
         "Dans Access : propriété **Image** du bouton (ou contrôle **Image**), `Mode affichage image` **Découpage**, "
         "`Type image` **Incorporé**. Les icônes blanches ou claires sont prévues pour un fond foncé (menu, photo, pastille).", "",
         "@@LOGOS@@", "",
         "## Toutes les icônes", "",
         "| Fichier | Taille | Couleur | Contrôle(s) | Écran(s) |", "|---|---|---|---|---|"]
    for (name, color, size, stroke), i in sorted(icones.items(), key=lambda kv: kv[1]["fichier"]):
        ctx = ", ".join(f"`{c}`" for c in i["ctx"]) or "icône décorative (titre de carte ou bandeau)"
        L.append(f"| `{i['fichier']}` | {size} × {size} px | `{color.upper()}` | {ctx} | {', '.join(i['ecrans'])} |")
    (MAQ / "ICONES.md").write_text("\n".join(L) + "\n")


def ecrire_logos(t, maq, assets, pos):
    """Section « Logos » de ICONES.md et logos.json (position en cm dans le formulaire)."""
    remplace = {"a": ("`Logo` (icône + nom)", "`Logo` (icône + nom)"),
                "b": ("`Logo` (bouton blanc arrondi + icône) et `Lbl_Titre` (nom)", "`Logo` (bouton blanc arrondi + icône)"),
                "c": ("`Logo` (icône + nom)", "`Logo` (icône + nom)"),
                "d": ("`Logo` (icône) et `Lbl_Titre` (nom)", "`Logo` (icône + nom)"),
                "e": ("`Logo` (image `marque/aurion-connexion.png`)", "`Logo` (image `marque/aurion-menu.png`)")}[t["design"]]
    L = ["## Logos complets (une seule image)", "",
         "Le logo entier (icône **et** nom de l'entreprise, avec la bonne police et les bonnes couleurs) est fourni en **une seule image** "
         "PNG transparente : insérer un contrôle **Image**, choisir le fichier, `Mode affichage image` **Découpage**, "
         "puis saisir la position et la taille ci-dessous (feuille de propriétés, onglet *Format*).", "",
         "| Fichier | Où | Gauche | Haut | Largeur | Hauteur | Remplace |", "|---|---|---:|---:|---:|---:|---|"]
    data = {}
    for k, (ou, lib) in enumerate([("connexion", "Formulaire de connexion"), ("menu", "Formulaire Menu")]):
        p = pos[str(assets / f"logo-{ou}.png")]
        data[ou] = p
        L.append(f"| `logo-{ou}.png` | {lib} | {cm(p['x'])} | {cm(p['y'])} | {cm(p['w'])} | {cm(p['h'])} | {remplace[k]} |")
    (maq / "logos.json").write_text(json.dumps(data))
    f = maq / "ICONES.md"
    f.write_text(f.read_text().replace("@@LOGOS@@", "\n".join(L)))


def controle(t, icones, pages, ASSETS):
    """Vérifie que chaque icône et chaque image utilisée par les écrans existe dans assets/."""
    manque = [f for f in ("logo-connexion.png", "logo-menu.png") if not (ASSETS / f).exists()]
    for (name, color, size, stroke), i in icones.items():
        if not (ASSETS / i["fichier"]).exists():
            manque.append(i["fichier"])
    for fic, titre, h in pages:
        for ref in re.findall(r'(?:src="|url\(["\']?)(?:\.\./)?assets/([^"\')]+)', h):
            if not (ASSETS / ref).exists():
                manque.append(f"{ref} ({titre})")
    return manque


# --------------------------------------------------------------------------
def cm(px):
    return f"{px / 37.795:.2f}".replace(".", ",")


def ecrire_cotes(cotes, chemin, dossier_png="maquettes/png"):
    L = ["# Cotes des contrôles", "",
         "Positions et tailles en **centimètres**, à saisir dans la feuille de propriétés d'Access "
         "(onglet *Format* : `Gauche`, `Haut`, `Largeur`, `Hauteur`).", "",
         "* **Menu** : mesurées depuis le coin haut-gauche du formulaire `Menu` (41,49 × 20,74 cm, sans la barre de titre).",
         (f"* **Autres écrans** : mesurées depuis le coin haut-gauche du **sous-formulaire** ({cm(CW)} × {cm(CH)} cm)."
          if dossier_png == "maquettes/png" else
          "* **Autres écrans** : mesurées depuis le coin haut-gauche du **sous-formulaire** (position et taille : ligne `Sous_Formulaire` du formulaire Menu)."),
         "* Les contrôles placés dans une carte sont donnés en position absolue dans le sous-formulaire.",
         "* Fichier généré par `outils/generer.py`.", ""]

    def table(items):
        out = ["| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |", "|---|---|---:|---:|---:|---:|"]
        vus = set()
        for i in items:
            k = (i["nom"], i["x"], i["y"])
            if k in vus:
                continue
            vus.add(k)
            out.append(f'| `{i["nom"]}` | {i["type"]} | {cm(i["x"])} | {cm(i["y"])} | {cm(i["w"])} | {cm(i["h"])} |')
        return out + [""]

    for fic, titre, _ in ECRANS:
        items = cotes.get(fic, [])
        if fic == "01-tableau-de-bord":
            L += ["## Formulaire « Menu » (commun à tous les écrans)", ""] + table([i for i in items if i["zone"] == "ecran"])
        zone = "ecran" if fic == "00-connexion" else "contenu"
        L += [f"## {titre}", "", f"Maquette : `{dossier_png}/{fic}.png`", ""] + table([i for i in items if i["zone"] == zone])
    chemin.write_text("\n".join(L))


def appliquer_theme(t):
    """Choisit le style courant : couleurs, dossiers de sortie et chemin des images."""
    global T, MAQ, ASSETS, ASSET_URL, NOM_APPLI
    T = t
    NOM_APPLI = t["societe"]
    if t["dossier"] == "maquettes":          # style bleu : emplacements historiques
        MAQ, ASSETS, ASSET_URL, fonts = DESIGN / "maquettes", DESIGN / "assets", "../assets", "fonts/"
    else:                                     # autres styles : design/styles/<style>/
        MAQ = DESIGN / t["dossier"]
        ASSETS, ASSET_URL, fonts = MAQ / "assets", "assets", "../../maquettes/fonts/"
    (MAQ / "png").mkdir(parents=True, exist_ok=True)
    (ASSETS / "photos").mkdir(parents=True, exist_ok=True)
    racine = ":root {\n" + "".join(f"  --{k}: {v};\n" for k, v in t["css"].items()) + "}\n\n"
    base = (ICI / "style-base.css").read_text().replace("url(fonts/", f"url({fonts}")
    (MAQ / "style.css").write_text(f"/* Style : {t['nom']} */\n" + racine + base)


def main():
    D.g = sys.modules[__name__]
    choix = sys.argv[1:]                     # ex. : python3 generer.py rose-blanc
    tmp = Path(tempfile.mkdtemp(prefix="rentalcar-"))
    jobs, ecr, verif, logos = [], [], [], []
    for t in THEMES:
        if choix and t["cle"] not in choix:
            continue
        appliquer_theme(t)
        (tmp / t["cle"]).mkdir()
        pages = []
        for fic, titre, fn in ECRANS:
            h = page(titre, fn())
            pages.append((fic, titre, h))
            (MAQ / f"{fic}.html").write_text(h)
            ecr.append({"html": (MAQ / f"{fic}.html").as_uri(), "out": str(MAQ / "png" / f"{fic}.png"),
                        "w": 1600, "h": 820, "transparent": False, "sel": "#fenetre",
                        "cotes": fic if t["cle"] == "bleu" else f"{t['cle']}/{fic}"})
        if t["design"] == "bleu":
            jobs += assets_jobs(tmp / t["cle"])
        else:
            for f in ASSETS.glob("*.png"):        # repartir d'un dossier propre
                f.unlink()
            icones = releve_icones(pages)
            jobs += assets_jobs(tmp / t["cle"], icones)
            logos += logos_jobs(t)
            jobs.append(planche_icones(icones, tmp / t["cle"]))
            ecrire_icones_md(icones)
            verif.append((t, icones, pages, MAQ, ASSETS))
    jf = tmp / "jobs.json"
    cf = tmp / "cotes.json"
    lf = tmp / "logos.json"
    jf.write_text(json.dumps({"assets": jobs, "ecrans": ecr, "cotes": str(cf), "logos": logos, "logos_out": str(lf)}))
    r = subprocess.run(["node", str(ICI / "rendre.mjs"), str(jf)], cwd=ICI)
    if r.returncode:
        sys.exit(r.returncode)
    pos_logos = json.loads(lf.read_text()) if logos else {}
    erreurs = 0
    for t, icones, pages, _maq, dossier_assets in verif:
        ecrire_logos(t, _maq, dossier_assets, pos_logos)
        m = controle(t, icones, pages, dossier_assets)
        erreurs += len(m)
        print(f"Contrôle {t['societe']} : {len(icones)} icônes" + (" – OK, rien ne manque" if not m else " – MANQUE : " + ", ".join(m)))
    if erreurs:
        sys.exit(1)
    cotes = json.loads(cf.read_text())
    for t in THEMES:
        pre = "" if t["cle"] == "bleu" else t["cle"] + "/"
        part = {k[len(pre):]: v for k, v in cotes.items() if (k.startswith(pre) if pre else "/" not in k)}
        if part:
            chemin = DESIGN / "COTES.md" if not pre else DESIGN / t["dossier"] / "COTES.md"
            ecrire_cotes(part, chemin, "maquettes/png" if not pre else "png")


if __name__ == "__main__":
    main()
